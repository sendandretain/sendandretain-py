from enum import Enum


class WebhookEventEmailOpenedType(str, Enum):
    EMAIL_OPENED = "email.opened"

    def __str__(self) -> str:
        return str(self.value)
