from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_automation_schema_1_variant_7_if_match import CreateAutomationSchema1Variant7IfMatch
from ..models.create_automation_schema_1_variant_7_if_no_match import CreateAutomationSchema1Variant7IfNoMatch
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_automation_schema_0 import CreateAutomationSchema0
    from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
    from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
    from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
    from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
    from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
    from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
    from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6
    from ..models.create_automation_schema_1_variant_7_branches_item import CreateAutomationSchema1Variant7BranchesItem
    from ..models.create_automation_schema_1_variant_7_filter_variant_0_item import (
        CreateAutomationSchema1Variant7FilterVariant0Item,
    )
    from ..models.create_automation_schema_1_variant_7_send_window import CreateAutomationSchema1Variant7SendWindow


T = TypeVar("T", bound="CreateAutomationSchema1Variant7")


@_attrs_define
class CreateAutomationSchema1Variant7:
    """
    Attributes:
        type_ (Literal['branch']):
        delay_seconds (int): Delay before this step runs (0 = immediate). Weekly = 604800.
        send_window (CreateAutomationSchema1Variant7SendWindow | Unset): Quiet-hours clamp; contact.attributes.timezone
            wins over this timezone.
        filter_ (CreateAutomationSchema0 | list[CreateAutomationSchema1Variant7FilterVariant0Item] | Unset): Evaluated
            against contact attributes ⊕ the trigger event.
        yes (list[CreateAutomationSchema1Variant0 | CreateAutomationSchema1Variant1 | CreateAutomationSchema1Variant2 |
            CreateAutomationSchema1Variant3 | CreateAutomationSchema1Variant4 | CreateAutomationSchema1Variant5 |
            CreateAutomationSchema1Variant6 | CreateAutomationSchema1Variant7] | Unset): Steps for contacts matching the
            filter.
        no (list[CreateAutomationSchema1Variant0 | CreateAutomationSchema1Variant1 | CreateAutomationSchema1Variant2 |
            CreateAutomationSchema1Variant3 | CreateAutomationSchema1Variant4 | CreateAutomationSchema1Variant5 |
            CreateAutomationSchema1Variant6 | CreateAutomationSchema1Variant7] | Unset): Steps for everyone else.
        branches (list[CreateAutomationSchema1Variant7BranchesItem] | Unset): Ordered arms — the first matching filter
            wins.
        else_steps (list[CreateAutomationSchema1Variant0 | CreateAutomationSchema1Variant1 |
            CreateAutomationSchema1Variant2 | CreateAutomationSchema1Variant3 | CreateAutomationSchema1Variant4 |
            CreateAutomationSchema1Variant5 | CreateAutomationSchema1Variant6 | CreateAutomationSchema1Variant7] | Unset):
            Steps for contacts matching no arm.
        if_match (CreateAutomationSchema1Variant7IfMatch | Unset):
        if_no_match (CreateAutomationSchema1Variant7IfNoMatch | Unset):
    """

    type_: Literal["branch"]
    delay_seconds: int
    send_window: CreateAutomationSchema1Variant7SendWindow | Unset = UNSET
    filter_: CreateAutomationSchema0 | list[CreateAutomationSchema1Variant7FilterVariant0Item] | Unset = UNSET
    yes: (
        list[
            CreateAutomationSchema1Variant0
            | CreateAutomationSchema1Variant1
            | CreateAutomationSchema1Variant2
            | CreateAutomationSchema1Variant3
            | CreateAutomationSchema1Variant4
            | CreateAutomationSchema1Variant5
            | CreateAutomationSchema1Variant6
            | CreateAutomationSchema1Variant7
        ]
        | Unset
    ) = UNSET
    no: (
        list[
            CreateAutomationSchema1Variant0
            | CreateAutomationSchema1Variant1
            | CreateAutomationSchema1Variant2
            | CreateAutomationSchema1Variant3
            | CreateAutomationSchema1Variant4
            | CreateAutomationSchema1Variant5
            | CreateAutomationSchema1Variant6
            | CreateAutomationSchema1Variant7
        ]
        | Unset
    ) = UNSET
    branches: list[CreateAutomationSchema1Variant7BranchesItem] | Unset = UNSET
    else_steps: (
        list[
            CreateAutomationSchema1Variant0
            | CreateAutomationSchema1Variant1
            | CreateAutomationSchema1Variant2
            | CreateAutomationSchema1Variant3
            | CreateAutomationSchema1Variant4
            | CreateAutomationSchema1Variant5
            | CreateAutomationSchema1Variant6
            | CreateAutomationSchema1Variant7
        ]
        | Unset
    ) = UNSET
    if_match: CreateAutomationSchema1Variant7IfMatch | Unset = UNSET
    if_no_match: CreateAutomationSchema1Variant7IfNoMatch | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
        from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
        from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
        from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
        from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
        from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
        from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6

        type_ = self.type_

        delay_seconds = self.delay_seconds

        send_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.send_window, Unset):
            send_window = self.send_window.to_dict()

        filter_: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, list):
            filter_ = []
            for componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item_data in self.filter_:
                componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item = (
                    componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item_data.to_dict()
                )
                filter_.append(componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item)

        else:
            filter_ = self.filter_.to_dict()

        yes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.yes, Unset):
            yes = []
            for yes_item_data in self.yes:
                yes_item: dict[str, Any]
                if isinstance(yes_item_data, CreateAutomationSchema1Variant0):
                    yes_item = yes_item_data.to_dict()
                elif isinstance(yes_item_data, CreateAutomationSchema1Variant1):
                    yes_item = yes_item_data.to_dict()
                elif isinstance(yes_item_data, CreateAutomationSchema1Variant2):
                    yes_item = yes_item_data.to_dict()
                elif isinstance(yes_item_data, CreateAutomationSchema1Variant3):
                    yes_item = yes_item_data.to_dict()
                elif isinstance(yes_item_data, CreateAutomationSchema1Variant4):
                    yes_item = yes_item_data.to_dict()
                elif isinstance(yes_item_data, CreateAutomationSchema1Variant5):
                    yes_item = yes_item_data.to_dict()
                elif isinstance(yes_item_data, CreateAutomationSchema1Variant6):
                    yes_item = yes_item_data.to_dict()
                else:
                    yes_item = yes_item_data.to_dict()

                yes.append(yes_item)

        no: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.no, Unset):
            no = []
            for no_item_data in self.no:
                no_item: dict[str, Any]
                if isinstance(no_item_data, CreateAutomationSchema1Variant0):
                    no_item = no_item_data.to_dict()
                elif isinstance(no_item_data, CreateAutomationSchema1Variant1):
                    no_item = no_item_data.to_dict()
                elif isinstance(no_item_data, CreateAutomationSchema1Variant2):
                    no_item = no_item_data.to_dict()
                elif isinstance(no_item_data, CreateAutomationSchema1Variant3):
                    no_item = no_item_data.to_dict()
                elif isinstance(no_item_data, CreateAutomationSchema1Variant4):
                    no_item = no_item_data.to_dict()
                elif isinstance(no_item_data, CreateAutomationSchema1Variant5):
                    no_item = no_item_data.to_dict()
                elif isinstance(no_item_data, CreateAutomationSchema1Variant6):
                    no_item = no_item_data.to_dict()
                else:
                    no_item = no_item_data.to_dict()

                no.append(no_item)

        branches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.branches, Unset):
            branches = []
            for branches_item_data in self.branches:
                branches_item = branches_item_data.to_dict()
                branches.append(branches_item)

        else_steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.else_steps, Unset):
            else_steps = []
            for else_steps_item_data in self.else_steps:
                else_steps_item: dict[str, Any]
                if isinstance(else_steps_item_data, CreateAutomationSchema1Variant0):
                    else_steps_item = else_steps_item_data.to_dict()
                elif isinstance(else_steps_item_data, CreateAutomationSchema1Variant1):
                    else_steps_item = else_steps_item_data.to_dict()
                elif isinstance(else_steps_item_data, CreateAutomationSchema1Variant2):
                    else_steps_item = else_steps_item_data.to_dict()
                elif isinstance(else_steps_item_data, CreateAutomationSchema1Variant3):
                    else_steps_item = else_steps_item_data.to_dict()
                elif isinstance(else_steps_item_data, CreateAutomationSchema1Variant4):
                    else_steps_item = else_steps_item_data.to_dict()
                elif isinstance(else_steps_item_data, CreateAutomationSchema1Variant5):
                    else_steps_item = else_steps_item_data.to_dict()
                elif isinstance(else_steps_item_data, CreateAutomationSchema1Variant6):
                    else_steps_item = else_steps_item_data.to_dict()
                else:
                    else_steps_item = else_steps_item_data.to_dict()

                else_steps.append(else_steps_item)

        if_match: str | Unset = UNSET
        if not isinstance(self.if_match, Unset):
            if_match = self.if_match.value

        if_no_match: str | Unset = UNSET
        if not isinstance(self.if_no_match, Unset):
            if_no_match = self.if_no_match.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "delaySeconds": delay_seconds,
            }
        )
        if send_window is not UNSET:
            field_dict["sendWindow"] = send_window
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if yes is not UNSET:
            field_dict["yes"] = yes
        if no is not UNSET:
            field_dict["no"] = no
        if branches is not UNSET:
            field_dict["branches"] = branches
        if else_steps is not UNSET:
            field_dict["elseSteps"] = else_steps
        if if_match is not UNSET:
            field_dict["ifMatch"] = if_match
        if if_no_match is not UNSET:
            field_dict["ifNoMatch"] = if_no_match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_automation_schema_0 import CreateAutomationSchema0
        from ..models.create_automation_schema_1_variant_0 import CreateAutomationSchema1Variant0
        from ..models.create_automation_schema_1_variant_1 import CreateAutomationSchema1Variant1
        from ..models.create_automation_schema_1_variant_2 import CreateAutomationSchema1Variant2
        from ..models.create_automation_schema_1_variant_3 import CreateAutomationSchema1Variant3
        from ..models.create_automation_schema_1_variant_4 import CreateAutomationSchema1Variant4
        from ..models.create_automation_schema_1_variant_5 import CreateAutomationSchema1Variant5
        from ..models.create_automation_schema_1_variant_6 import CreateAutomationSchema1Variant6
        from ..models.create_automation_schema_1_variant_7_branches_item import (
            CreateAutomationSchema1Variant7BranchesItem,
        )
        from ..models.create_automation_schema_1_variant_7_filter_variant_0_item import (
            CreateAutomationSchema1Variant7FilterVariant0Item,
        )
        from ..models.create_automation_schema_1_variant_7_send_window import CreateAutomationSchema1Variant7SendWindow

        d = dict(src_dict)
        type_ = cast(Literal["branch"], d.pop("type"))
        if type_ != "branch":
            raise ValueError(f"type must match const 'branch', got '{type_}'")

        delay_seconds = d.pop("delaySeconds")

        _send_window = d.pop("sendWindow", UNSET)
        send_window: CreateAutomationSchema1Variant7SendWindow | Unset
        if isinstance(_send_window, Unset):
            send_window = UNSET
        else:
            send_window = CreateAutomationSchema1Variant7SendWindow.from_dict(_send_window)

        def _parse_filter_(
            data: object,
        ) -> CreateAutomationSchema0 | list[CreateAutomationSchema1Variant7FilterVariant0Item] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_type_0 = []
                _filter_type_0 = data
                for componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item_data in _filter_type_0:
                    componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item = (
                        CreateAutomationSchema1Variant7FilterVariant0Item.from_dict(
                            componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item_data
                        )
                    )

                    filter_type_0.append(componentsschemas_create_automation_schema_1_variant_7_filter_variant_0_item)

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            filter_type_1 = CreateAutomationSchema0.from_dict(data)

            return filter_type_1

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        _yes = d.pop("yes", UNSET)
        yes: (
            list[
                CreateAutomationSchema1Variant0
                | CreateAutomationSchema1Variant1
                | CreateAutomationSchema1Variant2
                | CreateAutomationSchema1Variant3
                | CreateAutomationSchema1Variant4
                | CreateAutomationSchema1Variant5
                | CreateAutomationSchema1Variant6
                | CreateAutomationSchema1Variant7
            ]
            | Unset
        ) = UNSET
        if _yes is not UNSET:
            yes = []
            for yes_item_data in _yes:

                def _parse_yes_item(
                    data: object,
                ) -> (
                    CreateAutomationSchema1Variant0
                    | CreateAutomationSchema1Variant1
                    | CreateAutomationSchema1Variant2
                    | CreateAutomationSchema1Variant3
                    | CreateAutomationSchema1Variant4
                    | CreateAutomationSchema1Variant5
                    | CreateAutomationSchema1Variant6
                    | CreateAutomationSchema1Variant7
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_0 = CreateAutomationSchema1Variant0.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_1 = CreateAutomationSchema1Variant1.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_2 = CreateAutomationSchema1Variant2.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_3 = CreateAutomationSchema1Variant3.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_4 = CreateAutomationSchema1Variant4.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_5 = CreateAutomationSchema1Variant5.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_6 = CreateAutomationSchema1Variant6.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_create_automation_schema_1_type_7 = CreateAutomationSchema1Variant7.from_dict(
                        data
                    )

                    return componentsschemas_create_automation_schema_1_type_7

                yes_item = _parse_yes_item(yes_item_data)

                yes.append(yes_item)

        _no = d.pop("no", UNSET)
        no: (
            list[
                CreateAutomationSchema1Variant0
                | CreateAutomationSchema1Variant1
                | CreateAutomationSchema1Variant2
                | CreateAutomationSchema1Variant3
                | CreateAutomationSchema1Variant4
                | CreateAutomationSchema1Variant5
                | CreateAutomationSchema1Variant6
                | CreateAutomationSchema1Variant7
            ]
            | Unset
        ) = UNSET
        if _no is not UNSET:
            no = []
            for no_item_data in _no:

                def _parse_no_item(
                    data: object,
                ) -> (
                    CreateAutomationSchema1Variant0
                    | CreateAutomationSchema1Variant1
                    | CreateAutomationSchema1Variant2
                    | CreateAutomationSchema1Variant3
                    | CreateAutomationSchema1Variant4
                    | CreateAutomationSchema1Variant5
                    | CreateAutomationSchema1Variant6
                    | CreateAutomationSchema1Variant7
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_0 = CreateAutomationSchema1Variant0.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_1 = CreateAutomationSchema1Variant1.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_2 = CreateAutomationSchema1Variant2.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_3 = CreateAutomationSchema1Variant3.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_4 = CreateAutomationSchema1Variant4.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_5 = CreateAutomationSchema1Variant5.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_6 = CreateAutomationSchema1Variant6.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_create_automation_schema_1_type_7 = CreateAutomationSchema1Variant7.from_dict(
                        data
                    )

                    return componentsschemas_create_automation_schema_1_type_7

                no_item = _parse_no_item(no_item_data)

                no.append(no_item)

        _branches = d.pop("branches", UNSET)
        branches: list[CreateAutomationSchema1Variant7BranchesItem] | Unset = UNSET
        if _branches is not UNSET:
            branches = []
            for branches_item_data in _branches:
                branches_item = CreateAutomationSchema1Variant7BranchesItem.from_dict(branches_item_data)

                branches.append(branches_item)

        _else_steps = d.pop("elseSteps", UNSET)
        else_steps: (
            list[
                CreateAutomationSchema1Variant0
                | CreateAutomationSchema1Variant1
                | CreateAutomationSchema1Variant2
                | CreateAutomationSchema1Variant3
                | CreateAutomationSchema1Variant4
                | CreateAutomationSchema1Variant5
                | CreateAutomationSchema1Variant6
                | CreateAutomationSchema1Variant7
            ]
            | Unset
        ) = UNSET
        if _else_steps is not UNSET:
            else_steps = []
            for else_steps_item_data in _else_steps:

                def _parse_else_steps_item(
                    data: object,
                ) -> (
                    CreateAutomationSchema1Variant0
                    | CreateAutomationSchema1Variant1
                    | CreateAutomationSchema1Variant2
                    | CreateAutomationSchema1Variant3
                    | CreateAutomationSchema1Variant4
                    | CreateAutomationSchema1Variant5
                    | CreateAutomationSchema1Variant6
                    | CreateAutomationSchema1Variant7
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_0 = CreateAutomationSchema1Variant0.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_1 = CreateAutomationSchema1Variant1.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_2 = CreateAutomationSchema1Variant2.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_3 = CreateAutomationSchema1Variant3.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_4 = CreateAutomationSchema1Variant4.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_5 = CreateAutomationSchema1Variant5.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_create_automation_schema_1_type_6 = CreateAutomationSchema1Variant6.from_dict(
                            data
                        )

                        return componentsschemas_create_automation_schema_1_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_create_automation_schema_1_type_7 = CreateAutomationSchema1Variant7.from_dict(
                        data
                    )

                    return componentsschemas_create_automation_schema_1_type_7

                else_steps_item = _parse_else_steps_item(else_steps_item_data)

                else_steps.append(else_steps_item)

        _if_match = d.pop("ifMatch", UNSET)
        if_match: CreateAutomationSchema1Variant7IfMatch | Unset
        if isinstance(_if_match, Unset):
            if_match = UNSET
        else:
            if_match = CreateAutomationSchema1Variant7IfMatch(_if_match)

        _if_no_match = d.pop("ifNoMatch", UNSET)
        if_no_match: CreateAutomationSchema1Variant7IfNoMatch | Unset
        if isinstance(_if_no_match, Unset):
            if_no_match = UNSET
        else:
            if_no_match = CreateAutomationSchema1Variant7IfNoMatch(_if_no_match)

        create_automation_schema_1_variant_7 = cls(
            type_=type_,
            delay_seconds=delay_seconds,
            send_window=send_window,
            filter_=filter_,
            yes=yes,
            no=no,
            branches=branches,
            else_steps=else_steps,
            if_match=if_match,
            if_no_match=if_no_match,
        )

        create_automation_schema_1_variant_7.additional_properties = d
        return create_automation_schema_1_variant_7

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
