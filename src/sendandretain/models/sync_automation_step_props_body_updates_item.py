from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_automation_step_props_body_updates_item_props_overrides import (
        SyncAutomationStepPropsBodyUpdatesItemPropsOverrides,
    )


T = TypeVar("T", bound="SyncAutomationStepPropsBodyUpdatesItem")


@_attrs_define
class SyncAutomationStepPropsBodyUpdatesItem:
    """
    Attributes:
        position (int):
        props_overrides (SyncAutomationStepPropsBodyUpdatesItemPropsOverrides):
    """

    position: int
    props_overrides: SyncAutomationStepPropsBodyUpdatesItemPropsOverrides
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        props_overrides = self.props_overrides.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "props_overrides": props_overrides,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_automation_step_props_body_updates_item_props_overrides import (
            SyncAutomationStepPropsBodyUpdatesItemPropsOverrides,
        )

        d = dict(src_dict)
        position = d.pop("position")

        props_overrides = SyncAutomationStepPropsBodyUpdatesItemPropsOverrides.from_dict(d.pop("props_overrides"))

        sync_automation_step_props_body_updates_item = cls(
            position=position,
            props_overrides=props_overrides,
        )

        sync_automation_step_props_body_updates_item.additional_properties = d
        return sync_automation_step_props_body_updates_item

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
