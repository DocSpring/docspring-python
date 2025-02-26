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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from docspring.models.submission_batch import SubmissionBatch
from typing import Optional, Set
from typing_extensions import Self

class BatchGeneratePdfs201Response(BaseModel):
    """
    BatchGeneratePdfs201Response
    """ # noqa: E501
    status: StrictStr
    error: Optional[StrictStr] = None
    errors: Optional[List[StrictStr]] = None
    submission_batch: SubmissionBatch
    submissions: List[Dict[str, Any]]
    __properties: ClassVar[List[str]] = ["status", "error", "errors", "submission_batch", "submissions"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['success', 'error']):
            raise ValueError("must be one of enum values ('success', 'error')")
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
        """Create an instance of BatchGeneratePdfs201Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of submission_batch
        if self.submission_batch:
            _dict['submission_batch'] = self.submission_batch.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BatchGeneratePdfs201Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "error": obj.get("error"),
            "errors": obj.get("errors"),
            "submission_batch": SubmissionBatch.from_dict(obj["submission_batch"]) if obj.get("submission_batch") is not None else None,
            "submissions": obj.get("submissions")
        })
        return _obj


