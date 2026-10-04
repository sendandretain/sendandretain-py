from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_automation_metrics_response_200_ab_tests_item_arms_item import (
        GetAutomationMetricsResponse200AbTestsItemArmsItem,
    )


T = TypeVar("T", bound="GetAutomationMetricsResponse200AbTestsItem")


@_attrs_define
class GetAutomationMetricsResponse200AbTestsItem:
    """
    Attributes:
        step (str | Unset):
        leader (None | str | Unset):
        reason (None | str | Unset):
        arms (list[GetAutomationMetricsResponse200AbTestsItemArmsItem] | Unset):
    """

    step: str | Unset = UNSET
    leader: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    arms: list[GetAutomationMetricsResponse200AbTestsItemArmsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        step = self.step

        leader: None | str | Unset
        if isinstance(self.leader, Unset):
            leader = UNSET
        else:
            leader = self.leader

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        arms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.arms, Unset):
            arms = []
            for arms_item_data in self.arms:
                arms_item = arms_item_data.to_dict()
                arms.append(arms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if step is not UNSET:
            field_dict["step"] = step
        if leader is not UNSET:
            field_dict["leader"] = leader
        if reason is not UNSET:
            field_dict["reason"] = reason
        if arms is not UNSET:
            field_dict["arms"] = arms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_automation_metrics_response_200_ab_tests_item_arms_item import (
            GetAutomationMetricsResponse200AbTestsItemArmsItem,
        )

        d = dict(src_dict)
        step = d.pop("step", UNSET)

        def _parse_leader(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        leader = _parse_leader(d.pop("leader", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        _arms = d.pop("arms", UNSET)
        arms: list[GetAutomationMetricsResponse200AbTestsItemArmsItem] | Unset = UNSET
        if _arms is not UNSET:
            arms = []
            for arms_item_data in _arms:
                arms_item = GetAutomationMetricsResponse200AbTestsItemArmsItem.from_dict(arms_item_data)

                arms.append(arms_item)

        get_automation_metrics_response_200_ab_tests_item = cls(
            step=step,
            leader=leader,
            reason=reason,
            arms=arms,
        )

        get_automation_metrics_response_200_ab_tests_item.additional_properties = d
        return get_automation_metrics_response_200_ab_tests_item

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
