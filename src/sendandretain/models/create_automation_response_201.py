from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_automation_response_201_status import CreateAutomationResponse201Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAutomationResponse201")


@_attrs_define
class CreateAutomationResponse201:
    """
    Attributes:
        automation_id (str | Unset):
        step_count (int | Unset):
        status (CreateAutomationResponse201Status | Unset):
    """

    automation_id: str | Unset = UNSET
    step_count: int | Unset = UNSET
    status: CreateAutomationResponse201Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation_id = self.automation_id

        step_count = self.step_count

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automation_id is not UNSET:
            field_dict["automation_id"] = automation_id
        if step_count is not UNSET:
            field_dict["step_count"] = step_count
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automation_id = d.pop("automation_id", UNSET)

        step_count = d.pop("step_count", UNSET)

        _status = d.pop("status", UNSET)
        status: CreateAutomationResponse201Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateAutomationResponse201Status(_status)

        create_automation_response_201 = cls(
            automation_id=automation_id,
            step_count=step_count,
            status=status,
        )

        create_automation_response_201.additional_properties = d
        return create_automation_response_201

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
