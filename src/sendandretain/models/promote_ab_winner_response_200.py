from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromoteAbWinnerResponse200")


@_attrs_define
class PromoteAbWinnerResponse200:
    """
    Attributes:
        position (int | Unset):
        promoted_variant (str | Unset):
    """

    position: int | Unset = UNSET
    promoted_variant: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        promoted_variant = self.promoted_variant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if promoted_variant is not UNSET:
            field_dict["promoted_variant"] = promoted_variant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        position = d.pop("position", UNSET)

        promoted_variant = d.pop("promoted_variant", UNSET)

        promote_ab_winner_response_200 = cls(
            position=position,
            promoted_variant=promoted_variant,
        )

        promote_ab_winner_response_200.additional_properties = d
        return promote_ab_winner_response_200

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
