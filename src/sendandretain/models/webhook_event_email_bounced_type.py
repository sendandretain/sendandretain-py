from enum import Enum


class WebhookEventEmailBouncedType(str, Enum):
    EMAIL_BOUNCED = "email.bounced"

    def __str__(self) -> str:
        return str(self.value)
