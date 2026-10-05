from enum import Enum


class WebhookEventEmailComplainedType(str, Enum):
    EMAIL_COMPLAINED = "email.complained"

    def __str__(self) -> str:
        return str(self.value)
