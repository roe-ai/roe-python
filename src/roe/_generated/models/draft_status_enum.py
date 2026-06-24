from enum import Enum

class DraftStatusEnum(str, Enum):
    ERROR = "error"
    GENERATING = "generating"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
