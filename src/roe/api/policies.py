"""Policies API implementation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from roe.config import RoeConfig
from roe.models.policy import Policy, PolicyVersion
from roe.models.responses import PaginatedResponse
from roe.utils.http_client import RoeHTTPClient
from roe.utils.pagination import PaginationHelper

if TYPE_CHECKING:
    from roe.api.policies import PoliciesAPI


class PolicyVersionsAPI:
    """Nested API for policy version operations."""

    def __init__(self, policies_api: "PoliciesAPI"):
        """Initialize the versions API.

        Args:
            policies_api: Parent PoliciesAPI instance.
        """
        self._policies_api = policies_api

    @property
    def http_client(self) -> RoeHTTPClient:
        return self._policies_api.http_client

    def list(self, policy_id: str) -> list[PolicyVersion]:
        """List all versions of a policy.

        Args:
            policy_id: Policy UUID.

        Returns:
            List of policy versions.
        """
        response_data = self.http_client.get(
            f"/v1/policies/{policy_id}/versions/"
        )
        # Response is paginated: {"count": ..., "results": [...]}
        results = response_data.get("results", response_data)
        if isinstance(results, list):
            return [PolicyVersion(**version_data) for version_data in results]
        return []

    def retrieve(self, policy_id: str, version_id: str) -> PolicyVersion:
        """Retrieve a specific version of a policy.

        Args:
            policy_id: Policy UUID.
            version_id: Version UUID.

        Returns:
            PolicyVersion instance.
        """
        response_data = self.http_client.get(
            f"/v1/policies/{policy_id}/versions/{version_id}/"
        )
        return PolicyVersion(**response_data)

    def create(
        self,
        policy_id: str,
        content: dict[str, Any],
        version_name: str | None = None,
        base_version_id: str | None = None,
    ) -> PolicyVersion:
        """Create a new version of a policy.

        Creating a new version automatically sets it as the current version.

        Args:
            policy_id: Policy UUID.
            content: Policy content (guidelines, instructions, dispositions).
            version_name: Name for the version (auto-generated if not provided).
            base_version_id: ID of the version this was derived from.

        Returns:
            Created PolicyVersion instance.
        """
        json_data: dict[str, Any] = {"content": content}

        if version_name is not None:
            json_data["version_name"] = version_name
        if base_version_id is not None:
            json_data["base_version_id"] = base_version_id

        response_data = self.http_client.post(
            f"/v1/policies/{policy_id}/versions/", json_data=json_data
        )
        # POST returns partial data; re-fetch to get the full version
        version_id = response_data.get("id")
        if not version_id:
            raise ValueError(f"Unexpected response from server: {response_data}")
        return self.retrieve(policy_id, version_id)


class PoliciesAPI:
    """API for managing policies used by agentic workflows."""

    def __init__(self, config: RoeConfig, http_client: RoeHTTPClient):
        """Initialize the policies API.

        Args:
            config: Roe configuration.
            http_client: HTTP client instance.
        """
        self.config = config
        self.http_client = http_client
        self._versions = PolicyVersionsAPI(self)

    @property
    def versions(self) -> PolicyVersionsAPI:
        """Access the versions sub-API for policy version operations.

        Returns:
            PolicyVersionsAPI instance.

        Examples:
            versions = client.policies.versions.list("policy-uuid")
            version = client.policies.versions.retrieve("policy-uuid", "version-uuid")
        """
        return self._versions

    def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedResponse[Policy]:
        """List policies in the organization.

        Args:
            page: Page number (1-based).
            page_size: Number of results per page.

        Returns:
            Paginated list of policies.
        """
        params = PaginationHelper.build_query_params(
            organization_id=self.config.organization_id,
            page=page,
            page_size=page_size,
        )

        response_data = self.http_client.get("/v1/policies/", params=params)

        policies = [
            Policy(**policy_data) for policy_data in response_data["results"]
        ]

        return PaginatedResponse[Policy](
            count=response_data["count"],
            next=response_data.get("next"),
            previous=response_data.get("previous"),
            results=policies,
        )

    def retrieve(self, policy_id: str) -> Policy:
        """Retrieve a specific policy by ID.

        Args:
            policy_id: Policy UUID.

        Returns:
            Policy instance.
        """
        response_data = self.http_client.get(f"/v1/policies/{policy_id}/")
        return Policy(**response_data)

    def create(
        self,
        name: str,
        content: dict[str, Any],
        description: str = "",
        version_name: str | None = None,
    ) -> Policy:
        """Create a new policy with an initial version.

        This atomically creates the policy and its first version.
        The initial version is automatically set as the current version.

        Args:
            name: Name of the policy.
            content: Policy content (guidelines, instructions, dispositions).
            description: Description of the policy.
            version_name: Name for the initial version (defaults to "version 1").

        Returns:
            Created Policy instance.
        """
        json_data: dict[str, Any] = {
            "name": name,
            "content": content,
            "description": description,
        }

        if version_name is not None:
            json_data["version_name"] = version_name

        response_data = self.http_client.post("/v1/policies/", json_data=json_data)
        return Policy(**response_data)

    def update(
        self,
        policy_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> Policy:
        """Update a policy's metadata.

        Args:
            policy_id: Policy UUID.
            name: New name for the policy.
            description: New description.

        Returns:
            Updated Policy instance.
        """
        json_data: dict[str, Any] = {}

        if name is not None:
            json_data["name"] = name
        if description is not None:
            json_data["description"] = description

        response_data = self.http_client.put(
            f"/v1/policies/{policy_id}/", json_data=json_data
        )
        return Policy(**response_data)

    def delete(self, policy_id: str) -> None:
        """Delete a policy and all its versions.

        Args:
            policy_id: Policy UUID.
        """
        self.http_client.delete(f"/v1/policies/{policy_id}/")
