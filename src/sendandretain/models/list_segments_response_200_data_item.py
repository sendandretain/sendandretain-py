from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_segments_response_200_data_item_filter_item import ListSegmentsResponse200DataItemFilterItem


T = TypeVar("T", bound="ListSegmentsResponse200DataItem")


@_attrs_define
class ListSegmentsResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        description (None | str | Unset):
        filter_ (list[ListSegmentsResponse200DataItemFilterItem] | Unset):
        member_count (int | None | Unset): Cached; null until first refresh.
        count_refreshed_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    filter_: list[ListSegmentsResponse200DataItemFilterItem] | Unset = UNSET
    member_count: int | None | Unset = UNSET
    count_refreshed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        filter_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = []
            for filter_item_data in self.filter_:
                filter_item = filter_item_data.to_dict()
                filter_.append(filter_item)

        member_count: int | None | Unset
        if isinstance(self.member_count, Unset):
            member_count = UNSET
        else:
            member_count = self.member_count

        count_refreshed_at: None | str | Unset
        if isinstance(self.count_refreshed_at, Unset):
            count_refreshed_at = UNSET
        elif isinstance(self.count_refreshed_at, datetime.datetime):
            count_refreshed_at = self.count_refreshed_at.isoformat()
        else:
            count_refreshed_at = self.count_refreshed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if member_count is not UNSET:
            field_dict["member_count"] = member_count
        if count_refreshed_at is not UNSET:
            field_dict["count_refreshed_at"] = count_refreshed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_segments_response_200_data_item_filter_item import ListSegmentsResponse200DataItemFilterItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _filter_ = d.pop("filter", UNSET)
        filter_: list[ListSegmentsResponse200DataItemFilterItem] | Unset = UNSET
        if _filter_ is not UNSET:
            filter_ = []
            for filter_item_data in _filter_:
                filter_item = ListSegmentsResponse200DataItemFilterItem.from_dict(filter_item_data)

                filter_.append(filter_item)

        def _parse_member_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        member_count = _parse_member_count(d.pop("member_count", UNSET))

        def _parse_count_refreshed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                count_refreshed_at_type_0 = datetime.datetime.fromisoformat(data)

                return count_refreshed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        count_refreshed_at = _parse_count_refreshed_at(d.pop("count_refreshed_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        list_segments_response_200_data_item = cls(
            id=id,
            name=name,
            description=description,
            filter_=filter_,
            member_count=member_count,
            count_refreshed_at=count_refreshed_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        list_segments_response_200_data_item.additional_properties = d
        return list_segments_response_200_data_item

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
