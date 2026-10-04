from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.send_result_status import SendResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SendResult")


@_attrs_define
class SendResult:
    """
    Attributes:
        id (str): Message id — use it with GET /api/v1/emails/{id}.
        status (SendResultStatus): `sent` (delivered to provider synchronously), `queued` (throttled to the worker), or
            `scheduled`.
        deduplicated (bool | Unset): Present and true when a matching Idempotency-Key replayed a prior send.
    """

    id: str
    status: SendResultStatus
    deduplicated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        deduplicated = self.deduplicated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if deduplicated is not UNSET:
            field_dict["deduplicated"] = deduplicated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = SendResultStatus(d.pop("status"))

        deduplicated = d.pop("deduplicated", UNSET)

        send_result = cls(
            id=id,
            status=status,
            deduplicated=deduplicated,
        )

        send_result.additional_properties = d
        return send_result

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
