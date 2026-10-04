from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_error_code import ErrorErrorCode
from ..models.error_error_key_scope import ErrorErrorKeyScope
from ..models.error_error_required_grant import ErrorErrorRequiredGrant
from ..models.error_error_required_scope import ErrorErrorRequiredScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorError")


@_attrs_define
class ErrorError:
    """
    Attributes:
        code (ErrorErrorCode): Stable, machine-readable error code.
        message (str): Human-readable explanation.
        message_id (str | Unset): Present on send failures that were still logged (e.g. suppressed).
        request_id (str | Unset): Echoes the `X-Request-Id` header. Present on every error. Quote it in a support
            request.
        required_scope (ErrorErrorRequiredScope | Unset): On a 403 refused at the rung: the tier this endpoint needs.
        required_grant (ErrorErrorRequiredGrant | Unset): On a 403 refused at the grant: the key's rung was sufficient
            but it may not take the irreversible action. Not a tier — branch on this separately from `required_scope`.
        key_scope (ErrorErrorKeyScope | Unset): On a 403: the tier the calling key actually holds.
    """

    code: ErrorErrorCode
    message: str
    message_id: str | Unset = UNSET
    request_id: str | Unset = UNSET
    required_scope: ErrorErrorRequiredScope | Unset = UNSET
    required_grant: ErrorErrorRequiredGrant | Unset = UNSET
    key_scope: ErrorErrorKeyScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        message_id = self.message_id

        request_id = self.request_id

        required_scope: str | Unset = UNSET
        if not isinstance(self.required_scope, Unset):
            required_scope = self.required_scope.value

        required_grant: str | Unset = UNSET
        if not isinstance(self.required_grant, Unset):
            required_grant = self.required_grant.value

        key_scope: str | Unset = UNSET
        if not isinstance(self.key_scope, Unset):
            key_scope = self.key_scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if required_scope is not UNSET:
            field_dict["required_scope"] = required_scope
        if required_grant is not UNSET:
            field_dict["required_grant"] = required_grant
        if key_scope is not UNSET:
            field_dict["key_scope"] = key_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = ErrorErrorCode(d.pop("code"))

        message = d.pop("message")

        message_id = d.pop("message_id", UNSET)

        request_id = d.pop("request_id", UNSET)

        _required_scope = d.pop("required_scope", UNSET)
        required_scope: ErrorErrorRequiredScope | Unset
        if isinstance(_required_scope, Unset):
            required_scope = UNSET
        else:
            required_scope = ErrorErrorRequiredScope(_required_scope)

        _required_grant = d.pop("required_grant", UNSET)
        required_grant: ErrorErrorRequiredGrant | Unset
        if isinstance(_required_grant, Unset):
            required_grant = UNSET
        else:
            required_grant = ErrorErrorRequiredGrant(_required_grant)

        _key_scope = d.pop("key_scope", UNSET)
        key_scope: ErrorErrorKeyScope | Unset
        if isinstance(_key_scope, Unset):
            key_scope = UNSET
        else:
            key_scope = ErrorErrorKeyScope(_key_scope)

        error_error = cls(
            code=code,
            message=message,
            message_id=message_id,
            request_id=request_id,
            required_scope=required_scope,
            required_grant=required_grant,
            key_scope=key_scope,
        )

        error_error.additional_properties = d
        return error_error

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
