from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListWebhookDeliveriesResponse200DataItem")


@_attrs_define
class ListWebhookDeliveriesResponse200DataItem:
    """
    Attributes:
        id (str | Unset): Also the `webhook-id` header. Stable across retries — dedupe on it.
        event_type (str | Unset):
        message_id (None | str | Unset):
        status (str | Unset): `pending` (queued or backing off), `in_flight`, `delivered`, `failed` (attempts
            exhausted), `skipped` (endpoint disabled, unsubscribed, or returned 410).
        attempt (int | Unset):
        last_status_code (int | Unset):
        last_error (None | str | Unset):
        response_snippet (None | str | Unset): First 2 KB of your endpoint's response body — usually the whole answer.
        duration_ms (int | Unset):
        next_attempt_at (datetime.datetime | None | Unset):
        delivered_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
    """

    id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    message_id: None | str | Unset = UNSET
    status: str | Unset = UNSET
    attempt: int | Unset = UNSET
    last_status_code: int | Unset = UNSET
    last_error: None | str | Unset = UNSET
    response_snippet: None | str | Unset = UNSET
    duration_ms: int | Unset = UNSET
    next_attempt_at: datetime.datetime | None | Unset = UNSET
    delivered_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_type = self.event_type

        message_id: None | str | Unset
        if isinstance(self.message_id, Unset):
            message_id = UNSET
        else:
            message_id = self.message_id

        status = self.status

        attempt = self.attempt

        last_status_code = self.last_status_code

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        response_snippet: None | str | Unset
        if isinstance(self.response_snippet, Unset):
            response_snippet = UNSET
        else:
            response_snippet = self.response_snippet

        duration_ms = self.duration_ms

        next_attempt_at: None | str | Unset
        if isinstance(self.next_attempt_at, Unset):
            next_attempt_at = UNSET
        elif isinstance(self.next_attempt_at, datetime.datetime):
            next_attempt_at = self.next_attempt_at.isoformat()
        else:
            next_attempt_at = self.next_attempt_at

        delivered_at: None | str | Unset
        if isinstance(self.delivered_at, Unset):
            delivered_at = UNSET
        elif isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if status is not UNSET:
            field_dict["status"] = status
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if last_status_code is not UNSET:
            field_dict["last_status_code"] = last_status_code
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if response_snippet is not UNSET:
            field_dict["response_snippet"] = response_snippet
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if next_attempt_at is not UNSET:
            field_dict["next_attempt_at"] = next_attempt_at
        if delivered_at is not UNSET:
            field_dict["delivered_at"] = delivered_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        event_type = d.pop("event_type", UNSET)

        def _parse_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message_id = _parse_message_id(d.pop("message_id", UNSET))

        status = d.pop("status", UNSET)

        attempt = d.pop("attempt", UNSET)

        last_status_code = d.pop("last_status_code", UNSET)

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        def _parse_response_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_snippet = _parse_response_snippet(d.pop("response_snippet", UNSET))

        duration_ms = d.pop("duration_ms", UNSET)

        def _parse_next_attempt_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_attempt_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_attempt_at = _parse_next_attempt_at(d.pop("next_attempt_at", UNSET))

        def _parse_delivered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = datetime.datetime.fromisoformat(data)

                return delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        list_webhook_deliveries_response_200_data_item = cls(
            id=id,
            event_type=event_type,
            message_id=message_id,
            status=status,
            attempt=attempt,
            last_status_code=last_status_code,
            last_error=last_error,
            response_snippet=response_snippet,
            duration_ms=duration_ms,
            next_attempt_at=next_attempt_at,
            delivered_at=delivered_at,
            created_at=created_at,
        )

        list_webhook_deliveries_response_200_data_item.additional_properties = d
        return list_webhook_deliveries_response_200_data_item

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
