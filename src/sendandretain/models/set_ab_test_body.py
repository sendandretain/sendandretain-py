from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item import (
        AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item,
    )


T = TypeVar("T", bound="SetAbTestBody")


@_attrs_define
class SetAbTestBody:
    """
    Attributes:
        position (int): Send step to split.
        variants (list[AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item] | None): Weighted
            template VERSIONS. Create them with `PATCH /api/v1/templates/{slug}` + `variant_key`, publish each, then attach
            here. `null` clears the split.
    """

    position: int
    variants: list[AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        variants: list[dict[str, Any]] | None
        if isinstance(self.variants, list):
            variants = []
            for componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item_data in self.variants:
                componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item = componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item_data.to_dict()
                variants.append(
                    componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item
                )

        else:
            variants = self.variants

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "variants": variants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item import (
            AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item,
        )

        d = dict(src_dict)
        position = d.pop("position")

        def _parse_variants(
            data: object,
        ) -> list[AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variants_type_0 = []
                _variants_type_0 = data
                for componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item_data in _variants_type_0:
                    componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item = AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item.from_dict(
                        componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item_data
                    )

                    variants_type_0.append(
                        componentsschemas_automations_id_ab_test_post_request_body_content_application_json_variants_variant_0_item
                    )

                return variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AutomationsIdAbTestPostRequestBodyContentApplicationJsonVariantsVariant0Item] | None, data)

        variants = _parse_variants(d.pop("variants"))

        set_ab_test_body = cls(
            position=position,
            variants=variants,
        )

        set_ab_test_body.additional_properties = d
        return set_ab_test_body

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
