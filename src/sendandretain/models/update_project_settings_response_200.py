from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_project_settings_response_200_utm_type_0 import UpdateProjectSettingsResponse200UtmType0


T = TypeVar("T", bound="UpdateProjectSettingsResponse200")


@_attrs_define
class UpdateProjectSettingsResponse200:
    """
    Attributes:
        sends_paused (bool | Unset):
        daily_send_cap (int | Unset):
        utm (None | Unset | UpdateProjectSettingsResponse200UtmType0):
        default_locale (None | str | Unset):
    """

    sends_paused: bool | Unset = UNSET
    daily_send_cap: int | Unset = UNSET
    utm: None | Unset | UpdateProjectSettingsResponse200UtmType0 = UNSET
    default_locale: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_project_settings_response_200_utm_type_0 import UpdateProjectSettingsResponse200UtmType0

        sends_paused = self.sends_paused

        daily_send_cap = self.daily_send_cap

        utm: dict[str, Any] | None | Unset
        if isinstance(self.utm, Unset):
            utm = UNSET
        elif isinstance(self.utm, UpdateProjectSettingsResponse200UtmType0):
            utm = self.utm.to_dict()
        else:
            utm = self.utm

        default_locale: None | str | Unset
        if isinstance(self.default_locale, Unset):
            default_locale = UNSET
        else:
            default_locale = self.default_locale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sends_paused is not UNSET:
            field_dict["sends_paused"] = sends_paused
        if daily_send_cap is not UNSET:
            field_dict["daily_send_cap"] = daily_send_cap
        if utm is not UNSET:
            field_dict["utm"] = utm
        if default_locale is not UNSET:
            field_dict["default_locale"] = default_locale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_project_settings_response_200_utm_type_0 import UpdateProjectSettingsResponse200UtmType0

        d = dict(src_dict)
        sends_paused = d.pop("sends_paused", UNSET)

        daily_send_cap = d.pop("daily_send_cap", UNSET)

        def _parse_utm(data: object) -> None | Unset | UpdateProjectSettingsResponse200UtmType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                utm_type_0 = UpdateProjectSettingsResponse200UtmType0.from_dict(data)

                return utm_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateProjectSettingsResponse200UtmType0, data)

        utm = _parse_utm(d.pop("utm", UNSET))

        def _parse_default_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_locale = _parse_default_locale(d.pop("default_locale", UNSET))

        update_project_settings_response_200 = cls(
            sends_paused=sends_paused,
            daily_send_cap=daily_send_cap,
            utm=utm,
            default_locale=default_locale,
        )

        update_project_settings_response_200.additional_properties = d
        return update_project_settings_response_200

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
