from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_automation_response_200_steps_item_config_type_0 import (
        GetAutomationResponse200StepsItemConfigType0,
    )
    from ..models.get_automation_response_200_steps_item_props_overrides import (
        GetAutomationResponse200StepsItemPropsOverrides,
    )
    from ..models.get_automation_response_200_steps_item_send_window_type_0 import (
        GetAutomationResponse200StepsItemSendWindowType0,
    )
    from ..models.get_automation_response_200_steps_item_template_type_0 import (
        GetAutomationResponse200StepsItemTemplateType0,
    )


T = TypeVar("T", bound="GetAutomationResponse200StepsItem")


@_attrs_define
class GetAutomationResponse200StepsItem:
    """
    Attributes:
        id (str | Unset):
        position (int | Unset):
        parent_step_id (None | str | Unset):
        lane_key (None | str | Unset):
        type_ (str | Unset):
        delay_seconds (int | None | Unset):
        template_slug (None | str | Unset):
        template (GetAutomationResponse200StepsItemTemplateType0 | None | Unset): What a send step sends: the template's
            LIVE version, against the latest base version. `has_unpublished_changes` means a newer draft exists that no
            contact receives until it is published.
        config (GetAutomationResponse200StepsItemConfigType0 | None | Unset):
        props_overrides (GetAutomationResponse200StepsItemPropsOverrides | Unset):
        variants (Any | Unset):
        send_window (GetAutomationResponse200StepsItemSendWindowType0 | None | Unset):
        skipped (bool | Unset):
    """

    id: str | Unset = UNSET
    position: int | Unset = UNSET
    parent_step_id: None | str | Unset = UNSET
    lane_key: None | str | Unset = UNSET
    type_: str | Unset = UNSET
    delay_seconds: int | None | Unset = UNSET
    template_slug: None | str | Unset = UNSET
    template: GetAutomationResponse200StepsItemTemplateType0 | None | Unset = UNSET
    config: GetAutomationResponse200StepsItemConfigType0 | None | Unset = UNSET
    props_overrides: GetAutomationResponse200StepsItemPropsOverrides | Unset = UNSET
    variants: Any | Unset = UNSET
    send_window: GetAutomationResponse200StepsItemSendWindowType0 | None | Unset = UNSET
    skipped: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.get_automation_response_200_steps_item_config_type_0 import (
            GetAutomationResponse200StepsItemConfigType0,
        )
        from ..models.get_automation_response_200_steps_item_send_window_type_0 import (
            GetAutomationResponse200StepsItemSendWindowType0,
        )
        from ..models.get_automation_response_200_steps_item_template_type_0 import (
            GetAutomationResponse200StepsItemTemplateType0,
        )

        id = self.id

        position = self.position

        parent_step_id: None | str | Unset
        if isinstance(self.parent_step_id, Unset):
            parent_step_id = UNSET
        else:
            parent_step_id = self.parent_step_id

        lane_key: None | str | Unset
        if isinstance(self.lane_key, Unset):
            lane_key = UNSET
        else:
            lane_key = self.lane_key

        type_ = self.type_

        delay_seconds: int | None | Unset
        if isinstance(self.delay_seconds, Unset):
            delay_seconds = UNSET
        else:
            delay_seconds = self.delay_seconds

        template_slug: None | str | Unset
        if isinstance(self.template_slug, Unset):
            template_slug = UNSET
        else:
            template_slug = self.template_slug

        template: dict[str, Any] | None | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        elif isinstance(self.template, GetAutomationResponse200StepsItemTemplateType0):
            template = self.template.to_dict()
        else:
            template = self.template

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, GetAutomationResponse200StepsItemConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        props_overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props_overrides, Unset):
            props_overrides = self.props_overrides.to_dict()

        variants = self.variants

        send_window: dict[str, Any] | None | Unset
        if isinstance(self.send_window, Unset):
            send_window = UNSET
        elif isinstance(self.send_window, GetAutomationResponse200StepsItemSendWindowType0):
            send_window = self.send_window.to_dict()
        else:
            send_window = self.send_window

        skipped = self.skipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if parent_step_id is not UNSET:
            field_dict["parent_step_id"] = parent_step_id
        if lane_key is not UNSET:
            field_dict["lane_key"] = lane_key
        if type_ is not UNSET:
            field_dict["type"] = type_
        if delay_seconds is not UNSET:
            field_dict["delay_seconds"] = delay_seconds
        if template_slug is not UNSET:
            field_dict["template_slug"] = template_slug
        if template is not UNSET:
            field_dict["template"] = template
        if config is not UNSET:
            field_dict["config"] = config
        if props_overrides is not UNSET:
            field_dict["props_overrides"] = props_overrides
        if variants is not UNSET:
            field_dict["variants"] = variants
        if send_window is not UNSET:
            field_dict["send_window"] = send_window
        if skipped is not UNSET:
            field_dict["skipped"] = skipped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_automation_response_200_steps_item_config_type_0 import (
            GetAutomationResponse200StepsItemConfigType0,
        )
        from ..models.get_automation_response_200_steps_item_props_overrides import (
            GetAutomationResponse200StepsItemPropsOverrides,
        )
        from ..models.get_automation_response_200_steps_item_send_window_type_0 import (
            GetAutomationResponse200StepsItemSendWindowType0,
        )
        from ..models.get_automation_response_200_steps_item_template_type_0 import (
            GetAutomationResponse200StepsItemTemplateType0,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        position = d.pop("position", UNSET)

        def _parse_parent_step_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_step_id = _parse_parent_step_id(d.pop("parent_step_id", UNSET))

        def _parse_lane_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lane_key = _parse_lane_key(d.pop("lane_key", UNSET))

        type_ = d.pop("type", UNSET)

        def _parse_delay_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        delay_seconds = _parse_delay_seconds(d.pop("delay_seconds", UNSET))

        def _parse_template_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_slug = _parse_template_slug(d.pop("template_slug", UNSET))

        def _parse_template(data: object) -> GetAutomationResponse200StepsItemTemplateType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_type_0 = GetAutomationResponse200StepsItemTemplateType0.from_dict(data)

                return template_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAutomationResponse200StepsItemTemplateType0 | None | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_config(data: object) -> GetAutomationResponse200StepsItemConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = GetAutomationResponse200StepsItemConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAutomationResponse200StepsItemConfigType0 | None | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        _props_overrides = d.pop("props_overrides", UNSET)
        props_overrides: GetAutomationResponse200StepsItemPropsOverrides | Unset
        if isinstance(_props_overrides, Unset):
            props_overrides = UNSET
        else:
            props_overrides = GetAutomationResponse200StepsItemPropsOverrides.from_dict(_props_overrides)

        variants = d.pop("variants", UNSET)

        def _parse_send_window(data: object) -> GetAutomationResponse200StepsItemSendWindowType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                send_window_type_0 = GetAutomationResponse200StepsItemSendWindowType0.from_dict(data)

                return send_window_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAutomationResponse200StepsItemSendWindowType0 | None | Unset, data)

        send_window = _parse_send_window(d.pop("send_window", UNSET))

        skipped = d.pop("skipped", UNSET)

        get_automation_response_200_steps_item = cls(
            id=id,
            position=position,
            parent_step_id=parent_step_id,
            lane_key=lane_key,
            type_=type_,
            delay_seconds=delay_seconds,
            template_slug=template_slug,
            template=template,
            config=config,
            props_overrides=props_overrides,
            variants=variants,
            send_window=send_window,
            skipped=skipped,
        )

        get_automation_response_200_steps_item.additional_properties = d
        return get_automation_response_200_steps_item

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
