from enum import Enum


class GetMetricsResponse200Source(str, Enum):
    DAILY_ROLLUP = "daily_rollup"
    RAW = "raw"

    def __str__(self) -> str:
        return str(self.value)
