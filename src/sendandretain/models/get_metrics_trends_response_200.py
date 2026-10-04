from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_metrics_trends_response_200_series_item import GetMetricsTrendsResponse200SeriesItem
    from ..models.get_metrics_trends_response_200_totals import GetMetricsTrendsResponse200Totals


T = TypeVar("T", bound="GetMetricsTrendsResponse200")


@_attrs_define
class GetMetricsTrendsResponse200:
    """
    Attributes:
        days (int | Unset):
        series (list[GetMetricsTrendsResponse200SeriesItem] | Unset):
        totals (GetMetricsTrendsResponse200Totals | Unset):
    """

    days: int | Unset = UNSET
    series: list[GetMetricsTrendsResponse200SeriesItem] | Unset = UNSET
    totals: GetMetricsTrendsResponse200Totals | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if series is not UNSET:
            field_dict["series"] = series
        if totals is not UNSET:
            field_dict["totals"] = totals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_metrics_trends_response_200_series_item import GetMetricsTrendsResponse200SeriesItem
        from ..models.get_metrics_trends_response_200_totals import GetMetricsTrendsResponse200Totals

        d = dict(src_dict)
        days = d.pop("days", UNSET)

        _series = d.pop("series", UNSET)
        series: list[GetMetricsTrendsResponse200SeriesItem] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = GetMetricsTrendsResponse200SeriesItem.from_dict(series_item_data)

                series.append(series_item)

        _totals = d.pop("totals", UNSET)
        totals: GetMetricsTrendsResponse200Totals | Unset
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = GetMetricsTrendsResponse200Totals.from_dict(_totals)

        get_metrics_trends_response_200 = cls(
            days=days,
            series=series,
            totals=totals,
        )

        get_metrics_trends_response_200.additional_properties = d
        return get_metrics_trends_response_200

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
