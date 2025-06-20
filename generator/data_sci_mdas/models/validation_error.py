# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

from typing import List

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr
from whoopcommons.model.whoop_model import WhoopModel

from data_sci_mdas.models.validation_error_loc_inner import ValidationErrorLocInner


class ValidationError(WhoopModel):
    """
    ValidationError
    """

    loc: conlist(ValidationErrorLocInner) = Field(...)
    msg: StrictStr = Field(...)
    type: StrictStr = Field(...)
