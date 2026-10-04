from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RotateWebhookSecretBody")


@_attrs_define
class RotateWebhookSecretBody:
    """
    Attributes:
        grace_minutes (int | Unset): How long the OLD secret keeps verifying. Both secrets sign every delivery during
            the window, so you can deploy the new one on your own schedule. Defaults to 1440 (24h); maximum 10080 (7 days).
            Pass 0 to cut over immediately.
    """

    grace_minutes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grace_minutes = self.grace_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grace_minutes is not UNSET:
            field_dict["grace_minutes"] = grace_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grace_minutes = d.pop("grace_minutes", UNSET)

        rotate_webhook_secret_body = cls(
            grace_minutes=grace_minutes,
        )

        rotate_webhook_secret_body.additional_properties = d
        return rotate_webhook_secret_body

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
