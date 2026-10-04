from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_template_response_200_variables_item import GetTemplateResponse200VariablesItem


T = TypeVar("T", bound="GetTemplateResponse200")


@_attrs_define
class GetTemplateResponse200:
    """
    Attributes:
        id (str | Unset):
        slug (str | Unset):
        name (str | Unset):
        category (str | Unset):
        sender_id (None | str | Unset):
        published (bool | Unset):
        version (int | Unset):
        version_status (str | Unset):
        is_current (bool | Unset): True when this is the version that sends.
        subject (str | Unset):
        tsx_source (str | Unset):
        variables (list[GetTemplateResponse200VariablesItem] | Unset):
    """

    id: str | Unset = UNSET
    slug: str | Unset = UNSET
    name: str | Unset = UNSET
    category: str | Unset = UNSET
    sender_id: None | str | Unset = UNSET
    published: bool | Unset = UNSET
    version: int | Unset = UNSET
    version_status: str | Unset = UNSET
    is_current: bool | Unset = UNSET
    subject: str | Unset = UNSET
    tsx_source: str | Unset = UNSET
    variables: list[GetTemplateResponse200VariablesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        category = self.category

        sender_id: None | str | Unset
        if isinstance(self.sender_id, Unset):
            sender_id = UNSET
        else:
            sender_id = self.sender_id

        published = self.published

        version = self.version

        version_status = self.version_status

        is_current = self.is_current

        subject = self.subject

        tsx_source = self.tsx_source

        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if slug is not UNSET:
            field_dict["slug"] = slug
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if published is not UNSET:
            field_dict["published"] = published
        if version is not UNSET:
            field_dict["version"] = version
        if version_status is not UNSET:
            field_dict["version_status"] = version_status
        if is_current is not UNSET:
            field_dict["is_current"] = is_current
        if subject is not UNSET:
            field_dict["subject"] = subject
        if tsx_source is not UNSET:
            field_dict["tsx_source"] = tsx_source
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_template_response_200_variables_item import GetTemplateResponse200VariablesItem

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        slug = d.pop("slug", UNSET)

        name = d.pop("name", UNSET)

        category = d.pop("category", UNSET)

        def _parse_sender_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sender_id = _parse_sender_id(d.pop("sender_id", UNSET))

        published = d.pop("published", UNSET)

        version = d.pop("version", UNSET)

        version_status = d.pop("version_status", UNSET)

        is_current = d.pop("is_current", UNSET)

        subject = d.pop("subject", UNSET)

        tsx_source = d.pop("tsx_source", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: list[GetTemplateResponse200VariablesItem] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = GetTemplateResponse200VariablesItem.from_dict(variables_item_data)

                variables.append(variables_item)

        get_template_response_200 = cls(
            id=id,
            slug=slug,
            name=name,
            category=category,
            sender_id=sender_id,
            published=published,
            version=version,
            version_status=version_status,
            is_current=is_current,
            subject=subject,
            tsx_source=tsx_source,
            variables=variables,
        )

        get_template_response_200.additional_properties = d
        return get_template_response_200

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
