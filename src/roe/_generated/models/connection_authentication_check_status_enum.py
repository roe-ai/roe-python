from enum import Enum

class ConnectionAuthenticationCheckStatusEnum(str, Enum):
    FAILED = "failed"
    NOT_CONFIGURED = "not_configured"
    PASSED = "passed"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
