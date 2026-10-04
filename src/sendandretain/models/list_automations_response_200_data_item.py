from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAutomationsResponse200DataItem")


@_attrs_define
class ListAutomationsResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        status (str | Unset):
        trigger_event (str | Unset):
        priority (int | Unset):
        step_count (int | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    trigger_event: str | Unset = UNSET
    priority: int | Unset = UNSET
    step_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        trigger_event = self.trigger_event

        priority = self.priority

        step_count = self.step_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if trigger_event is not UNSET:
            field_dict["trigger_event"] = trigger_event
        if priority is not UNSET:
            field_dict["priority"] = priority
        if step_count is not UNSET:
            field_dict["step_count"] = step_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        trigger_event = d.pop("trigger_event", UNSET)

        priority = d.pop("priority", UNSET)

        step_count = d.pop("step_count", UNSET)

        list_automations_response_200_data_item = cls(
            id=id,
            name=name,
            status=status,
            trigger_event=trigger_event,
            priority=priority,
            step_count=step_count,
        )

        list_automations_response_200_data_item.additional_properties = d
        return list_automations_response_200_data_item

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
