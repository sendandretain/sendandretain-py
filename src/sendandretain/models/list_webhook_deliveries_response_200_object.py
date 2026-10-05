from enum import Enum


class ListWebhookDeliveriesResponse200Object(str, Enum):
    LIST = "list"

    def __str__(self) -> str:
        return str(self.value)
