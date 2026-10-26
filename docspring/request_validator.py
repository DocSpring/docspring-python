# coding: utf-8

"""Checks a request against API v2's request schemas (request_schemas.py, the schemas the API validates requests
with) before it's sent, and says what the API would say about it. api_clients/validator_conformance checks that it
agrees with the API."""

import functools
import inspect
import json
import math
import re
from typing import Any, Callable, Dict, List, Optional, Tuple, TypeVar

from docspring.exceptions import RequestValidationError
from docspring.request_schemas import REQUEST_SCHEMAS_JSON

Detail = Dict[str, str]

TYPE_NAMES = {
    "string": "a string",
    "integer": "an integer",
    "number": "a number",
    "boolean": "true or false",
    "object": "an object",
    "array": "an array",
    "null": "null",
}
# What a multipart body's file field holds when the API checks it
FILE_PLACEHOLDER = "(file)"
# A date and time as the API reads it (Ruby's DateTime.rfc3339, then json_schemer's checks)
DATE_TIME = re.compile(
    r"\A[ \t\n\v\f\r]*(-?\d{4})-(\d{2})-(\d{2})[Tt \t\n\v\f\r](\d{2}):(\d{2}):(\d{2})(?:\.\d+)?(?:[Zz]|([+-])(\d{2}):(\d{2}))\Z",
    re.ASCII,
)
# An absolute URI as the API reads it (RFC 3986, as Ruby's URI parser has it), a little looser for IP addresses
# Lookaheads check the escapes, so only character classes repeat: Java and PHP recurse on each repetition of a group
_SEGMENT = r"[%!$&-.0-9:;=@A-Z_a-z~/]"
URI = re.compile(
    r"\A(?![^?#]*%(?![0-9A-Fa-f]{2}))[A-Za-z][+\-.0-9A-Za-z]*:"
    r"(?://(?:[%!$&-.0-9:;=A-Z_a-z~]*@)?"
    r"(?:\[(?:[0-9A-Fa-f:.]+|[vV][0-9A-Fa-f]+\.[!$&-.0-9:;=A-Z_a-z~]+)\]|[%!$&-.0-9;=A-Z_a-z~]*)"
    r"(?::[0-9]*)?(?:/" + _SEGMENT + r"*)?"
    r"|/(?:(?!/)" + _SEGMENT + r"+)?"
    r"|(?!/)" + _SEGMENT + r"+"
    r"|)"
    r"(?:\?[^#]*)?"
    r"(?:#(?![^#]*%(?![0-9A-Fa-f]{2}))[%!$&-.0-9:;=@A-Z_a-z~/?]*)?\Z"
)
WHITESPACE = re.compile(r"[ \t\n\v\f\r]")

_schemas: Optional[Dict[str, Any]] = None
_patterns: Dict[str, Any] = {}


def schemas() -> Dict[str, Any]:
    global _schemas
    if _schemas is None:
        _schemas = json.loads(REQUEST_SCHEMAS_JSON)
    return _schemas


Function = TypeVar("Function", bound=Callable[..., Any])


def checks_request(operation_id: str) -> Callable[[Function], Function]:
    """Checks an operation's arguments before pydantic's validate_call converts them, and raises a
    RequestValidationError with the API's details when the API would reject the request. A dict with a key the API
    doesn't document, or a value out of range, gets what the API would say rather than pydantic's message. Off when
    the configuration's client_side_validation is."""

    def decorator(function: Function) -> Function:
        signature = inspect.signature(function)

        @functools.wraps(function)
        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            if self.api_client.configuration.client_side_validation:
                try:
                    arguments = signature.bind(self, *args, **kwargs).arguments
                except TypeError:
                    # A missing or unexpected argument, which the call itself reports
                    arguments = None
                if arguments is not None:
                    details = _argument_errors(operation_id, arguments, self.api_client.sanitize_for_serialization)
                    if details:
                        raise RequestValidationError(details)
            return function(self, *args, **kwargs)

        return wrapper  # type: ignore[return-value]

    return decorator


