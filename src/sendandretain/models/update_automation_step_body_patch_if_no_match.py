from enum import Enum


class UpdateAutomationStepBodyPatchIfNoMatch(str, Enum):
    CONTINUE = "continue"
    EXIT = "exit"

    def __str__(self) -> str:
        return str(self.value)
