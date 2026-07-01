"""Knowledge Base API — thin facade over the generated raw client.

Methods call the generated endpoint functions in
``roe._generated.api.knowledge_base`` and return the generated response models
directly. Non-2xx responses are translated to the typed ``RoeAPIException``
family at the wrapper boundary.

This is a hand-maintained ("manual") wrapper: the knowledge_base operations are
declared ``kind: manual`` in the SDK contract, so codegen does not generate this
module. It is wired explicitly in ``roe.client`` like agents/policies/users.
"""

from __future__ import annotations

from typing import Any
from uuid import UUID

from roe._generated.api.knowledge_base import (
    knowledge_base_catalog_retrieve,
    knowledge_base_create,
    knowledge_base_destroy,
    knowledge_base_draft_retrieve,
    knowledge_base_finalize_create,
    knowledge_base_import_lens_create,
    knowledge_base_lens_retrieve,
    knowledge_base_list,
    knowledge_base_regenerate_create,
    knowledge_base_resolve_create,
    knowledge_base_retrieve,
    knowledge_base_selection_partial_update,
    knowledge_base_sync_create,
    knowledge_base_unlink_destroy,
)
from roe._generated.client import AuthenticatedClient
from roe._generated.models.create_knowledge_base import CreateKnowledgeBase
from roe._generated.models.create_knowledge_base_request import (
    CreateKnowledgeBaseRequest,
)
from roe._generated.models.draft import Draft
from roe._generated.models.finalize_request import FinalizeRequest
from roe._generated.models.knowledge_base import KnowledgeBase
from roe._generated.models.knowledge_base_import_lens_create_body import (
    KnowledgeBaseImportLensCreateBody,
)
from roe._generated.models.paginated_knowledge_base_list import (
    PaginatedKnowledgeBaseList,
)
from roe._generated.models.patched_patch_selection_request import (
    PatchedPatchSelectionRequest,
)
from roe._generated.models.patched_patch_selection_request_refs_item import (
    PatchedPatchSelectionRequestRefsItem,
)
from roe._generated.models.regenerate_request import RegenerateRequest
from roe._generated.models.resolve_request import ResolveRequest
from roe._generated.models.resolve_request_refs_item import ResolveRequestRefsItem
from roe._generated.types import UNSET
from roe.config import RoeConfig
from roe.utils.generated_request import request_raw


