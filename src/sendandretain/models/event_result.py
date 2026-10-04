from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_result_skipped_item import EventResultSkippedItem


T = TypeVar("T", bound="EventResult")


@_attrs_define
class EventResult:
    """
    Attributes:
        id (str | Unset):
        enrolled (list[str] | Unset): Ids of automations the contact was enrolled into by this event.
        exited_runs (list[str] | Unset): Ids of in-flight automation runs this event caused to exit.
        skipped (list[EventResultSkippedItem] | Unset): Automations that trigger on this event but declined this
            contact, and why. An empty `enrolled` with an empty `skipped` means no automation listens to this event name at
            all — the two cases look identical otherwise.
        deduplicated (bool | Unset): Present and true when dedupe_key matched a prior event.
    """

    id: str | Unset = UNSET
    enrolled: list[str] | Unset = UNSET
    exited_runs: list[str] | Unset = UNSET
    skipped: list[EventResultSkippedItem] | Unset = UNSET
    deduplicated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enrolled: list[str] | Unset = UNSET
        if not isinstance(self.enrolled, Unset):
            enrolled = self.enrolled

        exited_runs: list[str] | Unset = UNSET
        if not isinstance(self.exited_runs, Unset):
            exited_runs = self.exited_runs

        skipped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)

        deduplicated = self.deduplicated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enrolled is not UNSET:
            field_dict["enrolled"] = enrolled
        if exited_runs is not UNSET:
            field_dict["exited_runs"] = exited_runs
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if deduplicated is not UNSET:
            field_dict["deduplicated"] = deduplicated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_result_skipped_item import EventResultSkippedItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        enrolled = cast(list[str], d.pop("enrolled", UNSET))

        exited_runs = cast(list[str], d.pop("exited_runs", UNSET))

        _skipped = d.pop("skipped", UNSET)
        skipped: list[EventResultSkippedItem] | Unset = UNSET
        if _skipped is not UNSET:
            skipped = []
            for skipped_item_data in _skipped:
                skipped_item = EventResultSkippedItem.from_dict(skipped_item_data)

                skipped.append(skipped_item)

        deduplicated = d.pop("deduplicated", UNSET)

        event_result = cls(
            id=id,
            enrolled=enrolled,
            exited_runs=exited_runs,
            skipped=skipped,
            deduplicated=deduplicated,
        )

        event_result.additional_properties = d
        return event_result

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
