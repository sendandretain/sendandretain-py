from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_automation_steps_schema_0_variant_3_attributes import AddAutomationStepsSchema0Variant3Attributes
    from ..models.add_automation_steps_schema_0_variant_3_send_window import AddAutomationStepsSchema0Variant3SendWindow


T = TypeVar("T", bound="AddAutomationStepsSchema0Variant3")


@_attrs_define
class AddAutomationStepsSchema0Variant3:
    """
    Attributes:
        type_ (Literal['set_attribute']):
        delay_seconds (int): Delay before this step runs (0 = immediate). Weekly = 604800.
        attributes (AddAutomationStepsSchema0Variant3Attributes | Unset): Attributes to shallow-merge onto the contact.
        add_tags (list[str] | Unset): Tags to add — segments filtering on contact.tags follow automatically.
        remove_tags (list[str] | Unset): Tags to remove.
        send_window (AddAutomationStepsSchema0Variant3SendWindow | Unset): Quiet-hours clamp;
            contact.attributes.timezone wins over this timezone.
    """

    type_: Literal["set_attribute"]
    delay_seconds: int
    attributes: AddAutomationStepsSchema0Variant3Attributes | Unset = UNSET
    add_tags: list[str] | Unset = UNSET
    remove_tags: list[str] | Unset = UNSET
    send_window: AddAutomationStepsSchema0Variant3SendWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        delay_seconds = self.delay_seconds

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        add_tags: list[str] | Unset = UNSET
        if not isinstance(self.add_tags, Unset):
            add_tags = self.add_tags

        remove_tags: list[str] | Unset = UNSET
        if not isinstance(self.remove_tags, Unset):
            remove_tags = self.remove_tags

        send_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_window, Unset):
            send_window = self.send_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "delaySeconds": delay_seconds,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if add_tags is not UNSET:
            field_dict["addTags"] = add_tags
        if remove_tags is not UNSET:
            field_dict["removeTags"] = remove_tags
        if send_window is not UNSET:
            field_dict["sendWindow"] = send_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_automation_steps_schema_0_variant_3_attributes import (
            AddAutomationStepsSchema0Variant3Attributes,
        )
        from ..models.add_automation_steps_schema_0_variant_3_send_window import (
            AddAutomationStepsSchema0Variant3SendWindow,
        )

        d = dict(src_dict)
        type_ = cast(Literal["set_attribute"], d.pop("type"))
        if type_ != "set_attribute":
            raise ValueError(f"type must match const 'set_attribute', got '{type_}'")

        delay_seconds = d.pop("delaySeconds")

        _attributes = d.pop("attributes", UNSET)
        attributes: AddAutomationStepsSchema0Variant3Attributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = AddAutomationStepsSchema0Variant3Attributes.from_dict(_attributes)

        add_tags = cast(list[str], d.pop("addTags", UNSET))

        remove_tags = cast(list[str], d.pop("removeTags", UNSET))

        _send_window = d.pop("sendWindow", UNSET)
        send_window: AddAutomationStepsSchema0Variant3SendWindow | Unset
        if isinstance(_send_window, Unset):
            send_window = UNSET
        else:
            send_window = AddAutomationStepsSchema0Variant3SendWindow.from_dict(_send_window)

        add_automation_steps_schema_0_variant_3 = cls(
            type_=type_,
            delay_seconds=delay_seconds,
            attributes=attributes,
            add_tags=add_tags,
            remove_tags=remove_tags,
            send_window=send_window,
        )

        add_automation_steps_schema_0_variant_3.additional_properties = d
        return add_automation_steps_schema_0_variant_3

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
