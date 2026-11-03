from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item import (
        AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0AdditionalPropertiesVariant0Item,
    )
    from ..models.update_automation_schema_0 import UpdateAutomationSchema0


T = TypeVar("T", bound="AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0")


@_attrs_define
class AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0:
    """Per-exit filters keyed by exit event name, e.g. { "team.plan_changed": [{ path: "event.properties.plan", op: "eq",
    value: "paid" }] } — that exit then fires only on a paid plan. Each key must also be in exitEvents.

    """

    additional_properties: dict[
        str,
        list[AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0AdditionalPropertiesVariant0Item]
        | UpdateAutomationSchema0,
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = []
                for componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item_data in prop:
                    componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item = componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item_data.to_dict()
                    field_dict[prop_name].append(
                        componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item
                    )

            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item import (
            AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0AdditionalPropertiesVariant0Item,
        )
        from ..models.update_automation_schema_0 import UpdateAutomationSchema0

        d = dict(src_dict)
        automations_id_patch_request_body_content_application_json_exit_filters_variant_0 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                list[
                    AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0AdditionalPropertiesVariant0Item
                ]
                | UpdateAutomationSchema0
            ):
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_0 = []
                    _additional_property_type_0 = data
                    for componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item_data in _additional_property_type_0:
                        componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item = AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0AdditionalPropertiesVariant0Item.from_dict(
                            componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item_data
                        )

                        additional_property_type_0.append(
                            componentsschemas_automations_id_patch_request_body_content_application_json_exit_filters_variant_0_additional_properties_variant_0_item
                        )

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = UpdateAutomationSchema0.from_dict(data)

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        automations_id_patch_request_body_content_application_json_exit_filters_variant_0.additional_properties = (
            additional_properties
        )
        return automations_id_patch_request_body_content_application_json_exit_filters_variant_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> (
        list[AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0AdditionalPropertiesVariant0Item]
        | UpdateAutomationSchema0
    ):
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: list[
            AutomationsIdPatchRequestBodyContentApplicationJsonExitFiltersVariant0AdditionalPropertiesVariant0Item
        ]
        | UpdateAutomationSchema0,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
