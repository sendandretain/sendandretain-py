from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event_email_canceled_type import WebhookEventEmailCanceledType
from ..models.webhook_event_email_canceled_version import WebhookEventEmailCanceledVersion

if TYPE_CHECKING:
    from ..models.webhook_event_email_canceled_data import WebhookEventEmailCanceledData


T = TypeVar("T", bound="WebhookEventEmailCanceled")


@_attrs_define
class WebhookEventEmailCanceled:
    """A scheduled send was canceled.

    Attributes:
        id (str): The delivery id — also sent as `webhook-id`. Dedupe on it.
        type_ (WebhookEventEmailCanceledType):
        version (WebhookEventEmailCanceledVersion):
        created_at (datetime.datetime): When we queued it.
        occurred_at (datetime.datetime): When it happened. Order on this, never on arrival.
        data (WebhookEventEmailCanceledData):
    """

    id: str
    type_: WebhookEventEmailCanceledType
    version: WebhookEventEmailCanceledVersion
    created_at: datetime.datetime
    occurred_at: datetime.datetime
    data: WebhookEventEmailCanceledData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        version = self.version.value

        created_at = self.created_at.isoformat()

        occurred_at = self.occurred_at.isoformat()

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "version": version,
                "created_at": created_at,
                "occurred_at": occurred_at,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_event_email_canceled_data import WebhookEventEmailCanceledData

        d = dict(src_dict)
        id = d.pop("id")

        type_ = WebhookEventEmailCanceledType(d.pop("type"))

        version = WebhookEventEmailCanceledVersion(d.pop("version"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        data = WebhookEventEmailCanceledData.from_dict(d.pop("data"))

        webhook_event_email_canceled = cls(
            id=id,
            type_=type_,
            version=version,
            created_at=created_at,
            occurred_at=occurred_at,
            data=data,
        )

        webhook_event_email_canceled.additional_properties = d
        return webhook_event_email_canceled

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
