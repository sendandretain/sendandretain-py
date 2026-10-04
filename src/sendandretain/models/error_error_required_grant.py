from enum import Enum


class ErrorErrorRequiredGrant(str, Enum):
    APPROVE = "approve"

    def __str__(self) -> str:
        return str(self.value)
