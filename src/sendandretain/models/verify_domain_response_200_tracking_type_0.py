from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyDomainResponse200TrackingType0")


@_attrs_define
class VerifyDomainResponse200TrackingType0:
    """Domain-level open/click tracking (Resend). Null for SendGrid — tracking is applied per send there. The tracking
    CNAME rides in dns_records (record: 'Tracking'); click events won't fire until it resolves.

        Attributes:
            open_ (bool | None | Unset):
            click (bool | None | Unset):
            subdomain (None | str | Unset):
    """

    open_: bool | None | Unset = UNSET
    click: bool | None | Unset = UNSET
    subdomain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_: bool | None | Unset
        if isinstance(self.open_, Unset):
            open_ = UNSET
        else:
            open_ = self.open_

        click: bool | None | Unset
        if isinstance(self.click, Unset):
            click = UNSET
        else:
            click = self.click

        subdomain: None | str | Unset
        if isinstance(self.subdomain, Unset):
            subdomain = UNSET
        else:
            subdomain = self.subdomain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_ is not UNSET:
            field_dict["open"] = open_
        if click is not UNSET:
            field_dict["click"] = click
        if subdomain is not UNSET:
            field_dict["subdomain"] = subdomain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_open_(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        open_ = _parse_open_(d.pop("open", UNSET))

        def _parse_click(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        click = _parse_click(d.pop("click", UNSET))

        def _parse_subdomain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subdomain = _parse_subdomain(d.pop("subdomain", UNSET))

        verify_domain_response_200_tracking_type_0 = cls(
            open_=open_,
            click=click,
            subdomain=subdomain,
        )

        verify_domain_response_200_tracking_type_0.additional_properties = d
        return verify_domain_response_200_tracking_type_0

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
