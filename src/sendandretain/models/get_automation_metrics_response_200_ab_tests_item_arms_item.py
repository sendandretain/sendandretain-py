from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAutomationMetricsResponse200AbTestsItemArmsItem")


@_attrs_define
class GetAutomationMetricsResponse200AbTestsItemArmsItem:
    """
    Attributes:
        variant (str | Unset):
        delivered (int | Unset):
        click_rate_pct (float | Unset):
        open_rate_pct (float | Unset):
    """

    variant: str | Unset = UNSET
    delivered: int | Unset = UNSET
    click_rate_pct: float | Unset = UNSET
    open_rate_pct: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant = self.variant

        delivered = self.delivered

        click_rate_pct = self.click_rate_pct

        open_rate_pct = self.open_rate_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variant is not UNSET:
            field_dict["variant"] = variant
        if delivered is not UNSET:
            field_dict["delivered"] = delivered
        if click_rate_pct is not UNSET:
            field_dict["click_rate_pct"] = click_rate_pct
        if open_rate_pct is not UNSET:
            field_dict["open_rate_pct"] = open_rate_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        variant = d.pop("variant", UNSET)

        delivered = d.pop("delivered", UNSET)

        click_rate_pct = d.pop("click_rate_pct", UNSET)

        open_rate_pct = d.pop("open_rate_pct", UNSET)

        get_automation_metrics_response_200_ab_tests_item_arms_item = cls(
            variant=variant,
            delivered=delivered,
            click_rate_pct=click_rate_pct,
            open_rate_pct=open_rate_pct,
        )

        get_automation_metrics_response_200_ab_tests_item_arms_item.additional_properties = d
        return get_automation_metrics_response_200_ab_tests_item_arms_item

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
