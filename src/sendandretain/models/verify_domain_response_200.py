from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verify_domain_response_200_dmarc import VerifyDomainResponse200Dmarc
    from ..models.verify_domain_response_200_dns_records_item import VerifyDomainResponse200DnsRecordsItem
    from ..models.verify_domain_response_200_tracking_type_0 import VerifyDomainResponse200TrackingType0


T = TypeVar("T", bound="VerifyDomainResponse200")


@_attrs_define
class VerifyDomainResponse200:
    """
    Attributes:
        domain (str | Unset):
        status (str | Unset):
        verified (bool | Unset):
        dns_records (list[VerifyDomainResponse200DnsRecordsItem] | Unset):
        dmarc (VerifyDomainResponse200Dmarc | Unset): Advisory DMARC state from our own DNS check. Never blocks
            verification; Gmail/Yahoo bulk-sender rules require a DMARC record on the From domain.
        tracking (None | Unset | VerifyDomainResponse200TrackingType0): Domain-level open/click tracking (Resend). Null
            for SendGrid — tracking is applied per send there. The tracking CNAME rides in dns_records (record: 'Tracking');
            click events won't fire until it resolves.
    """

    domain: str | Unset = UNSET
    status: str | Unset = UNSET
    verified: bool | Unset = UNSET
    dns_records: list[VerifyDomainResponse200DnsRecordsItem] | Unset = UNSET
    dmarc: VerifyDomainResponse200Dmarc | Unset = UNSET
    tracking: None | Unset | VerifyDomainResponse200TrackingType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.verify_domain_response_200_tracking_type_0 import VerifyDomainResponse200TrackingType0

        domain = self.domain

        status = self.status

        verified = self.verified

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
        elif isinstance(self.tracking, VerifyDomainResponse200TrackingType0):
            tracking = self.tracking.to_dict()
        else:
            tracking = self.tracking

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if domain is not UNSET:
            field_dict["domain"] = domain
        if status is not UNSET:
            field_dict["status"] = status
        if verified is not UNSET:
            field_dict["verified"] = verified
        if dns_records is not UNSET:
            field_dict["dns_records"] = dns_records
        if dmarc is not UNSET:
            field_dict["dmarc"] = dmarc
        if tracking is not UNSET:
            field_dict["tracking"] = tracking

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verify_domain_response_200_dmarc import VerifyDomainResponse200Dmarc
        from ..models.verify_domain_response_200_dns_records_item import VerifyDomainResponse200DnsRecordsItem
        from ..models.verify_domain_response_200_tracking_type_0 import VerifyDomainResponse200TrackingType0

        d = dict(src_dict)
        domain = d.pop("domain", UNSET)

        status = d.pop("status", UNSET)

        verified = d.pop("verified", UNSET)

        _dns_records = d.pop("dns_records", UNSET)
        dns_records: list[VerifyDomainResponse200DnsRecordsItem] | Unset = UNSET
        if _dns_records is not UNSET:
            dns_records = []
            for dns_records_item_data in _dns_records:
                dns_records_item = VerifyDomainResponse200DnsRecordsItem.from_dict(dns_records_item_data)

                dns_records.append(dns_records_item)

        _dmarc = d.pop("dmarc", UNSET)
        dmarc: VerifyDomainResponse200Dmarc | Unset
        if isinstance(_dmarc, Unset):
            dmarc = UNSET
        else:
            dmarc = VerifyDomainResponse200Dmarc.from_dict(_dmarc)

        def _parse_tracking(data: object) -> None | Unset | VerifyDomainResponse200TrackingType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tracking_type_0 = VerifyDomainResponse200TrackingType0.from_dict(data)

                return tracking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VerifyDomainResponse200TrackingType0, data)

        tracking = _parse_tracking(d.pop("tracking", UNSET))

        verify_domain_response_200 = cls(
            domain=domain,
            status=status,
            verified=verified,
            dns_records=dns_records,
            dmarc=dmarc,
            tracking=tracking,
        )

        verify_domain_response_200.additional_properties = d
        return verify_domain_response_200

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
