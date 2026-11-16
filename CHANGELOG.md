# Changelog

## 1.1.23

Built from roe-main release `1-1-5`.

### Added

- Added `ConnectorTypeEnum.SHIELD_ENGAGE` with value `shield_engage`, so you can use this connector type anywhere `ConnectorTypeEnum` is accepted, including `CreateConnectionRequest` and `TestConnectionCredentialsRequest`.

## 1.1.22

Built from roe-main release `1-1-5`.

### Added

- `client.connections.list(...)` now accepts an optional `lifecycle` (`str | None`) filter, and connection list responses can include `lifecycle` on `ConnectionList`. The generated models also add `LifecycleEnum` for lifecycle values.
- `client.connections.update(...)` and `client.connections.replace(...)` now accept optional `lifecycle` (`str | None`) and `confirm_in_use` (`bool | None`) parameters. The corresponding request models `UpdateConnectionRequest` and `PatchedUpdateConnectionRequest` now include `lifecycle` and `confirm_in_use`, and `Connection` responses can include `lifecycle`.
- Update and replace conflict responses now have a dedicated `ConnectionUpdateConflictResponse` model for 409 responses.
- `ListAgentJob` now includes the required `agent_version_id` field.

## 1.1.21

Built from roe-main release `1-1-4`.

### Added

- Added `ConnectorTypeEnum.ALLOY` (`"alloy"`) as a valid connector type, so you can now pass `alloy` anywhere `ConnectorTypeEnum` is used, including connection creation and credential testing requests.

## 1.1.20

Built from roe-main release `1-1-3`.

### Added

- Added a new `client.workflows` API with methods to manage workflows and versions: `client.workflows.create(...)`, `client.workflows.list(...)`, `client.workflows.retrieve(...)`, `client.workflows.update(...)`, `client.workflows.delete(...)`, `client.workflows.create_version(...)`, `client.workflows.list_versions(...)`, `client.workflows.retrieve_version(...)`, and `client.workflows.set_current_version(...)`.
- Added workflow run support on `client.workflows` with `client.workflows.run(...)`, `client.workflows.run_batch(...)`, `client.workflows.list_runs(...)`, and `client.workflows.retrieve_run(...)` so you can start and inspect workflow executions.
- Added raw workflow operations for direct endpoint access: `workflows_create`, `workflows_destroy`, `workflows_list`, `workflows_partial_update`, `workflows_retrieve`, `workflows_runs_create`, `workflows_runs_batch_create`, `workflows_runs_list`, `workflows_runs_retrieve`, `workflows_versions_create`, `workflows_versions_list`, `workflows_versions_retrieve`, and `workflows_versions_set_current_create`.
- Added workflow request, response, and pagination models under `roe._generated.models`, including `Workflow`, `WorkflowDetail`, `WorkflowVersion`, `WorkflowVersionDetail`, `WorkflowRun`, `WorkflowRunDetail`, `WorkflowRunBatch`, `PaginatedWorkflowList`, `PaginatedWorkflowVersionList`, `PaginatedWorkflowRunList`, `WorkflowCreateRequest`, `PatchedWorkflowUpdateRequest`, `WorkflowVersionCreateRequest`, `WorkflowRunCreateRequest`, and `WorkflowRunBatchCreateRequest`.
- Added workflow definition and step models under `roe._generated.models`, including `WorkflowDefinition`, `WorkflowDefinitionRequest`, `InputField`, `Condition`, `ApprovalBlock`, `ForEachBlock`, `IfBlock`, `ParallelBlock`, `AgentStep`, `ConnectionStep`, `EditFieldsStep`, `MergeStep`, and `StepRun`.
- Added workflow-related enums under `roe._generated.models`: `CombineEnum`, `GateKind`, `ModeEnum`, `OperatorEnum`, `StepRunDeliveryEnum`, `StepRunStatusEnum`, and `WorkflowRunStatusEnum`.

## 1.1.19

Built from roe-main release `1-1-2`.

### Added

- Added `ConnectorTypeEnum.SHIELD_API` (`"shield_api"`) as a supported connector type, so you can now pass `shield_api` anywhere `ConnectorTypeEnum` is used, including `CreateConnectionRequest` and `TestConnectionCredentialsRequest`.

## 1.1.18

Built from roe-main release `1-1-2`.

### Added

- `ConnectorTypeEnum` now includes `SLACK` and `SMTP`, so you can use `slack` and `smtp` as connector types anywhere this enum is accepted, including connection create, update, and credential test request models.

