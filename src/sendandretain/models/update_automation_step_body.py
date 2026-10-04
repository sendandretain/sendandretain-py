from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_automation_step_body_patch import UpdateAutomationStepBodyPatch


T = TypeVar("T", bound="UpdateAutomationStepBody")


@_attrs_define
class UpdateAutomationStepBody:
    """
    Attributes:
        automation (str): Automation id or name.
        position (int): The step's globally-unique position within the automation.
        patch (UpdateAutomationStepBodyPatch): Fields to change. Keys are validated against the step's actual type.
    """

    automation: str
    position: int
    patch: UpdateAutomationStepBodyPatch
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation = self.automation

        position = self.position

        patch = self.patch.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automation": automation,
                "position": position,
                "patch": patch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_automation_step_body_patch import UpdateAutomationStepBodyPatch

        d = dict(src_dict)
        automation = d.pop("automation")

        position = d.pop("position")

        patch = UpdateAutomationStepBodyPatch.from_dict(d.pop("patch"))

        update_automation_step_body = cls(
            automation=automation,
            position=position,
            patch=patch,
        )

        update_automation_step_body.additional_properties = d
        return update_automation_step_body

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
