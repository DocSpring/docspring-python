# coding: utf-8

"""
    DocSpring API

    DocSpring provides an API that helps you fill out and sign PDF templates.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CreateHtmlSubmissionData(BaseModel):
    """
    CreateHtmlSubmissionData
    """ # noqa: E501
    css: Optional[StrictStr] = None
    data: Optional[Dict[str, Any]] = None
    editable: Optional[StrictBool] = None
    expires_in: Optional[StrictInt] = None
    field_overrides: Optional[Dict[str, Any]] = None
    html: Optional[StrictStr] = None
    metadata: Optional[Dict[str, Any]] = None
    password: Optional[StrictStr] = None
    test: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["css", "data", "editable", "expires_in", "field_overrides", "html", "metadata", "password", "test"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateHtmlSubmissionData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateHtmlSubmissionData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "css": obj.get("css"),
            "data": obj.get("data"),
            "editable": obj.get("editable"),
            "expires_in": obj.get("expires_in"),
            "field_overrides": obj.get("field_overrides"),
            "html": obj.get("html"),
            "metadata": obj.get("metadata"),
            "password": obj.get("password"),
            "test": obj.get("test")
        })
        return _obj


