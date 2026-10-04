from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreflightAutomationResponse200ChecksItem")


@_attrs_define
class PreflightAutomationResponse200ChecksItem:
    """
    Attributes:
        pass_ (bool | Unset):
        blocking (bool | Unset):
        label (str | Unset):
        detail (str | Unset):
    """

    pass_: bool | Unset = UNSET
    blocking: bool | Unset = UNSET
    label: str | Unset = UNSET
    detail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pass_ = self.pass_

        blocking = self.blocking

        label = self.label

        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pass_ is not UNSET:
            field_dict["pass"] = pass_
        if blocking is not UNSET:
            field_dict["blocking"] = blocking
        if label is not UNSET:
            field_dict["label"] = label
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pass_ = d.pop("pass", UNSET)

        blocking = d.pop("blocking", UNSET)

        label = d.pop("label", UNSET)

        detail = d.pop("detail", UNSET)

        preflight_automation_response_200_checks_item = cls(
            pass_=pass_,
            blocking=blocking,
            label=label,
            detail=detail,
        )

        preflight_automation_response_200_checks_item.additional_properties = d
        return preflight_automation_response_200_checks_item

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
