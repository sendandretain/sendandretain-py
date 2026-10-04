from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_template_response_200_status import UpdateTemplateResponse200Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTemplateResponse200")


@_attrs_define
class UpdateTemplateResponse200:
    """
    Attributes:
        slug (str | Unset):
        version (int | Unset):
        status (UpdateTemplateResponse200Status | Unset):
    """

    slug: str | Unset = UNSET
    version: int | Unset = UNSET
    status: UpdateTemplateResponse200Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        version = self.version

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        slug = d.pop("slug", UNSET)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: UpdateTemplateResponse200Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateTemplateResponse200Status(_status)

        update_template_response_200 = cls(
            slug=slug,
            version=version,
            status=status,
        )

        update_template_response_200.additional_properties = d
        return update_template_response_200

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
