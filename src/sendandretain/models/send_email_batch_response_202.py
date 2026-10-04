from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_email_batch_response_202_data_item import SendEmailBatchResponse202DataItem


T = TypeVar("T", bound="SendEmailBatchResponse202")


@_attrs_define
class SendEmailBatchResponse202:
    """
    Attributes:
        data (list[SendEmailBatchResponse202DataItem] | Unset): Same order as the request.
        queued (int | Unset):
        failed (int | Unset):
    """

    data: list[SendEmailBatchResponse202DataItem] | Unset = UNSET
    queued: int | Unset = UNSET
    failed: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        queued = self.queued

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if queued is not UNSET:
            field_dict["queued"] = queued
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_email_batch_response_202_data_item import SendEmailBatchResponse202DataItem

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[SendEmailBatchResponse202DataItem] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = SendEmailBatchResponse202DataItem.from_dict(data_item_data)

                data.append(data_item)

        queued = d.pop("queued", UNSET)

        failed = d.pop("failed", UNSET)

        send_email_batch_response_202 = cls(
            data=data,
            queued=queued,
            failed=failed,
        )

        send_email_batch_response_202.additional_properties = d
        return send_email_batch_response_202

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
