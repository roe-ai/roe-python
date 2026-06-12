from enum import Enum

class StatusEnum(str, Enum):
    ACTIVE = "active"
    ERROR = "error"

    def __str__(self) -> str:
        return str(self.value)