# The query and body an operation's arguments make, as the SDK sends them (models, enums and dates as JSON)
def _argument_errors(operation_id: str, arguments: Dict[str, Any], serialize: Callable[[Any], Any]) -> List[Detail]:
    entry = schemas()["operations"][operation_id]
    query = {name: serialize(arguments[name]) for name in entry.get("query") or {} if arguments.get(name) is not None}
    body = None
    if entry.get("body"):
        if entry["body"]["mediaType"] == "multipart/form-data":
            properties = entry["body"]["schema"]["properties"]
            body = {
                name: FILE_PLACEHOLDER if properties[name].get("format") == "binary" else serialize(arguments[name])
                for name in properties
                if arguments.get(name) is not None
            }
        elif arguments.get("body") is not None:
            body = serialize(arguments["body"])
    return errors(operation_id, query=query, body=body)


def errors(operation_id: str, query: Optional[Dict[str, Any]] = None, body: Any = None) -> List[Detail]:
    """The details for a request to an operation (createSubmission)"""
    entry = schemas()["operations"][operation_id]
    details: List[Detail] = []
    if entry.get("query") and query:
        params = entry["query"]
        schema = {
            "type": "object",
            "properties": {name: param["schema"] for name, param in params.items()},
            "required": [name for name, param in params.items() if param["required"]],
            "additionalProperties": False,
        }
        details.extend(_validate_params(schema, query, "query"))
    if entry.get("body") and body is not None:
        if entry["body"]["mediaType"] == "multipart/form-data":
            values = {
                key: (FILE_PLACEHOLDER if not isinstance(value, (str, int, float, bool, list, dict)) and value is not None else value)
                for key, value in body.items()
            }
            details.extend(_validate_params(entry["body"]["schema"], values, "body"))
        else:
            details.extend(validate(entry["body"]["schema"], json.loads(body) if isinstance(body, str) else body, "body"))
    return details


def validate(schema: Any, data: Any, location: str) -> List[Detail]:
    """The details for `data` checked against `schema` at `location` (body or query)"""
    details: List[Detail] = []
    _check(schema, data, "", location, details)
    return details


# Query and multipart params arrive as strings, which the API converts where the schema types them
def _validate_params(schema: Dict[str, Any], data: Dict[str, Any], location: str) -> List[Detail]:
    properties = schema.get("properties") or {}
    converted = {key: _convert_param(value, properties.get(key)) for key, value in data.items()}
    return validate(schema, converted, location)


def _convert_param(value: Any, schema: Any) -> Any:
    if not isinstance(schema, dict):
        return value
    types = _types(schema)
    if isinstance(value, list) and "array" in types:
        return [_convert_param(item, schema.get("items")) for item in value]
    if not isinstance(value, str):
        return value
    if "integer" in types and re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    if "number" in types and re.fullmatch(r"-?[0-9]+(?:\.[0-9]+)?", value):
        return float(value) if "." in value else int(value)
    if "boolean" in types and value in ("true", "false"):
        return value == "true"
    return value


def _types(schema: Dict[str, Any]) -> List[str]:
    types = schema.get("type")
    if types is None:
        return []
    return types if isinstance(types, list) else [types]


def _resolve(schema: Any) -> Any:
    while isinstance(schema, dict) and "$ref" in schema:
        name = schema["$ref"].replace("#/components/schemas/", "", 1)
        schema = schemas()["components"]["schemas"][name]
    return schema


