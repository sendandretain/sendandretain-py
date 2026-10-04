from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RotateWebhookSecretResponse200")


@_attrs_define
class RotateWebhookSecretResponse200:
    """
    Attributes:
        secret (str | Unset): The new secret. Shown once.
        previous_secret_expires_at (datetime.datetime | Unset): After this, deliveries carry only the new signature.
    """

    secret: str | Unset = UNSET
    previous_secret_expires_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        previous_secret_expires_at: str | Unset = UNSET
        if not isinstance(self.previous_secret_expires_at, Unset):
            previous_secret_expires_at = self.previous_secret_expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret is not UNSET:
            field_dict["secret"] = secret
        if previous_secret_expires_at is not UNSET:
            field_dict["previous_secret_expires_at"] = previous_secret_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("secret", UNSET)

        _previous_secret_expires_at = d.pop("previous_secret_expires_at", UNSET)
        previous_secret_expires_at: datetime.datetime | Unset
        if isinstance(_previous_secret_expires_at, Unset):
            previous_secret_expires_at = UNSET
        else:
            previous_secret_expires_at = datetime.datetime.fromisoformat(_previous_secret_expires_at)

        rotate_webhook_secret_response_200 = cls(
            secret=secret,
            previous_secret_expires_at=previous_secret_expires_at,
        )

        rotate_webhook_secret_response_200.additional_properties = d
        return rotate_webhook_secret_response_200

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
