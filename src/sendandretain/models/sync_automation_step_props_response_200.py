from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncAutomationStepPropsResponse200")


@_attrs_define
class SyncAutomationStepPropsResponse200:
    """
    Attributes:
        updated (int | Unset):
        positions (list[int] | Unset):
    """

    updated: int | Unset = UNSET
    positions: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated = self.updated

        positions: list[int] | Unset = UNSET
        if not isinstance(self.positions, Unset):
            positions = self.positions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated is not UNSET:
            field_dict["updated"] = updated
        if positions is not UNSET:
            field_dict["positions"] = positions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        updated = d.pop("updated", UNSET)

        positions = cast(list[int], d.pop("positions", UNSET))

        sync_automation_step_props_response_200 = cls(
            updated=updated,
            positions=positions,
        )

        sync_automation_step_props_response_200.additional_properties = d
        return sync_automation_step_props_response_200

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
