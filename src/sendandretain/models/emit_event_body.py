from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.emit_event_body_contact_attributes import EmitEventBodyContactAttributes
    from ..models.emit_event_body_properties import EmitEventBodyProperties


T = TypeVar("T", bound="EmitEventBody")


@_attrs_define
class EmitEventBody:
    """
    Attributes:
        name (str): Event name. Letters, digits, and `_ . : -`.
        email (str | Unset): Identifies the contact; creates it if unknown. Provide this or external_id.
        external_id (str | Unset): Identifies an existing contact by your id. Provide this or email.
        properties (EmitEventBodyProperties | Unset): Event properties — available to automation trigger filters.
        dedupe_key (str | Unset): Idempotency key for this event. A repeat is a no-op for 30 days — the retention window
            on the event log. Past that the event row is pruned and its key becomes free again, so a replay of a genuinely
            old event is accepted as new. Automations are unaffected either way: enrolment is guarded by the run history,
            which is never pruned.
        occurred_at (datetime.datetime | Unset): ISO 8601 timestamp (with offset) of when the event happened.
        contact_attributes (EmitEventBodyContactAttributes | Unset): Attributes to upsert onto the contact alongside the
            event.
    """

    name: str
    email: str | Unset = UNSET
    external_id: str | Unset = UNSET
    properties: EmitEventBodyProperties | Unset = UNSET
    dedupe_key: str | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    contact_attributes: EmitEventBodyContactAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        external_id = self.external_id

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        dedupe_key = self.dedupe_key

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        contact_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_attributes, Unset):
            contact_attributes = self.contact_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if properties is not UNSET:
            field_dict["properties"] = properties
        if dedupe_key is not UNSET:
            field_dict["dedupe_key"] = dedupe_key
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if contact_attributes is not UNSET:
            field_dict["contact_attributes"] = contact_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.emit_event_body_contact_attributes import EmitEventBodyContactAttributes
        from ..models.emit_event_body_properties import EmitEventBodyProperties

        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email", UNSET)

        external_id = d.pop("external_id", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: EmitEventBodyProperties | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = EmitEventBodyProperties.from_dict(_properties)

        dedupe_key = d.pop("dedupe_key", UNSET)

        _occurred_at = d.pop("occurred_at", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)

        _contact_attributes = d.pop("contact_attributes", UNSET)
        contact_attributes: EmitEventBodyContactAttributes | Unset
        if isinstance(_contact_attributes, Unset):
            contact_attributes = UNSET
        else:
            contact_attributes = EmitEventBodyContactAttributes.from_dict(_contact_attributes)

        emit_event_body = cls(
            name=name,
            email=email,
            external_id=external_id,
            properties=properties,
            dedupe_key=dedupe_key,
            occurred_at=occurred_at,
            contact_attributes=contact_attributes,
        )

        emit_event_body.additional_properties = d
        return emit_event_body

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
