from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_metrics_response_200_by_day import GetMetricsResponse200ByDay
    from ..models.get_metrics_response_200_by_template import GetMetricsResponse200ByTemplate
    from ..models.get_metrics_response_200_period import GetMetricsResponse200Period
    from ..models.get_metrics_response_200_totals import GetMetricsResponse200Totals


T = TypeVar("T", bound="GetMetricsResponse200")


@_attrs_define
class GetMetricsResponse200:
    """
    Attributes:
        period (GetMetricsResponse200Period | Unset):
        totals (GetMetricsResponse200Totals | Unset):
        by_template (GetMetricsResponse200ByTemplate | Unset): Keyed by template slug.
        by_day (GetMetricsResponse200ByDay | Unset): Keyed by YYYY-MM-DD.
        warnings (list[str] | Unset): Deliverability tripwires, phrased as actions.
        truncated (bool | Unset): True when the window hit the query cap — narrow it for exact numbers.
    """

    period: GetMetricsResponse200Period | Unset = UNSET
    totals: GetMetricsResponse200Totals | Unset = UNSET
    by_template: GetMetricsResponse200ByTemplate | Unset = UNSET
    by_day: GetMetricsResponse200ByDay | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    truncated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        by_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_template, Unset):
            by_template = self.by_template.to_dict()

        by_day: dict[str, Any] | Unset = UNSET
        if not isinstance(self.by_day, Unset):
            by_day = self.by_day.to_dict()

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        truncated = self.truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if totals is not UNSET:
            field_dict["totals"] = totals
        if by_template is not UNSET:
            field_dict["by_template"] = by_template
        if by_day is not UNSET:
            field_dict["by_day"] = by_day
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_metrics_response_200_by_day import GetMetricsResponse200ByDay
        from ..models.get_metrics_response_200_by_template import GetMetricsResponse200ByTemplate
        from ..models.get_metrics_response_200_period import GetMetricsResponse200Period
        from ..models.get_metrics_response_200_totals import GetMetricsResponse200Totals

        d = dict(src_dict)
        _period = d.pop("period", UNSET)
        period: GetMetricsResponse200Period | Unset
        if isinstance(_period, Unset):
            period = UNSET
        else:
            period = GetMetricsResponse200Period.from_dict(_period)

        _totals = d.pop("totals", UNSET)
        totals: GetMetricsResponse200Totals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = GetMetricsResponse200Totals.from_dict(_totals)

        _by_template = d.pop("by_template", UNSET)
        by_template: GetMetricsResponse200ByTemplate | Unset
        if isinstance(_by_template, Unset):
            by_template = UNSET
        else:
            by_template = GetMetricsResponse200ByTemplate.from_dict(_by_template)

        _by_day = d.pop("by_day", UNSET)
        by_day: GetMetricsResponse200ByDay | Unset
        if isinstance(_by_day, Unset):
            by_day = UNSET
        else:
            by_day = GetMetricsResponse200ByDay.from_dict(_by_day)

        warnings = cast(list[str], d.pop("warnings", UNSET))

        truncated = d.pop("truncated", UNSET)

        get_metrics_response_200 = cls(
            period=period,
            totals=totals,
            by_template=by_template,
            by_day=by_day,
            warnings=warnings,
            truncated=truncated,
        )

        get_metrics_response_200.additional_properties = d
        return get_metrics_response_200

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
