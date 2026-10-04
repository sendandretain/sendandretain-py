from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_email_batch_response_202_data_item_error import SendEmailBatchResponse202DataItemError


T = TypeVar("T", bound="SendEmailBatchResponse202DataItem")


@_attrs_define
class SendEmailBatchResponse202DataItem:
    """
    Attributes:
        index (int | Unset):
        id (str | Unset):
        status (str | Unset):
        deduplicated (bool | Unset): An idempotency key matched a prior send.
        error (SendEmailBatchResponse202DataItemError | Unset): Present instead of `id`/`status` when this entry failed.
    """

    index: int | Unset = UNSET
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    deduplicated: bool | Unset = UNSET
    error: SendEmailBatchResponse202DataItemError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        id = self.id

        status = self.status

        deduplicated = self.deduplicated

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if deduplicated is not UNSET:
            field_dict["deduplicated"] = deduplicated
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_email_batch_response_202_data_item_error import SendEmailBatchResponse202DataItemError

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        deduplicated = d.pop("deduplicated", UNSET)

        _error = d.pop("error", UNSET)
        error: SendEmailBatchResponse202DataItemError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = SendEmailBatchResponse202DataItemError.from_dict(_error)

        send_email_batch_response_202_data_item = cls(
            index=index,
            id=id,
            status=status,
            deduplicated=deduplicated,
            error=error,
        )

        send_email_batch_response_202_data_item.additional_properties = d
        return send_email_batch_response_202_data_item

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