class KnowledgeBaseAPI:
    """API for managing Knowledge Base lenses and drafts."""

    def __init__(self, config: RoeConfig, raw_client: AuthenticatedClient):
        self.config = config
        self._raw = raw_client

    def _org(self) -> Any:
        org = self.config.organization_id
        return UUID(str(org)) if org else UNSET

    def list(
        self,
        page: int | None = None,
        page_size: int | None = None,
    ) -> PaginatedKnowledgeBaseList:
        """List all knowledge bases for the organisation."""
        response = request_raw(
            self._raw,
            knowledge_base_list,
            page=page if page is not None else UNSET,
            page_size=page_size if page_size is not None else UNSET,
            organization_id=self._org(),
        )
        return PaginatedKnowledgeBaseList.from_dict(response.json())

    def create(
        self,
        company: str,
        brief: str,
        name: str | None = None,
        product_name: str | None = None,
        website_url: str | None = None,
    ) -> CreateKnowledgeBase:
        """Create a new knowledge base draft (async generation)."""
        body = CreateKnowledgeBaseRequest(
            company=company,
            brief=brief,
            name=name if name is not None else UNSET,
            product_name=product_name if product_name is not None else UNSET,
            website_url=website_url if website_url is not None else UNSET,
        )
        response = request_raw(
            self._raw,
            knowledge_base_create,
            body=body,
            organization_id=self._org(),
        )
        return CreateKnowledgeBase.from_dict(response.json())

    def retrieve(self, knowledge_base_id: str) -> KnowledgeBase:
        """Retrieve a single knowledge base record."""
        response = request_raw(
            self._raw,
            knowledge_base_retrieve,
            UUID(str(knowledge_base_id)),
            organization_id=self._org(),
        )
        return KnowledgeBase.from_dict(response.json())

    def delete(self, knowledge_base_id: str) -> None:
        """Delete a knowledge base and its associated Atlas draft or lens."""
        request_raw(
            self._raw,
            knowledge_base_destroy,
            UUID(str(knowledge_base_id)),
            organization_id=self._org(),
        )

    def unlink(self, knowledge_base_id: str) -> None:
        """Unlink a knowledge base locally, preserving the Atlas lens."""
        request_raw(
            self._raw,
            knowledge_base_unlink_destroy,
            UUID(str(knowledge_base_id)),
            organization_id=self._org(),
        )

    def poll_draft(self, knowledge_base_id: str) -> Draft:
        """Poll the Atlas draft status until ready or error."""
        response = request_raw(
            self._raw,
            knowledge_base_draft_retrieve,
            UUID(str(knowledge_base_id)),
            organization_id=self._org(),
        )
        return Draft.from_dict(response.json())

    def patch_selection(
        self,
        knowledge_base_id: str,
        refs: list[dict[str, Any]],
        suggested_name: str | None = None,
    ) -> Draft:
        """Patch the draft's typology/tactic selection."""
        body = PatchedPatchSelectionRequest(
            refs=[PatchedPatchSelectionRequestRefsItem.from_dict(r) for r in refs],
            suggested_name=suggested_name if suggested_name is not None else UNSET,
        )
        response = request_raw(
            self._raw,
            knowledge_base_selection_partial_update,
            UUID(str(knowledge_base_id)),
            body=body,
            organization_id=self._org(),
        )
        return Draft.from_dict(response.json())

    def regenerate(
        self,
        knowledge_base_id: str,
        feedback: str | None = None,
    ) -> Draft:
        """Kick off an async regeneration round with optional feedback."""
        body = RegenerateRequest(
            feedback=feedback if feedback is not None else UNSET,
        )
        response = request_raw(
            self._raw,
            knowledge_base_regenerate_create,
            UUID(str(knowledge_base_id)),
            body=body,
            organization_id=self._org(),
        )
        return Draft.from_dict(response.json())

    def resolve(
        self,
        knowledge_base_id: str,
        refs: list[dict[str, Any]] | None = None,
        suggested_name: str | None = None,
        accept_summary: bool = False,
        discard: bool = False,
    ) -> Draft:
        """Approve or decline a pending regeneration proposal."""
        body = ResolveRequest(
            refs=[ResolveRequestRefsItem.from_dict(r) for r in refs]
            if refs is not None
            else UNSET,
            suggested_name=suggested_name if suggested_name is not None else UNSET,
            accept_summary=accept_summary,
            discard=discard,
        )
        response = request_raw(
            self._raw,
            knowledge_base_resolve_create,
            UUID(str(knowledge_base_id)),
            body=body,
            organization_id=self._org(),
        )
        return Draft.from_dict(response.json())

    def finalize(
        self,
        knowledge_base_id: str,
        name: str | None = None,
        mcp_enabled: bool = True,
        public: bool = True,
    ) -> KnowledgeBase:
        """Commit the draft into a permanent Atlas lens."""
        body = FinalizeRequest(
            name=name if name is not None else UNSET,
            mcp_enabled=mcp_enabled,
            public=public,
        )
        response = request_raw(
            self._raw,
            knowledge_base_finalize_create,
            UUID(str(knowledge_base_id)),
            body=body,
            organization_id=self._org(),
        )
        return KnowledgeBase.from_dict(response.json())

    def sync(self, knowledge_base_id: str) -> KnowledgeBase:
        """Sync the lens snapshot from Atlas (best-effort)."""
        response = request_raw(
            self._raw,
            knowledge_base_sync_create,
            UUID(str(knowledge_base_id)),
            organization_id=self._org(),
        )
        return KnowledgeBase.from_dict(response.json())

    def catalog(self) -> Any:
        """Fetch the names-only typology and tactic catalog."""
        response = request_raw(
            self._raw,
            knowledge_base_catalog_retrieve,
            organization_id=self._org(),
        )
        return response.json()

    def lens_by_atlas_id(self, atlas_lens_id: str) -> Any:
        """Fetch and optionally sync a lens by its Atlas ID."""
        response = request_raw(
            self._raw,
            knowledge_base_lens_retrieve,
            str(atlas_lens_id),
            organization_id=self._org(),
        )
        return response.json()

    def import_lens(self, atlas_lens_id: str) -> KnowledgeBase:
        """Import a finalized Atlas lens into roe-main by its atlas_lens_id."""
        body = KnowledgeBaseImportLensCreateBody.from_dict(
            {"atlas_lens_id": atlas_lens_id}
        )
        response = request_raw(
            self._raw,
            knowledge_base_import_lens_create,
            body=body,
            organization_id=self._org(),
        )
        return KnowledgeBase.from_dict(response.json())
