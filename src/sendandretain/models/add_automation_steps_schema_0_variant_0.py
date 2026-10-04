from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_automation_steps_schema_0_variant_0_props_overrides import (
        AddAutomationStepsSchema0Variant0PropsOverrides,
    )
    from ..models.add_automation_steps_schema_0_variant_0_send_window import AddAutomationStepsSchema0Variant0SendWindow


T = TypeVar("T", bound="AddAutomationStepsSchema0Variant0")


@_attrs_define
class AddAutomationStepsSchema0Variant0:
    """
    Attributes:
        type_ (Literal['send']):
        template_slug (str):
        delay_seconds (int): Delay before this step runs (0 = immediate). Weekly = 604800.
        props_overrides (AddAutomationStepsSchema0Variant0PropsOverrides | Unset):
        subject (str | Unset):
        preview_text (str | Unset):
        send_window (AddAutomationStepsSchema0Variant0SendWindow | Unset): Quiet-hours clamp;
            contact.attributes.timezone wins over this timezone.
    """

    type_: Literal["send"]
    template_slug: str
    delay_seconds: int
    props_overrides: AddAutomationStepsSchema0Variant0PropsOverrides | Unset = UNSET
    subject: str | Unset = UNSET
    preview_text: str | Unset = UNSET
    send_window: AddAutomationStepsSchema0Variant0SendWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        template_slug = self.template_slug

        delay_seconds = self.delay_seconds

        props_overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props_overrides, Unset):
            props_overrides = self.props_overrides.to_dict()

        subject = self.subject

        preview_text = self.preview_text

        send_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_window, Unset):
            send_window = self.send_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "templateSlug": template_slug,
                "delaySeconds": delay_seconds,
            }
        )
        if props_overrides is not UNSET:
            field_dict["propsOverrides"] = props_overrides
        if subject is not UNSET:
            field_dict["subject"] = subject
        if preview_text is not UNSET:
            field_dict["previewText"] = preview_text
        if send_window is not UNSET:
            field_dict["sendWindow"] = send_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_automation_steps_schema_0_variant_0_props_overrides import (
            AddAutomationStepsSchema0Variant0PropsOverrides,
        )
        from ..models.add_automation_steps_schema_0_variant_0_send_window import (
            AddAutomationStepsSchema0Variant0SendWindow,
        )

        d = dict(src_dict)
        type_ = cast(Literal["send"], d.pop("type"))
        if type_ != "send":
            raise ValueError(f"type must match const 'send', got '{type_}'")

        template_slug = d.pop("templateSlug")

        delay_seconds = d.pop("delaySeconds")

        _props_overrides = d.pop("propsOverrides", UNSET)
        props_overrides: AddAutomationStepsSchema0Variant0PropsOverrides | Unset
        if isinstance(_props_overrides, Unset):
            props_overrides = UNSET
        else:
            props_overrides = AddAutomationStepsSchema0Variant0PropsOverrides.from_dict(_props_overrides)

        subject = d.pop("subject", UNSET)

        preview_text = d.pop("previewText", UNSET)

        _send_window = d.pop("sendWindow", UNSET)
        send_window: AddAutomationStepsSchema0Variant0SendWindow | Unset
        if isinstance(_send_window, Unset):
            send_window = UNSET
        else:
            send_window = AddAutomationStepsSchema0Variant0SendWindow.from_dict(_send_window)

        add_automation_steps_schema_0_variant_0 = cls(
            type_=type_,
            template_slug=template_slug,
            delay_seconds=delay_seconds,
            props_overrides=props_overrides,
            subject=subject,
            preview_text=preview_text,
            send_window=send_window,
        )

        add_automation_steps_schema_0_variant_0.additional_properties = d
        return add_automation_steps_schema_0_variant_0

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
