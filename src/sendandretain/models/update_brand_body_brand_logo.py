from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBrandBodyBrandLogo")


@_attrs_define
class UpdateBrandBodyBrandLogo:
    """
    Attributes:
        light_url (str | Unset):
        dark_url (str | Unset):
        width (int | Unset):
    """

    light_url: str | Unset = UNSET
    dark_url: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        light_url = self.light_url

        dark_url = self.dark_url

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if light_url is not UNSET:
            field_dict["lightUrl"] = light_url
        if dark_url is not UNSET:
            field_dict["darkUrl"] = dark_url
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        light_url = d.pop("lightUrl", UNSET)

        dark_url = d.pop("darkUrl", UNSET)

        width = d.pop("width", UNSET)

        update_brand_body_brand_logo = cls(
            light_url=light_url,
            dark_url=dark_url,
            width=width,
        )

        update_brand_body_brand_logo.additional_properties = d
        return update_brand_body_brand_logo

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
