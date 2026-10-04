from enum import Enum


class CreateTemplateResponse201Status(str, Enum):
    DRAFT = "draft"

    def __str__(self) -> str:
        return str(self.value)
