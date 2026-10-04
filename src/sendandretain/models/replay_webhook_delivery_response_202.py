from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplayWebhookDeliveryResponse202")


@_attrs_define
class ReplayWebhookDeliveryResponse202:
    """
    Attributes:
        delivery_id (str | Unset):
    """

    delivery_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delivery_id = self.delivery_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delivery_id is not UNSET:
            field_dict["delivery_id"] = delivery_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivery_id = d.pop("delivery_id", UNSET)

        replay_webhook_delivery_response_202 = cls(
            delivery_id=delivery_id,
        )

        replay_webhook_delivery_response_202.additional_properties = d
        return replay_webhook_delivery_response_202

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
