from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDomainResponse201DmarcRecommendedRecord")


@_attrs_define
class CreateDomainResponse201DmarcRecommendedRecord:
    """Present while DMARC isn't confirmed — publish this TXT record.

    Attributes:
        type_ (str | Unset):
        name (str | Unset):
        value (str | Unset):
        note (str | Unset):
    """

    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    value: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        value = self.value

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        note = d.pop("note", UNSET)

        create_domain_response_201_dmarc_recommended_record = cls(
            type_=type_,
            name=name,
            value=value,
            note=note,
        )

        create_domain_response_201_dmarc_recommended_record.additional_properties = d
        return create_domain_response_201_dmarc_recommended_record

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
