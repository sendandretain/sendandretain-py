from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookEndpointBody")


@_attrs_define
class CreateWebhookEndpointBody:
    """
    Attributes:
        url (str): HTTPS endpoint that receives the events. Must resolve to a public address — private ranges, localhost
            and non-default ports are refused, and the check is repeated before every delivery.
        event_types (list[str]): Events to receive. Subscribe to `webhook.test` as well so you can verify the endpoint
            before real mail flows.
        description (None | str | Unset): Your own label. Never sent to the endpoint.
    """

    url: str
    event_types: list[str]
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        event_types = self.event_types

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "event_types": event_types,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        event_types = cast(list[str], d.pop("event_types"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        create_webhook_endpoint_body = cls(
            url=url,
            event_types=event_types,
            description=description,
        )

        create_webhook_endpoint_body.additional_properties = d
        return create_webhook_endpoint_body

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
