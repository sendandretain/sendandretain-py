from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddAutomationStepsSchema0Variant4SendWindow")


@_attrs_define
class AddAutomationStepsSchema0Variant4SendWindow:
    """Quiet-hours clamp; contact.attributes.timezone wins over this timezone.

    Attributes:
        days (list[int] | Unset):
        start_hour (int | Unset):
        end_hour (int | Unset):
        timezone (str | Unset):
    """

    days: list[int] | Unset = UNSET
    start_hour: int | Unset = UNSET
    end_hour: int | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days: list[int] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = self.days

        start_hour = self.start_hour

        end_hour = self.end_hour

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if start_hour is not UNSET:
            field_dict["startHour"] = start_hour
        if end_hour is not UNSET:
            field_dict["endHour"] = end_hour
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = cast(list[int], d.pop("days", UNSET))

        start_hour = d.pop("startHour", UNSET)

        end_hour = d.pop("endHour", UNSET)

        timezone = d.pop("timezone", UNSET)

        add_automation_steps_schema_0_variant_4_send_window = cls(
            days=days,
            start_hour=start_hour,
            end_hour=end_hour,
            timezone=timezone,
        )

        add_automation_steps_schema_0_variant_4_send_window.additional_properties = d
        return add_automation_steps_schema_0_variant_4_send_window

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
