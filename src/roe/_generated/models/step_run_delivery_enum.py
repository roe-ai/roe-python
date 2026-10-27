from enum import Enum

class StepRunDeliveryEnum(str, Enum):
    SENDING = "sending"
    SENT = "sent"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
