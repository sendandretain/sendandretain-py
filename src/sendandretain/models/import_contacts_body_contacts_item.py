from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_contacts_body_contacts_item_attributes import ImportContactsBodyContactsItemAttributes


T = TypeVar("T", bound="ImportContactsBodyContactsItem")


@_attrs_define
class ImportContactsBodyContactsItem:
    """
    Attributes:
        email (str):
        external_id (None | str | Unset):
        attributes (ImportContactsBodyContactsItemAttributes | Unset):
        tags (list[str] | Unset):
    """

    email: str
    external_id: None | str | Unset = UNSET
    attributes: ImportContactsBodyContactsItemAttributes | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_contacts_body_contacts_item_attributes import ImportContactsBodyContactsItemAttributes

        d = dict(src_dict)
        email = d.pop("email")

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        _attributes = d.pop("attributes", UNSET)
        attributes: ImportContactsBodyContactsItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ImportContactsBodyContactsItemAttributes.from_dict(_attributes)

        tags = cast(list[str], d.pop("tags", UNSET))

        import_contacts_body_contacts_item = cls(
            email=email,
            external_id=external_id,
            attributes=attributes,
            tags=tags,
        )

        import_contacts_body_contacts_item.additional_properties = d
        return import_contacts_body_contacts_item

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
