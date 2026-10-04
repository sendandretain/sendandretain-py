from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTemplatesResponse200DataItem")


@_attrs_define
class ListTemplatesResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        slug (str | Unset):
        name (str | Unset):
        description (None | str | Unset):
        category (str | Unset):
        sender_id (None | str | Unset):
        published (bool | Unset): True when a version is live and sendable.
        updated_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    category: str | Unset = UNSET
    sender_id: None | str | Unset = UNSET
    published: bool | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        category = self.category

        sender_id: None | str | Unset
        if isinstance(self.sender_id, Unset):
            sender_id = UNSET
        else:
            sender_id = self.sender_id

        published = self.published

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if category is not UNSET:
            field_dict["category"] = category
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if published is not UNSET:
            field_dict["published"] = published
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        category = d.pop("category", UNSET)

        def _parse_sender_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_id = _parse_sender_id(d.pop("sender_id", UNSET))

        published = d.pop("published", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        list_templates_response_200_data_item = cls(
            id=id,
            slug=slug,
            name=name,
            description=description,
            category=category,
            sender_id=sender_id,
            published=published,
            updated_at=updated_at,
        )

        list_templates_response_200_data_item.additional_properties = d
        return list_templates_response_200_data_item

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
