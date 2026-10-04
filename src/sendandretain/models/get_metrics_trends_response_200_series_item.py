from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMetricsTrendsResponse200SeriesItem")


@_attrs_define
class GetMetricsTrendsResponse200SeriesItem:
    """
    Attributes:
        day (str | Unset):
        sent (int | Unset):
        delivered (int | Unset):
        opened (int | Unset):
        clicked (int | Unset):
        bounced (int | Unset):
        complained (int | Unset):
        unsubscribed (int | Unset):
    """

    day: str | Unset = UNSET
    sent: int | Unset = UNSET
    delivered: int | Unset = UNSET
    opened: int | Unset = UNSET
    clicked: int | Unset = UNSET
    bounced: int | Unset = UNSET
    complained: int | Unset = UNSET
    unsubscribed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        sent = self.sent

        delivered = self.delivered

        opened = self.opened

        clicked = self.clicked

        bounced = self.bounced

        complained = self.complained

        unsubscribed = self.unsubscribed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if sent is not UNSET:
            field_dict["sent"] = sent
        if delivered is not UNSET:
            field_dict["delivered"] = delivered
        if opened is not UNSET:
            field_dict["opened"] = opened
        if clicked is not UNSET:
            field_dict["clicked"] = clicked
        if bounced is not UNSET:
            field_dict["bounced"] = bounced
        if complained is not UNSET:
            field_dict["complained"] = complained
        if unsubscribed is not UNSET:
            field_dict["unsubscribed"] = unsubscribed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        day = d.pop("day", UNSET)

        sent = d.pop("sent", UNSET)

        delivered = d.pop("delivered", UNSET)

        opened = d.pop("opened", UNSET)

        clicked = d.pop("clicked", UNSET)

        bounced = d.pop("bounced", UNSET)

        complained = d.pop("complained", UNSET)

        unsubscribed = d.pop("unsubscribed", UNSET)

        get_metrics_trends_response_200_series_item = cls(
            day=day,
            sent=sent,
            delivered=delivered,
            opened=opened,
            clicked=clicked,
            bounced=bounced,
            complained=complained,
            unsubscribed=unsubscribed,
        )

        get_metrics_trends_response_200_series_item.additional_properties = d
        return get_metrics_trends_response_200_series_item

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
