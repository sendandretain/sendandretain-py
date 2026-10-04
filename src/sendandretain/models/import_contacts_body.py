from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.import_contacts_body_contacts_item import ImportContactsBodyContactsItem


T = TypeVar("T", bound="ImportContactsBody")


@_attrs_define
class ImportContactsBody:
    """
    Attributes:
        contacts (list[ImportContactsBodyContactsItem]): Up to 1000 per call. Partial success — see `failed` /
            `failures`.
    """

    contacts: list[ImportContactsBodyContactsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contacts = []
        for contacts_item_data in self.contacts:
            contacts_item = contacts_item_data.to_dict()
            contacts.append(contacts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contacts": contacts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_contacts_body_contacts_item import ImportContactsBodyContactsItem

        d = dict(src_dict)
        contacts = []
        _contacts = d.pop("contacts")
        for contacts_item_data in _contacts:
            contacts_item = ImportContactsBodyContactsItem.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        import_contacts_body = cls(
            contacts=contacts,
        )

        import_contacts_body.additional_properties = d
        return import_contacts_body

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
