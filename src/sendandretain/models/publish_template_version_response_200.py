from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishTemplateVersionResponse200")


@_attrs_define
class PublishTemplateVersionResponse200:
    """
    Attributes:
        slug (str | Unset):
        version (int | Unset):
        variant_key (None | str | Unset):
        live (bool | Unset): True when this version is now what sends.
    """

    slug: str | Unset = UNSET
    version: int | Unset = UNSET
    variant_key: None | str | Unset = UNSET
    live: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        version = self.version

        variant_key: None | str | Unset
        if isinstance(self.variant_key, Unset):
            variant_key = UNSET
        else:
            variant_key = self.variant_key

        live = self.live

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if version is not UNSET:
            field_dict["version"] = version
        if variant_key is not UNSET:
            field_dict["variant_key"] = variant_key
        if live is not UNSET:
            field_dict["live"] = live

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        version = d.pop("version", UNSET)

        def _parse_variant_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_key = _parse_variant_key(d.pop("variant_key", UNSET))

        live = d.pop("live", UNSET)

        publish_template_version_response_200 = cls(
            slug=slug,
            version=version,
            variant_key=variant_key,
            live=live,
        )

        publish_template_version_response_200.additional_properties = d
        return publish_template_version_response_200

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
