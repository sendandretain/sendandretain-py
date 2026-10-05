from enum import Enum


class WebhookEventEmailUnsubscribedType(str, Enum):
    EMAIL_UNSUBSCRIBED = "email.unsubscribed"

    def __str__(self) -> str:
        return str(self.value)
