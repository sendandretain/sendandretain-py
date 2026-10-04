from enum import Enum


class CreateTemplateBodyCategory(str, Enum):
    LIFECYCLE = "lifecycle"
    TRANSACTIONAL = "transactional"

    def __str__(self) -> str:
        return str(self.value)
