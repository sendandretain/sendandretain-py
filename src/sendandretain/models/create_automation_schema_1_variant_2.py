from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_automation_schema_1_variant_2_send_window import CreateAutomationSchema1Variant2SendWindow


T = TypeVar("T", bound="CreateAutomationSchema1Variant2")


@_attrs_define
class CreateAutomationSchema1Variant2:
    """
    Attributes:
        type_ (Literal['wait_for_event']):
        event_name (str): contact_event name that resumes the run.
        timeout_seconds (int): Give up waiting after this many seconds (60s .. 90d) and continue.
        delay_seconds (int): Delay before this step runs (0 = immediate). Weekly = 604800.
        send_window (CreateAutomationSchema1Variant2SendWindow | Unset): Quiet-hours clamp; contact.attributes.timezone
            wins over this timezone.
    """

    type_: Literal["wait_for_event"]
    event_name: str
    timeout_seconds: int
    delay_seconds: int
    send_window: CreateAutomationSchema1Variant2SendWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        event_name = self.event_name

        timeout_seconds = self.timeout_seconds

        delay_seconds = self.delay_seconds

        send_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_window, Unset):
            send_window = self.send_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "eventName": event_name,
                "timeoutSeconds": timeout_seconds,
                "delaySeconds": delay_seconds,
            }
        )
        if send_window is not UNSET:
            field_dict["sendWindow"] = send_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_automation_schema_1_variant_2_send_window import CreateAutomationSchema1Variant2SendWindow

        d = dict(src_dict)
        type_ = cast(Literal["wait_for_event"], d.pop("type"))
        if type_ != "wait_for_event":
            raise ValueError(f"type must match const 'wait_for_event', got '{type_}'")

        event_name = d.pop("eventName")

        timeout_seconds = d.pop("timeoutSeconds")

        delay_seconds = d.pop("delaySeconds")

        _send_window = d.pop("sendWindow", UNSET)
        send_window: CreateAutomationSchema1Variant2SendWindow | Unset
        if isinstance(_send_window, Unset):
            send_window = UNSET
        else:
            send_window = CreateAutomationSchema1Variant2SendWindow.from_dict(_send_window)

        create_automation_schema_1_variant_2 = cls(
            type_=type_,
            event_name=event_name,
            timeout_seconds=timeout_seconds,
            delay_seconds=delay_seconds,
            send_window=send_window,
        )

        create_automation_schema_1_variant_2.additional_properties = d
        return create_automation_schema_1_variant_2

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
