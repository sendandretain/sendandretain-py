from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAutomationSchema1Variant5")


@_attrs_define
class CreateAutomationSchema1Variant5:
    """
    Attributes:
        type_ (Literal['exit']):
        label (str | Unset): Shown on the canvas and in exit counts.
        delay_seconds (int | Unset): Exits are immediate — put the wait on the step before. Default: 0.
    """

    type_: Literal["exit"]
    label: str | Unset = UNSET
    delay_seconds: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        label = self.label

        delay_seconds = self.delay_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label
        if delay_seconds is not UNSET:
            field_dict["delaySeconds"] = delay_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = cast(Literal["exit"], d.pop("type"))
        if type_ != "exit":
            raise ValueError(f"type must match const 'exit', got '{type_}'")

        label = d.pop("label", UNSET)

        delay_seconds = d.pop("delaySeconds", UNSET)

        create_automation_schema_1_variant_5 = cls(
            type_=type_,
            label=label,
            delay_seconds=delay_seconds,
        )

        create_automation_schema_1_variant_5.additional_properties = d
        return create_automation_schema_1_variant_5

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
