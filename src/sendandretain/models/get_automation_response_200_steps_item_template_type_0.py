from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAutomationResponse200StepsItemTemplateType0")


@_attrs_define
class GetAutomationResponse200StepsItemTemplateType0:
    """What a send step sends: the template's LIVE version, against the latest base version. `has_unpublished_changes`
    means a newer draft exists that no contact receives until it is published.

        Attributes:
            live_version (int | None | Unset):
            live_subject (None | str | Unset):
            latest_version (int | None | Unset):
            latest_subject (None | str | Unset):
            has_unpublished_changes (bool | Unset):
    """

    live_version: int | None | Unset = UNSET
    live_subject: None | str | Unset = UNSET
    latest_version: int | None | Unset = UNSET
    latest_subject: None | str | Unset = UNSET
    has_unpublished_changes: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        live_version: int | None | Unset
        if isinstance(self.live_version, Unset):
            live_version = UNSET
        else:
            live_version = self.live_version

        live_subject: None | str | Unset
        if isinstance(self.live_subject, Unset):
            live_subject = UNSET
        else:
            live_subject = self.live_subject

        latest_version: int | None | Unset
        if isinstance(self.latest_version, Unset):
            latest_version = UNSET
        else:
            latest_version = self.latest_version

        latest_subject: None | str | Unset
        if isinstance(self.latest_subject, Unset):
            latest_subject = UNSET
        else:
            latest_subject = self.latest_subject

        has_unpublished_changes = self.has_unpublished_changes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if live_version is not UNSET:
            field_dict["live_version"] = live_version
        if live_subject is not UNSET:
            field_dict["live_subject"] = live_subject
        if latest_version is not UNSET:
            field_dict["latest_version"] = latest_version
        if latest_subject is not UNSET:
            field_dict["latest_subject"] = latest_subject
        if has_unpublished_changes is not UNSET:
            field_dict["has_unpublished_changes"] = has_unpublished_changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_live_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        live_version = _parse_live_version(d.pop("live_version", UNSET))

        def _parse_live_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        live_subject = _parse_live_subject(d.pop("live_subject", UNSET))

        def _parse_latest_version(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_version = _parse_latest_version(d.pop("latest_version", UNSET))

        def _parse_latest_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_subject = _parse_latest_subject(d.pop("latest_subject", UNSET))

        has_unpublished_changes = d.pop("has_unpublished_changes", UNSET)

        get_automation_response_200_steps_item_template_type_0 = cls(
            live_version=live_version,
            live_subject=live_subject,
            latest_version=latest_version,
            latest_subject=latest_subject,
            has_unpublished_changes=has_unpublished_changes,
        )

        get_automation_response_200_steps_item_template_type_0.additional_properties = d
        return get_automation_response_200_steps_item_template_type_0

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
