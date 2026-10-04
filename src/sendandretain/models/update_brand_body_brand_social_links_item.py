from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_brand_body_brand_social_links_item_platform import UpdateBrandBodyBrandSocialLinksItemPlatform

T = TypeVar("T", bound="UpdateBrandBodyBrandSocialLinksItem")


@_attrs_define
class UpdateBrandBodyBrandSocialLinksItem:
    """
    Attributes:
        platform (UpdateBrandBodyBrandSocialLinksItemPlatform):
        url (str):
    """

    platform: UpdateBrandBodyBrandSocialLinksItemPlatform
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform = self.platform.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "platform": platform,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = UpdateBrandBodyBrandSocialLinksItemPlatform(d.pop("platform"))

        url = d.pop("url")

        update_brand_body_brand_social_links_item = cls(
            platform=platform,
            url=url,
        )

        update_brand_body_brand_social_links_item.additional_properties = d
        return update_brand_body_brand_social_links_item

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
