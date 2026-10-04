from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListTemplateVersionsResponse200DataItem")


@_attrs_define
class ListTemplateVersionsResponse200DataItem:
    """
    Attributes:
        version (int | Unset):
        status (str | Unset):
        subject (str | Unset):
        variant_key (None | str | Unset):
        locale (None | str | Unset):
        is_current (bool | Unset):
        created_at (datetime.datetime | Unset):
    """

    version: int | Unset = UNSET
    status: str | Unset = UNSET
    subject: str | Unset = UNSET
    variant_key: None | str | Unset = UNSET
    locale: None | str | Unset = UNSET
    is_current: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        status = self.status

        subject = self.subject

        variant_key: None | str | Unset
        if isinstance(self.variant_key, Unset):
            variant_key = UNSET
        else:
            variant_key = self.variant_key

        locale: None | str | Unset
        if isinstance(self.locale, Unset):
            locale = UNSET
        else:
            locale = self.locale

        is_current = self.is_current

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if subject is not UNSET:
            field_dict["subject"] = subject
        if variant_key is not UNSET:
            field_dict["variant_key"] = variant_key
        if locale is not UNSET:
            field_dict["locale"] = locale
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version", UNSET)

        status = d.pop("status", UNSET)

        subject = d.pop("subject", UNSET)

        def _parse_variant_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variant_key = _parse_variant_key(d.pop("variant_key", UNSET))

        def _parse_locale(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locale = _parse_locale(d.pop("locale", UNSET))

        is_current = d.pop("is_current", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        list_template_versions_response_200_data_item = cls(
            version=version,
            status=status,
            subject=subject,
            variant_key=variant_key,
            locale=locale,
            is_current=is_current,
            created_at=created_at,
        )

        list_template_versions_response_200_data_item.additional_properties = d
        return list_template_versions_response_200_data_item

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
