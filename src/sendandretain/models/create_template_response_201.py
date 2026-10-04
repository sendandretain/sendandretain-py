from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_template_response_201_status import CreateTemplateResponse201Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTemplateResponse201")


@_attrs_define
class CreateTemplateResponse201:
    """
    Attributes:
        id (str | Unset):
        slug (str | Unset):
        version (int | Unset):
        status (CreateTemplateResponse201Status | Unset):
    """

    id: str | Unset = UNSET
    slug: str | Unset = UNSET
    version: int | Unset = UNSET
    status: CreateTemplateResponse201Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        version = self.version

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: CreateTemplateResponse201Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateTemplateResponse201Status(_status)

        create_template_response_201 = cls(
            id=id,
            slug=slug,
            version=version,
            status=status,
        )

        create_template_response_201.additional_properties = d
        return create_template_response_201

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
