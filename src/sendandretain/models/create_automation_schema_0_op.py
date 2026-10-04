from enum import Enum


class CreateAutomationSchema0Op(str, Enum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
