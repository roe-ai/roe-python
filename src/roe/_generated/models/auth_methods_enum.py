from enum import Enum

class AuthMethodsEnum(str, Enum):
    BROWSER_SIGN_IN = "browser_sign_in"
    MANUAL = "manual"
    PROVIDER_CONSENT = "provider_consent"

    def __str__(self) -> str:
        return str(self.value)
