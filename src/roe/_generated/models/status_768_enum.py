from enum import Enum

class Status768Enum(str, Enum):
    ACTIVE = "active"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
