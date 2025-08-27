"""Authentication handling for the Roe AI SDK."""

from roe.config import RoeConfig


class RoeAuth:
    """Handles authentication for Roe AI API requests."""

    def __init__(self, config: RoeConfig):
        """Initialize authentication with config.

        Args:
            config: Roe configuration containing API key.
        """
        self.config = config

    def get_headers(self) -> dict[str, str]:
        """Get authentication headers for API requests.

        Returns:
            Dictionary of headers including Authorization.
        """
        return {
            "Authorization": f"Bearer {self.config.api_key}",
            "User-Agent": "roe-python/0.1.0",
        }
