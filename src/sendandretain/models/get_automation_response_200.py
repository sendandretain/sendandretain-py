from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_automation_response_200_steps_item import GetAutomationResponse200StepsItem


T = TypeVar("T", bound="GetAutomationResponse200")


@_attrs_define
class GetAutomationResponse200:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        status (str | Unset):
        trigger_event (str | Unset):
        trigger_filter (Any | Unset):
        priority (int | Unset):
        exclusive (bool | Unset):
        exit_events (list[str] | Unset):
        exit_event (None | str | Unset):
        allow_reenrollment (bool | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        steps (list[GetAutomationResponse200StepsItem] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    trigger_event: str | Unset = UNSET
    trigger_filter: Any | Unset = UNSET
    priority: int | Unset = UNSET
    exclusive: bool | Unset = UNSET
    exit_events: list[str] | Unset = UNSET
    exit_event: None | str | Unset = UNSET
    allow_reenrollment: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    steps: list[GetAutomationResponse200StepsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        trigger_event = self.trigger_event

        trigger_filter = self.trigger_filter

        priority = self.priority

        exclusive = self.exclusive

        exit_events: list[str] | Unset = UNSET
        if not isinstance(self.exit_events, Unset):
            exit_events = self.exit_events

        exit_event: None | str | Unset
        if isinstance(self.exit_event, Unset):
            exit_event = UNSET
        else:
            exit_event = self.exit_event

        allow_reenrollment = self.allow_reenrollment

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if trigger_event is not UNSET:
            field_dict["trigger_event"] = trigger_event
        if trigger_filter is not UNSET:
            field_dict["trigger_filter"] = trigger_filter
        if priority is not UNSET:
            field_dict["priority"] = priority
        if exclusive is not UNSET:
            field_dict["exclusive"] = exclusive
        if exit_events is not UNSET:
            field_dict["exit_events"] = exit_events
        if exit_event is not UNSET:
            field_dict["exit_event"] = exit_event
        if allow_reenrollment is not UNSET:
            field_dict["allow_reenrollment"] = allow_reenrollment
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_automation_response_200_steps_item import GetAutomationResponse200StepsItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        trigger_event = d.pop("trigger_event", UNSET)

        trigger_filter = d.pop("trigger_filter", UNSET)

        priority = d.pop("priority", UNSET)

        exclusive = d.pop("exclusive", UNSET)

        exit_events = cast(list[str], d.pop("exit_events", UNSET))

        def _parse_exit_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exit_event = _parse_exit_event(d.pop("exit_event", UNSET))

        allow_reenrollment = d.pop("allow_reenrollment", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        _steps = d.pop("steps", UNSET)
        steps: list[GetAutomationResponse200StepsItem] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = GetAutomationResponse200StepsItem.from_dict(steps_item_data)

                steps.append(steps_item)

        get_automation_response_200 = cls(
            id=id,
            name=name,
            status=status,
            trigger_event=trigger_event,
            trigger_filter=trigger_filter,
            priority=priority,
            exclusive=exclusive,
            exit_events=exit_events,
            exit_event=exit_event,
            allow_reenrollment=allow_reenrollment,
            created_at=created_at,
            updated_at=updated_at,
            steps=steps,
        )

        get_automation_response_200.additional_properties = d
        return get_automation_response_200

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
