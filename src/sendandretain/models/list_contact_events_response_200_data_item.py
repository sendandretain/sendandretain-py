from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_contact_events_response_200_data_item_properties import (
        ListContactEventsResponse200DataItemProperties,
    )


T = TypeVar("T", bound="ListContactEventsResponse200DataItem")


@_attrs_define
class ListContactEventsResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        properties (ListContactEventsResponse200DataItemProperties | Unset):
        dedupe_key (None | str | Unset):
        occurred_at (datetime.datetime | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    properties: ListContactEventsResponse200DataItemProperties | Unset = UNSET
    dedupe_key: None | str | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        dedupe_key: None | str | Unset
        if isinstance(self.dedupe_key, Unset):
            dedupe_key = UNSET
        else:
            dedupe_key = self.dedupe_key

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if properties is not UNSET:
            field_dict["properties"] = properties
        if dedupe_key is not UNSET:
            field_dict["dedupe_key"] = dedupe_key
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_contact_events_response_200_data_item_properties import (
            ListContactEventsResponse200DataItemProperties,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: ListContactEventsResponse200DataItemProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = ListContactEventsResponse200DataItemProperties.from_dict(_properties)

        def _parse_dedupe_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dedupe_key = _parse_dedupe_key(d.pop("dedupe_key", UNSET))

        _occurred_at = d.pop("occurred_at", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        list_contact_events_response_200_data_item = cls(
            id=id,
            name=name,
            properties=properties,
            dedupe_key=dedupe_key,
            occurred_at=occurred_at,
            created_at=created_at,
        )

        list_contact_events_response_200_data_item.additional_properties = d
        return list_contact_events_response_200_data_item

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
