from enum import Enum


class CreateAutomationSchema1Variant7FilterVariant0ItemOp(str, Enum):
    CONTAINS = "contains"
    EQ = "eq"
    EXISTS = "exists"
    GT = "gt"
    IN = "in"
    LT = "lt"
    NEQ = "neq"
    NOT_EXISTS = "not_exists"
    OLDER_THAN_DAYS = "older_than_days"
    WITHIN_DAYS = "within_days"

    def __str__(self) -> str:
        return str(self.value)
