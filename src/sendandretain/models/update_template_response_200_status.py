from enum import Enum


class UpdateTemplateResponse200Status(str, Enum):
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
