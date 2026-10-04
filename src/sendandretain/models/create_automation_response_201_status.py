from enum import Enum


class CreateAutomationResponse201Status(str, Enum):
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
