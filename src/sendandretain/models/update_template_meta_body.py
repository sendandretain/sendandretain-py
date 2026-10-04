from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTemplateMetaBody")


@_attrs_define
class UpdateTemplateMetaBody:
    """
    Attributes:
        subject (str | Unset): New subject line.
        preview_text (str | Unset): Inbox preview text (the preheader). Rewrites the template's `<Preview>` line. Pass
            `""` to clear it.
        sender_id (None | Unset | UUID): Sender identity for this template. `null` resets to the project default sender.
    """

    subject: str | Unset = UNSET
    preview_text: str | Unset = UNSET
    sender_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        preview_text = self.preview_text

        sender_id: None | str | Unset
        if isinstance(self.sender_id, Unset):
            sender_id = UNSET
        elif isinstance(self.sender_id, UUID):
            sender_id = str(self.sender_id)
        else:
            sender_id = self.sender_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subject is not UNSET:
            field_dict["subject"] = subject
        if preview_text is not UNSET:
            field_dict["preview_text"] = preview_text
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject = d.pop("subject", UNSET)

        preview_text = d.pop("preview_text", UNSET)

        def _parse_sender_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sender_id_type_0 = UUID(data)

                return sender_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sender_id = _parse_sender_id(d.pop("sender_id", UNSET))

        update_template_meta_body = cls(
            subject=subject,
            preview_text=preview_text,
            sender_id=sender_id,
        )

        update_template_meta_body.additional_properties = d
        return update_template_meta_body

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
