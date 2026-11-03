from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.render_template_response_200_headers import RenderTemplateResponse200Headers
    from ..models.render_template_response_200_link_check import RenderTemplateResponse200LinkCheck
    from ..models.render_template_response_200_props_used import RenderTemplateResponse200PropsUsed


T = TypeVar("T", bound="RenderTemplateResponse200")


@_attrs_define
class RenderTemplateResponse200:
    """
    Attributes:
        slug (str | Unset):
        version (int | Unset):
        as_sent (bool | Unset):
        subject (str | Unset):
        html (str | Unset):
        text (str | Unset):
        headers (RenderTemplateResponse200Headers | Unset): Present when `as_sent`: the headers a send carries,
            including `List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click`.
        link_check (RenderTemplateResponse200LinkCheck | Unset): Present with `check_links`: `{ checked, broken: [{ url,
            kind, status?, error? }], skipped }`.
        props_used (RenderTemplateResponse200PropsUsed | Unset): The props actually rendered with — generated examples
            when you passed none.
    """

    slug: str | Unset = UNSET
    version: int | Unset = UNSET
    as_sent: bool | Unset = UNSET
    subject: str | Unset = UNSET
    html: str | Unset = UNSET
    text: str | Unset = UNSET
    headers: RenderTemplateResponse200Headers | Unset = UNSET
    link_check: RenderTemplateResponse200LinkCheck | Unset = UNSET
    props_used: RenderTemplateResponse200PropsUsed | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        version = self.version

        as_sent = self.as_sent

        subject = self.subject

        html = self.html

        text = self.text

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        link_check: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_check, Unset):
            link_check = self.link_check.to_dict()

        props_used: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props_used, Unset):
            props_used = self.props_used.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slug is not UNSET:
            field_dict["slug"] = slug
        if version is not UNSET:
            field_dict["version"] = version
        if as_sent is not UNSET:
            field_dict["as_sent"] = as_sent
        if subject is not UNSET:
            field_dict["subject"] = subject
        if html is not UNSET:
            field_dict["html"] = html
        if text is not UNSET:
            field_dict["text"] = text
        if headers is not UNSET:
            field_dict["headers"] = headers
        if link_check is not UNSET:
            field_dict["link_check"] = link_check
        if props_used is not UNSET:
            field_dict["props_used"] = props_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.render_template_response_200_headers import RenderTemplateResponse200Headers
        from ..models.render_template_response_200_link_check import RenderTemplateResponse200LinkCheck
        from ..models.render_template_response_200_props_used import RenderTemplateResponse200PropsUsed

        d = dict(src_dict)
        slug = d.pop("slug", UNSET)

        version = d.pop("version", UNSET)

        as_sent = d.pop("as_sent", UNSET)

        subject = d.pop("subject", UNSET)

        html = d.pop("html", UNSET)

        text = d.pop("text", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: RenderTemplateResponse200Headers | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = RenderTemplateResponse200Headers.from_dict(_headers)

        _link_check = d.pop("link_check", UNSET)
        link_check: RenderTemplateResponse200LinkCheck | Unset
        if isinstance(_link_check, Unset):
            link_check = UNSET
        else:
            link_check = RenderTemplateResponse200LinkCheck.from_dict(_link_check)

        _props_used = d.pop("props_used", UNSET)
        props_used: RenderTemplateResponse200PropsUsed | Unset
        if isinstance(_props_used, Unset):
            props_used = UNSET
        else:
            props_used = RenderTemplateResponse200PropsUsed.from_dict(_props_used)

        render_template_response_200 = cls(
            slug=slug,
            version=version,
            as_sent=as_sent,
            subject=subject,
            html=html,
            text=text,
            headers=headers,
            link_check=link_check,
            props_used=props_used,
        )

        render_template_response_200.additional_properties = d
        return render_template_response_200

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
