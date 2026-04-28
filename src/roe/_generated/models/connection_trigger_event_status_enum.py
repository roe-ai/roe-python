from enum import Enum

class ConnectionTriggerEventStatusEnum(str, Enum):
    COMPLETED = "completed"
    DETECTED = "detected"
    FAILED = "failed"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
