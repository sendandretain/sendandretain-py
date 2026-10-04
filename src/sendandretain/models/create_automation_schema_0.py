from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_automation_schema_0_op import CreateAutomationSchema0Op

if TYPE_CHECKING:
    from ..models.create_automation_schema_0_conditions_variant_0 import CreateAutomationSchema0ConditionsVariant0


T = TypeVar("T", bound="CreateAutomationSchema0")


@_attrs_define
class CreateAutomationSchema0:
    """
    Attributes:
        op (CreateAutomationSchema0Op):
        conditions (list[CreateAutomationSchema0 | CreateAutomationSchema0ConditionsVariant0]):
    """

    op: CreateAutomationSchema0Op
    conditions: list[CreateAutomationSchema0 | CreateAutomationSchema0ConditionsVariant0]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_automation_schema_0_conditions_variant_0 import CreateAutomationSchema0ConditionsVariant0

        op = self.op.value

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item: dict[str, Any]
            if isinstance(conditions_item_data, CreateAutomationSchema0ConditionsVariant0):
                conditions_item = conditions_item_data.to_dict()
            else:
                conditions_item = conditions_item_data.to_dict()

            conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "op": op,
                "conditions": conditions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_automation_schema_0_conditions_variant_0 import CreateAutomationSchema0ConditionsVariant0

        d = dict(src_dict)
        op = CreateAutomationSchema0Op(d.pop("op"))

        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in _conditions:

            def _parse_conditions_item(
                data: object,
            ) -> CreateAutomationSchema0 | CreateAutomationSchema0ConditionsVariant0:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    conditions_item_type_0 = CreateAutomationSchema0ConditionsVariant0.from_dict(data)

                    return conditions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                conditions_item_type_1 = CreateAutomationSchema0.from_dict(data)

                return conditions_item_type_1

            conditions_item = _parse_conditions_item(conditions_item_data)

            conditions.append(conditions_item)

        create_automation_schema_0 = cls(
            op=op,
            conditions=conditions,
        )

        create_automation_schema_0.additional_properties = d
        return create_automation_schema_0

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
