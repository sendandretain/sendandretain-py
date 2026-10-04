from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_connection_status_response_200_domains_item import GetConnectionStatusResponse200DomainsItem
    from ..models.get_connection_status_response_200_provider_type_0 import GetConnectionStatusResponse200ProviderType0
    from ..models.get_connection_status_response_200_senders_item import GetConnectionStatusResponse200SendersItem


T = TypeVar("T", bound="GetConnectionStatusResponse200")


@_attrs_define
class GetConnectionStatusResponse200:
    """
    Attributes:
        ready (bool | Unset): True when this project can actually send right now.
        provider (GetConnectionStatusResponse200ProviderType0 | None | Unset):
        domains (list[GetConnectionStatusResponse200DomainsItem] | Unset): Per-domain status incl. advisory
            `dmarc_status` (unknown | missing | found) — DMARC is not part of `ready`.
        senders (list[GetConnectionStatusResponse200SendersItem] | Unset):
        sends_paused (bool | Unset):
        daily_send_cap (int | None | Unset):
        settings_url (str | Unset): Where a human pastes the provider API key.
    """

    ready: bool | Unset = UNSET
    provider: GetConnectionStatusResponse200ProviderType0 | None | Unset = UNSET
    domains: list[GetConnectionStatusResponse200DomainsItem] | Unset = UNSET
    senders: list[GetConnectionStatusResponse200SendersItem] | Unset = UNSET
    sends_paused: bool | Unset = UNSET
    daily_send_cap: int | None | Unset = UNSET
    settings_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_connection_status_response_200_provider_type_0 import (
            GetConnectionStatusResponse200ProviderType0,
        )

        ready = self.ready

        provider: dict[str, Any] | None | Unset
        if isinstance(self.provider, Unset):
            provider = UNSET
        elif isinstance(self.provider, GetConnectionStatusResponse200ProviderType0):
            provider = self.provider.to_dict()
        else:
            provider = self.provider

        domains: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.domains, Unset):
            domains = []
            for domains_item_data in self.domains:
                domains_item = domains_item_data.to_dict()
                domains.append(domains_item)

        senders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.senders, Unset):
            senders = []
            for senders_item_data in self.senders:
                senders_item = senders_item_data.to_dict()
                senders.append(senders_item)

        sends_paused = self.sends_paused

        daily_send_cap: int | None | Unset
        if isinstance(self.daily_send_cap, Unset):
            daily_send_cap = UNSET
        else:
            daily_send_cap = self.daily_send_cap

        settings_url = self.settings_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ready is not UNSET:
            field_dict["ready"] = ready
        if provider is not UNSET:
            field_dict["provider"] = provider
        if domains is not UNSET:
            field_dict["domains"] = domains
        if senders is not UNSET:
            field_dict["senders"] = senders
        if sends_paused is not UNSET:
            field_dict["sends_paused"] = sends_paused
        if daily_send_cap is not UNSET:
            field_dict["daily_send_cap"] = daily_send_cap
        if settings_url is not UNSET:
            field_dict["settings_url"] = settings_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_connection_status_response_200_domains_item import GetConnectionStatusResponse200DomainsItem
        from ..models.get_connection_status_response_200_provider_type_0 import (
            GetConnectionStatusResponse200ProviderType0,
        )
        from ..models.get_connection_status_response_200_senders_item import GetConnectionStatusResponse200SendersItem

        d = dict(src_dict)
        ready = d.pop("ready", UNSET)

        def _parse_provider(data: object) -> GetConnectionStatusResponse200ProviderType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_type_0 = GetConnectionStatusResponse200ProviderType0.from_dict(data)

                return provider_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetConnectionStatusResponse200ProviderType0 | None | Unset, data)

        provider = _parse_provider(d.pop("provider", UNSET))

        _domains = d.pop("domains", UNSET)
        domains: list[GetConnectionStatusResponse200DomainsItem] | Unset = UNSET
        if _domains is not UNSET:
            domains = []
            for domains_item_data in _domains:
                domains_item = GetConnectionStatusResponse200DomainsItem.from_dict(domains_item_data)

                domains.append(domains_item)

        _senders = d.pop("senders", UNSET)
        senders: list[GetConnectionStatusResponse200SendersItem] | Unset = UNSET
        if _senders is not UNSET:
            senders = []
            for senders_item_data in _senders:
                senders_item = GetConnectionStatusResponse200SendersItem.from_dict(senders_item_data)

                senders.append(senders_item)

        sends_paused = d.pop("sends_paused", UNSET)

        def _parse_daily_send_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        daily_send_cap = _parse_daily_send_cap(d.pop("daily_send_cap", UNSET))

        settings_url = d.pop("settings_url", UNSET)

        get_connection_status_response_200 = cls(
            ready=ready,
            provider=provider,
            domains=domains,
            senders=senders,
            sends_paused=sends_paused,
            daily_send_cap=daily_send_cap,
            settings_url=settings_url,
        )

        get_connection_status_response_200.additional_properties = d
        return get_connection_status_response_200

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
