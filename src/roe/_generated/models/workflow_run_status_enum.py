from enum import Enum

class WorkflowRunStatusEnum(str, Enum):
    CANCELLED = "cancelled"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
