from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_template_translation_response_201_status import AddTemplateTranslationResponse201Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTemplateTranslationResponse201")


@_attrs_define
class AddTemplateTranslationResponse201:
    """
    Attributes:
        slug (str | Unset):
        locale (str | Unset):
        version (int | Unset):
        status (AddTemplateTranslationResponse201Status | Unset):
    """

    slug: str | Unset = UNSET
    locale: str | Unset = UNSET
    version: int | Unset = UNSET
    status: AddTemplateTranslationResponse201Status | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        locale = self.locale

        version = self.version

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if locale is not UNSET:
            field_dict["locale"] = locale
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        locale = d.pop("locale", UNSET)

        version = d.pop("version", UNSET)

        _status = d.pop("status", UNSET)
        status: AddTemplateTranslationResponse201Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AddTemplateTranslationResponse201Status(_status)

        add_template_translation_response_201 = cls(
            slug=slug,
            locale=locale,
            version=version,
            status=status,
        )

        add_template_translation_response_201.additional_properties = d
        return add_template_translation_response_201

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
