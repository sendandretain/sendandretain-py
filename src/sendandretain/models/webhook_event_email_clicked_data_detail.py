from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEventEmailClickedDataDetail")


@_attrs_define
class WebhookEventEmailClickedDataDetail:
    """Provider detail, normalised. Fields are present only when the provider reported them.

    Attributes:
        link (bool | float | str | Unset):
        user_agent (bool | float | str | Unset):
        ip (bool | float | str | Unset):
    """

    link: bool | float | str | Unset = UNSET
    user_agent: bool | float | str | Unset = UNSET
    ip: bool | float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link: bool | float | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        user_agent: bool | float | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        ip: bool | float | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link is not UNSET:
            field_dict["link"] = link
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_link(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        link = _parse_link(d.pop("link", UNSET))

        def _parse_user_agent(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

        def _parse_ip(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        webhook_event_email_clicked_data_detail = cls(
            link=link,
            user_agent=user_agent,
            ip=ip,
        )

        webhook_event_email_clicked_data_detail.additional_properties = d
        return webhook_event_email_clicked_data_detail

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
