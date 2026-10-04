from enum import Enum


class AddAutomationStepsSchema0Variant4Method(str, Enum):
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
