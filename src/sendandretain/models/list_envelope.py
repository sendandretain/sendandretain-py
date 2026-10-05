from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_envelope_object import ListEnvelopeObject

T = TypeVar("T", bound="ListEnvelope")


@_attrs_define
class ListEnvelope:
    """Every list answers this shape. Keep requesting with `?cursor=<next_cursor>` until `has_more` is false.

    Attributes:
        object_ (ListEnvelopeObject):
        data (list[Any]):
        has_more (bool):
        next_cursor (None | str):
    """

    object_: ListEnvelopeObject
    data: list[Any]
    has_more: bool
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.value

        data = self.data

        has_more = self.has_more

        next_cursor: None | str
        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "data": data,
                "has_more": has_more,
                "next_cursor": next_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_ = ListEnvelopeObject(d.pop("object"))

        data = cast(list[Any], d.pop("data"))

        has_more = d.pop("has_more")

        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        list_envelope = cls(
            object_=object_,
            data=data,
            has_more=has_more,
            next_cursor=next_cursor,
        )

        list_envelope.additional_properties = d
        return list_envelope

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
