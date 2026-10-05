from enum import Enum


class WebhookEventEmailFailedType(str, Enum):
    EMAIL_FAILED = "email.failed"

    def __str__(self) -> str:
        return str(self.value)
