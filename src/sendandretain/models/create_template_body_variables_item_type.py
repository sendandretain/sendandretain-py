from enum import Enum


class CreateTemplateBodyVariablesItemType(str, Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
