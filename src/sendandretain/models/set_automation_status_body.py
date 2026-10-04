from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_automation_status_body_status import SetAutomationStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetAutomationStatusBody")


@_attrs_define
class SetAutomationStatusBody:
    """
    Attributes:
        status (SetAutomationStatusBodyStatus): `active` starts real sending; `paused` stops it.
        confirm (bool | Unset): Required (`true`) to activate. Pausing needs no confirmation.
    """

    status: SetAutomationStatusBodyStatus
    confirm: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        confirm = self.confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if confirm is not UNSET:
            field_dict["confirm"] = confirm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = SetAutomationStatusBodyStatus(d.pop("status"))

        confirm = d.pop("confirm", UNSET)

        set_automation_status_body = cls(
            status=status,
            confirm=confirm,
        )

        set_automation_status_body.additional_properties = d
        return set_automation_status_body

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
