from enum import Enum


class ListAutomationsResponse200Object(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
