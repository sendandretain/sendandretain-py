from enum import Enum


class ListSuppressionsReason(str, Enum):
    BOUNCE = "bounce"
    COMPLAINT = "complaint"
    INVALID = "invalid"
    MANUAL = "manual"
    UNSUBSCRIBE = "unsubscribe"

    def __str__(self) -> str:
        return str(self.value)
