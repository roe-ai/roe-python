# Changelog

## 2.0.0

Version synchronization across `roe-ai` (Python), `roe-typescript`,
and `roe-golang`. The public SDK packages now share a single patch counter,
driven by the SDK OpenAPI spec via the roe-main release pipeline (see
`roe-main/roe-sdk/targets.yml`).

`roe-mcp` is a private consumer of the published Python SDK, not a public
SDK release target.

### Added

- Generated friendly wrapper support via `openapi/wrappers.yml` and
  `scripts/generate-sdk`.
- `client.discovery.list_agent_engine_types()`.
- `client.discovery.list_supported_models(capability=...)`.
- `client.tables.upload(...)`.

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
