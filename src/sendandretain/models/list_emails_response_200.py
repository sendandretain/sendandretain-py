from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_status import MessageStatus


T = TypeVar("T", bound="ListEmailsResponse200")


@_attrs_define
class ListEmailsResponse200:
    """
    Attributes:
        data (list[MessageStatus] | Unset):
        has_more (bool | Unset):
    """

    data: list[MessageStatus] | Unset = UNSET
    has_more: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if has_more is not UNSET:
            field_dict["has_more"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_status import MessageStatus

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[MessageStatus] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = MessageStatus.from_dict(data_item_data)

                data.append(data_item)

        has_more = d.pop("has_more", UNSET)

        list_emails_response_200 = cls(
            data=data,
            has_more=has_more,
        )

        list_emails_response_200.additional_properties = d
        return list_emails_response_200

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
