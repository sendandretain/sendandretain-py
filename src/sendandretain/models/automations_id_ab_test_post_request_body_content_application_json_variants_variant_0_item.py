from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item")


@_attrs_define
class AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item:
    """
    Attributes:
        variant_key (str):
        version_id (UUID):
        weight (float | Unset):  Default: 1.0.
    """

    variant_key: str
    version_id: UUID
    weight: float | Unset = 1.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant_key = self.variant_key

        version_id = str(self.version_id)

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variantKey": variant_key,
                "versionId": version_id,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        variant_key = d.pop("variantKey")

        version_id = UUID(d.pop("versionId"))

        weight = d.pop("weight", UNSET)

        automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item = cls(
            variant_key=variant_key,
            version_id=version_id,
            weight=weight,
        )

        automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item.additional_properties = d
        return automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item

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
