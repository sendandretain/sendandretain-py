from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportSuppressionsResponse200")


@_attrs_define
class ImportSuppressionsResponse200:
    """
    Attributes:
        imported (int | Unset):
        failed (int | Unset):
        failures (list[str] | Unset):
    """

    imported: int | Unset = UNSET
    failed: int | Unset = UNSET
    failures: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        imported = self.imported

        failed = self.failed

        failures: list[str] | Unset = UNSET
        if not isinstance(self.failures, Unset):
            failures = self.failures

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if imported is not UNSET:
            field_dict["imported"] = imported
        if failed is not UNSET:
            field_dict["failed"] = failed
        if failures is not UNSET:
            field_dict["failures"] = failures

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        imported = d.pop("imported", UNSET)

        failed = d.pop("failed", UNSET)

        failures = cast(list[str], d.pop("failures", UNSET))

        import_suppressions_response_200 = cls(
            imported=imported,
            failed=failed,
            failures=failures,
        )

        import_suppressions_response_200.additional_properties = d
        return import_suppressions_response_200

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