def _check(schema: Any, data: Any, pointer: str, location: str, details: List[Detail]) -> None:
    schema = _resolve(schema)
    if not isinstance(schema, dict):
        return
    if "discriminator" in schema:
        _check_union(schema, data, pointer, location, details)
        return

    if "type" in schema and not any(_is_type(data, type_) for type_ in _types(schema)):
        message = "must be a JSON object" if pointer == "" and location == "body" else _type_message(_types(schema))
        details.append(_detail(location, pointer, "type", message))
    if "enum" in schema and not any(_json_equal(value, data) for value in schema["enum"]):
        values = ", ".join(_to_json(value) for value in schema["enum"])
        details.append(_detail(location, pointer, "enum", f"must be one of: {values}"))
    if "const" in schema and not _json_equal(schema["const"], data):
        details.append(_detail(location, pointer, "const", f"must be {_to_json(schema['const'])}"))

    if isinstance(data, str):
        _check_string(schema, data, pointer, location, details)
    elif isinstance(data, (int, float)) and not isinstance(data, bool):
        _check_number(schema, data, pointer, location, details)
    elif isinstance(data, list):
        _check_array(schema, data, pointer, location, details)
    elif isinstance(data, dict):
        _check_object(schema, data, pointer, location, details)


def _check_union(schema: Dict[str, Any], data: Any, pointer: str, location: str, details: List[Detail]) -> None:
    """A union (oneOf with a discriminator): the discriminator property's value picks the variant, and only that one is
    checked, as the API does"""
    if not isinstance(data, dict):
        details.append(_detail(location, pointer, "type", f"must be {TYPE_NAMES['object']}"))
        return

    name = schema["discriminator"]["propertyName"]
    child = f"{pointer}/{_escape(name)}"
    if name not in data:
        details.append(_detail(location, child, "required", "is required"))
        return

    # [value, $ref] pairs, in the order the API lists them
    mapping = schema["discriminator"]["mapping"]
    variant = next((ref for value, ref in mapping if value == data[name]), None) if isinstance(data[name], str) else None
    if variant:
        _check({"$ref": variant}, data, pointer, location, details)
        return

    values = ", ".join(_to_json(value) for value, _ref in mapping)
    details.append(_detail(location, child, "enum", f"must be one of: {values}"))


def _check_string(schema: Dict[str, Any], data: str, pointer: str, location: str, details: List[Detail]) -> None:
    length = len(data)
    if "minLength" in schema and length < schema["minLength"]:
        limit = schema["minLength"]
        details.append(_detail(location, pointer, "minLength", _at_least(limit, f"must be at least {_count(limit, 'character')}")))
    if "maxLength" in schema and length > schema["maxLength"]:
        details.append(_detail(location, pointer, "maxLength", f"must be at most {_count(schema['maxLength'], 'character')}"))
    if "pattern" in schema and not _pattern(schema["pattern"]).search(data):
        message = schema.get("x-pattern-message") or f"must match the pattern {schema['pattern']}"
        details.append(_detail(location, pointer, "pattern", message))
    if "format" in schema and not _format(schema["format"], data):
        message = schemas()["formatMessages"].get(schema["format"]) or f"must be a valid {schema['format']}"
        details.append(_detail(location, pointer, "format", message))


def _check_number(schema: Dict[str, Any], data: Any, pointer: str, location: str, details: List[Detail]) -> None:
    if "minimum" in schema and data < schema["minimum"]:
        details.append(_detail(location, pointer, "minimum", f"must be at least {_number(schema['minimum'])}"))
    if "maximum" in schema and data > schema["maximum"]:
        details.append(_detail(location, pointer, "maximum", f"must be at most {_number(schema['maximum'])}"))
    if "exclusiveMinimum" in schema and data <= schema["exclusiveMinimum"]:
        details.append(_detail(location, pointer, "exclusiveMinimum", f"must be greater than {_number(schema['exclusiveMinimum'])}"))
    if "exclusiveMaximum" in schema and data >= schema["exclusiveMaximum"]:
        details.append(_detail(location, pointer, "exclusiveMaximum", f"must be less than {_number(schema['exclusiveMaximum'])}"))


