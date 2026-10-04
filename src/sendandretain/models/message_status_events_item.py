from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageStatusEventsItem")


@_attrs_define
class MessageStatusEventsItem:
    """
    Attributes:
        type_ (str | Unset):
        provider (str | Unset):
        occurred_at (datetime.datetime | Unset):
    """

    type_: str | Unset = UNSET
    provider: str | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        provider = self.provider

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if provider is not UNSET:
            field_dict["provider"] = provider
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        provider = d.pop("provider", UNSET)

        _occurred_at = d.pop("occurred_at", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)

        message_status_events_item = cls(
            type_=type_,
            provider=provider,
            occurred_at=occurred_at,
        )

        message_status_events_item.additional_properties = d
        return message_status_events_item

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
