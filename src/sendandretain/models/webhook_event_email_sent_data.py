from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_event_email_sent_data_detail import WebhookEventEmailSentDataDetail
    from ..models.webhook_message import WebhookMessage


T = TypeVar("T", bound="WebhookEventEmailSentData")


@_attrs_define
class WebhookEventEmailSentData:
    """
    Attributes:
        event_id (None | str):
        message (None | WebhookMessage):
        detail (WebhookEventEmailSentDataDetail): Provider detail, normalised. Fields are present only when the provider
            reported them.
    """

    event_id: None | str
    message: None | WebhookMessage
    detail: WebhookEventEmailSentDataDetail
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_message import WebhookMessage

        event_id: None | str
        event_id = self.event_id

        message: dict[str, Any] | None
        if isinstance(self.message, WebhookMessage):
            message = self.message.to_dict()
        else:
            message = self.message

        detail = self.detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_id": event_id,
                "message": message,
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_email_sent_data_detail import WebhookEventEmailSentDataDetail
        from ..models.webhook_message import WebhookMessage

        d = dict(src_dict)

        def _parse_event_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        event_id = _parse_event_id(d.pop("event_id"))

        def _parse_message(data: object) -> None | WebhookMessage:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_0 = WebhookMessage.from_dict(data)

                return message_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WebhookMessage, data)

        message = _parse_message(d.pop("message"))

        detail = WebhookEventEmailSentDataDetail.from_dict(d.pop("detail"))

        webhook_event_email_sent_data = cls(
            event_id=event_id,
            message=message,
            detail=detail,
        )

        webhook_event_email_sent_data.additional_properties = d
        return webhook_event_email_sent_data

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
