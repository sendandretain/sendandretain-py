from enum import Enum


class WebhookEventEmailDeliveredType(str, Enum):
    EMAIL_DELIVERED = "email.delivered"

    def __str__(self) -> str:
        return str(self.value)
