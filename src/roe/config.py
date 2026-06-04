"""Configuration management for the Roe SDK."""

import os

from pydantic import BaseModel, Field


class RoeConfig(BaseModel):
    """Configuration for the Roe SDK."""

    api_key: str = Field(..., description="Roe API key")
    organization_id: str = Field(..., description="Organization ID")
    base_url: str = Field(
        default="https://api.roe-ai.com", description="Base URL for the API"
    )
    timeout: float = Field(default=60.0, description="Request timeout in seconds")
    max_retries: int = Field(default=3, description="Maximum number of retries")
    batch_chunk_delay: float = Field(
        default=10.0,
        description="Delay in seconds between batch chunk requests",
    )

    @classmethod
    def from_env(
        cls,
        api_key: str | None = None,
        organization_id: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        batch_chunk_delay: float | None = None,
    ) -> "RoeConfig":
        """Create configuration from environment variables and parameters.

        Args:
            api_key: API key. If not provided, uses ROE_API_KEY env var.
            organization_id: Organization ID. If not provided, uses ROE_ORGANIZATION_ID env var.
            base_url: Base URL. If not provided, uses ROE_BASE_URL env var or default.
            timeout: Request timeout. If not provided, uses ROE_TIMEOUT env var or default.
            max_retries: Max retries. If not provided, uses ROE_MAX_RETRIES env var or default.
            batch_chunk_delay: Delay between batch chunks. If not provided, uses ROE_BATCH_CHUNK_DELAY env var or default.

        Returns:
            RoeConfig instance.

        Raises:
            ValueError: If required parameters are missing.
        """
        # Get values from parameters or environment variables
        api_key = api_key or os.getenv("ROE_API_KEY")
        organization_id = organization_id or os.getenv("ROE_ORGANIZATION_ID")
        base_url = base_url or os.getenv("ROE_BASE_URL", "https://api.roe-ai.com")
        timeout = timeout or float(os.getenv("ROE_TIMEOUT", "60.0"))
        max_retries = max_retries or int(os.getenv("ROE_MAX_RETRIES", "3"))
        batch_chunk_delay = batch_chunk_delay if batch_chunk_delay is not None else float(
            os.getenv("ROE_BATCH_CHUNK_DELAY", "10.0")
        )

        if not api_key:
            raise ValueError(
                "API key is required. Provide it as a parameter or set the ROE_API_KEY environment variable."
            )

        if not organization_id:
            raise ValueError(
                "Organization ID is required. Provide it as a parameter or set the ROE_ORGANIZATION_ID environment variable."
            )

        return cls(
            api_key=api_key,
            organization_id=organization_id,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
            batch_chunk_delay=batch_chunk_delay,
        )
