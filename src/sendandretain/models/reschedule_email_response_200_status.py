from enum import Enum


class RescheduleEmailResponse200Status(str, Enum):
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
