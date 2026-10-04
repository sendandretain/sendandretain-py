from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_domain_response_201_dmarc import CreateDomainResponse201Dmarc
    from ..models.create_domain_response_201_dns_records_item import CreateDomainResponse201DnsRecordsItem
    from ..models.create_domain_response_201_tracking_type_0 import CreateDomainResponse201TrackingType0


T = TypeVar("T", bound="CreateDomainResponse201")


@_attrs_define
class CreateDomainResponse201:
    """
    Attributes:
        id (str | Unset):
        domain (str | Unset):
        status (str | Unset):
        dns_records (list[CreateDomainResponse201DnsRecordsItem] | Unset):
        dmarc (CreateDomainResponse201Dmarc | Unset): Advisory DMARC state from our own DNS check. Never blocks
            verification; Gmail/Yahoo bulk-sender rules require a DMARC record on the From domain.
        tracking (CreateDomainResponse201TrackingType0 | None | Unset): Domain-level open/click tracking (Resend). Null
            for SendGrid — tracking is applied per send there. The tracking CNAME rides in dns_records (record: 'Tracking');
            click events won't fire until it resolves.
    """

    id: str | Unset = UNSET
    domain: str | Unset = UNSET
    status: str | Unset = UNSET
    dns_records: list[CreateDomainResponse201DnsRecordsItem] | Unset = UNSET
    dmarc: CreateDomainResponse201Dmarc | Unset = UNSET
    tracking: CreateDomainResponse201TrackingType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_domain_response_201_tracking_type_0 import CreateDomainResponse201TrackingType0

        id = self.id

        domain = self.domain

        status = self.status

        dns_records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dns_records, Unset):
            dns_records = []
            for dns_records_item_data in self.dns_records:
                dns_records_item = dns_records_item_data.to_dict()
                dns_records.append(dns_records_item)

        dmarc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dmarc, Unset):
            dmarc = self.dmarc.to_dict()

        tracking: dict[str, Any] | None | Unset
        if isinstance(self.tracking, Unset):
            tracking = UNSET
        elif isinstance(self.tracking, CreateDomainResponse201TrackingType0):
            tracking = self.tracking.to_dict()
        else:
            tracking = self.tracking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if domain is not UNSET:
            field_dict["domain"] = domain
        if status is not UNSET:
            field_dict["status"] = status
        if dns_records is not UNSET:
            field_dict["dns_records"] = dns_records
        if dmarc is not UNSET:
            field_dict["dmarc"] = dmarc
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_domain_response_201_dmarc import CreateDomainResponse201Dmarc
        from ..models.create_domain_response_201_dns_records_item import CreateDomainResponse201DnsRecordsItem
        from ..models.create_domain_response_201_tracking_type_0 import CreateDomainResponse201TrackingType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        domain = d.pop("domain", UNSET)

        status = d.pop("status", UNSET)

        _dns_records = d.pop("dns_records", UNSET)
        dns_records: list[CreateDomainResponse201DnsRecordsItem] | Unset = UNSET
        if _dns_records is not UNSET:
            dns_records = []
            for dns_records_item_data in _dns_records:
                dns_records_item = CreateDomainResponse201DnsRecordsItem.from_dict(dns_records_item_data)

                dns_records.append(dns_records_item)

        _dmarc = d.pop("dmarc", UNSET)
        dmarc: CreateDomainResponse201Dmarc | Unset
        if isinstance(_dmarc, Unset):
            dmarc = UNSET
        else:
            dmarc = CreateDomainResponse201Dmarc.from_dict(_dmarc)

        def _parse_tracking(data: object) -> CreateDomainResponse201TrackingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tracking_type_0 = CreateDomainResponse201TrackingType0.from_dict(data)

                return tracking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateDomainResponse201TrackingType0 | None | Unset, data)

        tracking = _parse_tracking(d.pop("tracking", UNSET))

        create_domain_response_201 = cls(
            id=id,
            domain=domain,
            status=status,
            dns_records=dns_records,
            dmarc=dmarc,
            tracking=tracking,
        )

        create_domain_response_201.additional_properties = d
        return create_domain_response_201

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
