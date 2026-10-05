from enum import Enum


class WebhookEventEmailSuppressedType(str, Enum):
    EMAIL_SUPPRESSED = "email.suppressed"

    def __str__(self) -> str:
        return str(self.value)
