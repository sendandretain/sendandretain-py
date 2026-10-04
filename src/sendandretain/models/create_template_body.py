from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_template_body_category import CreateTemplateBodyCategory
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_template_body_variables_item import CreateTemplateBodyVariablesItem


T = TypeVar("T", bound="CreateTemplateBody")


@_attrs_define
class CreateTemplateBody:
    """
    Attributes:
        slug (str): kebab-case identity, unique in the project. This is what `POST /api/v1/emails` sends by.
        name (str): Human label for the dashboard.
        category (CreateTemplateBodyCategory): `transactional` (receipts, resets — delivered even to unsubscribed
            contacts) or `lifecycle` (marketing — not delivered to unsubscribed contacts). Both carry List-Unsubscribe
            headers and an unsubscribe footer; the category decides only who an existing unsubscribe blocks.
        subject (str): Subject line. Supports `{{variable}}` interpolation.
        tsx_source (str): react.email TSX. May import only `react` and `@react-email/components` — the allowlist is
            enforced at compile time and a violation returns `invalid_request`.
        description (str | Unset):
        variables (list[CreateTemplateBodyVariablesItem] | Unset): Declared template variables, used to generate example
            props for rendering.
    """

    slug: str
    name: str
    category: CreateTemplateBodyCategory
    subject: str
    tsx_source: str
    description: str | Unset = UNSET
    variables: list[CreateTemplateBodyVariablesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        name = self.name

        category = self.category.value

        subject = self.subject

        tsx_source = self.tsx_source

        description = self.description

        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "category": category,
                "subject": subject,
                "tsx_source": tsx_source,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_template_body_variables_item import CreateTemplateBodyVariablesItem

        d = dict(src_dict)
        slug = d.pop("slug")

        name = d.pop("name")

        category = CreateTemplateBodyCategory(d.pop("category"))

        subject = d.pop("subject")

        tsx_source = d.pop("tsx_source")

        description = d.pop("description", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: list[CreateTemplateBodyVariablesItem] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = CreateTemplateBodyVariablesItem.from_dict(variables_item_data)

                variables.append(variables_item)

        create_template_body = cls(
            slug=slug,
            name=name,
            category=category,
            subject=subject,
            tsx_source=tsx_source,
            description=description,
            variables=variables,
        )

        create_template_body.additional_properties = d
        return create_template_body

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