## 1.1.17

Built from roe-main release `1-1-1`.

### Added

- Added `ConnectorTypeEnum.SIFT_API` with value `"sift_api"`, so you can use `sift_api` anywhere connector types are accepted, including `CreateConnectionRequest` and `TestConnectionCredentialsRequest`.

## 1.1.16

Built from roe-main release `1-1-1`.

### Added

- The raw client operation `agents_jobs_list` now accepts an optional `review_state` query parameter, with the new `ReviewStateEnum` model under `roe._generated.models` for its values. `client.agents.jobs.list(...)` does not expose this filter yet.
- `ListAgentJob` now includes a required `review_state` field of type `ReviewStateEnum`, so agent job list responses expose each job's review state.
- `SkillSetGenerationRun` now includes a required `error` field, so callers can read the reported failure reason when a run provides one.

## 1.1.15

Built from roe-main release `1-1-0`.

### Added

- Added the `client.skill_sets` resource with methods to create, list, retrieve, update, and delete skill sets, plus version workflows via `client.skill_sets.create_version(...)`, `client.skill_sets.list_versions(...)`, `client.skill_sets.retrieve_version(...)`, `client.skill_sets.generate_version(...)`, `client.skill_sets.get_generation(...)`, `client.skill_sets.cancel_generation(...)`, and `client.skill_sets.set_current_version(...)`. New generated models under `roe._generated.models` support these APIs, including `CreateSkillSetRequest`, `CreateSkillSetVersionRequest`, `GenerateSkillSetVersionRequest`, `SkillSet`, `SkillSetVersion`, `PublicSkillSetGeneration`, `PaginatedSkillSetList`, `PaginatedSkillSetVersionList`, and related types.
- Added raw client operations for the skill set API: `skill_sets_create`, `skill_sets_destroy`, `skill_sets_generate_version`, `skill_sets_generation_cancel`, `skill_sets_generation_retrieve`, `skill_sets_list`, `skill_sets_partial_update`, `skill_sets_retrieve`, `skill_sets_set_current_version`, `skill_sets_versions_create`, `skill_sets_versions_list`, and `skill_sets_versions_retrieve`. Use these if you call the generated low-level operations directly.
- The raw client operation `agents_list` now accepts the optional `tags_match` query parameter. `client.agents.list(...)` does not expose it yet.
- Added connection-related models `ConnectionAuthenticationCheck`, `ConnectionAuthenticationCheckStatusEnum`, `ConnectionAuthenticationChecks`, and `ConnectorBrowserSession`, and added the optional `checks` field to `TestConnection`. `Connection` now includes required `browser_session_expires_at`, and `ConnectorMetadata` now includes required `browser_session`.
- `AgentTag` now includes the required `private` field.

### Changed

- **Breaking.** `AgentJobResultItem.cost`, `AgentJobResultItem.input_tokens`, `AgentJobResultItem.output_tokens`, `AgentJobResultResponse.input_tokens`, and `AgentJobResultResponse.output_tokens` are no longer guaranteed to be present. Update callers to handle these attributes as optional.

### Removed

- **Breaking.** Removed the `client.knowledge_base` methods `catalog(...)`, `create(...)`, `delete(...)`, `finalize(...)`, `import_lens(...)`, `lens_by_atlas_id(...)`, `list(...)`, `patch_selection(...)`, `poll_draft(...)`, `regenerate(...)`, `resolve(...)`, `retrieve(...)`, `sync(...)`, and `unlink(...)`. Calls using the knowledge base resource must be migrated away from these SDK entry points.
- **Breaking.** Removed raw client operations `knowledge_base_catalog_retrieve`, `knowledge_base_create`, `knowledge_base_destroy`, `knowledge_base_draft_retrieve`, `knowledge_base_finalize_create`, `knowledge_base_import_lens_create`, `knowledge_base_lens_retrieve`, `knowledge_base_list`, `knowledge_base_regenerate_create`, `knowledge_base_resolve_create`, `knowledge_base_retrieve`, `knowledge_base_selection_partial_update`, `knowledge_base_sync_create`, and `knowledge_base_unlink_destroy`. If you depend on generated low-level knowledge base calls, you must stop importing and calling these operations.
- **Breaking.** Removed knowledge base models from `roe._generated.models`, including `CreateKnowledgeBase`, `CreateKnowledgeBaseRequest`, `Draft`, `DraftRef`, `DraftStatusEnum`, `FinalizeRequest`, `KnowledgeBase`, `KnowledgeBaseStatusEnum`, `PaginatedKnowledgeBaseList`, `PatchedPatchSelectionRequest`, `PendingProposal`, `RegenerateRequest`, `RelevanceEnum`, and `ResolveRequest`. Update imports and type references to avoid these removed model classes.

