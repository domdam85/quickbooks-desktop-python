# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .date_driven_term import DateDrivenTerm

__all__ = ["DateDrivenTermListResponse"]


class DateDrivenTermListResponse(BaseModel):
    data: List[DateDrivenTerm]
    """The array of date-driven terms."""

    object_type: Literal["list"] = FieldInfo(alias="objectType")
    """The type of object. This value is always `"list"`."""

    url: str
    """The endpoint URL where this list can be accessed."""
