from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEventEmailComplainedDataDetail")


@_attrs_define
class WebhookEventEmailComplainedDataDetail:
    """Provider detail, normalised. Fields are present only when the provider reported them.

    Attributes:
        feedback_type (bool | float | str | Unset):
    """

    feedback_type: bool | float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feedback_type: bool | float | str | Unset
        if isinstance(self.feedback_type, Unset):
            feedback_type = UNSET
        else:
            feedback_type = self.feedback_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feedback_type is not UNSET:
            field_dict["feedback_type"] = feedback_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_feedback_type(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        feedback_type = _parse_feedback_type(d.pop("feedback_type", UNSET))

        webhook_event_email_complained_data_detail = cls(
            feedback_type=feedback_type,
        )

        webhook_event_email_complained_data_detail.additional_properties = d
        return webhook_event_email_complained_data_detail

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
