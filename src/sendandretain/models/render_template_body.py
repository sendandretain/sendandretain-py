from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.render_template_body_props import RenderTemplateBodyProps


T = TypeVar("T", bound="RenderTemplateBody")


@_attrs_define
class RenderTemplateBody:
    """
    Attributes:
        version (int | Unset): Version to render. Omit for the latest.
        props (RenderTemplateBodyProps | Unset): Values for the template's variables. Omit to render with generated
            example props.
    """

    version: int | Unset = UNSET
    props: RenderTemplateBodyProps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if props is not UNSET:
            field_dict["props"] = props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.render_template_body_props import RenderTemplateBodyProps

        d = dict(src_dict)
        version = d.pop("version", UNSET)

        _props = d.pop("props", UNSET)
        props: RenderTemplateBodyProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = RenderTemplateBodyProps.from_dict(_props)

        render_template_body = cls(
            version=version,
            props=props,
        )

        render_template_body.additional_properties = d
        return render_template_body

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
