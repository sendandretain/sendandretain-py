from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item import (
        AutomationsIdPatchRequestBodyContentApplicationJsonTriggerFilterVariant0Variant0Item,
    )
    from ..models.update_automation_schema_0 import UpdateAutomationSchema0


T = TypeVar("T", bound="UpdateAutomationBody")


@_attrs_define
class UpdateAutomationBody:
    """
    Attributes:
        name (str | Unset):
        trigger_event (str | Unset): New trigger. Affects FUTURE enrollments only.
        trigger_filter (list[AutomationsIdPatchRequestBodyContentApplicationJsonTriggerFilterVariant0Variant0Item] |
            None | Unset | UpdateAutomationSchema0): New filter, or null to clear it (every occurrence enrolls).
        priority (int | Unset): Lower runs first when several automations match.
        exclusive (bool | Unset):
        exit_events (list[str] | None | Unset): Events that end an in-flight run early, ORed. Replaces `exit_event`; []
            or null clears.
        exit_event (None | str | Unset): Deprecated single-event form, still accepted. Prefer `exit_events`. null
            clears.
        allow_reenrollment (bool | Unset):
        reenrollment_cooldown_seconds (int | Unset):
    """

    name: str | Unset = UNSET
    trigger_event: str | Unset = UNSET
    trigger_filter: (
        list[AutomationsIdPatchRequestBodyContentApplicationJsonTriggerFilterVariant0Variant0Item]
        | None
        | Unset
        | UpdateAutomationSchema0
    ) = UNSET
    priority: int | Unset = UNSET
    exclusive: bool | Unset = UNSET
    exit_events: list[str] | None | Unset = UNSET
    exit_event: None | str | Unset = UNSET
    allow_reenrollment: bool | Unset = UNSET
    reenrollment_cooldown_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.update_automation_schema_0 import UpdateAutomationSchema0

        name = self.name

        trigger_event = self.trigger_event

        trigger_filter: dict[str, Any] | list[dict[str, Any]] | None | Unset
        if isinstance(self.trigger_filter, Unset):
            trigger_filter = UNSET
        elif isinstance(self.trigger_filter, list):
            trigger_filter = []
            for componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item_data in self.trigger_filter:
                componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item = componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item_data.to_dict()
                trigger_filter.append(
                    componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item
                )

        elif isinstance(self.trigger_filter, UpdateAutomationSchema0):
            trigger_filter = self.trigger_filter.to_dict()
        else:
            trigger_filter = self.trigger_filter

        priority = self.priority

        exclusive = self.exclusive

        exit_events: list[str] | None | Unset
        if isinstance(self.exit_events, Unset):
            exit_events = UNSET
        elif isinstance(self.exit_events, list):
            exit_events = self.exit_events

        else:
            exit_events = self.exit_events

        exit_event: None | str | Unset
        if isinstance(self.exit_event, Unset):
            exit_event = UNSET
        else:
            exit_event = self.exit_event

        allow_reenrollment = self.allow_reenrollment

        reenrollment_cooldown_seconds = self.reenrollment_cooldown_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
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
        if reenrollment_cooldown_seconds is not UNSET:
            field_dict["reenrollment_cooldown_seconds"] = reenrollment_cooldown_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item import (
            AutomationsIdPatchRequestBodyContentApplicationJsonTriggerFilterVariant0Variant0Item,
        )
        from ..models.update_automation_schema_0 import UpdateAutomationSchema0

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        trigger_event = d.pop("trigger_event", UNSET)

        def _parse_trigger_filter(
            data: object,
        ) -> (
            list[AutomationsIdPatchRequestBodyContentApplicationJsonTriggerFilterVariant0Variant0Item]
            | None
            | Unset
            | UpdateAutomationSchema0
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trigger_filter_type_0_type_0 = []
                _trigger_filter_type_0_type_0 = data
                for componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item_data in _trigger_filter_type_0_type_0:
                    componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item = AutomationsIdPatchRequestBodyContentApplicationJsonTriggerFilterVariant0Variant0Item.from_dict(
                        componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item_data
                    )

                    trigger_filter_type_0_type_0.append(
                        componentsschemas_automations_id_patch_request_body_content_application_json_trigger_filter_variant_0_variant_0_item
                    )

                return trigger_filter_type_0_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                trigger_filter_type_0_type_1 = UpdateAutomationSchema0.from_dict(data)

                return trigger_filter_type_0_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[AutomationsIdPatchRequestBodyContentApplicationJsonTriggerFilterVariant0Variant0Item]
                | None
                | Unset
                | UpdateAutomationSchema0,
                data,
            )

        trigger_filter = _parse_trigger_filter(d.pop("trigger_filter", UNSET))

        priority = d.pop("priority", UNSET)

        exclusive = d.pop("exclusive", UNSET)

        def _parse_exit_events(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exit_events_type_0 = cast(list[str], data)

                return exit_events_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exit_events = _parse_exit_events(d.pop("exit_events", UNSET))

        def _parse_exit_event(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exit_event = _parse_exit_event(d.pop("exit_event", UNSET))

        allow_reenrollment = d.pop("allow_reenrollment", UNSET)

        reenrollment_cooldown_seconds = d.pop("reenrollment_cooldown_seconds", UNSET)

        update_automation_body = cls(
            name=name,
            trigger_event=trigger_event,
            trigger_filter=trigger_filter,
            priority=priority,
            exclusive=exclusive,
            exit_events=exit_events,
            exit_event=exit_event,
            allow_reenrollment=allow_reenrollment,
            reenrollment_cooldown_seconds=reenrollment_cooldown_seconds,
        )

        update_automation_body.additional_properties = d
        return update_automation_body

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
