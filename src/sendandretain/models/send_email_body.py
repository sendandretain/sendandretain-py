from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_email_body_attachments_item import SendEmailBodyAttachmentsItem
    from ..models.send_email_body_headers import SendEmailBodyHeaders
    from ..models.send_email_body_props import SendEmailBodyProps
    from ..models.send_email_body_tags_item import SendEmailBodyTagsItem


T = TypeVar("T", bound="SendEmailBody")


@_attrs_define
class SendEmailBody:
    """
    Attributes:
        to (str): Recipient email address. Single recipient — there are no bulk sends.
        template (str): Slug of a published template in this project.
        cc (list[str] | str | Unset): Carbon-copy recipient(s) of the same message — a string or array. Not a way to
            bulk-send.
        bcc (list[str] | str | Unset): Blind-carbon-copy recipient(s) — a string or array.
        props (SendEmailBodyProps | Unset): Values for the template's variables.
        locale (str | Unset): Deliver a published translation for this locale (e.g. `fr`, `pt-BR`); falls back to the
            base language when no translation exists.
        from_ (str | Unset): Sender, as `Name <addr@domain>` or a bare address. The address must be on a verified
            sending domain in this project. Omit to use the project's default sender.
        reply_to (list[str] | str | Unset): Reply-To address(es) — a string or array.
        headers (SendEmailBodyHeaders | Unset): Custom email headers. Reserved headers (List-Unsubscribe, Idempotency-
            Key, Cc/Bcc/Reply-To) are rejected.
        tags (list[SendEmailBodyTagsItem] | Unset): Up to 10 {name,value} metadata tags, forwarded to the provider for
            analytics.
        scheduled_at (str | Unset): ISO 8601 timestamp, or natural language like `in 2 hours` / `tomorrow 9am`. A future
            value schedules the send via the worker. Cannot be combined with attachments. Manage with PATCH (reschedule) /
            DELETE (cancel).
        attachments (list[SendEmailBodyAttachmentsItem] | Unset): Up to 10 attachments (base64 content). Total ≤ ~5 MB.
            Cannot be combined with scheduled_at.
    """

    to: str
    template: str
    cc: list[str] | str | Unset = UNSET
    bcc: list[str] | str | Unset = UNSET
    props: SendEmailBodyProps | Unset = UNSET
    locale: str | Unset = UNSET
    from_: str | Unset = UNSET
    reply_to: list[str] | str | Unset = UNSET
    headers: SendEmailBodyHeaders | Unset = UNSET
    tags: list[SendEmailBodyTagsItem] | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    attachments: list[SendEmailBodyAttachmentsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to = self.to

        template = self.template

        cc: list[str] | str | Unset
        if isinstance(self.cc, Unset):
            cc = UNSET
        elif isinstance(self.cc, list):
            cc = self.cc

        else:
            cc = self.cc

        bcc: list[str] | str | Unset
        if isinstance(self.bcc, Unset):
            bcc = UNSET
        elif isinstance(self.bcc, list):
            bcc = self.bcc

        else:
            bcc = self.bcc

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        locale = self.locale

        from_ = self.from_

        reply_to: list[str] | str | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        elif isinstance(self.reply_to, list):
            reply_to = self.reply_to

        else:
            reply_to = self.reply_to

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        scheduled_at = self.scheduled_at

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
                "template": template,
            }
        )
        if cc is not UNSET:
            field_dict["cc"] = cc
        if bcc is not UNSET:
            field_dict["bcc"] = bcc
        if props is not UNSET:
            field_dict["props"] = props
        if locale is not UNSET:
            field_dict["locale"] = locale
        if from_ is not UNSET:
            field_dict["from"] = from_
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if headers is not UNSET:
            field_dict["headers"] = headers
        if tags is not UNSET:
            field_dict["tags"] = tags
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_email_body_attachments_item import SendEmailBodyAttachmentsItem
        from ..models.send_email_body_headers import SendEmailBodyHeaders
        from ..models.send_email_body_props import SendEmailBodyProps
        from ..models.send_email_body_tags_item import SendEmailBodyTagsItem

        d = dict(src_dict)
        to = d.pop("to")

        template = d.pop("template")

        def _parse_cc(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cc_type_1 = cast(list[str], data)

                return cc_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        cc = _parse_cc(d.pop("cc", UNSET))

        def _parse_bcc(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bcc_type_1 = cast(list[str], data)

                return bcc_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        bcc = _parse_bcc(d.pop("bcc", UNSET))

        _props = d.pop("props", UNSET)
        props: SendEmailBodyProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = SendEmailBodyProps.from_dict(_props)

        locale = d.pop("locale", UNSET)

        from_ = d.pop("from", UNSET)

        def _parse_reply_to(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reply_to_type_1 = cast(list[str], data)

                return reply_to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        _headers = d.pop("headers", UNSET)
        headers: SendEmailBodyHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = SendEmailBodyHeaders.from_dict(_headers)

        _tags = d.pop("tags", UNSET)
        tags: list[SendEmailBodyTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = SendEmailBodyTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        scheduled_at = d.pop("scheduled_at", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[SendEmailBodyAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = SendEmailBodyAttachmentsItem.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        send_email_body = cls(
            to=to,
            template=template,
            cc=cc,
            bcc=bcc,
            props=props,
            locale=locale,
            from_=from_,
            reply_to=reply_to,
            headers=headers,
            tags=tags,
            scheduled_at=scheduled_at,
            attachments=attachments,
        )

        send_email_body.additional_properties = d
        return send_email_body

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
