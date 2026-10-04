from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_automation_metrics_response_200_ab_tests_item import GetAutomationMetricsResponse200AbTestsItem
    from ..models.get_automation_metrics_response_200_by_step import GetAutomationMetricsResponse200ByStep
    from ..models.get_automation_metrics_response_200_by_variant import GetAutomationMetricsResponse200ByVariant
    from ..models.get_automation_metrics_response_200_run_counts import GetAutomationMetricsResponse200RunCounts


T = TypeVar("T", bound="GetAutomationMetricsResponse200")


@_attrs_define
class GetAutomationMetricsResponse200:
    """
    Attributes:
        since (datetime.datetime | Unset):
        run_counts (GetAutomationMetricsResponse200RunCounts | Unset):
        by_step (GetAutomationMetricsResponse200ByStep | Unset): Keyed by `step N`.
        by_variant (GetAutomationMetricsResponse200ByVariant | Unset): Keyed by `step N / variant`.
        ab_tests (list[GetAutomationMetricsResponse200AbTestsItem] | Unset):
    """

    since: datetime.datetime | Unset = UNSET
    run_counts: GetAutomationMetricsResponse200RunCounts | Unset = UNSET
    by_step: GetAutomationMetricsResponse200ByStep | Unset = UNSET
    by_variant: GetAutomationMetricsResponse200ByVariant | Unset = UNSET
    ab_tests: list[GetAutomationMetricsResponse200AbTestsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()

        run_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.run_counts, Unset):
            run_counts = self.run_counts.to_dict()

        by_step: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_step, Unset):
            by_step = self.by_step.to_dict()

        by_variant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_variant, Unset):
            by_variant = self.by_variant.to_dict()

        ab_tests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ab_tests, Unset):
            ab_tests = []
            for ab_tests_item_data in self.ab_tests:
                ab_tests_item = ab_tests_item_data.to_dict()
                ab_tests.append(ab_tests_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if since is not UNSET:
            field_dict["since"] = since
        if run_counts is not UNSET:
            field_dict["run_counts"] = run_counts
        if by_step is not UNSET:
            field_dict["by_step"] = by_step
        if by_variant is not UNSET:
            field_dict["by_variant"] = by_variant
        if ab_tests is not UNSET:
            field_dict["ab_tests"] = ab_tests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_automation_metrics_response_200_ab_tests_item import (
            GetAutomationMetricsResponse200AbTestsItem,
        )
        from ..models.get_automation_metrics_response_200_by_step import GetAutomationMetricsResponse200ByStep
        from ..models.get_automation_metrics_response_200_by_variant import GetAutomationMetricsResponse200ByVariant
        from ..models.get_automation_metrics_response_200_run_counts import GetAutomationMetricsResponse200RunCounts

        d = dict(src_dict)
        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since, Unset):
            since = UNSET
        else:
            since = datetime.datetime.fromisoformat(_since)

        _run_counts = d.pop("run_counts", UNSET)
        run_counts: GetAutomationMetricsResponse200RunCounts | Unset
        if isinstance(_run_counts, Unset):
            run_counts = UNSET
        else:
            run_counts = GetAutomationMetricsResponse200RunCounts.from_dict(_run_counts)

        _by_step = d.pop("by_step", UNSET)
        by_step: GetAutomationMetricsResponse200ByStep | Unset
        if isinstance(_by_step, Unset):
            by_step = UNSET
        else:
            by_step = GetAutomationMetricsResponse200ByStep.from_dict(_by_step)

        _by_variant = d.pop("by_variant", UNSET)
        by_variant: GetAutomationMetricsResponse200ByVariant | Unset
        if isinstance(_by_variant, Unset):
            by_variant = UNSET
        else:
            by_variant = GetAutomationMetricsResponse200ByVariant.from_dict(_by_variant)

        _ab_tests = d.pop("ab_tests", UNSET)
        ab_tests: list[GetAutomationMetricsResponse200AbTestsItem] | Unset = UNSET
        if _ab_tests is not UNSET:
            ab_tests = []
            for ab_tests_item_data in _ab_tests:
                ab_tests_item = GetAutomationMetricsResponse200AbTestsItem.from_dict(ab_tests_item_data)

                ab_tests.append(ab_tests_item)

        get_automation_metrics_response_200 = cls(
            since=since,
            run_counts=run_counts,
            by_step=by_step,
            by_variant=by_variant,
            ab_tests=ab_tests,
        )

        get_automation_metrics_response_200.additional_properties = d
        return get_automation_metrics_response_200

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
