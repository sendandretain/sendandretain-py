from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.settings_patch_request_body_content_application_json_utm_variant_0_params import (
        SettingsPatchRequestBodyContentApplicationJsonUtmVariant0Params,
    )


T = TypeVar("T", bound="SettingsPatchRequestBodyContentApplicationJsonUtmVariant0")


@_attrs_define
class SettingsPatchRequestBodyContentApplicationJsonUtmVariant0:
    """
    Attributes:
        enabled (bool):
        params (SettingsPatchRequestBodyContentApplicationJsonUtmVariant0Params):
    """

    enabled: bool
    params: SettingsPatchRequestBodyContentApplicationJsonUtmVariant0Params
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "params": params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settings_patch_request_body_content_application_json_utm_variant_0_params import (
            SettingsPatchRequestBodyContentApplicationJsonUtmVariant0Params,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled")

        params = SettingsPatchRequestBodyContentApplicationJsonUtmVariant0Params.from_dict(d.pop("params"))

        settings_patch_request_body_content_application_json_utm_variant_0 = cls(
            enabled=enabled,
            params=params,
        )

        settings_patch_request_body_content_application_json_utm_variant_0.additional_properties = d
        return settings_patch_request_body_content_application_json_utm_variant_0

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
