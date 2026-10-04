from enum import Enum


class ImportSuppressionsBodyEntriesItemReason(str, Enum):
    MANUAL = "manual"
    UNSUBSCRIBE = "unsubscribe"

    def __str__(self) -> str:
        return str(self.value)
