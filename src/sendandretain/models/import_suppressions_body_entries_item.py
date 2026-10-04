from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_suppressions_body_entries_item_reason import ImportSuppressionsBodyEntriesItemReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportSuppressionsBodyEntriesItem")


@_attrs_define
class ImportSuppressionsBodyEntriesItem:
    """
    Attributes:
        email (str):
        reason (ImportSuppressionsBodyEntriesItemReason | Unset):
        note (str | Unset):
    """

    email: str
    reason: ImportSuppressionsBodyEntriesItemReason | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        _reason = d.pop("reason", UNSET)
        reason: ImportSuppressionsBodyEntriesItemReason | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ImportSuppressionsBodyEntriesItemReason(_reason)

        note = d.pop("note", UNSET)

        import_suppressions_body_entries_item = cls(
            email=email,
            reason=reason,
            note=note,
        )

        import_suppressions_body_entries_item.additional_properties = d
        return import_suppressions_body_entries_item

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