## 1.1.14

Built from roe-main release `1-0-96`.

### Added

- `ConnectorTypeEnum` now includes `METABASE` (`"metabase"`), so you can use `metabase` anywhere connector types are accepted, including `CreateConnectionRequest.type` and `TestConnectionCredentialsRequest.type`.

## 1.1.13

Built from roe-main release `1-0-96`.

### Removed

- **Breaking.** Removed the `NullEnum` model from `roe._generated.models`; update any imports or type references that still use `NullEnum`.

## 1.1.12

Built from roe-main release `1-0-96`.

### Added

- Added `roe._generated.models.NullEnum` and `roe._generated.models.SkillGenerationStateEnum`. `BaseAgent` responses now include the required `skill_generation_state` field.
- Added `roe._generated.models.PostActionSpec` and `roe._generated.models.PostActionSpecRequest` for agent version post-actions. `AgentVersion` now includes required `post_actions`, and `AgentVersionCreateRequest` accepts optional `post_actions` so you can configure or replace post-actions when creating a version.
- Added `ConnectorTypeEnum.SIFT` (`"sift"`) as a supported connector type anywhere `ConnectorTypeEnum` is used, including connection creation and credential testing requests.

## 1.1.11

Built from roe-main release `1-0-95`.

### Added

- `ConnectorTypeEnum` now includes the `shield` value, so you can use `ConnectorTypeEnum.SHIELD` anywhere connector types are accepted, including models such as `CreateConnectionRequest` and `TestConnectionCredentialsRequest`.
- `SupportedLLMModel` now has a required `supports_thinking` field. Callers reading or constructing `roe._generated.models.SupportedLLMModel` should handle this attribute.

## 1.1.10

Built from roe-main release `1-0-94`.

### Added

- `roe._generated.models.AgentVersion` now includes the required `supports_memory` attribute, so callers can inspect whether an agent version's engine supports memory profiles.

## 1.1.9

Built from roe-main release `1-0-93`.

### Added

- `client.agents.jobs.resend_webhook(...)` now accepts an optional `webhook_id` parameter of type `str | None`, so you can resend a job completion webhook to a specific webhook instead of all webhooks attached to the job's agent.

## 1.1.8

Built from roe-main release `1-0-93`.

### Added

- Added support for resending an agent job webhook with `client.agents.jobs.resend_webhook(...)`, and the corresponding raw operation `agents_jobs_webhook_resend_create` for `POST /v1/agents/jobs/{job_id}/webhook/resend/`.
- Added `ResendAgentJobWebhookRequest` for resend requests and `AgentJobWebhookResendResponse` for the resend result under `roe._generated.models`.

## 1.1.7

Built from roe-main release `1-0-91`.

### Added

- The raw client operation `connections_list` now accepts an optional `ordering` query parameter. `client.connections.list(...)` does not expose it yet.
- `roe._generated.models.Connection` and `roe._generated.models.ConnectionList` now include the required `credentials_configured` field.

## 1.1.6

### Added

- `skip_cache=True` parameter on `client.agents.run(...)`, `run_many(...)`,
  `run_sync(...)`, `run_version(...)`, and `run_version_sync(...)`. Sends the
  `X-Skip-Cache: true` header so the backend bypasses the job-result cache and
  forces a fresh run (the fresh result still refreshes the cache).
  Note: `skip_cache` is now a reserved parameter name on these methods (like
  `metadata` and `idempotency_key`); an agent input literally named
  `skip_cache` can no longer be passed via `**inputs` — use `run_many`'s
  dict-based inputs for such agents.

## 1.1.5

Built from roe-main release `1-0-87`.

### Added

- Added agent job listing via `client.agents.jobs.list(...)`, and the corresponding raw operation `agents_jobs_list` for `GET /v1/agents/{agent_id}/jobs/`.
- Added the agent job list response models `AgentJobEvaluation`, `AgentJobFeedbackNested`, `AgentJobStatusEvent`, `JobInput`, `ListAgentJob`, `PaginatedListAgentJobList`, and `ReviewStatusEnum` under `roe._generated.models` for working with listed job data.

