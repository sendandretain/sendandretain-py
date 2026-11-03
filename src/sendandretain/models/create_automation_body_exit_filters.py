from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item import (
        AutomationsPostRequestBodyContentApplicationJsonExitFiltersAdditionalPropertiesVariant0Item,
    )
    from ..models.create_automation_schema_0 import CreateAutomationSchema0


T = TypeVar("T", bound="CreateAutomationBodyExitFilters")


@_attrs_define
class CreateAutomationBodyExitFilters:
    """Per-exit filters keyed by exit event name, e.g. { "team.plan_changed": [{ path: "event.properties.plan", op: "eq",
    value: "paid" }] } — that exit then fires only on a paid plan. Each key must also be in exitEvents.

    """

    additional_properties: dict[
        str,
        CreateAutomationSchema0
        | list[AutomationsPostRequestBodyContentApplicationJsonExitFiltersAdditionalPropertiesVariant0Item],
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = []
                for componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item_data in prop:
                    componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item = componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item_data.to_dict()
                    field_dict[prop_name].append(
                        componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item
                    )

            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item import (
            AutomationsPostRequestBodyContentApplicationJsonExitFiltersAdditionalPropertiesVariant0Item,
        )
        from ..models.create_automation_schema_0 import CreateAutomationSchema0

        d = dict(src_dict)
        create_automation_body_exit_filters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> (
                CreateAutomationSchema0
                | list[AutomationsPostRequestBodyContentApplicationJsonExitFiltersAdditionalPropertiesVariant0Item]
            ):
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_0 = []
                    _additional_property_type_0 = data
                    for componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item_data in _additional_property_type_0:
                        componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item = AutomationsPostRequestBodyContentApplicationJsonExitFiltersAdditionalPropertiesVariant0Item.from_dict(
                            componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item_data
                        )

                        additional_property_type_0.append(
                            componentsschemas_automations_post_request_body_content_application_json_exit_filters_additional_properties_variant_0_item
                        )

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = CreateAutomationSchema0.from_dict(data)

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        create_automation_body_exit_filters.additional_properties = additional_properties
        return create_automation_body_exit_filters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> (
        CreateAutomationSchema0
        | list[AutomationsPostRequestBodyContentApplicationJsonExitFiltersAdditionalPropertiesVariant0Item]
    ):
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: CreateAutomationSchema0
        | list[AutomationsPostRequestBodyContentApplicationJsonExitFiltersAdditionalPropertiesVariant0Item],
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
