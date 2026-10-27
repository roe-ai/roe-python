from enum import Enum

class StepRunStatusEnum(str, Enum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    SKIPPED = "skipped"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
