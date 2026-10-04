from enum import Enum


class CreateAutomationSchema1Variant4Method(str, Enum):
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
