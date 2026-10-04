from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSenderResponse201")


@_attrs_define
class CreateSenderResponse201:
    """
    Attributes:
        id (str | Unset):
        from_name (str | Unset):
        from_email (str | Unset):
        is_default (bool | Unset):
    """

    id: str | Unset = UNSET
    from_name: str | Unset = UNSET
    from_email: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        from_name = self.from_name

        from_email = self.from_email

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if from_name is not UNSET:
            field_dict["from_name"] = from_name
        if from_email is not UNSET:
            field_dict["from_email"] = from_email
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        from_name = d.pop("from_name", UNSET)

        from_email = d.pop("from_email", UNSET)

        is_default = d.pop("is_default", UNSET)

        create_sender_response_201 = cls(
            id=id,
            from_name=from_name,
            from_email=from_email,
            is_default=is_default,
        )

        create_sender_response_201.additional_properties = d
        return create_sender_response_201

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
