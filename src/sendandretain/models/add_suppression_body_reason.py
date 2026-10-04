from enum import Enum


class AddSuppressionBodyReason(str, Enum):
    BOUNCE = "bounce"
    COMPLAINT = "complaint"
    MANUAL = "manual"
    UNSUBSCRIBE = "unsubscribe"

    def __str__(self) -> str:
        return str(self.value)
