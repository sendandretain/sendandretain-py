from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automations_post_request_body_content_application_json_trigger_filter_variant_0_item import (
        AutomationsPostRequestBodyContentApplicationJsonTriggerFilterVariant0Item,
    )
    from ..models.create_automation_schema_0 import CreateAutomationSchema0
    from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
    from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
    from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
    from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
    from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
    from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
    from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6
    from ..models.create_automation_schema_1_variant_7 import CreateAutomationSchema1Variant7


T = TypeVar("T", bound="CreateAutomationBody")


@_attrs_define
class CreateAutomationBody:
    """
    Attributes:
        name (str): Display name, unique within the project.
        trigger_event (str): Contact event that enrolls a contact.
        trigger_filter (CreateAutomationSchema0 |
            list[AutomationsPostRequestBodyContentApplicationJsonTriggerFilterVariant0Item] | Unset): Conditions over
            contact attributes ⊕ event properties. All must match to enroll.
        priority (int | Unset): Lower runs first when several automations match. Default 100.
        exclusive (bool | Unset): When true (default), a contact already in this automation is not re-enrolled.
        exit_events (list[str] | Unset): Events that end an in-flight run early, ORed.
        exit_event (str | Unset): Deprecated single-event form, still accepted. Prefer `exit_events`.
        allow_reenrollment (bool | Unset): Allow a contact to enroll again after finishing.
        reenrollment_cooldown_seconds (int | Unset):
        steps (list[CreateAutomationSchema1Variant0 | CreateAutomationSchema1Variant1 | CreateAutomationSchema1Variant2
            | CreateAutomationSchema1Variant3 | CreateAutomationSchema1Variant4 | CreateAutomationSchema1Variant5 |
            CreateAutomationSchema1Variant6 | CreateAutomationSchema1Variant7] | Unset): Steps in order. Omit to create an
            empty shell and append later.
    """

    name: str
    trigger_event: str
    trigger_filter: (
        CreateAutomationSchema0
        | list[AutomationsPostRequestBodyContentApplicationJsonTriggerFilterVariant0Item]
        | Unset
    ) = UNSET
    priority: int | Unset = UNSET
    exclusive: bool | Unset = UNSET
    exit_events: list[str] | Unset = UNSET
    exit_event: str | Unset = UNSET
    allow_reenrollment: bool | Unset = UNSET
    reenrollment_cooldown_seconds: int | Unset = UNSET
    steps: (
        list[
            CreateAutomationSchema1Variant0
            | CreateAutomationSchema1Variant1
            | CreateAutomationSchema1Variant2
            | CreateAutomationSchema1Variant3
            | CreateAutomationSchema1Variant4
            | CreateAutomationSchema1Variant5
            | CreateAutomationSchema1Variant6
            | CreateAutomationSchema1Variant7
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
        from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
        from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
        from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
        from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
        from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
        from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6

        name = self.name

        trigger_event = self.trigger_event

        trigger_filter: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.trigger_filter, Unset):
            trigger_filter = UNSET
        elif isinstance(self.trigger_filter, list):
            trigger_filter = []
            for componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item_data in self.trigger_filter:
                componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item = componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item_data.to_dict()
                trigger_filter.append(
                    componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item
                )

        else:
            trigger_filter = self.trigger_filter.to_dict()

        priority = self.priority

        exclusive = self.exclusive

        exit_events: list[str] | Unset = UNSET
        if not isinstance(self.exit_events, Unset):
            exit_events = self.exit_events

        exit_event = self.exit_event

        allow_reenrollment = self.allow_reenrollment

        reenrollment_cooldown_seconds = self.reenrollment_cooldown_seconds

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item: dict[str, Any]
                if isinstance(steps_item_data, CreateAutomationSchema1Variant0):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant1):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant2):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant3):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant4):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant5):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant6):
                    steps_item = steps_item_data.to_dict()
                else:
                    steps_item = steps_item_data.to_dict()

                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "trigger_event": trigger_event,
            }
        )
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
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_post_request_body_content_application_json_trigger_filter_variant_0_item import (
            AutomationsPostRequestBodyContentApplicationJsonTriggerFilterVariant0Item,
        )
        from ..models.create_automation_schema_0 import CreateAutomationSchema0
        from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
        from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
        from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
        from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
        from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
        from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
        from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6
        from ..models.create_automation_schema_1_variant_7 import CreateAutomationSchema1Variant7

        d = dict(src_dict)
        name = d.pop("name")

        trigger_event = d.pop("trigger_event")

        def _parse_trigger_filter(
            data: object,
        ) -> (
            CreateAutomationSchema0
            | list[AutomationsPostRequestBodyContentApplicationJsonTriggerFilterVariant0Item]
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                trigger_filter_type_0 = []
                _trigger_filter_type_0 = data
                for componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item_data in _trigger_filter_type_0:
                    componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item = AutomationsPostRequestBodyContentApplicationJsonTriggerFilterVariant0Item.from_dict(
                        componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item_data
                    )

                    trigger_filter_type_0.append(
                        componentsschemas_automations_post_request_body_content_application_json_trigger_filter_variant_0_item
                    )

                return trigger_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            trigger_filter_type_1 = CreateAutomationSchema0.from_dict(data)

            return trigger_filter_type_1

        trigger_filter = _parse_trigger_filter(d.pop("trigger_filter", UNSET))

        priority = d.pop("priority", UNSET)

        exclusive = d.pop("exclusive", UNSET)

        exit_events = cast(list[str], d.pop("exit_events", UNSET))

        exit_event = d.pop("exit_event", UNSET)

        allow_reenrollment = d.pop("allow_reenrollment", UNSET)

        reenrollment_cooldown_seconds = d.pop("reenrollment_cooldown_seconds", UNSET)

        _steps = d.pop("steps", UNSET)
        steps: (
            list[
                CreateAutomationSchema1Variant0
                | CreateAutomationSchema1Variant1
                | CreateAutomationSchema1Variant2
                | CreateAutomationSchema1Variant3
                | CreateAutomationSchema1Variant4
                | CreateAutomationSchema1Variant5
                | CreateAutomationSchema1Variant6
                | CreateAutomationSchema1Variant7
            ]
            | Unset
        ) = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:

                def _parse_steps_item(
                    data: object,
                ) -> (
                    CreateAutomationSchema1Variant0
                    | CreateAutomationSchema1Variant1
                    | CreateAutomationSchema1Variant2
                    | CreateAutomationSchema1Variant3
                    | CreateAutomationSchema1Variant4
                    | CreateAutomationSchema1Variant5
                    | CreateAutomationSchema1Variant6
                    | CreateAutomationSchema1Variant7
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_0 = CreateAutomationSchema1Variant0.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_1 = CreateAutomationSchema1Variant1.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_2 = CreateAutomationSchema1Variant2.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_3 = CreateAutomationSchema1Variant3.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_4 = CreateAutomationSchema1Variant4.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_5 = CreateAutomationSchema1Variant5.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_6 = CreateAutomationSchema1Variant6.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_create_automation_schema_1_type_7 = CreateAutomationSchema1Variant7.from_dict(
                        data
                    )

                    return componentsschemas_create_automation_schema_1_type_7

                steps_item = _parse_steps_item(steps_item_data)

                steps.append(steps_item)

        create_automation_body = cls(
            name=name,
            trigger_event=trigger_event,
            trigger_filter=trigger_filter,
            priority=priority,
            exclusive=exclusive,
            exit_events=exit_events,
            exit_event=exit_event,
            allow_reenrollment=allow_reenrollment,
            reenrollment_cooldown_seconds=reenrollment_cooldown_seconds,
            steps=steps,
        )

        create_automation_body.additional_properties = d
        return create_automation_body

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
