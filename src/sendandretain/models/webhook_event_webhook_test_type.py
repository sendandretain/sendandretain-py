from enum import Enum


class WebhookEventWebhookTestType(str, Enum):
    WEBHOOK_TEST = "webhook.test"

    def __str__(self) -> str:
        return str(self.value)