def _check_array(schema: Dict[str, Any], data: List[Any], pointer: str, location: str, details: List[Detail]) -> None:
    if "minItems" in schema and len(data) < schema["minItems"]:
        limit = schema["minItems"]
        details.append(_detail(location, pointer, "minItems", _at_least(limit, f"must have at least {_count(limit, 'item')}")))
    if "maxItems" in schema and len(data) > schema["maxItems"]:
        details.append(_detail(location, pointer, "maxItems", f"must have at most {_count(schema['maxItems'], 'item')}"))
    if schema.get("uniqueItems") and not _unique(data):
        duplicate = _first_duplicate(data)
        message = f"has {_to_json(duplicate[0])} more than once" if duplicate else "can't contain the same item twice"
        details.append(_detail(location, pointer, "uniqueItems", message))
    if "items" in schema:
        for index, item in enumerate(data):
            _check(schema["items"], item, f"{pointer}/{index}", location, details)


def _check_object(schema: Dict[str, Any], data: Dict[str, Any], pointer: str, location: str, details: List[Detail]) -> None:
    for name in schema.get("required") or []:
        if name not in data:
            details.append(_detail(location, f"{pointer}/{_escape(name)}", "required", "is required"))

    properties = schema.get("properties") or {}
    additional = schema.get("additionalProperties")
    for name, value in data.items():
        child = f"{pointer}/{_escape(name)}"
        if name in properties:
            _check(properties[name], value, child, location, details)
        elif additional is False:
            details.append(_unknown_property(schema, name, child, location))
        elif isinstance(additional, dict):
            _check(additional, value, child, location, details)


def _unknown_property(schema: Dict[str, Any], name: str, pointer: str, location: str) -> Detail:
    not_allowed = (schema.get("x-not-allowed-properties") or {}).get(name)
    if not_allowed:
        return _detail(location, pointer, "not_allowed", not_allowed)

    noun = "query parameter" if location == "query" else "property"
    custom = schema.get("x-unknown-property-message")
    message = custom or f"isn't a documented {noun}"
    snake = _underscore(name)
    if snake != name and snake in (schema.get("properties") or {}):
        plural = "settings" if custom else ("properties" if noun == "property" else "query parameters")
        message += f". API v2 names {plural} in snake_case: '{snake}'"
    return _detail(location, pointer, "unknown_property", message)


def _detail(location: str, pointer: str, code: str, message: str) -> Detail:
    if location != "query":
        return {"code": code, "message": message, "pointer": pointer}
    parameter = pointer[1:].split("/")[0].replace("~1", "/").replace("~0", "~")
    return {"code": code, "message": message, "parameter": parameter}


def _is_type(data: Any, type_: str) -> bool:
    if type_ == "string":
        return isinstance(data, str)
    if type_ == "integer":
        if isinstance(data, bool):
            return False
        return isinstance(data, int) or (isinstance(data, float) and math.isfinite(data) and data == math.floor(data))
    if type_ == "number":
        return isinstance(data, (int, float)) and not isinstance(data, bool)
    if type_ == "boolean":
        return isinstance(data, bool)
    if type_ == "object":
        return isinstance(data, dict)
    if type_ == "array":
        return isinstance(data, list)
    if type_ == "null":
        return data is None
    return False


# Patterns are ECMA-262 regexps, as OpenAPI says: ^ and $ are the start and end of the value, not of a line. The
# API's patterns only use ^ as the first character and $ as the last (api_clients/scripts/extract_request_schemas).
def _pattern(pattern: str) -> Any:
    if pattern not in _patterns:
        anchored = "\\A" + pattern[1:] if pattern.startswith("^") else pattern
        # A $ after an even number of backslashes is the anchor
        if anchored.endswith("$") and (len(anchored) - 1 - len(anchored[:-1].rstrip("\\"))) % 2 == 0:
            anchored = anchored[:-1] + "\\Z"
        _patterns[pattern] = re.compile(anchored, re.ASCII)
    return _patterns[pattern]


