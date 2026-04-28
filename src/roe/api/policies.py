"""Policies API — thin facade over the generated raw client.

Methods call the generated endpoint functions in ``roe._generated.api.v1``
and return the generated response models directly. Non-2xx responses are
translated to the typed ``RoeAPIException`` family at the wrapper boundary.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

from roe._generated.api.v1 import (
    v1_policies_create,
    v1_policies_destroy,
    v1_policies_list,
    v1_policies_partial_update,
    v1_policies_retrieve,
    v1_policies_versions_create,
    v1_policies_versions_list,
    v1_policies_versions_retrieve,
)
from roe._generated.client import AuthenticatedClient
from roe._generated.models.create_policy import CreatePolicy
from roe._generated.models.create_policy_request import CreatePolicyRequest
from roe._generated.models.create_policy_version_request import (
    CreatePolicyVersionRequest,
)
from roe._generated.models.paginated_policy_list import PaginatedPolicyList
from roe._generated.models.paginated_policy_version_list import (
    PaginatedPolicyVersionList,
)
from roe._generated.models.patched_update_policy_request import (
    PatchedUpdatePolicyRequest,
)
from roe._generated.models.policy import Policy
from roe._generated.models.policy_version import PolicyVersion
from roe._generated.types import UNSET
from roe.config import RoeConfig
from roe.exceptions import translate_response

if TYPE_CHECKING:
    pass


class PolicyVersionsAPI:
    """Nested API for policy version operations."""

    def __init__(self, config: RoeConfig, raw_client: AuthenticatedClient):
        self.config = config
        self._raw = raw_client

    def list(
        self,
        policy_id: str,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedPolicyVersionList:
        """List versions of a policy."""
        resp = v1_policies_versions_list.sync_detailed(
            policy_id=UUID(policy_id),
            client=self._raw,
            page=page if page is not None else UNSET,
            page_size=page_size if page_size is not None else UNSET,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
        return resp.parsed  # type: ignore[return-value]

    def retrieve(self, policy_id: str, version_id: str) -> PolicyVersion:
        """Retrieve a specific version of a policy."""
        resp = v1_policies_versions_retrieve.sync_detailed(
            policy_id=UUID(policy_id),
            version_id=UUID(version_id),
            client=self._raw,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
        return resp.parsed  # type: ignore[return-value]

    def create(
        self,
        policy_id: str,
        content: dict[str, Any],
        version_name: str | None = None,
        base_version_id: str | None = None,
    ) -> PolicyVersion:
        """Create a new policy version (auto-set as current). Re-fetches for full data."""
        body = CreatePolicyVersionRequest(
            content=content,
            version_name=version_name if version_name is not None else UNSET,
            base_version_id=UUID(base_version_id) if base_version_id else UNSET,
        )
        resp = v1_policies_versions_create.sync_detailed(
            policy_id=UUID(policy_id),
            client=self._raw,
            body=body,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
        created = resp.parsed
        if created is None or created.id is None:
            raise ValueError(f"Unexpected response from server: status={resp.status_code}")
        # POST returns partial data; re-fetch to get the full version.
        return self.retrieve(policy_id, str(created.id))


class PoliciesAPI:
    """API for managing policies used by agentic workflows."""

    def __init__(self, config: RoeConfig, raw_client: AuthenticatedClient):
        self.config = config
        self._raw = raw_client
        self._versions = PolicyVersionsAPI(config, raw_client)

    @property
    def versions(self) -> PolicyVersionsAPI:
        """Access the versions sub-API for policy version operations."""
        return self._versions

    def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedPolicyList:
        """List policies in the organization."""
        resp = v1_policies_list.sync_detailed(
            client=self._raw,
            page=page if page is not None else UNSET,
            page_size=page_size if page_size is not None else UNSET,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
        return resp.parsed  # type: ignore[return-value]

    def retrieve(self, policy_id: str) -> Policy:
        """Retrieve a specific policy by ID."""
        resp = v1_policies_retrieve.sync_detailed(
            id=UUID(policy_id),
            client=self._raw,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
        return resp.parsed  # type: ignore[return-value]

    def create(
        self,
        name: str,
        content: dict[str, Any],
        description: str = "",
        version_name: str | None = None,
    ) -> CreatePolicy:
        """Create a new policy with an initial version."""
        body = CreatePolicyRequest(
            name=name,
            content=content,
            description=description,
            version_name=version_name if version_name is not None else UNSET,
        )
        resp = v1_policies_create.sync_detailed(
            client=self._raw,
            body=body,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
        return resp.parsed  # type: ignore[return-value]

    def update(
        self,
        policy_id: str,
        name: str | None = None,
        description: str | None = None,
    ) -> Any:
        """Update a policy's metadata via PATCH (partial update)."""
        body = PatchedUpdatePolicyRequest(
            name=name if name is not None else UNSET,
            description=description if description is not None else UNSET,
        )
        resp = v1_policies_partial_update.sync_detailed(
            id=UUID(policy_id),
            client=self._raw,
            body=body,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
        return resp.parsed

    def delete(self, policy_id: str) -> None:
        """Delete a policy and all its versions."""
        resp = v1_policies_destroy.sync_detailed(
            id=UUID(policy_id),
            client=self._raw,
            organization_id=UUID(self.config.organization_id),
        )
        translate_response(resp)
