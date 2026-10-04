from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_segment_body_filter_item import CreateSegmentBodyFilterItem


T = TypeVar("T", bound="CreateSegmentBody")


@_attrs_define
class CreateSegmentBody:
    """
    Attributes:
        name (str): Unique within the project.
        filter_ (list[CreateSegmentBodyFilterItem]): Conditions over contact attributes and tags. All must match.
        description (None | str | Unset):
    """

    name: str
    filter_: list[CreateSegmentBodyFilterItem]
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        filter_ = []
        for filter_item_data in self.filter_:
            filter_item = filter_item_data.to_dict()
            filter_.append(filter_item)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filter": filter_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_segment_body_filter_item import CreateSegmentBodyFilterItem

        d = dict(src_dict)
        name = d.pop("name")

        filter_ = []
        _filter_ = d.pop("filter")
        for filter_item_data in _filter_:
            filter_item = CreateSegmentBodyFilterItem.from_dict(filter_item_data)

            filter_.append(filter_item)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        create_segment_body = cls(
            name=name,
            filter_=filter_,
            description=description,
        )

        create_segment_body.additional_properties = d
        return create_segment_body

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
