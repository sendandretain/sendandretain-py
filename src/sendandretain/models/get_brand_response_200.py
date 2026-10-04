from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_brand_response_200_brand import GetBrandResponse200Brand


T = TypeVar("T", bound="GetBrandResponse200")


@_attrs_define
class GetBrandResponse200:
    """
    Attributes:
        name (str | Unset):
        brand (GetBrandResponse200Brand | Unset):
        website_url (None | str | Unset):
    """

    name: str | Unset = UNSET
    brand: GetBrandResponse200Brand | Unset = UNSET
    website_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        brand: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brand, Unset):
            brand = self.brand.to_dict()

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if brand is not UNSET:
            field_dict["brand"] = brand
        if website_url is not UNSET:
            field_dict["website_url"] = website_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_brand_response_200_brand import GetBrandResponse200Brand

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _brand = d.pop("brand", UNSET)
        brand: GetBrandResponse200Brand | Unset
        if isinstance(_brand, Unset):
            brand = UNSET
        else:
            brand = GetBrandResponse200Brand.from_dict(_brand)

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        get_brand_response_200 = cls(
            name=name,
            brand=brand,
            website_url=website_url,
        )

        get_brand_response_200.additional_properties = d
        return get_brand_response_200

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
