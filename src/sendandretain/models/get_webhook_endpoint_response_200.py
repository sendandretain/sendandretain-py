from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWebhookEndpointResponse200")


@_attrs_define
class GetWebhookEndpointResponse200:
    """
    Attributes:
        id (str | Unset):
        url (str | Unset):
        description (None | str | Unset):
        event_types (list[str] | Unset):
        enabled (bool | Unset):
        disabled_at (datetime.datetime | None | Unset):
        disabled_reason (None | str | Unset): `consecutive_failures` (auto-disabled after sustained failure), `manual`
            (you disabled it, or the endpoint returned 410 Gone), or `url_unsafe` (the URL stopped resolving to a public
            address).
        secret_hint (str | Unset): Last four characters of the signing secret, so you can tell which one is configured.
            The full secret is returned ONLY when the endpoint is created or its secret is rotated.
        consecutive_failures (int | Unset):
        last_delivery_at (datetime.datetime | None | Unset):
        last_success_at (datetime.datetime | None | Unset):
        last_error (None | str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    url: str | Unset = UNSET
    description: None | str | Unset = UNSET
    event_types: list[str] | Unset = UNSET
    enabled: bool | Unset = UNSET
    disabled_at: datetime.datetime | None | Unset = UNSET
    disabled_reason: None | str | Unset = UNSET
    secret_hint: str | Unset = UNSET
    consecutive_failures: int | Unset = UNSET
    last_delivery_at: datetime.datetime | None | Unset = UNSET
    last_success_at: datetime.datetime | None | Unset = UNSET
    last_error: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        event_types: list[str] | Unset = UNSET
        if not isinstance(self.event_types, Unset):
            event_types = self.event_types

        enabled = self.enabled

        disabled_at: None | str | Unset
        if isinstance(self.disabled_at, Unset):
            disabled_at = UNSET
        elif isinstance(self.disabled_at, datetime.datetime):
            disabled_at = self.disabled_at.isoformat()
        else:
            disabled_at = self.disabled_at

        disabled_reason: None | str | Unset
        if isinstance(self.disabled_reason, Unset):
            disabled_reason = UNSET
        else:
            disabled_reason = self.disabled_reason

        secret_hint = self.secret_hint

        consecutive_failures = self.consecutive_failures

        last_delivery_at: None | str | Unset
        if isinstance(self.last_delivery_at, Unset):
            last_delivery_at = UNSET
        elif isinstance(self.last_delivery_at, datetime.datetime):
            last_delivery_at = self.last_delivery_at.isoformat()
        else:
            last_delivery_at = self.last_delivery_at

        last_success_at: None | str | Unset
        if isinstance(self.last_success_at, Unset):
            last_success_at = UNSET
        elif isinstance(self.last_success_at, datetime.datetime):
            last_success_at = self.last_success_at.isoformat()
        else:
            last_success_at = self.last_success_at

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if event_types is not UNSET:
            field_dict["event_types"] = event_types
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
        if disabled_reason is not UNSET:
            field_dict["disabled_reason"] = disabled_reason
        if secret_hint is not UNSET:
            field_dict["secret_hint"] = secret_hint
        if consecutive_failures is not UNSET:
            field_dict["consecutive_failures"] = consecutive_failures
        if last_delivery_at is not UNSET:
            field_dict["last_delivery_at"] = last_delivery_at
        if last_success_at is not UNSET:
            field_dict["last_success_at"] = last_success_at
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        url = d.pop("url", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        event_types = cast(list[str], d.pop("event_types", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_disabled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_at_type_0 = datetime.datetime.fromisoformat(data)

                return disabled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        disabled_at = _parse_disabled_at(d.pop("disabled_at", UNSET))

        def _parse_disabled_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disabled_reason = _parse_disabled_reason(d.pop("disabled_reason", UNSET))

        secret_hint = d.pop("secret_hint", UNSET)

        consecutive_failures = d.pop("consecutive_failures", UNSET)

        def _parse_last_delivery_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_delivery_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_delivery_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("last_delivery_at", UNSET))

        def _parse_last_success_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_success_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_success_at = _parse_last_success_at(d.pop("last_success_at", UNSET))

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        get_webhook_endpoint_response_200 = cls(
            id=id,
            url=url,
            description=description,
            event_types=event_types,
            enabled=enabled,
            disabled_at=disabled_at,
            disabled_reason=disabled_reason,
            secret_hint=secret_hint,
            consecutive_failures=consecutive_failures,
            last_delivery_at=last_delivery_at,
            last_success_at=last_success_at,
            last_error=last_error,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_webhook_endpoint_response_200.additional_properties = d
        return get_webhook_endpoint_response_200

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
