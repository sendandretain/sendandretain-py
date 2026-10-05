from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_contacts_response_200_object import ListContactsResponse200Object

if TYPE_CHECKING:
    from ..models.list_contacts_response_200_data_item import ListContactsResponse200DataItem


T = TypeVar("T", bound="ListContactsResponse200")


@_attrs_define
class ListContactsResponse200:
    """
    Attributes:
        data (list[ListContactsResponse200DataItem]):
        has_more (bool): More rows exist after this page.
        object_ (ListContactsResponse200Object):
        next_cursor (None | str): Pass as `?cursor=` for the next page. Null on the last page.
    """

    data: list[ListContactsResponse200DataItem]
    has_more: bool
    object_: ListContactsResponse200Object
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        has_more = self.has_more

        object_ = self.object_.value

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "has_more": has_more,
                "object": object_,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_contacts_response_200_data_item import ListContactsResponse200DataItem

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ListContactsResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        has_more = d.pop("has_more")

        object_ = ListContactsResponse200Object(d.pop("object"))

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        list_contacts_response_200 = cls(
            data=data,
            has_more=has_more,
            object_=object_,
            next_cursor=next_cursor,
        )

        list_contacts_response_200.additional_properties = d
        return list_contacts_response_200

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
