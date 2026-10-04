from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_template_body_category import UpdateTemplateBodyCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_template_body_variables_item import UpdateTemplateBodyVariablesItem


T = TypeVar("T", bound="UpdateTemplateBody")


@_attrs_define
class UpdateTemplateBody:
    """
    Attributes:
        subject (str | Unset): New subject line.
        tsx_source (str | Unset): New TSX source. Omit to carry the current source forward.
        variables (list[UpdateTemplateBodyVariablesItem] | Unset):
        name (str | Unset):
        category (UpdateTemplateBodyCategory | Unset):
        variant_key (str | Unset): Create this draft as an A/B variant instead of the base mainline.
    """

    subject: str | Unset = UNSET
    tsx_source: str | Unset = UNSET
    variables: list[UpdateTemplateBodyVariablesItem] | Unset = UNSET
    name: str | Unset = UNSET
    category: UpdateTemplateBodyCategory | Unset = UNSET
    variant_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        tsx_source = self.tsx_source

        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        name = self.name

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        variant_key = self.variant_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if tsx_source is not UNSET:
            field_dict["tsx_source"] = tsx_source
        if variables is not UNSET:
            field_dict["variables"] = variables
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if variant_key is not UNSET:
            field_dict["variant_key"] = variant_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_template_body_variables_item import UpdateTemplateBodyVariablesItem

        d = dict(src_dict)
        subject = d.pop("subject", UNSET)

        tsx_source = d.pop("tsx_source", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: list[UpdateTemplateBodyVariablesItem] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = UpdateTemplateBodyVariablesItem.from_dict(variables_item_data)

                variables.append(variables_item)

        name = d.pop("name", UNSET)

        _category = d.pop("category", UNSET)
        category: UpdateTemplateBodyCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = UpdateTemplateBodyCategory(_category)

        variant_key = d.pop("variant_key", UNSET)

        update_template_body = cls(
            subject=subject,
            tsx_source=tsx_source,
            variables=variables,
            name=name,
            category=category,
            variant_key=variant_key,
        )

        update_template_body.additional_properties = d
        return update_template_body

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
