from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_automation_steps_schema_0_variant_0 import AddAutomationStepsSchema0Variant0
    from ..models.add_automation_steps_schema_0_variant_1 import AddAutomationStepsSchema0Variant1
    from ..models.add_automation_steps_schema_0_variant_2 import AddAutomationStepsSchema0Variant2
    from ..models.add_automation_steps_schema_0_variant_3 import AddAutomationStepsSchema0Variant3
    from ..models.add_automation_steps_schema_0_variant_4 import AddAutomationStepsSchema0Variant4
    from ..models.add_automation_steps_schema_0_variant_5 import AddAutomationStepsSchema0Variant5
    from ..models.add_automation_steps_schema_0_variant_6 import AddAutomationStepsSchema0Variant6
    from ..models.add_automation_steps_schema_0_variant_7 import AddAutomationStepsSchema0Variant7


T = TypeVar("T", bound="AddAutomationStepsBody")


@_attrs_define
class AddAutomationStepsBody:
    """
    Attributes:
        automation (str): Automation id or name.
        steps (list[AddAutomationStepsSchema0Variant0 | AddAutomationStepsSchema0Variant1 |
            AddAutomationStepsSchema0Variant2 | AddAutomationStepsSchema0Variant3 | AddAutomationStepsSchema0Variant4 |
            AddAutomationStepsSchema0Variant5 | AddAutomationStepsSchema0Variant6 | AddAutomationStepsSchema0Variant7]):
            Steps to append, in order.
        after_position (int | Unset): Insert after this position instead of appending. Requires a paused automation.
        parent_step_id (UUID | Unset): Append into a branch lane owned by this step.
        lane_key (str | Unset): Which lane of the parent branch — e.g. `yes` / `no`, or a multi-branch key.
    """

    automation: str
    steps: list[
        AddAutomationStepsSchema0Variant0
        | AddAutomationStepsSchema0Variant1
        | AddAutomationStepsSchema0Variant2
        | AddAutomationStepsSchema0Variant3
        | AddAutomationStepsSchema0Variant4
        | AddAutomationStepsSchema0Variant5
        | AddAutomationStepsSchema0Variant6
        | AddAutomationStepsSchema0Variant7
    ]
    after_position: int | Unset = UNSET
    parent_step_id: UUID | Unset = UNSET
    lane_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_automation_steps_schema_0_variant_0 import AddAutomationStepsSchema0Variant0
        from ..models.add_automation_steps_schema_0_variant_1 import AddAutomationStepsSchema0Variant1
        from ..models.add_automation_steps_schema_0_variant_2 import AddAutomationStepsSchema0Variant2
        from ..models.add_automation_steps_schema_0_variant_3 import AddAutomationStepsSchema0Variant3
        from ..models.add_automation_steps_schema_0_variant_4 import AddAutomationStepsSchema0Variant4
        from ..models.add_automation_steps_schema_0_variant_5 import AddAutomationStepsSchema0Variant5
        from ..models.add_automation_steps_schema_0_variant_6 import AddAutomationStepsSchema0Variant6

        automation = self.automation

        steps = []
        for steps_item_data in self.steps:
            steps_item: dict[str, Any]
            if isinstance(steps_item_data, AddAutomationStepsSchema0Variant0):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant1):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant2):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant3):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant4):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant5):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant6):
                steps_item = steps_item_data.to_dict()
            else:
                steps_item = steps_item_data.to_dict()

            steps.append(steps_item)

        after_position = self.after_position

        parent_step_id: str | Unset = UNSET
        if not isinstance(self.parent_step_id, Unset):
            parent_step_id = str(self.parent_step_id)

        lane_key = self.lane_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automation": automation,
                "steps": steps,
            }
        )
        if after_position is not UNSET:
            field_dict["after_position"] = after_position
        if parent_step_id is not UNSET:
            field_dict["parent_step_id"] = parent_step_id
        if lane_key is not UNSET:
            field_dict["lane_key"] = lane_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_automation_steps_schema_0_variant_0 import AddAutomationStepsSchema0Variant0
        from ..models.add_automation_steps_schema_0_variant_1 import AddAutomationStepsSchema0Variant1
        from ..models.add_automation_steps_schema_0_variant_2 import AddAutomationStepsSchema0Variant2
        from ..models.add_automation_steps_schema_0_variant_3 import AddAutomationStepsSchema0Variant3
        from ..models.add_automation_steps_schema_0_variant_4 import AddAutomationStepsSchema0Variant4
        from ..models.add_automation_steps_schema_0_variant_5 import AddAutomationStepsSchema0Variant5
        from ..models.add_automation_steps_schema_0_variant_6 import AddAutomationStepsSchema0Variant6
        from ..models.add_automation_steps_schema_0_variant_7 import AddAutomationStepsSchema0Variant7

        d = dict(src_dict)
        automation = d.pop("automation")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:

            def _parse_steps_item(
                data: object,
            ) -> (
                AddAutomationStepsSchema0Variant0
                | AddAutomationStepsSchema0Variant1
                | AddAutomationStepsSchema0Variant2
                | AddAutomationStepsSchema0Variant3
                | AddAutomationStepsSchema0Variant4
                | AddAutomationStepsSchema0Variant5
                | AddAutomationStepsSchema0Variant6
                | AddAutomationStepsSchema0Variant7
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_0 = (
                        AddAutomationStepsSchema0Variant0.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_1 = (
                        AddAutomationStepsSchema0Variant1.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_2 = (
                        AddAutomationStepsSchema0Variant2.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_3 = (
                        AddAutomationStepsSchema0Variant3.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_4 = (
                        AddAutomationStepsSchema0Variant4.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_5 = (
                        AddAutomationStepsSchema0Variant5.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_6 = (
                        AddAutomationStepsSchema0Variant6.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_add_automation_steps_schema_0_type_7 = AddAutomationStepsSchema0Variant7.from_dict(
                    data
                )

                return componentsschemas_add_automation_steps_schema_0_type_7

            steps_item = _parse_steps_item(steps_item_data)

            steps.append(steps_item)

        after_position = d.pop("after_position", UNSET)

        _parent_step_id = d.pop("parent_step_id", UNSET)
        parent_step_id: UUID | Unset
        if isinstance(_parent_step_id, Unset):
            parent_step_id = UNSET
        else:
            parent_step_id = UUID(_parent_step_id)

        lane_key = d.pop("lane_key", UNSET)

        add_automation_steps_body = cls(
            automation=automation,
            steps=steps,
            after_position=after_position,
            parent_step_id=parent_step_id,
            lane_key=lane_key,
        )

        add_automation_steps_body.additional_properties = d
        return add_automation_steps_body

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
