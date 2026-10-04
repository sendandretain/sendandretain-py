from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_brand_response_200_brand import UpdateBrandResponse200Brand


T = TypeVar("T", bound="UpdateBrandResponse200")


@_attrs_define
class UpdateBrandResponse200:
    """
    Attributes:
        brand (UpdateBrandResponse200Brand | Unset):
        brief_updated (bool | Unset):
    """

    brand: UpdateBrandResponse200Brand | Unset = UNSET
    brief_updated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand: dict[str, Any] | Unset = UNSET
        if not isinstance(self.brand, Unset):
            brand = self.brand.to_dict()

        brief_updated = self.brief_updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brand is not UNSET:
            field_dict["brand"] = brand
        if brief_updated is not UNSET:
            field_dict["brief_updated"] = brief_updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_brand_response_200_brand import UpdateBrandResponse200Brand

        d = dict(src_dict)
        _brand = d.pop("brand", UNSET)
        brand: UpdateBrandResponse200Brand | Unset
        if isinstance(_brand, Unset):
            brand = UNSET
        else:
            brand = UpdateBrandResponse200Brand.from_dict(_brand)

        brief_updated = d.pop("brief_updated", UNSET)

        update_brand_response_200 = cls(
            brand=brand,
            brief_updated=brief_updated,
        )

        update_brand_response_200.additional_properties = d
        return update_brand_response_200

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
