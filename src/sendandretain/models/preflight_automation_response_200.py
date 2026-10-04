from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preflight_automation_response_200_checks_item import PreflightAutomationResponse200ChecksItem


T = TypeVar("T", bound="PreflightAutomationResponse200")


@_attrs_define
class PreflightAutomationResponse200:
    """
    Attributes:
        ready (bool | Unset): True when nothing blocking would stop activation.
        checks (list[PreflightAutomationResponse200ChecksItem] | Unset):
    """

    ready: bool | Unset = UNSET
    checks: list[PreflightAutomationResponse200ChecksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ready = self.ready

        checks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = []
            for checks_item_data in self.checks:
                checks_item = checks_item_data.to_dict()
                checks.append(checks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ready is not UNSET:
            field_dict["ready"] = ready
        if checks is not UNSET:
            field_dict["checks"] = checks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preflight_automation_response_200_checks_item import PreflightAutomationResponse200ChecksItem

        d = dict(src_dict)
        ready = d.pop("ready", UNSET)

        _checks = d.pop("checks", UNSET)
        checks: list[PreflightAutomationResponse200ChecksItem] | Unset = UNSET
        if _checks is not UNSET:
            checks = []
            for checks_item_data in _checks:
                checks_item = PreflightAutomationResponse200ChecksItem.from_dict(checks_item_data)

                checks.append(checks_item)

        preflight_automation_response_200 = cls(
            ready=ready,
            checks=checks,
        )

        preflight_automation_response_200.additional_properties = d
        return preflight_automation_response_200

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
