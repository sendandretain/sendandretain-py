from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBrandBodyBrandColors")


@_attrs_define
class UpdateBrandBodyBrandColors:
    """
    Attributes:
        primary (str | Unset):
        accent (str | Unset):
        background (str | Unset):
        text (str | Unset):
        muted (str | Unset):
    """

    primary: str | Unset = UNSET
    accent: str | Unset = UNSET
    background: str | Unset = UNSET
    text: str | Unset = UNSET
    muted: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary = self.primary

        accent = self.accent

        background = self.background

        text = self.text

        muted = self.muted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["primary"] = primary
        if accent is not UNSET:
            field_dict["accent"] = accent
        if background is not UNSET:
            field_dict["background"] = background
        if text is not UNSET:
            field_dict["text"] = text
        if muted is not UNSET:
            field_dict["muted"] = muted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        primary = d.pop("primary", UNSET)

        accent = d.pop("accent", UNSET)

        background = d.pop("background", UNSET)

        text = d.pop("text", UNSET)

        muted = d.pop("muted", UNSET)

        update_brand_body_brand_colors = cls(
            primary=primary,
            accent=accent,
            background=background,
            text=text,
            muted=muted,
        )

        update_brand_body_brand_colors.additional_properties = d
        return update_brand_body_brand_colors

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
