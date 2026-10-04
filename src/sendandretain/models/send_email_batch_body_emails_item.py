from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_email_batch_body_emails_item_attachments_item import SendEmailBatchBodyEmailsItemAttachmentsItem
    from ..models.send_email_batch_body_emails_item_headers import SendEmailBatchBodyEmailsItemHeaders
    from ..models.send_email_batch_body_emails_item_props import SendEmailBatchBodyEmailsItemProps
    from ..models.send_email_batch_body_emails_item_tags_item import SendEmailBatchBodyEmailsItemTagsItem


T = TypeVar("T", bound="SendEmailBatchBodyEmailsItem")


@_attrs_define
class SendEmailBatchBodyEmailsItem:
    """
    Attributes:
        to (str):
        template (str):
        cc (list[str] | str | Unset):
        bcc (list[str] | str | Unset):
        props (SendEmailBatchBodyEmailsItemProps | Unset):
        locale (str | Unset):
        from_ (str | Unset):
        reply_to (list[str] | str | Unset):
        headers (SendEmailBatchBodyEmailsItemHeaders | Unset):
        tags (list[SendEmailBatchBodyEmailsItemTagsItem] | Unset):
        scheduled_at (str | Unset):
        attachments (list[SendEmailBatchBodyEmailsItemAttachmentsItem] | Unset):
        idempotency_key (str | Unset):
    """

    to: str
    template: str
    cc: list[str] | str | Unset = UNSET
    bcc: list[str] | str | Unset = UNSET
    props: SendEmailBatchBodyEmailsItemProps | Unset = UNSET
    locale: str | Unset = UNSET
    from_: str | Unset = UNSET
    reply_to: list[str] | str | Unset = UNSET
    headers: SendEmailBatchBodyEmailsItemHeaders | Unset = UNSET
    tags: list[SendEmailBatchBodyEmailsItemTagsItem] | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    attachments: list[SendEmailBatchBodyEmailsItemAttachmentsItem] | Unset = UNSET
    idempotency_key: str | Unset = UNSET
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

        idempotency_key = self.idempotency_key

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
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_email_batch_body_emails_item_attachments_item import (
            SendEmailBatchBodyEmailsItemAttachmentsItem,
        )
        from ..models.send_email_batch_body_emails_item_headers import SendEmailBatchBodyEmailsItemHeaders
        from ..models.send_email_batch_body_emails_item_props import SendEmailBatchBodyEmailsItemProps
        from ..models.send_email_batch_body_emails_item_tags_item import SendEmailBatchBodyEmailsItemTagsItem

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
        props: SendEmailBatchBodyEmailsItemProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = SendEmailBatchBodyEmailsItemProps.from_dict(_props)

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
        headers: SendEmailBatchBodyEmailsItemHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = SendEmailBatchBodyEmailsItemHeaders.from_dict(_headers)

        _tags = d.pop("tags", UNSET)
        tags: list[SendEmailBatchBodyEmailsItemTagsItem] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = SendEmailBatchBodyEmailsItemTagsItem.from_dict(tags_item_data)

                tags.append(tags_item)

        scheduled_at = d.pop("scheduled_at", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[SendEmailBatchBodyEmailsItemAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = SendEmailBatchBodyEmailsItemAttachmentsItem.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        idempotency_key = d.pop("idempotency_key", UNSET)

        send_email_batch_body_emails_item = cls(
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
            idempotency_key=idempotency_key,
        )

        send_email_batch_body_emails_item.additional_properties = d
        return send_email_batch_body_emails_item

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
