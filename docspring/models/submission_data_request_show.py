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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SubmissionDataRequestShow(BaseModel):
    """
    SubmissionDataRequestShow
    """ # noqa: E501
    id: Optional[StrictStr]
    email: Optional[StrictStr]
    name: Optional[StrictStr]
    order: Optional[StrictInt]
    sort_order: StrictInt
    fields: Optional[List[StrictStr]]
    metadata: Optional[Dict[str, Any]]
    state: StrictStr
    viewed_at: Optional[StrictStr]
    completed_at: Optional[StrictStr]
    data: Optional[Dict[str, Any]]
    auth_type: StrictStr
    auth_second_factor_type: StrictStr
    auth_provider: Optional[StrictStr]
    auth_session_started_at: Optional[StrictStr]
    auth_session_id_hash: Optional[StrictStr]
    auth_user_id_hash: Optional[StrictStr]
    auth_username_hash: Optional[StrictStr]
    auth_phone_number_hash: Optional[StrictStr]
    ip_address: Optional[StrictStr]
    user_agent: Optional[StrictStr]
    submission_id: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["id", "email", "name", "order", "sort_order", "fields", "metadata", "state", "viewed_at", "completed_at", "data", "auth_type", "auth_second_factor_type", "auth_provider", "auth_session_started_at", "auth_session_id_hash", "auth_user_id_hash", "auth_username_hash", "auth_phone_number_hash", "ip_address", "user_agent", "submission_id"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pending', 'completed']):
            raise ValueError("must be one of enum values ('pending', 'completed')")
        return value

    @field_validator('auth_type')
    def auth_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['none', 'password', 'oauth', 'email_link', 'phone_number', 'ldap', 'saml']):
            raise ValueError("must be one of enum values ('none', 'password', 'oauth', 'email_link', 'phone_number', 'ldap', 'saml')")
        return value

    @field_validator('auth_second_factor_type')
    def auth_second_factor_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['none', 'phone_number', 'totp', 'mobile_push', 'security_key', 'fingerprint']):
            raise ValueError("must be one of enum values ('none', 'phone_number', 'totp', 'mobile_push', 'security_key', 'fingerprint')")
        return value

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
        """Create an instance of SubmissionDataRequestShow from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if viewed_at (nullable) is None
        # and model_fields_set contains the field
        if self.viewed_at is None and "viewed_at" in self.model_fields_set:
            _dict['viewed_at'] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completed_at'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if auth_provider (nullable) is None
        # and model_fields_set contains the field
        if self.auth_provider is None and "auth_provider" in self.model_fields_set:
            _dict['auth_provider'] = None

        # set to None if auth_session_started_at (nullable) is None
        # and model_fields_set contains the field
        if self.auth_session_started_at is None and "auth_session_started_at" in self.model_fields_set:
            _dict['auth_session_started_at'] = None

        # set to None if auth_session_id_hash (nullable) is None
        # and model_fields_set contains the field
        if self.auth_session_id_hash is None and "auth_session_id_hash" in self.model_fields_set:
            _dict['auth_session_id_hash'] = None

        # set to None if auth_user_id_hash (nullable) is None
        # and model_fields_set contains the field
        if self.auth_user_id_hash is None and "auth_user_id_hash" in self.model_fields_set:
            _dict['auth_user_id_hash'] = None

        # set to None if auth_username_hash (nullable) is None
        # and model_fields_set contains the field
        if self.auth_username_hash is None and "auth_username_hash" in self.model_fields_set:
            _dict['auth_username_hash'] = None

        # set to None if auth_phone_number_hash (nullable) is None
        # and model_fields_set contains the field
        if self.auth_phone_number_hash is None and "auth_phone_number_hash" in self.model_fields_set:
            _dict['auth_phone_number_hash'] = None

        # set to None if ip_address (nullable) is None
        # and model_fields_set contains the field
        if self.ip_address is None and "ip_address" in self.model_fields_set:
            _dict['ip_address'] = None

        # set to None if user_agent (nullable) is None
        # and model_fields_set contains the field
        if self.user_agent is None and "user_agent" in self.model_fields_set:
            _dict['user_agent'] = None

        # set to None if submission_id (nullable) is None
        # and model_fields_set contains the field
        if self.submission_id is None and "submission_id" in self.model_fields_set:
            _dict['submission_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubmissionDataRequestShow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "name": obj.get("name"),
            "order": obj.get("order"),
            "sort_order": obj.get("sort_order"),
            "fields": obj.get("fields"),
            "metadata": obj.get("metadata"),
            "state": obj.get("state"),
            "viewed_at": obj.get("viewed_at"),
            "completed_at": obj.get("completed_at"),
            "data": obj.get("data"),
            "auth_type": obj.get("auth_type"),
            "auth_second_factor_type": obj.get("auth_second_factor_type"),
            "auth_provider": obj.get("auth_provider"),
            "auth_session_started_at": obj.get("auth_session_started_at"),
            "auth_session_id_hash": obj.get("auth_session_id_hash"),
            "auth_user_id_hash": obj.get("auth_user_id_hash"),
            "auth_username_hash": obj.get("auth_username_hash"),
            "auth_phone_number_hash": obj.get("auth_phone_number_hash"),
            "ip_address": obj.get("ip_address"),
            "user_agent": obj.get("user_agent"),
            "submission_id": obj.get("submission_id")
        })
        return _obj