## 1.1.4

Built from roe-main release `1-0-87`.

### Added

- The raw client operation `agents_list` now accepts optional filters `created_from`, `created_to`, `creator_id`, `include_untagged`, `job_count_max`, `job_count_min`, `most_recent_job_from`, `most_recent_job_to`, and `name`. `client.agents.list(...)` still takes only `page` and `page_size`.

## 1.1.3

Built from roe-main release `1-0-86`.

### Changed

- Regenerated from the latest SDK spec; no changes to the generated API surface.

## 1.1.2

Built from roe-main release `1-0-86`.

### Added

- Added `client.agents.jobs.retrieve_artifact(...)` to fetch an agent job artifact result, and added the raw client operation `agents_jobs_artifacts_result_retrieve` plus the `AgentJobArtifactResult` model for lower-level access.
- Added agent and policy replacement methods with `client.agents.replace(...)`, `client.agents.versions.replace(...)`, and `client.policies.replace(...)`.
- Added connection management APIs: `client.connections.create(...)`, `client.connections.list(...)`, `client.connections.retrieve(...)`, `client.connections.update(...)`, `client.connections.replace(...)`, `client.connections.delete(...)`, `client.connections.test(...)`, and `client.connections.test_credentials(...)`.
- Added connector discovery APIs with `client.connectors.list(...)` and `client.connectors.retrieve(...)`, and `ConnectorTypeEnum` now includes `google_docs` and `google_sheets`.
- Added knowledge base APIs with `client.knowledge_base.catalog(...)`, `client.knowledge_base.create(...)`, `client.knowledge_base.list(...)`, `client.knowledge_base.retrieve(...)`, `client.knowledge_base.delete(...)`, `client.knowledge_base.poll_draft(...)`, `client.knowledge_base.patch_selection(...)`, `client.knowledge_base.finalize(...)`, `client.knowledge_base.regenerate(...)`, `client.knowledge_base.resolve(...)`, `client.knowledge_base.sync(...)`, `client.knowledge_base.unlink(...)`, `client.knowledge_base.import_lens(...)`, and `client.knowledge_base.lens_by_atlas_id(...)`.
- Added the corresponding raw knowledge base operations `knowledge_base_catalog_retrieve`, `knowledge_base_create`, `knowledge_base_destroy`, `knowledge_base_draft_retrieve`, `knowledge_base_finalize_create`, `knowledge_base_import_lens_create`, `knowledge_base_lens_retrieve`, `knowledge_base_list`, `knowledge_base_regenerate_create`, `knowledge_base_resolve_create`, `knowledge_base_retrieve`, `knowledge_base_selection_partial_update`, `knowledge_base_sync_create`, and `knowledge_base_unlink_destroy`, along with models `CreateKnowledgeBase`, `CreateKnowledgeBaseRequest`, `Draft`, `DraftRef`, `DraftStatusEnum`, `FinalizeRequest`, `KnowledgeBase`, `KnowledgeBaseStatusEnum`, `PaginatedKnowledgeBaseList`, `PatchedPatchSelectionRequest`, `PendingProposal`, `RegenerateRequest`, `RelevanceEnum`, and `ResolveRequest`.
- Added table APIs with `client.tables.list(...)`, `client.tables.describe(...)`, `client.tables.preview(...)`, `client.tables.query(...)`, `client.tables.query_result(...)`, and `client.tables.delete(...)`.
- Added the `AgentJobCancelAllResponse` model for agent job cancellation responses.

### Removed

- **Breaking.** Removed the `organization_id` parameter from `agents_jobs_references_retrieve`; update any calls to stop passing `organization_id`.

## 1.1.1

Built from roe-main release `1-1-1`.

### Added

