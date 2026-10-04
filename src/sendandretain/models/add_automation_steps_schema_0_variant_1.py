from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddAutomationStepsSchema0Variant1")


@_attrs_define
class AddAutomationStepsSchema0Variant1:
    """
    Attributes:
        type_ (Literal['delay']):
        delay_seconds (int): How long to wait before continuing, in seconds (min 60s). Weekly = 604800.
    """

    type_: Literal["delay"]
    delay_seconds: int

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        delay_seconds = self.delay_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
                "delaySeconds": delay_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["delay"], d.pop("type"))
        if type_ != "delay":
            raise ValueError(f"type must match const 'delay', got '{type_}'")

        delay_seconds = d.pop("delaySeconds")

        add_automation_steps_schema_0_variant_1 = cls(
            type_=type_,
            delay_seconds=delay_seconds,
        )

        return add_automation_steps_schema_0_variant_1
