from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_status_events_item import MessageStatusEventsItem


T = TypeVar("T", bound="MessageStatus")


@_attrs_define
class MessageStatus:
    """
    Attributes:
        id (str | Unset):
        to (str | Unset):
        from_ (str | Unset):
        subject (str | Unset):
        template (None | str | Unset):
        status (str | Unset): Latest status on the delivery ladder.
        last_event (None | str | Unset): Type of the newest event in `events`, or null before the first.
        source (str | Unset):
        error (None | str | Unset):
        suppressed_reason (None | str | Unset):
        provider (None | str | Unset):
        provider_message_id (None | str | Unset):
        ab_variant (None | str | Unset):
        scheduled_at (datetime.datetime | None | Unset):
        sent_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
        events (list[MessageStatusEventsItem] | Unset): Provider events for this message, oldest first (max 100).
    """

    id: str | Unset = UNSET
    to: str | Unset = UNSET
    from_: str | Unset = UNSET
    subject: str | Unset = UNSET
    template: None | str | Unset = UNSET
    status: str | Unset = UNSET
    last_event: None | str | Unset = UNSET
    source: str | Unset = UNSET
    error: None | str | Unset = UNSET
    suppressed_reason: None | str | Unset = UNSET
    provider: None | str | Unset = UNSET
    provider_message_id: None | str | Unset = UNSET
    ab_variant: None | str | Unset = UNSET
    scheduled_at: datetime.datetime | None | Unset = UNSET
    sent_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    events: list[MessageStatusEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        to = self.to

        from_ = self.from_

        subject = self.subject

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        status = self.status

        last_event: None | str | Unset
        if isinstance(self.last_event, Unset):
            last_event = UNSET
        else:
            last_event = self.last_event

        source = self.source

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        suppressed_reason: None | str | Unset
        if isinstance(self.suppressed_reason, Unset):
            suppressed_reason = UNSET
        else:
            suppressed_reason = self.suppressed_reason

        provider: None | str | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        else:
            provider = self.provider

        provider_message_id: None | str | Unset
        if isinstance(self.provider_message_id, Unset):
            provider_message_id = UNSET
        else:
            provider_message_id = self.provider_message_id

        ab_variant: None | str | Unset
        if isinstance(self.ab_variant, Unset):
            ab_variant = UNSET
        else:
            ab_variant = self.ab_variant

        scheduled_at: None | str | Unset
        if isinstance(self.scheduled_at, Unset):
            scheduled_at = UNSET
        elif isinstance(self.scheduled_at, datetime.datetime):
            scheduled_at = self.scheduled_at.isoformat()
        else:
            scheduled_at = self.scheduled_at

        sent_at: None | str | Unset
        if isinstance(self.sent_at, Unset):
            sent_at = UNSET
        elif isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if to is not UNSET:
            field_dict["to"] = to
        if from_ is not UNSET:
            field_dict["from"] = from_
        if subject is not UNSET:
            field_dict["subject"] = subject
        if template is not UNSET:
            field_dict["template"] = template
        if status is not UNSET:
            field_dict["status"] = status
        if last_event is not UNSET:
            field_dict["last_event"] = last_event
        if source is not UNSET:
            field_dict["source"] = source
        if error is not UNSET:
            field_dict["error"] = error
        if suppressed_reason is not UNSET:
            field_dict["suppressed_reason"] = suppressed_reason
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_message_id is not UNSET:
            field_dict["provider_message_id"] = provider_message_id
        if ab_variant is not UNSET:
            field_dict["ab_variant"] = ab_variant
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_status_events_item import MessageStatusEventsItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        to = d.pop("to", UNSET)

        from_ = d.pop("from", UNSET)

        subject = d.pop("subject", UNSET)

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        status = d.pop("status", UNSET)

        def _parse_last_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_event = _parse_last_event(d.pop("last_event", UNSET))

        source = d.pop("source", UNSET)

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_suppressed_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suppressed_reason = _parse_suppressed_reason(d.pop("suppressed_reason", UNSET))

        def _parse_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        def _parse_provider_message_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_message_id = _parse_provider_message_id(d.pop("provider_message_id", UNSET))

        def _parse_ab_variant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ab_variant = _parse_ab_variant(d.pop("ab_variant", UNSET))

        def _parse_scheduled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_at_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_at = _parse_scheduled_at(d.pop("scheduled_at", UNSET))

        def _parse_sent_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_at_type_0 = datetime.datetime.fromisoformat(data)

                return sent_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sent_at = _parse_sent_at(d.pop("sent_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _events = d.pop("events", UNSET)
        events: list[MessageStatusEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = MessageStatusEventsItem.from_dict(events_item_data)

                events.append(events_item)

        message_status = cls(
            id=id,
            to=to,
            from_=from_,
            subject=subject,
            template=template,
            status=status,
            last_event=last_event,
            source=source,
            error=error,
            suppressed_reason=suppressed_reason,
            provider=provider,
            provider_message_id=provider_message_id,
            ab_variant=ab_variant,
            scheduled_at=scheduled_at,
            sent_at=sent_at,
            created_at=created_at,
            events=events,
        )

        message_status.additional_properties = d
        return message_status

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
