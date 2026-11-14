from enum import Enum

class HealthEnum(str, Enum):
    CONNECTED = "connected"
    CONNECTING = "connecting"
    EXPIRED = "expired"
    FAILED = "failed"
    NEEDS_ATTENTION = "needs_attention"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
