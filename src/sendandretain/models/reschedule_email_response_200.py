from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reschedule_email_response_200_status import RescheduleEmailResponse200Status
from ..types import UNSET, Unset

T = TypeVar("T", bound="RescheduleEmailResponse200")


@_attrs_define
class RescheduleEmailResponse200:
    """
    Attributes:
        id (str | Unset):
        status (RescheduleEmailResponse200Status | Unset):
        scheduled_at (str | Unset):
    """

    id: str | Unset = UNSET
    status: RescheduleEmailResponse200Status | Unset = UNSET
    scheduled_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        scheduled_at = self.scheduled_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if scheduled_at is not UNSET:
            field_dict["scheduled_at"] = scheduled_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: RescheduleEmailResponse200Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RescheduleEmailResponse200Status(_status)

        scheduled_at = d.pop("scheduled_at", UNSET)

        reschedule_email_response_200 = cls(
            id=id,
            status=status,
            scheduled_at=scheduled_at,
        )

        reschedule_email_response_200.additional_properties = d
        return reschedule_email_response_200

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
