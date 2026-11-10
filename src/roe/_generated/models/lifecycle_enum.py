from enum import Enum

class LifecycleEnum(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DISCONNECTED = "disconnected"

    def __str__(self) -> str:
        return str(self.value)