- Added the `client.agents` API with methods to manage agents and run them: `client.agents.create(...)`, `client.agents.list(...)`, `client.agents.retrieve(...)`, `client.agents.update(...)`, `client.agents.delete(...)`, `client.agents.duplicate(...)`, `client.agents.run(...)`, `client.agents.run_many(...)`, `client.agents.run_sync(...)`, `client.agents.run_version(...)`, and `client.agents.run_version_sync(...)`.
- Added `client.agents.jobs` methods to manage agent runs and results: `client.agents.jobs.cancel(...)`, `client.agents.jobs.cancel_all(...)`, `client.agents.jobs.delete_data(...)`, `client.agents.jobs.download_reference(...)`, `client.agents.jobs.retrieve_result(...)`, `client.agents.jobs.retrieve_result_many(...)`, `client.agents.jobs.retrieve_status(...)`, and `client.agents.jobs.retrieve_status_many(...)`.
- Added the `client.agents.versions` API for agent version management with `client.agents.versions.create(...)`, `client.agents.versions.list(...)`, `client.agents.versions.retrieve(...)`, `client.agents.versions.retrieve_current(...)`, `client.agents.versions.update(...)`, and `client.agents.versions.delete(...)`.
- Added the `client.policies` API with `client.policies.create(...)`, `client.policies.list(...)`, `client.policies.retrieve(...)`, `client.policies.update(...)`, and `client.policies.delete(...)`, plus policy version methods `client.policies.versions.create(...)`, `client.policies.versions.list(...)`, and `client.policies.versions.retrieve(...)`.
- Added `client.users.me(...)` to retrieve the current user.

## 1.1.0

Built from roe-main release `1-0-83`.

### Added

- Added connection and connector raw client operations on `client`, including `connections_create`, `connections_list`, `connections_retrieve`, `connections_update`, `connections_partial_update`, `connections_destroy`, `connections_test_create`, `connections_test_credentials_create`, `connectors_retrieve`, and `connectors_retrieve_by_type`. These endpoints are supported by new models in `roe._generated.models`, including `Connection`, `ConnectionList`, `CreateConnectionRequest`, `UpdateConnectionRequest`, `PatchedUpdateConnectionRequest`, `TestConnection`, `TestConnectionCredentialsRequest`, `ConnectorListResponse`, `ConnectorMetadata`, `DuplicateConnectionResponse`, `DuplicateConnectionExisting`, `ConnectionDeleteErrorResponse`, `DependentAgentInfo`, `MessageResponse`, `User`, `ConnectorTypeEnum`, `StatusEnum`, and `ColorEnum`.
- Added table raw client operations on `client`: `tables_list`, `tables_describe_retrieve`, `tables_preview_retrieve`, `tables_query_create`, `tables_query_result_retrieve`, and `tables_destroy`. New table-related models in `roe._generated.models` include `Table`, `TableColumn`, `TableListResponse`, `TableDescribeResponse`, `TablePreviewResponse`, `TableQueryRequest`, `TableQuerySubmitResponse`, `TableQueryResultResponse`, and `TableQueryStatusEnum`.
- `agents_jobs_references_retrieve` now accepts an optional `download` query parameter, so callers can pass `download=` when retrieving a job reference.
- Added new generated models in `roe._generated.models` for agent requests and status/tag data: `AgentExecutionRequest`, `AgentJobResultManyRequest`, `AgentJobSingleStatus`, `AgentJobStatusManyRequest`, `AgentRunAsyncManyRequest`, `AgentTag`, `AgentVersionUpdateRequest`, and `PatchedAgentVersionUpdateRequest`. Also added shared error and pagination models `ApiErrorResponse`, `ErrorDetailResponse`, `PaginatedConnectionListList`, `PolicyDeleteConflict`, and `QdrantCleanupErrorResponse`.

### Changed

- **Breaking.** `AgentJobDeleteDataResponse.errors` is now required and typed as `list[...] | None` instead of an unconstrained array, so callers should handle `None` explicitly while still expecting the field to be present.
- **Breaking.** `AgentJobStatus` changed shape: `error_message` and `status` are now nullable, `timestamp` is now an optional nullable `float`, and new required fields `created_at`, `id`, and `last_updated_at` were added. Update any code that assumed `timestamp`, `error_message`, or `status` were always present and non-null.
- **Breaking.** `engine_config` and `input_definitions` on `AgentVersionCreateRequest` are no longer guaranteed to be present.
- **Breaking.** `BaseAgent.most_recent_job` is now nullable, and `BaseAgent.tags` is now a list of `AgentTag` instead of a string.
- **Breaking.** `engine_config`, `input_definitions`, and `organization_id` on `BaseAgentCreateRequest` are no longer guaranteed to be present.
- **Breaking.** `PolicyVersion.base_version_id` is now nullable.

### Removed

