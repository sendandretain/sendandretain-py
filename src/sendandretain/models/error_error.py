from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_error_code import ErrorErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorError")


@_attrs_define
class ErrorError:
    """
    Attributes:
        code (ErrorErrorCode): Stable, machine-readable error code.
        message (str): Human-readable explanation.
        message_id (str | Unset): Present on send failures that were still logged (e.g. suppressed).
    """

    code: ErrorErrorCode
    message: str
    message_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        message_id = self.message_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if message_id is not UNSET:
            field_dict["message_id"] = message_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = ErrorErrorCode(d.pop("code"))

        message = d.pop("message")

        message_id = d.pop("message_id", UNSET)

        error_error = cls(
            code=code,
            message=message,
            message_id=message_id,
        )

        error_error.additional_properties = d
        return error_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
