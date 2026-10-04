from enum import Enum


class SendResultStatus(str, Enum):
    QUEUED = "queued"
    SCHEDULED = "scheduled"
    SENT = "sent"

    def __str__(self) -> str:
        return str(self.value)
