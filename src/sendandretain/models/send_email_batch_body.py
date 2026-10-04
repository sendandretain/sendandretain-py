from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.send_email_batch_body_emails_item import SendEmailBatchBodyEmailsItem


T = TypeVar("T", bound="SendEmailBatchBody")


@_attrs_define
class SendEmailBatchBody:
    """
    Attributes:
        emails (list[SendEmailBatchBodyEmailsItem]): Up to 100 distinct messages, each with its own recipient and
            template. Results come back in this order.
    """

    emails: list[SendEmailBatchBodyEmailsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()
            emails.append(emails_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_email_batch_body_emails_item import SendEmailBatchBodyEmailsItem

        d = dict(src_dict)
        emails = []
        _emails = d.pop("emails")
        for emails_item_data in _emails:
            emails_item = SendEmailBatchBodyEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        send_email_batch_body = cls(
            emails=emails,
        )

        send_email_batch_body.additional_properties = d
        return send_email_batch_body

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
