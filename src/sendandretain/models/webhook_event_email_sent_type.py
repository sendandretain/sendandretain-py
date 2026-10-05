from enum import Enum


class WebhookEventEmailSentType(str, Enum):
    EMAIL_SENT = "email.sent"

    def __str__(self) -> str:
        return str(self.value)
