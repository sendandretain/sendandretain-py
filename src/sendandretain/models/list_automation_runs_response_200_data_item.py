from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_automation_runs_response_200_data_item_variant_assignments import (
        ListAutomationRunsResponse200DataItemVariantAssignments,
    )


T = TypeVar("T", bound="ListAutomationRunsResponse200DataItem")


@_attrs_define
class ListAutomationRunsResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        status (str | Unset):
        contact_email (None | str | Unset):
        current_step_id (None | str | Unset):
        next_step_at (datetime.datetime | None | Unset):
        waiting_for_event (None | str | Unset):
        wait_until (datetime.datetime | None | Unset):
        exit_step_id (None | str | Unset):
        variant_assignments (ListAutomationRunsResponse200DataItemVariantAssignments | Unset):
        cancel_reason (None | str | Unset):
        started_at (datetime.datetime | Unset):
        finished_at (datetime.datetime | None | Unset):
    """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    contact_email: None | str | Unset = UNSET
    current_step_id: None | str | Unset = UNSET
    next_step_at: datetime.datetime | None | Unset = UNSET
    waiting_for_event: None | str | Unset = UNSET
    wait_until: datetime.datetime | None | Unset = UNSET
    exit_step_id: None | str | Unset = UNSET
    variant_assignments: ListAutomationRunsResponse200DataItemVariantAssignments | Unset = UNSET
    cancel_reason: None | str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        contact_email: None | str | Unset
        if isinstance(self.contact_email, Unset):
            contact_email = UNSET
        else:
            contact_email = self.contact_email

        current_step_id: None | str | Unset
        if isinstance(self.current_step_id, Unset):
            current_step_id = UNSET
        else:
            current_step_id = self.current_step_id

        next_step_at: None | str | Unset
        if isinstance(self.next_step_at, Unset):
            next_step_at = UNSET
        elif isinstance(self.next_step_at, datetime.datetime):
            next_step_at = self.next_step_at.isoformat()
        else:
            next_step_at = self.next_step_at

        waiting_for_event: None | str | Unset
        if isinstance(self.waiting_for_event, Unset):
            waiting_for_event = UNSET
        else:
            waiting_for_event = self.waiting_for_event

        wait_until: None | str | Unset
        if isinstance(self.wait_until, Unset):
            wait_until = UNSET
        elif isinstance(self.wait_until, datetime.datetime):
            wait_until = self.wait_until.isoformat()
        else:
            wait_until = self.wait_until

        exit_step_id: None | str | Unset
        if isinstance(self.exit_step_id, Unset):
            exit_step_id = UNSET
        else:
            exit_step_id = self.exit_step_id

        variant_assignments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variant_assignments, Unset):
            variant_assignments = self.variant_assignments.to_dict()

        cancel_reason: None | str | Unset
        if isinstance(self.cancel_reason, Unset):
            cancel_reason = UNSET
        else:
            cancel_reason = self.cancel_reason

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if contact_email is not UNSET:
            field_dict["contact_email"] = contact_email
        if current_step_id is not UNSET:
            field_dict["current_step_id"] = current_step_id
        if next_step_at is not UNSET:
            field_dict["next_step_at"] = next_step_at
        if waiting_for_event is not UNSET:
            field_dict["waiting_for_event"] = waiting_for_event
        if wait_until is not UNSET:
            field_dict["wait_until"] = wait_until
        if exit_step_id is not UNSET:
            field_dict["exit_step_id"] = exit_step_id
        if variant_assignments is not UNSET:
            field_dict["variant_assignments"] = variant_assignments
        if cancel_reason is not UNSET:
            field_dict["cancel_reason"] = cancel_reason
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_automation_runs_response_200_data_item_variant_assignments import (
            ListAutomationRunsResponse200DataItemVariantAssignments,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        def _parse_contact_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_email = _parse_contact_email(d.pop("contact_email", UNSET))

        def _parse_current_step_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        current_step_id = _parse_current_step_id(d.pop("current_step_id", UNSET))

        def _parse_next_step_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_step_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_step_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_step_at = _parse_next_step_at(d.pop("next_step_at", UNSET))

        def _parse_waiting_for_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waiting_for_event = _parse_waiting_for_event(d.pop("waiting_for_event", UNSET))

        def _parse_wait_until(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wait_until_type_0 = datetime.datetime.fromisoformat(data)

                return wait_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        wait_until = _parse_wait_until(d.pop("wait_until", UNSET))

        def _parse_exit_step_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exit_step_id = _parse_exit_step_id(d.pop("exit_step_id", UNSET))

        _variant_assignments = d.pop("variant_assignments", UNSET)
        variant_assignments: ListAutomationRunsResponse200DataItemVariantAssignments | Unset
        if isinstance(_variant_assignments, Unset):
            variant_assignments = UNSET
        else:
            variant_assignments = ListAutomationRunsResponse200DataItemVariantAssignments.from_dict(
                _variant_assignments
            )

        def _parse_cancel_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancel_reason = _parse_cancel_reason(d.pop("cancel_reason", UNSET))

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)

        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        list_automation_runs_response_200_data_item = cls(
            id=id,
            status=status,
            contact_email=contact_email,
            current_step_id=current_step_id,
            next_step_at=next_step_at,
            waiting_for_event=waiting_for_event,
            wait_until=wait_until,
            exit_step_id=exit_step_id,
            variant_assignments=variant_assignments,
            cancel_reason=cancel_reason,
            started_at=started_at,
            finished_at=finished_at,
        )

        list_automation_runs_response_200_data_item.additional_properties = d
        return list_automation_runs_response_200_data_item

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
