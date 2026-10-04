from enum import Enum


class EventResultSkippedItemReason(str, Enum):
    ALREADY_RUNNING = "already_running"
    EXCLUSIVE = "exclusive"
    FILTERED = "filtered"
    GUARDED = "guarded"
    NO_STEPS = "no_steps"
    SUPPRESSED = "suppressed"

    def __str__(self) -> str:
        return str(self.value)
