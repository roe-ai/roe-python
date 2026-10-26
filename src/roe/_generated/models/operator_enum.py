from enum import Enum

class OperatorEnum(str, Enum):
    CONTAINS = "contains"
    EQUALS = "equals"
    GREATER_THAN = "greater_than"
    IS_EMPTY = "is_empty"
    IS_FALSE = "is_false"
    IS_NOT_EMPTY = "is_not_empty"
    IS_TRUE = "is_true"
    LESS_THAN = "less_than"
    NOT_EQUALS = "not_equals"

    def __str__(self) -> str:
        return str(self.value)
