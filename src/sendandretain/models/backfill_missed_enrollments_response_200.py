from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackfillMissedEnrollmentsResponse200")


@_attrs_define
class BackfillMissedEnrollmentsResponse200:
    """
    Attributes:
        dry_run (bool | Unset):
        since (str | Unset):
        window_clamped (bool | Unset):
        would_enroll (int | Unset):
        enrolled (int | Unset):
        skipped_already_resolved (int | Unset):
        skipped_by_guards (int | Unset):
    """

    dry_run: bool | Unset = UNSET
    since: str | Unset = UNSET
    window_clamped: bool | Unset = UNSET
    would_enroll: int | Unset = UNSET
    enrolled: int | Unset = UNSET
    skipped_already_resolved: int | Unset = UNSET
    skipped_by_guards: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dry_run = self.dry_run

        since = self.since

        window_clamped = self.window_clamped

        would_enroll = self.would_enroll

        enrolled = self.enrolled

        skipped_already_resolved = self.skipped_already_resolved

        skipped_by_guards = self.skipped_by_guards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if since is not UNSET:
            field_dict["since"] = since
        if window_clamped is not UNSET:
            field_dict["window_clamped"] = window_clamped
        if would_enroll is not UNSET:
            field_dict["would_enroll"] = would_enroll
        if enrolled is not UNSET:
            field_dict["enrolled"] = enrolled
        if skipped_already_resolved is not UNSET:
            field_dict["skipped_already_resolved"] = skipped_already_resolved
        if skipped_by_guards is not UNSET:
            field_dict["skipped_by_guards"] = skipped_by_guards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dry_run = d.pop("dry_run", UNSET)

        since = d.pop("since", UNSET)

        window_clamped = d.pop("window_clamped", UNSET)

        would_enroll = d.pop("would_enroll", UNSET)

        enrolled = d.pop("enrolled", UNSET)

        skipped_already_resolved = d.pop("skipped_already_resolved", UNSET)

        skipped_by_guards = d.pop("skipped_by_guards", UNSET)

        backfill_missed_enrollments_response_200 = cls(
            dry_run=dry_run,
            since=since,
            window_clamped=window_clamped,
            would_enroll=would_enroll,
            enrolled=enrolled,
            skipped_already_resolved=skipped_already_resolved,
            skipped_by_guards=skipped_by_guards,
        )

        backfill_missed_enrollments_response_200.additional_properties = d
        return backfill_missed_enrollments_response_200

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
