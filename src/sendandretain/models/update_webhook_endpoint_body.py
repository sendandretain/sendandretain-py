from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookEndpointBody")


@_attrs_define
class UpdateWebhookEndpointBody:
    """
    Attributes:
        url (str | Unset): Replacement URL. Re-validated on save.
        event_types (list[str] | Unset): Replacement subscription list. Not merged with the old one.
        description (None | str | Unset):
        enabled (bool | Unset): `false` pauses delivery without losing the endpoint or its secret. `true` resumes it AND
            clears the consecutive-failure count.
    """

    url: str | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        event_types = cast(list[str], d.pop("event_types", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        update_webhook_endpoint_body = cls(
            url=url,
            event_types=event_types,
            description=description,
            enabled=enabled,
        )

        update_webhook_endpoint_body.additional_properties = d
        return update_webhook_endpoint_body

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
