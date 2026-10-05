from enum import Enum


class WebhookEventEmailClickedType(str, Enum):
    EMAIL_CLICKED = "email.clicked"

    def __str__(self) -> str:
        return str(self.value)
