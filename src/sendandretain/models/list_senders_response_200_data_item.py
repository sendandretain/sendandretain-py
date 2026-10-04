from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListSendersResponse200DataItem")


@_attrs_define
class ListSendersResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        from_name (str | Unset):
        from_email (str | Unset):
        reply_to (None | str | Unset):
        is_default (bool | Unset):
        domain (None | str | Unset):
        domain_verified (bool | Unset): False means sends from this identity are refused.
        created_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    from_name: str | Unset = UNSET
    from_email: str | Unset = UNSET
    reply_to: None | str | Unset = UNSET
    is_default: bool | Unset = UNSET
    domain: None | str | Unset = UNSET
    domain_verified: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        from_name = self.from_name

        from_email = self.from_email

        reply_to: None | str | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

        is_default = self.is_default

        domain: None | str | Unset
        if isinstance(self.domain, Unset):
            domain = UNSET
        else:
            domain = self.domain

        domain_verified = self.domain_verified

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if from_name is not UNSET:
            field_dict["from_name"] = from_name
        if from_email is not UNSET:
            field_dict["from_email"] = from_email
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if domain is not UNSET:
            field_dict["domain"] = domain
        if domain_verified is not UNSET:
            field_dict["domain_verified"] = domain_verified
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        from_name = d.pop("from_name", UNSET)

        from_email = d.pop("from_email", UNSET)

        def _parse_reply_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        is_default = d.pop("is_default", UNSET)

        def _parse_domain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain = _parse_domain(d.pop("domain", UNSET))

        domain_verified = d.pop("domain_verified", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        list_senders_response_200_data_item = cls(
            id=id,
            from_name=from_name,
            from_email=from_email,
            reply_to=reply_to,
            is_default=is_default,
            domain=domain,
            domain_verified=domain_verified,
            created_at=created_at,
        )

        list_senders_response_200_data_item.additional_properties = d
        return list_senders_response_200_data_item

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
