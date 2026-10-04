from enum import Enum


class EmitEventResponse202Status(str, Enum):
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
