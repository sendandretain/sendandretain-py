from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_automation_steps_schema_0_variant_0 import AddAutomationStepsSchema0Variant0
    from ..models.add_automation_steps_schema_0_variant_1 import AddAutomationStepsSchema0Variant1
    from ..models.add_automation_steps_schema_0_variant_2 import AddAutomationStepsSchema0Variant2
    from ..models.add_automation_steps_schema_0_variant_3 import AddAutomationStepsSchema0Variant3
    from ..models.add_automation_steps_schema_0_variant_4 import AddAutomationStepsSchema0Variant4
    from ..models.add_automation_steps_schema_0_variant_5 import AddAutomationStepsSchema0Variant5
    from ..models.add_automation_steps_schema_0_variant_6 import AddAutomationStepsSchema0Variant6
    from ..models.add_automation_steps_schema_0_variant_7 import AddAutomationStepsSchema0Variant7
    from ..models.add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item import (
        AddAutomationStepsSchema0Variant7BranchesFilterVariant0Item,
    )
    from ..models.add_automation_steps_schema_1 import AddAutomationStepsSchema1


T = TypeVar("T", bound="AddAutomationStepsSchema0Variant7BranchesItem")


@_attrs_define
class AddAutomationStepsSchema0Variant7BranchesItem:
    """
    Attributes:
        key (str):
        filter_ (AddAutomationStepsSchema1 | list[AddAutomationStepsSchema0Variant7BranchesFilterVariant0Item]):
        label (str | Unset):
        steps (list[AddAutomationStepsSchema0Variant0 | AddAutomationStepsSchema0Variant1 |
            AddAutomationStepsSchema0Variant2 | AddAutomationStepsSchema0Variant3 | AddAutomationStepsSchema0Variant4 |
            AddAutomationStepsSchema0Variant5 | AddAutomationStepsSchema0Variant6 | AddAutomationStepsSchema0Variant7] |
            Unset):
    """

    key: str
    filter_: AddAutomationStepsSchema1 | list[AddAutomationStepsSchema0Variant7BranchesFilterVariant0Item]
    label: str | Unset = UNSET
    steps: (
        list[
            AddAutomationStepsSchema0Variant0
            | AddAutomationStepsSchema0Variant1
            | AddAutomationStepsSchema0Variant2
            | AddAutomationStepsSchema0Variant3
            | AddAutomationStepsSchema0Variant4
            | AddAutomationStepsSchema0Variant5
            | AddAutomationStepsSchema0Variant6
            | AddAutomationStepsSchema0Variant7
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_automation_steps_schema_0_variant_0 import AddAutomationStepsSchema0Variant0
        from ..models.add_automation_steps_schema_0_variant_1 import AddAutomationStepsSchema0Variant1
        from ..models.add_automation_steps_schema_0_variant_2 import AddAutomationStepsSchema0Variant2
        from ..models.add_automation_steps_schema_0_variant_3 import AddAutomationStepsSchema0Variant3
        from ..models.add_automation_steps_schema_0_variant_4 import AddAutomationStepsSchema0Variant4
        from ..models.add_automation_steps_schema_0_variant_5 import AddAutomationStepsSchema0Variant5
        from ..models.add_automation_steps_schema_0_variant_6 import AddAutomationStepsSchema0Variant6

        key = self.key

        filter_: dict[str, Any] | list[dict[str, Any]]
        if isinstance(self.filter_, list):
            filter_ = []
            for (
                componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item_data
            ) in self.filter_:
                componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item = componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item_data.to_dict()
                filter_.append(componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item)

        else:
            filter_ = self.filter_.to_dict()

        label = self.label

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item: dict[str, Any]
                if isinstance(steps_item_data, AddAutomationStepsSchema0Variant0):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant1):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant2):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant3):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant4):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant5):
                    steps_item = steps_item_data.to_dict()
                elif isinstance(steps_item_data, AddAutomationStepsSchema0Variant6):
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
        from ..models.add_automation_steps_schema_0_variant_0 import AddAutomationStepsSchema0Variant0
        from ..models.add_automation_steps_schema_0_variant_1 import AddAutomationStepsSchema0Variant1
        from ..models.add_automation_steps_schema_0_variant_2 import AddAutomationStepsSchema0Variant2
        from ..models.add_automation_steps_schema_0_variant_3 import AddAutomationStepsSchema0Variant3
        from ..models.add_automation_steps_schema_0_variant_4 import AddAutomationStepsSchema0Variant4
        from ..models.add_automation_steps_schema_0_variant_5 import AddAutomationStepsSchema0Variant5
        from ..models.add_automation_steps_schema_0_variant_6 import AddAutomationStepsSchema0Variant6
        from ..models.add_automation_steps_schema_0_variant_7 import AddAutomationStepsSchema0Variant7
        from ..models.add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item import (
            AddAutomationStepsSchema0Variant7BranchesFilterVariant0Item,
        )
        from ..models.add_automation_steps_schema_1 import AddAutomationStepsSchema1

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_filter_(
            data: object,
        ) -> AddAutomationStepsSchema1 | list[AddAutomationStepsSchema0Variant7BranchesFilterVariant0Item]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_type_0 = []
                _filter_type_0 = data
                for (
                    componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item_data
                ) in _filter_type_0:
                    componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item = AddAutomationStepsSchema0Variant7BranchesFilterVariant0Item.from_dict(
                        componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item_data
                    )

                    filter_type_0.append(
                        componentsschemas_add_automation_steps_schema_0_variant_7_branches_filter_variant_0_item
                    )

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            filter_type_1 = AddAutomationStepsSchema1.from_dict(data)

            return filter_type_1

        filter_ = _parse_filter_(d.pop("filter"))

        label = d.pop("label", UNSET)

        _steps = d.pop("steps", UNSET)
        steps: (
            list[
                AddAutomationStepsSchema0Variant0
                | AddAutomationStepsSchema0Variant1
                | AddAutomationStepsSchema0Variant2
                | AddAutomationStepsSchema0Variant3
                | AddAutomationStepsSchema0Variant4
                | AddAutomationStepsSchema0Variant5
                | AddAutomationStepsSchema0Variant6
                | AddAutomationStepsSchema0Variant7
            ]
            | Unset
        ) = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:

                def _parse_steps_item(
                    data: object,
                ) -> (
                    AddAutomationStepsSchema0Variant0
                    | AddAutomationStepsSchema0Variant1
                    | AddAutomationStepsSchema0Variant2
                    | AddAutomationStepsSchema0Variant3
                    | AddAutomationStepsSchema0Variant4
                    | AddAutomationStepsSchema0Variant5
                    | AddAutomationStepsSchema0Variant6
                    | AddAutomationStepsSchema0Variant7
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_add_automation_steps_schema_0_type_0 = (
                            AddAutomationStepsSchema0Variant0.from_dict(data)
                        )

                        return componentsschemas_add_automation_steps_schema_0_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_add_automation_steps_schema_0_type_1 = (
                            AddAutomationStepsSchema0Variant1.from_dict(data)
                        )

                        return componentsschemas_add_automation_steps_schema_0_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_add_automation_steps_schema_0_type_2 = (
                            AddAutomationStepsSchema0Variant2.from_dict(data)
                        )

                        return componentsschemas_add_automation_steps_schema_0_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_add_automation_steps_schema_0_type_3 = (
                            AddAutomationStepsSchema0Variant3.from_dict(data)
                        )

                        return componentsschemas_add_automation_steps_schema_0_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_add_automation_steps_schema_0_type_4 = (
                            AddAutomationStepsSchema0Variant4.from_dict(data)
                        )

                        return componentsschemas_add_automation_steps_schema_0_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_add_automation_steps_schema_0_type_5 = (
                            AddAutomationStepsSchema0Variant5.from_dict(data)
                        )

                        return componentsschemas_add_automation_steps_schema_0_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_add_automation_steps_schema_0_type_6 = (
                            AddAutomationStepsSchema0Variant6.from_dict(data)
                        )

                        return componentsschemas_add_automation_steps_schema_0_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_add_automation_steps_schema_0_type_7 = (
                        AddAutomationStepsSchema0Variant7.from_dict(data)
                    )

                    return componentsschemas_add_automation_steps_schema_0_type_7

                steps_item = _parse_steps_item(steps_item_data)

                steps.append(steps_item)

        add_automation_steps_schema_0_variant_7_branches_item = cls(
            key=key,
            filter_=filter_,
            label=label,
            steps=steps,
        )

        add_automation_steps_schema_0_variant_7_branches_item.additional_properties = d
        return add_automation_steps_schema_0_variant_7_branches_item

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
