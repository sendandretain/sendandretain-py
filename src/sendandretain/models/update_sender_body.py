from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSenderBody")


@_attrs_define
class UpdateSenderBody:
    """
    Attributes:
        from_name (str | Unset): New display name.
        reply_to (None | str | Unset): New Reply-To. null clears it.
        is_default (bool | Unset): Pass `true` to make this the project default (demotes the previous one).
    """

    from_name: str | Unset = UNSET
    reply_to: None | str | Unset = UNSET
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_name = self.from_name

        reply_to: None | str | Unset
        if isinstance(self.reply_to, Unset):
            reply_to = UNSET
        else:
            reply_to = self.reply_to

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_name is not UNSET:
            field_dict["from_name"] = from_name
        if reply_to is not UNSET:
            field_dict["reply_to"] = reply_to
        if is_default is not UNSET:
            field_dict["is_default"] = is_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_name = d.pop("from_name", UNSET)

        def _parse_reply_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reply_to = _parse_reply_to(d.pop("reply_to", UNSET))

        is_default = d.pop("is_default", UNSET)

        update_sender_body = cls(
            from_name=from_name,
            reply_to=reply_to,
            is_default=is_default,
        )

        update_sender_body.additional_properties = d
        return update_sender_body

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
