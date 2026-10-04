from enum import Enum


class AddAutomationStepsSchema0Variant7IfMatch(str, Enum):
    CONTINUE = "continue"
    EXIT = "exit"

    def __str__(self) -> str:
        return str(self.value)
