from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_template_body_variables_item_type import UpdateTemplateBodyVariablesItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTemplateBodyVariablesItem")


@_attrs_define
class UpdateTemplateBodyVariablesItem:
    """
    Attributes:
        name (str):
        type_ (UpdateTemplateBodyVariablesItemType | Unset):  Default: UpdateTemplateBodyVariablesItemType.STRING.
        required (bool | Unset):
        example (Any | Unset):
        fallback (Any | Unset):
    """

    name: str
    type_: UpdateTemplateBodyVariablesItemType | Unset = UpdateTemplateBodyVariablesItemType.STRING
    required: bool | Unset = UNSET
    example: Any | Unset = UNSET
    fallback: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        required = self.required

        example = self.example

        fallback = self.fallback

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if required is not UNSET:
            field_dict["required"] = required
        if example is not UNSET:
            field_dict["example"] = example
        if fallback is not UNSET:
            field_dict["fallback"] = fallback

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _type_ = d.pop("type", UNSET)
        type_: UpdateTemplateBodyVariablesItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpdateTemplateBodyVariablesItemType(_type_)

        required = d.pop("required", UNSET)

        example = d.pop("example", UNSET)

        fallback = d.pop("fallback", UNSET)

        update_template_body_variables_item = cls(
            name=name,
            type_=type_,
            required=required,
            example=example,
            fallback=fallback,
        )

        update_template_body_variables_item.additional_properties = d
        return update_template_body_variables_item

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
