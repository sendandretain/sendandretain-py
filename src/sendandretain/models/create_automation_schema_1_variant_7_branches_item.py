from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_automation_schema_0 import CreateAutomationSchema0
    from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
    from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
    from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
    from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
    from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
    from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
    from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6
    from ..models.create_automation_schema_1_variant_7 import CreateAutomationSchema1Variant7
    from ..models.create_automation_schema_1_variant_7_branches_filter_variant_0_item import (
        CreateAutomationSchema1Variant7BranchesFilterVariant0Item,
    )


T = TypeVar("T", bound="CreateAutomationSchema1Variant7BranchesItem")


@_attrs_define
class CreateAutomationSchema1Variant7BranchesItem:
    """
    Attributes:
        key (str):
        filter_ (CreateAutomationSchema0 | list[CreateAutomationSchema1Variant7BranchesFilterVariant0Item]):
        label (str | Unset):
        steps (list[CreateAutomationSchema1Variant0 | CreateAutomationSchema1Variant1 | CreateAutomationSchema1Variant2
            | CreateAutomationSchema1Variant3 | CreateAutomationSchema1Variant4 | CreateAutomationSchema1Variant5 |
            CreateAutomationSchema1Variant6 | CreateAutomationSchema1Variant7] | Unset):
    """

    key: str
    filter_: CreateAutomationSchema0 | list[CreateAutomationSchema1Variant7BranchesFilterVariant0Item]
    label: str | Unset = UNSET
    steps: (
        list[
            CreateAutomationSchema1Variant0
            | CreateAutomationSchema1Variant1
            | CreateAutomationSchema1Variant2
            | CreateAutomationSchema1Variant3
            | CreateAutomationSchema1Variant4
            | CreateAutomationSchema1Variant5
            | CreateAutomationSchema1Variant6
            | CreateAutomationSchema1Variant7
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
        from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
        from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
        from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
        from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
        from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
        from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6

        key = self.key

        filter_: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.filter_, list):
            filter_ = []
            for (
                componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item_data
            ) in self.filter_:
                componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item = (
                    componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item_data.to_dict()
                )
                filter_.append(componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item)

        else:
            filter_ = self.filter_.to_dict()

        label = self.label

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item: dict[str, Any]
                if isinstance(steps_item_data, CreateAutomationSchema1Variant0):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant1):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant2):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant3):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant4):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant5):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, CreateAutomationSchema1Variant6):
                    steps_item = steps_item_data.to_dict()
                else:
                    steps_item = steps_item_data.to_dict()

                steps.append(steps_item)

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
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_automation_schema_0 import CreateAutomationSchema0
        from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
        from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
        from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
        from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
        from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
        from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
        from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6
        from ..models.create_automation_schema_1_variant_7 import CreateAutomationSchema1Variant7
        from ..models.create_automation_schema_1_variant_7_branches_filter_variant_0_item import (
            CreateAutomationSchema1Variant7BranchesFilterVariant0Item,
        )

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_filter_(
            data: object,
        ) -> CreateAutomationSchema0 | list[CreateAutomationSchema1Variant7BranchesFilterVariant0Item]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_type_0 = []
                _filter_type_0 = data
                for (
                    componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item_data
                ) in _filter_type_0:
                    componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item = (
                        CreateAutomationSchema1Variant7BranchesFilterVariant0Item.from_dict(
                            componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item_data
                        )
                    )

                    filter_type_0.append(
                        componentsschemas_create_automation_schema_1_variant_7_branches_filter_variant_0_item
                    )

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            filter_type_1 = CreateAutomationSchema0.from_dict(data)

            return filter_type_1

        filter_ = _parse_filter_(d.pop("filter"))

        label = d.pop("label", UNSET)

        _steps = d.pop("steps", UNSET)
        steps: (
            list[
                CreateAutomationSchema1Variant0
                | CreateAutomationSchema1Variant1
                | CreateAutomationSchema1Variant2
                | CreateAutomationSchema1Variant3
                | CreateAutomationSchema1Variant4
                | CreateAutomationSchema1Variant5
                | CreateAutomationSchema1Variant6
                | CreateAutomationSchema1Variant7
            ]
            | Unset
        ) = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:

                def _parse_steps_item(
                    data: object,
                ) -> (
                    CreateAutomationSchema1Variant0
                    | CreateAutomationSchema1Variant1
                    | CreateAutomationSchema1Variant2
                    | CreateAutomationSchema1Variant3
                    | CreateAutomationSchema1Variant4
                    | CreateAutomationSchema1Variant5
                    | CreateAutomationSchema1Variant6
                    | CreateAutomationSchema1Variant7
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_0 = CreateAutomationSchema1Variant0.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_1 = CreateAutomationSchema1Variant1.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_2 = CreateAutomationSchema1Variant2.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_3 = CreateAutomationSchema1Variant3.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_4 = CreateAutomationSchema1Variant4.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_5 = CreateAutomationSchema1Variant5.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_6 = CreateAutomationSchema1Variant6.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_create_automation_schema_1_type_7 = CreateAutomationSchema1Variant7.from_dict(
                        data
                    )

                    return componentsschemas_create_automation_schema_1_type_7

                steps_item = _parse_steps_item(steps_item_data)

                steps.append(steps_item)

        create_automation_schema_1_variant_7_branches_item = cls(
            key=key,
            filter_=filter_,
            label=label,
            steps=steps,
        )

        create_automation_schema_1_variant_7_branches_item.additional_properties = d
        return create_automation_schema_1_variant_7_branches_item

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
