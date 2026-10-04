from enum import Enum


class CancelEmailResponse200Status(str, Enum):
    CANCELED = "canceled"

    def __str__(self) -> str:
        return str(self.value)
