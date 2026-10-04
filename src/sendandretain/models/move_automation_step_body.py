from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.move_automation_step_body_direction import MoveAutomationStepBodyDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveAutomationStepBody")


@_attrs_define
class MoveAutomationStepBody:
    """
    Attributes:
        automation (str): Automation id or name.
        position (int): Step to move.
        direction (MoveAutomationStepBodyDirection | Unset): Shift one slot among lane siblings.
        to_index (int | Unset): Target index among lane siblings. Wins over `direction`.
    """

    automation: str
    position: int
    direction: MoveAutomationStepBodyDirection | Unset = UNSET
    to_index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation = self.automation

        position = self.position

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        to_index = self.to_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automation": automation,
                "position": position,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if to_index is not UNSET:
            field_dict["to_index"] = to_index

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automation = d.pop("automation")

        position = d.pop("position")

        _direction = d.pop("direction", UNSET)
        direction: MoveAutomationStepBodyDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = MoveAutomationStepBodyDirection(_direction)

        to_index = d.pop("to_index", UNSET)

        move_automation_step_body = cls(
            automation=automation,
            position=position,
            direction=direction,
            to_index=to_index,
        )

        move_automation_step_body.additional_properties = d
        return move_automation_step_body

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
