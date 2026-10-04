from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackfillMissedEnrollmentsBody")


@_attrs_define
class BackfillMissedEnrollmentsBody:
    """
    Attributes:
        since (str | Unset):
        dry_run (bool | Unset):  Default: True.
        max_contacts (int | Unset):  Default: 1000.
    """

    since: str | Unset = UNSET
    dry_run: bool | Unset = True
    max_contacts: int | Unset = 1000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        since = self.since

        dry_run = self.dry_run

        max_contacts = self.max_contacts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if since is not UNSET:
            field_dict["since"] = since
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if max_contacts is not UNSET:
            field_dict["max_contacts"] = max_contacts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        since = d.pop("since", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        max_contacts = d.pop("max_contacts", UNSET)

        backfill_missed_enrollments_body = cls(
            since=since,
            dry_run=dry_run,
            max_contacts=max_contacts,
        )

        backfill_missed_enrollments_body.additional_properties = d
        return backfill_missed_enrollments_body

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