- **Breaking.** Removed the renamed request models `AgentExecutionRequestRequest`, `AgentJobResultManyRequestRequest`, `AgentJobStatusManyRequestRequest`, `AgentRunAsyncManyRequestRequest`, `AgentVersionUpdateRequestRequest`, and `PatchedPatchedAgentVersionUpdateRequestRequest`; update imports and type references to the corresponding `*Request` models without the duplicated suffix.
- **Breaking.** Removed `ErrorResponse` and `PaginatedAgentJobResultItemList`; update code that imported or matched these generated models to use the current response types exposed by each operation.

## 1.0.803

### Changed

- Regenerated from the latest SDK spec; no changes to the generated API surface.

## 1.0.802

Version synchronization across `roe-ai` (Python), `roe-typescript`,
and `roe-golang`. The public SDK packages now share a single 1.0.x patch counter,
driven by the SDK OpenAPI spec via the roe-main release pipeline (see
`roe-main/roe-sdk/targets.yml`).

### Added

- Generated friendly wrapper support via `openapi/wrappers.yml` and
  `scripts/generate-sdk`.
- `client.discovery.list_agent_engine_types()`.
- `client.discovery.list_supported_models(capability=...)`.
- `client.tables.upload(...)`.
- Public SDK wrappers now route common 404 cases through
  `RoeAPIException` instead of generated error-body parsers.
- `client.agents.run(..., idempotency_key=...)` and
  `client.agents.run_version(..., idempotency_key=...)`.

## 1.0.0

**Generated-client migration.** The hand-written API surface
(`AgentsAPI`, `PoliciesAPI`, and friends) is now a thin facade over the
generated `roe._generated` raw OpenAPI client. The custom HTTP layer that
duplicated retry, multipart, and error-mapping behavior has been deleted.
Codegen is driven by `roe-ai/roe-main` PR #3111.

### Removed (breaking)

- `RoeHTTPClient` and `RoeClient.http_client`. The shared `httpx.Client`
  is now an internal `RoeClient._httpx_client`.
- Hand-written response data classes — `Agent`, `BaseAgent`,
  `AgentVersion`, `AgentInputDefinition`, `Policy`, `PolicyVersion`,
  `AgentDatum`, `AgentJobResult`, `AgentJobStatus`, `Reference`,
  `JobDataDeleteResponse`, `PaginatedResponse[T]`, `UserInfo`,
  `ErrorResponse`. Use the equivalents under
  `roe._generated.models` going forward.
- `roe.models.{agent,policy,responses,user}` modules.
- `http_client` constructor parameter on internal `AgentsAPI` /
  `PoliciesAPI`.

### Changed (breaking)

- `Job.wait()` now returns the generated `AgentJobResultResponse`.
  Field names line up 1:1 with the previous hand-written model in most
  cases; failed jobs whose result-fetch fails get a synthesized response
  with terminal `status` and `error_message` stuffed into
  `additional_properties`.
- `JobBatch.wait()` now returns `list[AgentJobResultItem | None]`.
- `client.policies.update()` and `client.agents.update()` (and the
  version variants) now use **PATCH** instead of PUT — the generated
  PUT requires a fully-populated request body, while these wrappers
  accept partial updates.
- `client.policies.versions.list()` is paginated (was a flat list).
- `client.raw` (the generated `AuthenticatedClient`) now inherits
  the same retry budget and typed exception classes that SDK calls
  use, since both share the underlying `httpx.Client` with
  `RoeRetryTransport`.

### Kept

- `RoeClient`, `RoeConfig`, `RoeAuth`.
- `client.agents.*`, `client.policies.*` method names + signatures.
- `Job`, `JobBatch`, `JobStatus`.
- `FileUpload`.
- All six exception classes (`RoeAPIException`, `BadRequestError`,
  `AuthenticationError`, `InsufficientCreditsError`, `ForbiddenError`,
  `NotFoundError`, `ServerError`) and their constructor signatures.
- `client.raw` / `roe._generated`.

### Migration

```python
# Before
from roe.models.agent import BaseAgent
from roe.models.responses import JobStatus, AgentJobResult, Reference

# After
from roe._generated.models import BaseAgent
from roe import JobStatus  # JobStatus enum re-exported at the top level
from roe._generated.models import AgentJobResultResponse, Reference
```

```python
# `update` is now PATCH-shaped — pass only the fields you want to change.
client.policies.update("policy-uuid", name="Renamed Policy")  # unchanged signature
```

```python
# `client.policies.versions.list()` is now paginated:
result = client.policies.versions.list("policy-uuid")
for version in result.results:
    print(version.id, version.version_name)
```
