from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConnectionStatusResponse200ProviderType0")


@_attrs_define
class GetConnectionStatusResponse200ProviderType0:
    """
    Attributes:
        name (str | Unset):
        status (str | Unset):
        webhook_registered (bool | Unset):
        error_message (None | str | Unset):
    """

    name: str | Unset = UNSET
    status: str | Unset = UNSET
    webhook_registered: bool | Unset = UNSET
    error_message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        webhook_registered = self.webhook_registered

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if webhook_registered is not UNSET:
            field_dict["webhook_registered"] = webhook_registered
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        webhook_registered = d.pop("webhook_registered", UNSET)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        get_connection_status_response_200_provider_type_0 = cls(
            name=name,
            status=status,
            webhook_registered=webhook_registered,
            error_message=error_message,
        )

        get_connection_status_response_200_provider_type_0.additional_properties = d
        return get_connection_status_response_200_provider_type_0

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