def _format(format_: str, data: str) -> bool:
    if format_ == "uri":
        return data.isascii() and not WHITESPACE.search(data) and URI.match(data) is not None
    if format_ == "date-time":
        return _date_time(data)
    return True


def _date_time(data: str) -> bool:
    match = DATE_TIME.match(data)
    if not match:
        return False
    year, month, day, hour, minute, second = (int(value) for value in match.groups()[:6])
    if not (1 <= month <= 12 and 1 <= day <= _days_in_month(year, month)):
        return False
    if not (hour <= 23 and minute <= 59 and second <= 60):
        return False
    offset = 0
    if match.group(7):
        offset_hours, offset_minutes = int(match.group(8)), int(match.group(9))
        if offset_hours > 23 or offset_minutes > 59:
            return False
        offset = (-1 if match.group(7) == "-" else 1) * (offset_hours * 60 + offset_minutes)
    # A leap second is only at the end of a UTC day
    return second < 60 or (hour * 60 + minute - offset) % 1440 == 1439


# Before the Gregorian calendar (1582), the API's dates are Julian: every fourth year is a leap year
def _days_in_month(year: int, month: int) -> int:
    leap = year % 4 == 0 and (year < 1583 or year % 100 != 0 or year % 400 == 0)
    if month == 2 and leap:
        return 29
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]


def _unique(data: List[Any]) -> bool:
    return not any(_json_equal(item, other) for index, item in enumerate(data) for other in data[index + 1:])


# The API names the first value that it counts twice, counting 1 and 1.0 as different values (Ruby's tally)
def _first_duplicate(data: List[Any]) -> Optional[Tuple[Any]]:
    counts: Dict[Any, int] = {}
    firsts: Dict[Any, Any] = {}
    for item in data:
        key = _tally_key(item)
        counts[key] = counts.get(key, 0) + 1
        firsts.setdefault(key, item)
    for key, count in counts.items():
        if count > 1:
            return (firsts[key],)
    return None


def _tally_key(value: Any) -> Any:
    if isinstance(value, bool):
        return ("b", value)
    if isinstance(value, int):
        return ("i", value)
    if isinstance(value, float):
        return ("f", value)
    if isinstance(value, list):
        return ("l", tuple(_tally_key(item) for item in value))
    if isinstance(value, dict):
        return ("d", frozenset((key, _tally_key(item)) for key, item in value.items()))
    return ("v", value)


# JSON equality: numbers by value, objects regardless of key order
def _json_equal(left: Any, right: Any) -> bool:
    left_number = isinstance(left, (int, float)) and not isinstance(left, bool)
    right_number = isinstance(right, (int, float)) and not isinstance(right, bool)
    if left_number or right_number:
        return left_number and right_number and left == right
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(_json_equal(value, right[key]) for key, value in left.items())
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(_json_equal(a, b) for a, b in zip(left, right))
    return type(left) is type(right) and left == right


def _type_message(types: List[str]) -> str:
    names = [TYPE_NAMES.get(type_, type_) for type_ in types]
    connector = ", or " if len(names) > 1 and any(" or " in name for name in names) else " or "
    if len(names) == 1:
        return f"must be {names[0]}"
    if len(names) == 2:
        return f"must be {connector.join(names)}"
    return f"must be {', '.join(names[:-1])}{connector}{names[-1]}"


def _at_least(limit: Any, message: str) -> str:
    return "can't be empty" if limit == 1 else message


def _count(number: Any, noun: str) -> str:
    return f"{_number(number)} {noun if number == 1 else noun + 's'}"


# A number as the API writes it: 1 and 1.5 as they are, 2.0 as 2.0
def _number(number: Any) -> str:
    return str(number)


def _to_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _escape(token: str) -> str:
    return str(token).replace("~", "~0").replace("/", "~1")


def _underscore(name: str) -> str:
    name = re.sub(r"([A-Z\d]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", name)
    return name.replace("-", "_").lower()
