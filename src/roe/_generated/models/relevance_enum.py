from enum import Enum

class RelevanceEnum(str, Enum):
    CORE = "core"
    EDGE = "edge"
    WATCH = "watch"

    def __str__(self) -> str:
        return str(self.value)
