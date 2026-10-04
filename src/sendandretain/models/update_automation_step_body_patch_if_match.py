from enum import Enum


class UpdateAutomationStepBodyPatchIfMatch(str, Enum):
    CONTINUE = "continue"
    EXIT = "exit"

    def __str__(self) -> str:
        return str(self.value)
