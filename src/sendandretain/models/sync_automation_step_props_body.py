from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_automation_step_props_body_updates_item import SyncAutomationStepPropsBodyUpdatesItem


T = TypeVar("T", bound="SyncAutomationStepPropsBody")


@_attrs_define
class SyncAutomationStepPropsBody:
    """
    Attributes:
        automation (str): Automation id or name.
        updates (list[SyncAutomationStepPropsBodyUpdatesItem]): One entry per send step, addressed by its global
            `position`.
        merge (bool | Unset): Shallow-merge into existing overrides instead of replacing them.
    """

    automation: str
    updates: list[SyncAutomationStepPropsBodyUpdatesItem]
    merge: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation = self.automation

        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)

        merge = self.merge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automation": automation,
                "updates": updates,
            }
        )
        if merge is not UNSET:
            field_dict["merge"] = merge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_automation_step_props_body_updates_item import SyncAutomationStepPropsBodyUpdatesItem

        d = dict(src_dict)
        automation = d.pop("automation")

        updates = []
        _updates = d.pop("updates")
        for updates_item_data in _updates:
            updates_item = SyncAutomationStepPropsBodyUpdatesItem.from_dict(updates_item_data)

            updates.append(updates_item)

        merge = d.pop("merge", UNSET)

        sync_automation_step_props_body = cls(
            automation=automation,
            updates=updates,
            merge=merge,
        )

        sync_automation_step_props_body.additional_properties = d
        return sync_automation_step_props_body

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
