"""Roe AI Python SDK

A Python SDK for interacting with the Roe AI API.

Basic usage:
    from roe import RoeClient

    client = RoeClient(
        api_key="your-api-key",
        organization_id="your-org-uuid"
    )

    # List agents
    agents = client.agents.list()

    # Run an agent
    result = client.agents.run(
        agent_id="agent-uuid",
        document="path/to/file.pdf",
        prompt="Analyze this document"
    )
"""

from roe.client import RoeClient
from roe.exceptions import (
    AuthenticationError,
    BadRequestError,
    ForbiddenError,
    InsufficientCreditsError,
    NotFoundError,
    RoeAPIException,
    ServerError,
)
from roe.models import FileUpload
from roe.models.responses import (
    AgentDatum,
    AgentJobResult,
    AgentJobStatus,
    JobDataDeleteResponse,
    JobStatus,
    Reference,
)

__version__ = "0.2.9"

__all__ = [
    # Main client
    "RoeClient",
    # Helper classes
    "FileUpload",
    # Response models
    "AgentDatum",
    "AgentJobResult",
    "AgentJobStatus",
    "JobDataDeleteResponse",
    "JobStatus",
    "Reference",
    # Exceptions
    "RoeAPIException",
    "AuthenticationError",
    "BadRequestError",
    "ForbiddenError",
    "InsufficientCreditsError",
    "NotFoundError",
    "ServerError",
]
