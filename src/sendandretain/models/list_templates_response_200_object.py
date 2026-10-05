from enum import Enum


class ListTemplatesResponse200Object(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
