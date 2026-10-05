from enum import Enum


class WebhookEventEmailDeliveryDelayedType(str, Enum):
    EMAIL_DELIVERY_DELAYED = "email.delivery_delayed"

    def __str__(self) -> str:
        return str(self.value)
