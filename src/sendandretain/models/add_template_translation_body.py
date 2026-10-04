from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTemplateTranslationBody")


@_attrs_define
class AddTemplateTranslationBody:
    """
    Attributes:
        locale (str): BCP-47-ish locale tag.
        subject (str): Translated subject line.
        tsx_source (str | Unset): Translated TSX. Omit to translate the subject only and reuse the base layout.
    """

    locale: str
    subject: str
    tsx_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locale = self.locale

        subject = self.subject

        tsx_source = self.tsx_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "locale": locale,
                "subject": subject,
            }
        )
        if tsx_source is not UNSET:
            field_dict["tsx_source"] = tsx_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        locale = d.pop("locale")

        subject = d.pop("subject")

        tsx_source = d.pop("tsx_source", UNSET)

        add_template_translation_body = cls(
            locale=locale,
            subject=subject,
            tsx_source=tsx_source,
        )

        add_template_translation_body.additional_properties = d
        return add_template_translation_body

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
