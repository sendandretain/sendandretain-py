from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_step_schema_0_conditions_variant_0_op import UpdateStepSchema0ConditionsVariant0Op
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStepSchema0ConditionsVariant0")


@_attrs_define
class UpdateStepSchema0ConditionsVariant0:
    """
    Attributes:
        path (str): contact.attributes.<key>, contact.engagement.<key>, contact.subscriptionStatus, or
            event.properties.<key> (bare = event property). Engagement fields: emailsReceived, emailsSinceEngaged,
            daysSinceEngaged, openCount, clickCount, openRate, clickRate, lastOpenedAt, lastClickedAt.
        op (UpdateStepSchema0ConditionsVariant0Op | Unset):  Default: UpdateStepSchema0ConditionsVariant0Op.EQ.
        value (Any | Unset):
    """

    path: str
    op: UpdateStepSchema0ConditionsVariant0Op | Unset = UpdateStepSchema0ConditionsVariant0Op.EQ
    value: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        op: str | Unset = UNSET
        if not isinstance(self.op, Unset):
            op = self.op.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if op is not UNSET:
            field_dict["op"] = op
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path")

        _op = d.pop("op", UNSET)
        op: UpdateStepSchema0ConditionsVariant0Op | Unset
        if isinstance(_op, Unset):
            op = UNSET
        else:
            op = UpdateStepSchema0ConditionsVariant0Op(_op)

        value = d.pop("value", UNSET)

        update_step_schema_0_conditions_variant_0 = cls(
            path=path,
            op=op,
            value=value,
        )

        update_step_schema_0_conditions_variant_0.additional_properties = d
        return update_step_schema_0_conditions_variant_0

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
