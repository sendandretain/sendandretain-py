from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item import (
        AutomationsStepsPutRequestBodyContentApplicationJsonPatchBranchesFilterVariant0Item,
    )
    from ..models.update_step_schema_0 import UpdateStepSchema0


T = TypeVar("T", bound="UpdateAutomationStepBodyPatchBranchesItem")


@_attrs_define
class UpdateAutomationStepBodyPatchBranchesItem:
    """
    Attributes:
        key (str):
        filter_ (list[AutomationsStepsPutRequestBodyContentApplicationJsonPatchBranchesFilterVariant0Item] |
            UpdateStepSchema0):
        label (str | Unset):
    """

    key: str
    filter_: (
        list[AutomationsStepsPutRequestBodyContentApplicationJsonPatchBranchesFilterVariant0Item] | UpdateStepSchema0
    )
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        filter_: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.filter_, list):
            filter_ = []
            for componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item_data in self.filter_:
                componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item = componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item_data.to_dict()
                filter_.append(
                    componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item
                )

        else:
            filter_ = self.filter_.to_dict()

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "filter": filter_,
            }
        )
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item import (
            AutomationsStepsPutRequestBodyContentApplicationJsonPatchBranchesFilterVariant0Item,
        )
        from ..models.update_step_schema_0 import UpdateStepSchema0

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_filter_(
            data: object,
        ) -> (
            list[AutomationsStepsPutRequestBodyContentApplicationJsonPatchBranchesFilterVariant0Item]
            | UpdateStepSchema0
        ):
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_type_0 = []
                _filter_type_0 = data
                for componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item_data in _filter_type_0:
                    componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item = AutomationsStepsPutRequestBodyContentApplicationJsonPatchBranchesFilterVariant0Item.from_dict(
                        componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item_data
                    )

                    filter_type_0.append(
                        componentsschemas_automations_steps_put_request_body_content_application_json_patch_branches_filter_variant_0_item
                    )

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            filter_type_1 = UpdateStepSchema0.from_dict(data)

            return filter_type_1

        filter_ = _parse_filter_(d.pop("filter"))

        label = d.pop("label", UNSET)

        update_automation_step_body_patch_branches_item = cls(
            key=key,
            filter_=filter_,
            label=label,
        )

        update_automation_step_body_patch_branches_item.additional_properties = d
        return update_automation_step_body_patch_branches_item

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
