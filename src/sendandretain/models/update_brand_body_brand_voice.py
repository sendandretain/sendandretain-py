from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBrandBodyBrandVoice")


@_attrs_define
class UpdateBrandBodyBrandVoice:
    """
    Attributes:
        traits (list[str] | Unset):
        guidance (str | Unset):  Default: ''.
    """

    traits: list[str] | Unset = UNSET
    guidance: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        traits: list[str] | Unset = UNSET
        if not isinstance(self.traits, Unset):
            traits = self.traits

        guidance = self.guidance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if traits is not UNSET:
            field_dict["traits"] = traits
        if guidance is not UNSET:
            field_dict["guidance"] = guidance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        traits = cast(list[str], d.pop("traits", UNSET))

        guidance = d.pop("guidance", UNSET)

        update_brand_body_brand_voice = cls(
            traits=traits,
            guidance=guidance,
        )

        update_brand_body_brand_voice.additional_properties = d
        return update_brand_body_brand_voice

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
