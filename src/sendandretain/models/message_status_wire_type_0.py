from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_status_wire_type_0_headers import MessageStatusWireType0Headers


T = TypeVar("T", bound="MessageStatusWireType0")


@_attrs_define
class MessageStatusWireType0:
    """The message as the provider received it, for a message that went out (null otherwise). `headers` always — including
    `List-Unsubscribe` and `List-Unsubscribe-Post`; `subject`, `html` and `text` with `?include=body`. Bodies are not
    archived: this is rebuilt from the stored version and props with the project's CURRENT settings (`reconstructed:
    true`, explained in `note`).

        Attributes:
            reconstructed (bool | Unset):
            note (str | Unset):
            headers (MessageStatusWireType0Headers | Unset):
            subject (str | Unset):
            html (str | Unset):
            text (str | Unset):
    """

    reconstructed: bool | Unset = UNSET
    note: str | Unset = UNSET
    headers: MessageStatusWireType0Headers | Unset = UNSET
    subject: str | Unset = UNSET
    html: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reconstructed = self.reconstructed

        note = self.note

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        subject = self.subject

        html = self.html

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reconstructed is not UNSET:
            field_dict["reconstructed"] = reconstructed
        if note is not UNSET:
            field_dict["note"] = note
        if headers is not UNSET:
            field_dict["headers"] = headers
        if subject is not UNSET:
            field_dict["subject"] = subject
        if html is not UNSET:
            field_dict["html"] = html
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_status_wire_type_0_headers import MessageStatusWireType0Headers

        d = dict(src_dict)
        reconstructed = d.pop("reconstructed", UNSET)

        note = d.pop("note", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: MessageStatusWireType0Headers | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = MessageStatusWireType0Headers.from_dict(_headers)

        subject = d.pop("subject", UNSET)

        html = d.pop("html", UNSET)

        text = d.pop("text", UNSET)

        message_status_wire_type_0 = cls(
            reconstructed=reconstructed,
            note=note,
            headers=headers,
            subject=subject,
            html=html,
            text=text,
        )

        message_status_wire_type_0.additional_properties = d
        return message_status_wire_type_0

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
