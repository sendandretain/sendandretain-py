from enum import Enum


class WebhookEventEmailCanceledType(str, Enum):
    EMAIL_CANCELED = "email.canceled"

    def __str__(self) -> str:
        return str(self.value)
