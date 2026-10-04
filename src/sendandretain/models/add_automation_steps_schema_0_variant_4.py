from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.add_automation_steps_schema_0_variant_4_method import AddAutomationStepsSchema0Variant4Method
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_automation_steps_schema_0_variant_4_send_window import AddAutomationStepsSchema0Variant4SendWindow


T = TypeVar("T", bound="AddAutomationStepsSchema0Variant4")


@_attrs_define
class AddAutomationStepsSchema0Variant4:
    """
    Attributes:
        type_ (Literal['webhook']):
        url (str): Public HTTPS endpoint to POST to.
        delay_seconds (int): Delay before this step runs (0 = immediate). Weekly = 604800.
        method (AddAutomationStepsSchema0Variant4Method | Unset):  Default:
            AddAutomationStepsSchema0Variant4Method.POST.
        send_window (AddAutomationStepsSchema0Variant4SendWindow | Unset): Quiet-hours clamp;
            contact.attributes.timezone wins over this timezone.
    """

    type_: Literal["webhook"]
    url: str
    delay_seconds: int
    method: AddAutomationStepsSchema0Variant4Method | Unset = AddAutomationStepsSchema0Variant4Method.POST
    send_window: AddAutomationStepsSchema0Variant4SendWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        delay_seconds = self.delay_seconds

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        send_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_window, Unset):
            send_window = self.send_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url": url,
                "delaySeconds": delay_seconds,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if send_window is not UNSET:
            field_dict["sendWindow"] = send_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_automation_steps_schema_0_variant_4_send_window import (
            AddAutomationStepsSchema0Variant4SendWindow,
        )

        d = dict(src_dict)
        type_ = cast(Literal["webhook"], d.pop("type"))
        if type_ != "webhook":
            raise ValueError(f"type must match const 'webhook', got '{type_}'")

        url = d.pop("url")

        delay_seconds = d.pop("delaySeconds")

        _method = d.pop("method", UNSET)
        method: AddAutomationStepsSchema0Variant4Method | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = AddAutomationStepsSchema0Variant4Method(_method)

        _send_window = d.pop("sendWindow", UNSET)
        send_window: AddAutomationStepsSchema0Variant4SendWindow | Unset
        if isinstance(_send_window, Unset):
            send_window = UNSET
        else:
            send_window = AddAutomationStepsSchema0Variant4SendWindow.from_dict(_send_window)

        add_automation_steps_schema_0_variant_4 = cls(
            type_=type_,
            url=url,
            delay_seconds=delay_seconds,
            method=method,
            send_window=send_window,
        )

        add_automation_steps_schema_0_variant_4.additional_properties = d
        return add_automation_steps_schema_0_variant_4

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
