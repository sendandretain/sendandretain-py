from enum import Enum


class ErrorErrorCode(str, Enum):
    CONFLICT = "conflict"
    DAILY_CAP = "daily_cap"
    FORBIDDEN = "forbidden"
    INTERNAL = "internal"
    INVALID_REQUEST = "invalid_request"
    MONTHLY_CAP = "monthly_cap"
    NOT_FOUND = "not_found"
    PROPOSAL_REJECTED = "proposal_rejected"
    PROVIDER_ERROR = "provider_error"
    RATE_LIMITED = "rate_limited"
    SENDS_PAUSED = "sends_paused"
    SUPPRESSED = "suppressed"
    TEMPLATE_NOT_FOUND = "template_not_found"
    TEMPLATE_NOT_PUBLISHED = "template_not_published"
    UNAUTHORIZED = "unauthorized"
    UPSTREAM_ERROR = "upstream_error"
    VALIDATION_ERROR = "validation_error"

    def __str__(self) -> str:
        return str(self.value)
