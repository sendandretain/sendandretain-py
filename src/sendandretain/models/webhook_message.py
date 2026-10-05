from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_message_tags_type_0_item import WebhookMessageTagsType0Item


T = TypeVar("T", bound="WebhookMessage")


@_attrs_define
class WebhookMessage:
    """The message the event is about.

    Attributes:
        id (str):
        to (str):
        from_ (str):
        status (str):
        source (str):
        created_at (datetime.datetime):
        subject (None | str | Unset):
        template (None | str | Unset):
        tags (list[WebhookMessageTagsType0Item] | None | Unset):
        sent_at (datetime.datetime | None | Unset):
    """

    id: str
    to: str
    from_: str
    status: str
    source: str
    created_at: datetime.datetime
    subject: None | str | Unset = UNSET
    template: None | str | Unset = UNSET
    tags: list[WebhookMessageTagsType0Item] | None | Unset = UNSET
    sent_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        to = self.to

        from_ = self.from_

        status = self.status

        source = self.source

        created_at = self.created_at.isoformat()

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        tags: list[dict[str, Any]] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        sent_at: None | str | Unset
        if isinstance(self.sent_at, Unset):
            sent_at = UNSET
        elif isinstance(self.sent_at, datetime.datetime):
            sent_at = self.sent_at.isoformat()
        else:
            sent_at = self.sent_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "to": to,
                "from": from_,
                "status": status,
                "source": source,
                "created_at": created_at,
            }
        )
        if subject is not UNSET:
            field_dict["subject"] = subject
        if template is not UNSET:
            field_dict["template"] = template
        if tags is not UNSET:
            field_dict["tags"] = tags
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_message_tags_type_0_item import WebhookMessageTagsType0Item

        d = dict(src_dict)
        id = d.pop("id")

        to = d.pop("to")

        from_ = d.pop("from")

        status = d.pop("status")

        source = d.pop("source")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_tags(data: object) -> list[WebhookMessageTagsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = WebhookMessageTagsType0Item.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WebhookMessageTagsType0Item] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

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

        webhook_message = cls(
            id=id,
            to=to,
            from_=from_,
            status=status,
            source=source,
            created_at=created_at,
            subject=subject,
            template=template,
            tags=tags,
            sent_at=sent_at,
        )

        webhook_message.additional_properties = d
        return webhook_message

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
