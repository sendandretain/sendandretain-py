from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_brand_body_brand_colors import UpdateBrandBodyBrandColors
    from ..models.update_brand_body_brand_fonts import UpdateBrandBodyBrandFonts
    from ..models.update_brand_body_brand_logo import UpdateBrandBodyBrandLogo
    from ..models.update_brand_body_brand_social_links_item import UpdateBrandBodyBrandSocialLinksItem
    from ..models.update_brand_body_brand_voice import UpdateBrandBodyBrandVoice


T = TypeVar("T", bound="UpdateBrandBodyBrand")


@_attrs_define
class UpdateBrandBodyBrand:
    """Brand kit. A provided section REPLACES the stored one; omitted sections are untouched.

    Attributes:
        logo (UpdateBrandBodyBrandLogo | Unset):
        colors (UpdateBrandBodyBrandColors | Unset):
        fonts (UpdateBrandBodyBrandFonts | Unset):
        voice (UpdateBrandBodyBrandVoice | Unset):
        sign_off (str | Unset):
        footer_address (str | Unset):
        social_links (list[UpdateBrandBodyBrandSocialLinksItem] | Unset):
    """

    logo: UpdateBrandBodyBrandLogo | Unset = UNSET
    colors: UpdateBrandBodyBrandColors | Unset = UNSET
    fonts: UpdateBrandBodyBrandFonts | Unset = UNSET
    voice: UpdateBrandBodyBrandVoice | Unset = UNSET
    sign_off: str | Unset = UNSET
    footer_address: str | Unset = UNSET
    social_links: list[UpdateBrandBodyBrandSocialLinksItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.logo, Unset):
            logo = self.logo.to_dict()

        colors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors.to_dict()

        fonts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fonts, Unset):
            fonts = self.fonts.to_dict()

        voice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voice, Unset):
            voice = self.voice.to_dict()

        sign_off = self.sign_off

        footer_address = self.footer_address

        social_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.social_links, Unset):
            social_links = []
            for social_links_item_data in self.social_links:
                social_links_item = social_links_item_data.to_dict()
                social_links.append(social_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logo is not UNSET:
            field_dict["logo"] = logo
        if colors is not UNSET:
            field_dict["colors"] = colors
        if fonts is not UNSET:
            field_dict["fonts"] = fonts
        if voice is not UNSET:
            field_dict["voice"] = voice
        if sign_off is not UNSET:
            field_dict["signOff"] = sign_off
        if footer_address is not UNSET:
            field_dict["footerAddress"] = footer_address
        if social_links is not UNSET:
            field_dict["socialLinks"] = social_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_brand_body_brand_colors import UpdateBrandBodyBrandColors
        from ..models.update_brand_body_brand_fonts import UpdateBrandBodyBrandFonts
        from ..models.update_brand_body_brand_logo import UpdateBrandBodyBrandLogo
        from ..models.update_brand_body_brand_social_links_item import UpdateBrandBodyBrandSocialLinksItem
        from ..models.update_brand_body_brand_voice import UpdateBrandBodyBrandVoice

        d = dict(src_dict)
        _logo = d.pop("logo", UNSET)
        logo: UpdateBrandBodyBrandLogo | Unset
        if isinstance(_logo, Unset):
            logo = UNSET
        else:
            logo = UpdateBrandBodyBrandLogo.from_dict(_logo)

        _colors = d.pop("colors", UNSET)
        colors: UpdateBrandBodyBrandColors | Unset
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = UpdateBrandBodyBrandColors.from_dict(_colors)

        _fonts = d.pop("fonts", UNSET)
        fonts: UpdateBrandBodyBrandFonts | Unset
        if isinstance(_fonts, Unset):
            fonts = UNSET
        else:
            fonts = UpdateBrandBodyBrandFonts.from_dict(_fonts)

        _voice = d.pop("voice", UNSET)
        voice: UpdateBrandBodyBrandVoice | Unset
        if isinstance(_voice, Unset):
            voice = UNSET
        else:
            voice = UpdateBrandBodyBrandVoice.from_dict(_voice)

        sign_off = d.pop("signOff", UNSET)

        footer_address = d.pop("footerAddress", UNSET)

        _social_links = d.pop("socialLinks", UNSET)
        social_links: list[UpdateBrandBodyBrandSocialLinksItem] | Unset = UNSET
        if _social_links is not UNSET:
            social_links = []
            for social_links_item_data in _social_links:
                social_links_item = UpdateBrandBodyBrandSocialLinksItem.from_dict(social_links_item_data)

                social_links.append(social_links_item)

        update_brand_body_brand = cls(
            logo=logo,
            colors=colors,
            fonts=fonts,
            voice=voice,
            sign_off=sign_off,
            footer_address=footer_address,
            social_links=social_links,
        )

        update_brand_body_brand.additional_properties = d
        return update_brand_body_brand

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
