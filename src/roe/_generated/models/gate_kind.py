from enum import Enum

class GateKind(str, Enum):
    FEEDBACK = "feedback"
    MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
