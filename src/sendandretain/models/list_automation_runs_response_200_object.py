from enum import Enum


class ListAutomationRunsResponse200Object(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
