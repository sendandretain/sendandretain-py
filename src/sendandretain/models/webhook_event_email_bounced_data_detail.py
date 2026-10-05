from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEventEmailBouncedDataDetail")


@_attrs_define
class WebhookEventEmailBouncedDataDetail:
    """Provider detail, normalised. Fields are present only when the provider reported them.

    Attributes:
        type_ (bool | float | str | Unset):
        sub_type (bool | float | str | Unset):
        diagnostic (bool | float | str | Unset):
    """

    type_: bool | float | str | Unset = UNSET
    sub_type: bool | float | str | Unset = UNSET
    diagnostic: bool | float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: bool | float | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        sub_type: bool | float | str | Unset
        if isinstance(self.sub_type, Unset):
            sub_type = UNSET
        else:
            sub_type = self.sub_type

        diagnostic: bool | float | str | Unset
        if isinstance(self.diagnostic, Unset):
            diagnostic = UNSET
        else:
            diagnostic = self.diagnostic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sub_type is not UNSET:
            field_dict["sub_type"] = sub_type
        if diagnostic is not UNSET:
            field_dict["diagnostic"] = diagnostic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_sub_type(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        sub_type = _parse_sub_type(d.pop("sub_type", UNSET))

        def _parse_diagnostic(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        diagnostic = _parse_diagnostic(d.pop("diagnostic", UNSET))

        webhook_event_email_bounced_data_detail = cls(
            type_=type_,
            sub_type=sub_type,
            diagnostic=diagnostic,
        )

        webhook_event_email_bounced_data_detail.additional_properties = d
        return webhook_event_email_bounced_data_detail

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
