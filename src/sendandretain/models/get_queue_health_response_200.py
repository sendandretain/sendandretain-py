from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetQueueHealthResponse200")


@_attrs_define
class GetQueueHealthResponse200:
    """
    Attributes:
        pending_due_now (int | Unset):
        oldest_pending_age_seconds (int | None | Unset):
        processing (int | Unset):
        dead_letter (int | Unset):
    """

    pending_due_now: int | Unset = UNSET
    oldest_pending_age_seconds: int | None | Unset = UNSET
    processing: int | Unset = UNSET
    dead_letter: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pending_due_now = self.pending_due_now

        oldest_pending_age_seconds: int | None | Unset
        if isinstance(self.oldest_pending_age_seconds, Unset):
            oldest_pending_age_seconds = UNSET
        else:
            oldest_pending_age_seconds = self.oldest_pending_age_seconds

        processing = self.processing

        dead_letter = self.dead_letter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pending_due_now is not UNSET:
            field_dict["pending_due_now"] = pending_due_now
        if oldest_pending_age_seconds is not UNSET:
            field_dict["oldest_pending_age_seconds"] = oldest_pending_age_seconds
        if processing is not UNSET:
            field_dict["processing"] = processing
        if dead_letter is not UNSET:
            field_dict["dead_letter"] = dead_letter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pending_due_now = d.pop("pending_due_now", UNSET)

        def _parse_oldest_pending_age_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        oldest_pending_age_seconds = _parse_oldest_pending_age_seconds(d.pop("oldest_pending_age_seconds", UNSET))

        processing = d.pop("processing", UNSET)

        dead_letter = d.pop("dead_letter", UNSET)

        get_queue_health_response_200 = cls(
            pending_due_now=pending_due_now,
            oldest_pending_age_seconds=oldest_pending_age_seconds,
            processing=processing,
            dead_letter=dead_letter,
        )

        get_queue_health_response_200.additional_properties = d
        return get_queue_health_response_200

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
