from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_result_skipped_item_reason import EventResultSkippedItemReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventResultSkippedItem")


@_attrs_define
class EventResultSkippedItem:
    """
    Attributes:
        automation_id (str | Unset):
        reason (EventResultSkippedItemReason | Unset): `filtered` — the trigger filter excluded this contact. `guarded`
            — they have already been through this flow. `suppressed` — they opted out. `exclusive` — a higher-priority
            exclusive automation took them. `no_steps` — the automation has no steps. `already_running` — a run is already
            in flight.
    """

    automation_id: str | Unset = UNSET
    reason: EventResultSkippedItemReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation_id = self.automation_id

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automation_id is not UNSET:
            field_dict["automation_id"] = automation_id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automation_id = d.pop("automation_id", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: EventResultSkippedItemReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = EventResultSkippedItemReason(_reason)

        event_result_skipped_item = cls(
            automation_id=automation_id,
            reason=reason,
        )

        event_result_skipped_item.additional_properties = d
        return event_result_skipped_item

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
