from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_domains_response_200_data_item_dns_records_item import (
        ListDomainsResponse200DataItemDnsRecordsItem,
    )


T = TypeVar("T", bound="ListDomainsResponse200DataItem")


@_attrs_define
class ListDomainsResponse200DataItem:
    """
    Attributes:
        id (str | Unset):
        domain (str | Unset):
        provider (str | Unset):
        status (str | Unset):
        verified (bool | Unset):
        dns_records (list[ListDomainsResponse200DataItemDnsRecordsItem] | Unset):
        region (None | str | Unset):
        verified_at (datetime.datetime | None | Unset):
        last_checked_at (datetime.datetime | None | Unset):
        created_at (datetime.datetime | Unset):
        dmarc_status (str | Unset): Advisory DMARC presence from our own DNS check: unknown | missing | found. Never
            affects `verified`.
        dmarc_record (None | str | Unset):
        dmarc_checked_at (datetime.datetime | None | Unset):
        open_tracking (bool | None | Unset): Open/click tracking flags. Null = never read from the provider (Resend) or
            per-send default applies (SendGrid).
        click_tracking (bool | None | Unset):
        tracking_subdomain (None | str | Unset):
    """

    id: str | Unset = UNSET
    domain: str | Unset = UNSET
    provider: str | Unset = UNSET
    status: str | Unset = UNSET
    verified: bool | Unset = UNSET
    dns_records: list[ListDomainsResponse200DataItemDnsRecordsItem] | Unset = UNSET
    region: None | str | Unset = UNSET
    verified_at: datetime.datetime | None | Unset = UNSET
    last_checked_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    dmarc_status: str | Unset = UNSET
    dmarc_record: None | str | Unset = UNSET
    dmarc_checked_at: datetime.datetime | None | Unset = UNSET
    open_tracking: bool | None | Unset = UNSET
    click_tracking: bool | None | Unset = UNSET
    tracking_subdomain: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        domain = self.domain

        provider = self.provider

        status = self.status

        verified = self.verified

        dns_records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dns_records, Unset):
            dns_records = []
            for dns_records_item_data in self.dns_records:
                dns_records_item = dns_records_item_data.to_dict()
                dns_records.append(dns_records_item)

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        verified_at: None | str | Unset
        if isinstance(self.verified_at, Unset):
            verified_at = UNSET
        elif isinstance(self.verified_at, datetime.datetime):
            verified_at = self.verified_at.isoformat()
        else:
            verified_at = self.verified_at

        last_checked_at: None | str | Unset
        if isinstance(self.last_checked_at, Unset):
            last_checked_at = UNSET
        elif isinstance(self.last_checked_at, datetime.datetime):
            last_checked_at = self.last_checked_at.isoformat()
        else:
            last_checked_at = self.last_checked_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        dmarc_status = self.dmarc_status

        dmarc_record: None | str | Unset
        if isinstance(self.dmarc_record, Unset):
            dmarc_record = UNSET
        else:
            dmarc_record = self.dmarc_record

        dmarc_checked_at: None | str | Unset
        if isinstance(self.dmarc_checked_at, Unset):
            dmarc_checked_at = UNSET
        elif isinstance(self.dmarc_checked_at, datetime.datetime):
            dmarc_checked_at = self.dmarc_checked_at.isoformat()
        else:
            dmarc_checked_at = self.dmarc_checked_at

        open_tracking: bool | None | Unset
        if isinstance(self.open_tracking, Unset):
            open_tracking = UNSET
        else:
            open_tracking = self.open_tracking

        click_tracking: bool | None | Unset
        if isinstance(self.click_tracking, Unset):
            click_tracking = UNSET
        else:
            click_tracking = self.click_tracking

        tracking_subdomain: None | str | Unset
        if isinstance(self.tracking_subdomain, Unset):
            tracking_subdomain = UNSET
        else:
            tracking_subdomain = self.tracking_subdomain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status
        if verified is not UNSET:
            field_dict["verified"] = verified
        if dns_records is not UNSET:
            field_dict["dns_records"] = dns_records
        if region is not UNSET:
            field_dict["region"] = region
        if verified_at is not UNSET:
            field_dict["verified_at"] = verified_at
        if last_checked_at is not UNSET:
            field_dict["last_checked_at"] = last_checked_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if dmarc_status is not UNSET:
            field_dict["dmarc_status"] = dmarc_status
        if dmarc_record is not UNSET:
            field_dict["dmarc_record"] = dmarc_record
        if dmarc_checked_at is not UNSET:
            field_dict["dmarc_checked_at"] = dmarc_checked_at
        if open_tracking is not UNSET:
            field_dict["open_tracking"] = open_tracking
        if click_tracking is not UNSET:
            field_dict["click_tracking"] = click_tracking
        if tracking_subdomain is not UNSET:
            field_dict["tracking_subdomain"] = tracking_subdomain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_domains_response_200_data_item_dns_records_item import (
            ListDomainsResponse200DataItemDnsRecordsItem,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        domain = d.pop("domain", UNSET)

        provider = d.pop("provider", UNSET)

        status = d.pop("status", UNSET)

        verified = d.pop("verified", UNSET)

        _dns_records = d.pop("dns_records", UNSET)
        dns_records: list[ListDomainsResponse200DataItemDnsRecordsItem] | Unset = UNSET
        if _dns_records is not UNSET:
            dns_records = []
            for dns_records_item_data in _dns_records:
                dns_records_item = ListDomainsResponse200DataItemDnsRecordsItem.from_dict(dns_records_item_data)

                dns_records.append(dns_records_item)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_verified_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                verified_at_type_0 = datetime.datetime.fromisoformat(data)

                return verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        verified_at = _parse_verified_at(d.pop("verified_at", UNSET))

        def _parse_last_checked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_checked_at = _parse_last_checked_at(d.pop("last_checked_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        dmarc_status = d.pop("dmarc_status", UNSET)

        def _parse_dmarc_record(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dmarc_record = _parse_dmarc_record(d.pop("dmarc_record", UNSET))

        def _parse_dmarc_checked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dmarc_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return dmarc_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        dmarc_checked_at = _parse_dmarc_checked_at(d.pop("dmarc_checked_at", UNSET))

        def _parse_open_tracking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        open_tracking = _parse_open_tracking(d.pop("open_tracking", UNSET))

        def _parse_click_tracking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        click_tracking = _parse_click_tracking(d.pop("click_tracking", UNSET))

        def _parse_tracking_subdomain(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracking_subdomain = _parse_tracking_subdomain(d.pop("tracking_subdomain", UNSET))

        list_domains_response_200_data_item = cls(
            id=id,
            domain=domain,
            provider=provider,
            status=status,
            verified=verified,
            dns_records=dns_records,
            region=region,
            verified_at=verified_at,
            last_checked_at=last_checked_at,
            created_at=created_at,
            dmarc_status=dmarc_status,
            dmarc_record=dmarc_record,
            dmarc_checked_at=dmarc_checked_at,
            open_tracking=open_tracking,
            click_tracking=click_tracking,
            tracking_subdomain=tracking_subdomain,
        )

        list_domains_response_200_data_item.additional_properties = d
        return list_domains_response_200_data_item

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
