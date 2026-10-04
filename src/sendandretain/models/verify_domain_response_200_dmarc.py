from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verify_domain_response_200_dmarc_recommended_record import (
        VerifyDomainResponse200DmarcRecommendedRecord,
    )


T = TypeVar("T", bound="VerifyDomainResponse200Dmarc")


@_attrs_define
class VerifyDomainResponse200Dmarc:
    """Advisory DMARC state from our own DNS check. Never blocks verification; Gmail/Yahoo bulk-sender rules require a
    DMARC record on the From domain.

        Attributes:
            status (str | Unset): unknown (not checked / DNS error) | missing | found.
            record (None | str | Unset): The DMARC TXT record found, if any.
            recommended_record (VerifyDomainResponse200DmarcRecommendedRecord | Unset): Present while DMARC isn't confirmed
                — publish this TXT record.
    """

    status: str | Unset = UNSET
    record: None | str | Unset = UNSET
    recommended_record: VerifyDomainResponse200DmarcRecommendedRecord | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        record: None | str | Unset
        if isinstance(self.record, Unset):
            record = UNSET
        else:
            record = self.record

        recommended_record: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recommended_record, Unset):
            recommended_record = self.recommended_record.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if record is not UNSET:
            field_dict["record"] = record
        if recommended_record is not UNSET:
            field_dict["recommendedRecord"] = recommended_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.verify_domain_response_200_dmarc_recommended_record import (
            VerifyDomainResponse200DmarcRecommendedRecord,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        def _parse_record(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        record = _parse_record(d.pop("record", UNSET))

        _recommended_record = d.pop("recommendedRecord", UNSET)
        recommended_record: VerifyDomainResponse200DmarcRecommendedRecord | Unset
        if isinstance(_recommended_record, Unset):
            recommended_record = UNSET
        else:
            recommended_record = VerifyDomainResponse200DmarcRecommendedRecord.from_dict(_recommended_record)

        verify_domain_response_200_dmarc = cls(
            status=status,
            record=record,
            recommended_record=recommended_record,
        )

        verify_domain_response_200_dmarc.additional_properties = d
        return verify_domain_response_200_dmarc

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
