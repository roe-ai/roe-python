"""Policies API — thin facade over the generated raw client.

Methods call the generated endpoint functions in ``roe._generated.api.v1``
and return the generated response models directly. Non-2xx responses are
translated to the typed ``RoeAPIException`` family at the wrapper boundary.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from uuid import UUID

from roe._generated.api.policies import (
    policies_create,
    policies_destroy,
    policies_list,
    policies_partial_update,
    policies_retrieve,
    policies_versions_create,
    policies_versions_list,
    policies_versions_retrieve,
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
from roe.api._policies_generated import GeneratedPoliciesAPI
from roe.config import RoeConfig
from roe.utils.generated_request import request_json, request_raw


_ZERO_UUID = "00000000-0000-0000-0000-000000000000"


def _normalize_policy_version_wire(data: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(data)
    if normalized.get("base_version_id") is None:
        normalized["base_version_id"] = _ZERO_UUID
    return normalized


def _parse_policy_version(data: dict[str, Any]) -> PolicyVersion:
    return PolicyVersion.from_dict(_normalize_policy_version_wire(data))


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
        response = request_raw(
            self._raw,
            policies_versions_list,
            UUID(str(policy_id)),
            page=page if page is not None else UNSET,
            page_size=page_size if page_size is not None else UNSET,
            organization_id=UUID(str(self.config.organization_id)),
        )
        data = response.json()
        return PaginatedPolicyVersionList(
            count=data["count"],
            results=[_parse_policy_version(item) for item in data.get("results", [])],
            next_=data.get("next"),
            previous=data.get("previous"),
        )

    def retrieve(self, policy_id: str, version_id: str) -> PolicyVersion:
        """Retrieve a specific version of a policy."""
        response = request_raw(
            self._raw,
            policies_versions_retrieve,
            UUID(str(policy_id)),
            UUID(str(version_id)),
            organization_id=UUID(str(self.config.organization_id)),
        )
        return _parse_policy_version(response.json())

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
            base_version_id=UUID(str(base_version_id)) if base_version_id else UNSET,
        )
        resp = request_json(
            self._raw,
            policies_versions_create,
            UUID(str(policy_id)),
            body=body,
            organization_id=UUID(str(self.config.organization_id)),
        )
        created = resp.parsed
        if created is None or created.id is None:
            raise ValueError(
                f"Unexpected response from server: status={resp.status_code}"
            )
        # POST returns partial data; re-fetch to get the full version.
        return self.retrieve(policy_id, str(created.id))


class PoliciesAPI(GeneratedPoliciesAPI):
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
        response = request_raw(
            self._raw,
            policies_list,
            page=page if page is not None else UNSET,
            page_size=page_size if page_size is not None else UNSET,
            organization_id=UUID(str(self.config.organization_id)),
        )
        return PaginatedPolicyList.from_dict(response.json())

    def retrieve(self, policy_id: str) -> Policy:
        """Retrieve a specific policy by ID."""
        response = request_raw(
            self._raw,
            policies_retrieve,
            UUID(str(policy_id)),
            organization_id=UUID(str(self.config.organization_id)),
        )
        return Policy.from_dict(response.json())

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
        resp = request_json(
            self._raw,
            policies_create,
            body=body,
            organization_id=UUID(str(self.config.organization_id)),
        )
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
        resp = request_json(
            self._raw,
            policies_partial_update,
            UUID(str(policy_id)),
            body=body,
            organization_id=UUID(str(self.config.organization_id)),
        )
        return resp.parsed

    def delete(self, policy_id: str) -> None:
        """Delete a policy and all its versions."""
        request_raw(
            self._raw,
            policies_destroy,
            UUID(str(policy_id)),
            organization_id=UUID(str(self.config.organization_id)),
        )
