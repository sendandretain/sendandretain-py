from enum import Enum


class ErrorErrorKeyScope(str, Enum):
    ADMIN = "admin"
    READ = "read"
    WRITE = "write"

    def __str__(self) -> str:
        return str(self.value)
