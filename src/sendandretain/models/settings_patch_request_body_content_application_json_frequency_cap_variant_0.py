from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingsPatchRequestBodyContentApplicationJsonFrequencyCapVariant0")


@_attrs_define
class SettingsPatchRequestBodyContentApplicationJsonFrequencyCapVariant0:
    """
    Attributes:
        max_ (int):
        window_hours (int):
        enabled (bool | Unset):  Default: True.
    """

    max_: int
    window_hours: int
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        window_hours = self.window_hours

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max": max_,
                "window_hours": window_hours,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_ = d.pop("max")

        window_hours = d.pop("window_hours")

        enabled = d.pop("enabled", UNSET)

        settings_patch_request_body_content_application_json_frequency_cap_variant_0 = cls(
            max_=max_,
            window_hours=window_hours,
            enabled=enabled,
        )

        settings_patch_request_body_content_application_json_frequency_cap_variant_0.additional_properties = d
        return settings_patch_request_body_content_application_json_frequency_cap_variant_0

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
