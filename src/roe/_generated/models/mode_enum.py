from enum import Enum

class ModeEnum(str, Enum):
    APPEND = "append"
    COMBINE = "combine"

    def __str__(self) -> str:
        return str(self.value)
