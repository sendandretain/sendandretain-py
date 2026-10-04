from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_automation_step_body_patch_if_match import UpdateAutomationStepBodyPatchIfMatch
from ..models.update_automation_step_body_patch_if_no_match import UpdateAutomationStepBodyPatchIfNoMatch
from ..models.update_automation_step_body_patch_method import UpdateAutomationStepBodyPatchMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item import (
        AutomationsStepsPutRequestBodyContentApplicationJsonPatchFilterVariant0Item,
    )
    from ..models.update_automation_step_body_patch_attributes import UpdateAutomationStepBodyPatchAttributes
    from ..models.update_automation_step_body_patch_branches_item import UpdateAutomationStepBodyPatchBranchesItem
    from ..models.update_automation_step_body_patch_props_overrides import UpdateAutomationStepBodyPatchPropsOverrides
    from ..models.update_automation_step_body_patch_send_window import UpdateAutomationStepBodyPatchSendWindow
    from ..models.update_step_schema_0 import UpdateStepSchema0


T = TypeVar("T", bound="UpdateAutomationStepBodyPatch")


@_attrs_define
class UpdateAutomationStepBodyPatch:
    """Fields to change. Keys are validated against the step's actual type.

    Attributes:
        template_slug (str | Unset):
        props_overrides (UpdateAutomationStepBodyPatchPropsOverrides | Unset):
        subject (None | str | Unset): Send steps: per-step subject override ({{vars}} ok); null clears.
        preview_text (None | str | Unset): Send steps: per-step inbox preview text ({{vars}} ok); null clears.
        event_name (str | Unset):
        timeout_seconds (int | Unset):
        filter_ (list[AutomationsStepsPutRequestBodyContentApplicationJsonPatchFilterVariant0Item] | Unset |
            UpdateStepSchema0):
        if_match (UpdateAutomationStepBodyPatchIfMatch | Unset):
        if_no_match (UpdateAutomationStepBodyPatchIfNoMatch | Unset):
        branches (list[UpdateAutomationStepBodyPatchBranchesItem] | Unset): Multi branch only: replace the ordered arms
            (first match wins).
        convert_kind (Literal['yes_no'] | Unset):
        label (str | Unset): Exit steps: the label shown in metrics.
        attributes (UpdateAutomationStepBodyPatchAttributes | Unset):
        add_tags (list[str] | Unset):
        remove_tags (list[str] | Unset):
        url (str | Unset):
        method (UpdateAutomationStepBodyPatchMethod | Unset):
        delay_seconds (int | Unset):
        skipped (bool | Unset): Debug switch: runs walk past this step without executing it — no send, no webhook, no
            wait. Editable while the automation is active.
        send_window (UpdateAutomationStepBodyPatchSendWindow | Unset): Quiet-hours clamp; contact.attributes.timezone
            wins over this timezone.
    """

    template_slug: str | Unset = UNSET
    props_overrides: UpdateAutomationStepBodyPatchPropsOverrides | Unset = UNSET
    subject: None | str | Unset = UNSET
    preview_text: None | str | Unset = UNSET
    event_name: str | Unset = UNSET
    timeout_seconds: int | Unset = UNSET
    filter_: (
        list[AutomationsStepsPutRequestBodyContentApplicationJsonPatchFilterVariant0Item] | Unset | UpdateStepSchema0
    ) = UNSET
    if_match: UpdateAutomationStepBodyPatchIfMatch | Unset = UNSET
    if_no_match: UpdateAutomationStepBodyPatchIfNoMatch | Unset = UNSET
    branches: list[UpdateAutomationStepBodyPatchBranchesItem] | Unset = UNSET
    convert_kind: Literal["yes_no"] | Unset = UNSET
    label: str | Unset = UNSET
    attributes: UpdateAutomationStepBodyPatchAttributes | Unset = UNSET
    add_tags: list[str] | Unset = UNSET
    remove_tags: list[str] | Unset = UNSET
    url: str | Unset = UNSET
    method: UpdateAutomationStepBodyPatchMethod | Unset = UNSET
    delay_seconds: int | Unset = UNSET
    skipped: bool | Unset = UNSET
    send_window: UpdateAutomationStepBodyPatchSendWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template_slug = self.template_slug

        props_overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props_overrides, Unset):
            props_overrides = self.props_overrides.to_dict()

        subject: None | str | Unset
        if isinstance(self.subject, Unset):
            subject = UNSET
        else:
            subject = self.subject

        preview_text: None | str | Unset
        if isinstance(self.preview_text, Unset):
            preview_text = UNSET
        else:
            preview_text = self.preview_text

        event_name = self.event_name

        timeout_seconds = self.timeout_seconds

        filter_: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, list):
            filter_ = []
            for componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item_data in self.filter_:
                componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item = componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item_data.to_dict()
                filter_.append(
                    componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item
                )

        else:
            filter_ = self.filter_.to_dict()

        if_match: str | Unset = UNSET
        if not isinstance(self.if_match, Unset):
            if_match = self.if_match.value

        if_no_match: str | Unset = UNSET
        if not isinstance(self.if_no_match, Unset):
            if_no_match = self.if_no_match.value

        branches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = []
            for branches_item_data in self.branches:
                branches_item = branches_item_data.to_dict()
                branches.append(branches_item)

        convert_kind = self.convert_kind

        label = self.label

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        add_tags: list[str] | Unset = UNSET
        if not isinstance(self.add_tags, Unset):
            add_tags = self.add_tags

        remove_tags: list[str] | Unset = UNSET
        if not isinstance(self.remove_tags, Unset):
            remove_tags = self.remove_tags

        url = self.url

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        delay_seconds = self.delay_seconds

        skipped = self.skipped

        send_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_window, Unset):
            send_window = self.send_window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template_slug is not UNSET:
            field_dict["templateSlug"] = template_slug
        if props_overrides is not UNSET:
            field_dict["propsOverrides"] = props_overrides
        if subject is not UNSET:
            field_dict["subject"] = subject
        if preview_text is not UNSET:
            field_dict["previewText"] = preview_text
        if event_name is not UNSET:
            field_dict["eventName"] = event_name
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if if_match is not UNSET:
            field_dict["ifMatch"] = if_match
        if if_no_match is not UNSET:
            field_dict["ifNoMatch"] = if_no_match
        if branches is not UNSET:
            field_dict["branches"] = branches
        if convert_kind is not UNSET:
            field_dict["convertKind"] = convert_kind
        if label is not UNSET:
            field_dict["label"] = label
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if add_tags is not UNSET:
            field_dict["addTags"] = add_tags
        if remove_tags is not UNSET:
            field_dict["removeTags"] = remove_tags
        if url is not UNSET:
            field_dict["url"] = url
        if method is not UNSET:
            field_dict["method"] = method
        if delay_seconds is not UNSET:
            field_dict["delaySeconds"] = delay_seconds
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if send_window is not UNSET:
            field_dict["sendWindow"] = send_window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item import (
            AutomationsStepsPutRequestBodyContentApplicationJsonPatchFilterVariant0Item,
        )
        from ..models.update_automation_step_body_patch_attributes import UpdateAutomationStepBodyPatchAttributes
        from ..models.update_automation_step_body_patch_branches_item import UpdateAutomationStepBodyPatchBranchesItem
        from ..models.update_automation_step_body_patch_props_overrides import (
            UpdateAutomationStepBodyPatchPropsOverrides,
        )
        from ..models.update_automation_step_body_patch_send_window import UpdateAutomationStepBodyPatchSendWindow
        from ..models.update_step_schema_0 import UpdateStepSchema0

        d = dict(src_dict)
        template_slug = d.pop("templateSlug", UNSET)

        _props_overrides = d.pop("propsOverrides", UNSET)
        props_overrides: UpdateAutomationStepBodyPatchPropsOverrides | Unset
        if isinstance(_props_overrides, Unset):
            props_overrides = UNSET
        else:
            props_overrides = UpdateAutomationStepBodyPatchPropsOverrides.from_dict(_props_overrides)

        def _parse_subject(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subject = _parse_subject(d.pop("subject", UNSET))

        def _parse_preview_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preview_text = _parse_preview_text(d.pop("previewText", UNSET))

        event_name = d.pop("eventName", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        def _parse_filter_(
            data: object,
        ) -> (
            list[AutomationsStepsPutRequestBodyContentApplicationJsonPatchFilterVariant0Item]
            | Unset
            | UpdateStepSchema0
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_type_0 = []
                _filter_type_0 = data
                for componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item_data in _filter_type_0:
                    componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item = AutomationsStepsPutRequestBodyContentApplicationJsonPatchFilterVariant0Item.from_dict(
                        componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item_data
                    )

                    filter_type_0.append(
                        componentsschemas_automations_steps_put_request_body_content_application_json_patch_filter_variant_0_item
                    )

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            filter_type_1 = UpdateStepSchema0.from_dict(data)

            return filter_type_1

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        _if_match = d.pop("ifMatch", UNSET)
        if_match: UpdateAutomationStepBodyPatchIfMatch | Unset
        if isinstance(_if_match, Unset):
            if_match = UNSET
        else:
            if_match = UpdateAutomationStepBodyPatchIfMatch(_if_match)

        _if_no_match = d.pop("ifNoMatch", UNSET)
        if_no_match: UpdateAutomationStepBodyPatchIfNoMatch | Unset
        if isinstance(_if_no_match, Unset):
            if_no_match = UNSET
        else:
            if_no_match = UpdateAutomationStepBodyPatchIfNoMatch(_if_no_match)

        _branches = d.pop("branches", UNSET)
        branches: list[UpdateAutomationStepBodyPatchBranchesItem] | Unset = UNSET
        if _branches is not UNSET:
            branches = []
            for branches_item_data in _branches:
                branches_item = UpdateAutomationStepBodyPatchBranchesItem.from_dict(branches_item_data)

                branches.append(branches_item)

        convert_kind = cast(Literal["yes_no"] | Unset, d.pop("convertKind", UNSET))
        if convert_kind != "yes_no" and not isinstance(convert_kind, Unset):
            raise ValueError(f"convertKind must match const 'yes_no', got '{convert_kind}'")

        label = d.pop("label", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: UpdateAutomationStepBodyPatchAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UpdateAutomationStepBodyPatchAttributes.from_dict(_attributes)

        add_tags = cast(list[str], d.pop("addTags", UNSET))

        remove_tags = cast(list[str], d.pop("removeTags", UNSET))

        url = d.pop("url", UNSET)

        _method = d.pop("method", UNSET)
        method: UpdateAutomationStepBodyPatchMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = UpdateAutomationStepBodyPatchMethod(_method)

        delay_seconds = d.pop("delaySeconds", UNSET)

        skipped = d.pop("skipped", UNSET)

        _send_window = d.pop("sendWindow", UNSET)
        send_window: UpdateAutomationStepBodyPatchSendWindow | Unset
        if isinstance(_send_window, Unset):
            send_window = UNSET
        else:
            send_window = UpdateAutomationStepBodyPatchSendWindow.from_dict(_send_window)

        update_automation_step_body_patch = cls(
            template_slug=template_slug,
            props_overrides=props_overrides,
            subject=subject,
            preview_text=preview_text,
            event_name=event_name,
            timeout_seconds=timeout_seconds,
            filter_=filter_,
            if_match=if_match,
            if_no_match=if_no_match,
            branches=branches,
            convert_kind=convert_kind,
            label=label,
            attributes=attributes,
            add_tags=add_tags,
            remove_tags=remove_tags,
            url=url,
            method=method,
            delay_seconds=delay_seconds,
            skipped=skipped,
            send_window=send_window,
        )

        update_automation_step_body_patch.additional_properties = d
        return update_automation_step_body_patch

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
