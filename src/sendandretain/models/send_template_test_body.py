from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.send_template_test_body_props import SendTemplateTestBodyProps


T = TypeVar("T", bound="SendTemplateTestBody")


@_attrs_define
class SendTemplateTestBody:
    """
    Attributes:
        to (str): Where to send the test.
        version (int | Unset): Version to send. Omit for the latest — drafts included.
        props (SendTemplateTestBodyProps | Unset): Values for the template's variables.
    """

    to: str
    version: int | Unset = UNSET
    props: SendTemplateTestBodyProps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to = self.to

        version = self.version

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "to": to,
            }
        )
        if version is not UNSET:
            field_dict["version"] = version
        if props is not UNSET:
            field_dict["props"] = props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.send_template_test_body_props import SendTemplateTestBodyProps

        d = dict(src_dict)
        to = d.pop("to")

        version = d.pop("version", UNSET)

        _props = d.pop("props", UNSET)
        props: SendTemplateTestBodyProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = SendTemplateTestBodyProps.from_dict(_props)

        send_template_test_body = cls(
            to=to,
            version=version,
            props=props,
        )

        send_template_test_body.additional_properties = d
        return send_template_test_body

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
