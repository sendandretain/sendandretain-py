from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_onboarding_steps_response_200_steps_item import GetOnboardingStepsResponse200StepsItem


T = TypeVar("T", bound="GetOnboardingStepsResponse200")


@_attrs_define
class GetOnboardingStepsResponse200:
    """
    Attributes:
        phase (None | str | Unset): understand | strategy | content | live, or null once complete.
        complete (bool | Unset):
        done_count (int | Unset):
        total_count (int | Unset):
        next_ (None | str | Unset): Address of the first unfinished step, e.g. `1.5`.
        steps (list[GetOnboardingStepsResponse200StepsItem] | Unset): Each: `address`, `key`, `title`, `phase`, `done`,
            `in_progress`, `detail[]`.
    """

    phase: None | str | Unset = UNSET
    complete: bool | Unset = UNSET
    done_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    next_: None | str | Unset = UNSET
    steps: list[GetOnboardingStepsResponse200StepsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase: None | str | Unset
        if isinstance(self.phase, Unset):
            phase = UNSET
        else:
            phase = self.phase

        complete = self.complete

        done_count = self.done_count

        total_count = self.total_count

        next_: None | str | Unset
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase is not UNSET:
            field_dict["phase"] = phase
        if complete is not UNSET:
            field_dict["complete"] = complete
        if done_count is not UNSET:
            field_dict["done_count"] = done_count
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_ is not UNSET:
            field_dict["next"] = next_
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_onboarding_steps_response_200_steps_item import GetOnboardingStepsResponse200StepsItem

        d = dict(src_dict)

        def _parse_phase(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phase = _parse_phase(d.pop("phase", UNSET))

        complete = d.pop("complete", UNSET)

        done_count = d.pop("done_count", UNSET)

        total_count = d.pop("total_count", UNSET)

        def _parse_next_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_ = _parse_next_(d.pop("next", UNSET))

        _steps = d.pop("steps", UNSET)
        steps: list[GetOnboardingStepsResponse200StepsItem] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = GetOnboardingStepsResponse200StepsItem.from_dict(steps_item_data)

                steps.append(steps_item)

        get_onboarding_steps_response_200 = cls(
            phase=phase,
            complete=complete,
            done_count=done_count,
            total_count=total_count,
            next_=next_,
            steps=steps,
        )

        get_onboarding_steps_response_200.additional_properties = d
        return get_onboarding_steps_response_200

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
