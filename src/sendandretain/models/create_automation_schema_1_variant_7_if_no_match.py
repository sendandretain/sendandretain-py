from enum import Enum


class CreateAutomationSchema1Variant7IfNoMatch(str, Enum):
    CONTINUE = "continue"
    EXIT = "exit"

    def __str__(self) -> str:
        return str(self.value)
