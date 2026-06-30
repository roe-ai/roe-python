# Python SDK Examples

<!-- AUTO-GENERATED. Do not edit by hand. -->

## Examples

Copy-ready calls for every SDK operation. Required and optional inputs are shown inline in each code block.

### Agents

#### `agents_list`

List agents or create a new agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.list(
    page=1,  # optional
    page_size=1,  # optional
)
```

#### `agents_create`

Create a new base agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.create(
    name="name",  # required
    engine_class_id="engine_class_id",  # required
    input_definitions=[{"key": "text", "data_type": "text/plain"}],  # optional
    engine_config={"model": "gpt-5.5-2026-04-23"},  # optional
    version_name="version_name",  # optional
    description="description",  # optional
)
```

#### `agents_jobs_results_create`

Get results for multiple agent jobs

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.retrieve_result_many(
    job_ids=["job_id"],
)
```

#### `agents_jobs_statuses_create`

Get status for multiple agent jobs

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.retrieve_status_many(
    job_ids=["job_id"],
)
```

#### `agents_jobs_artifacts_result_retrieve`

Get tool result artifact (result only)

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.retrieve_artifact(
    job_id="job_id",  # required
    artifact_key="artifact_key",  # required
)
```

#### `agents_jobs_references_retrieve`

Serve a reference file associated with an agent job.

```python
from roe import RoeClient

client = RoeClient()

content = client.agents.jobs.download_reference(
    job_id="job_id",
    resource_id="resource_id",
    as_attachment=False,
)
```

#### `agents_jobs_result_retrieve`

Get agent job result data.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.retrieve_result(
    job_id="job_id",  # required
)
```

#### `agents_jobs_cancel_create`

Cancel an agent job

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.cancel(
    job_id="job_id",  # required
)
```

#### `agents_jobs_delete_data_create`

Delete agent job data

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.delete_data(
    job_id="job_id",  # required
)
```

#### `agents_jobs_status_retrieve`

Get agent job status.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.retrieve_status(
    job_id="job_id",  # required
)
```

#### `agents_run`

Run agent synchronously

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.run_sync(
    agent_id="agent_id",
    text="text",
    metadata={},
)
```

#### `agents_run_async_create`

Run agent asynchronously.

```python
from roe import RoeClient

client = RoeClient()

job = client.agents.run(
    agent_id="agent_id",
    timeout_seconds=300,
    text="text",
    metadata={},
)
```

#### `agents_run_async_many`

Run agent asynchronously with multiple inputs

```python
from roe import RoeClient

client = RoeClient()

batch = client.agents.run_many(
    agent_id="agent_id",
    batch_inputs=[{"text": "text"}],
    timeout_seconds=300,
    metadata={},
)
```

#### `agents_run_version`

Run agent version synchronously

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.run_version_sync(
    agent_id="agent_id",
    version_id="version_id",
    text="text",
    metadata={},
)
```

#### `agents_run_versions_async_create`

Run agent version asynchronously.

```python
from roe import RoeClient

client = RoeClient()

job = client.agents.run_version(
    agent_id="agent_id",
    version_id="version_id",
    timeout_seconds=300,
    text="text",
    metadata={},
)
```

#### `agents_destroy`

Delete a base agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.delete(
    agent_id="agent_id",  # required
)
```

#### `agents_retrieve`

Retrieve an agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.retrieve(
    agent_id="agent_id",  # required
)
```

#### `agents_partial_update`

Partially update an agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.update(
    agent_id="agent_id",  # required
    name="name",  # optional
    disable_cache=True,  # optional
    cache_failed_jobs=True,  # optional
)
```

#### `agents_update`

Update a base agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.replace(
    agent_id="agent_id",  # required
    name="name",  # optional
    disable_cache=True,  # optional
    cache_failed_jobs=True,  # optional
)
```

#### `agents_duplicate_create`

Duplicate an agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.duplicate(
    agent_id="agent_id",  # required
)
```

#### `agents_jobs_cancel_all_create`

Cancel all running agent jobs (:cancelAll)

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.jobs.cancel_all(
    agent_id="agent_id",  # required
)
```

#### `agents_versions_list`

List agent versions.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.versions.list(
    agent_id="agent_id",  # required
)
```

#### `agents_versions_create`

Create a new agent version.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.versions.create(
    agent_id="agent_id",  # required
    input_definitions=[{"key": "text", "data_type": "text/plain"}],  # optional
    engine_config={"model": "gpt-5.5-2026-04-23"},  # optional
    version_name="version_name",  # optional
    description="description",  # optional
)
```

#### `agents_versions_current_retrieve`

Retrieve the current version of an agent.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.versions.retrieve_current(
    agent_id="agent_id",  # required
)
```

#### `agents_versions_destroy`

Delete an agent version.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.versions.delete(
    agent_id="agent_id",  # required
    version_id="version_id",  # required
)
```

#### `agents_versions_retrieve`

Retrieve an agent version.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.versions.retrieve(
    agent_id="agent_id",  # required
    version_id="version_id",  # required
    get_supports_eval=True,  # optional
)
```

#### `agents_versions_partial_update`

Partially update an agent version.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.versions.update(
    agent_id="agent_id",  # required
    version_id="version_id",  # required
    version_name="version_name",  # optional
    description="description",  # optional
)
```

#### `agents_versions_update`

Update an agent version.

```python
from roe import RoeClient

client = RoeClient()

result = client.agents.versions.replace(
    agent_id="agent_id",  # required
    version_id="version_id",  # required
    version_name="version_name",  # optional
    description="description",  # optional
)
```

### Connections

#### `connections_list`

List/create connections.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.list(
    connector_type="connector_type",  # optional
    search="search",  # optional
    page=1,  # optional
    page_size=1,  # optional
)
```

#### `connections_create`

List/create connections.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.create(
    connector_type="connector_type",  # required
    name="name",  # required
    config={},  # required
    description="description",  # optional
    auth_config={},  # optional
)
```

#### `connections_test_credentials_create`

Test credentials without storing them.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.test_credentials(
    connector_type="connector_type",  # required
    config={},  # required
    auth_config={},  # optional
)
```

#### `connections_destroy`

Manage connection.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.delete(
    connection_id="connection_id",  # required
)
```

#### `connections_retrieve`

Manage connection.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.retrieve(
    connection_id="connection_id",  # required
)
```

#### `connections_partial_update`

Manage connection.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.update(
    connection_id="connection_id",  # required
    name="name",  # optional
    description="description",  # optional
    config={},  # optional
    auth_config={},  # optional
)
```

#### `connections_update`

Manage connection.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.replace(
    connection_id="connection_id",  # required
    name="name",  # optional
    description="description",  # optional
    config={},  # optional
    auth_config={},  # optional
)
```

#### `connections_test_create`

Test connection.

```python
from roe import RoeClient

client = RoeClient()

result = client.connections.test(
    connection_id="connection_id",  # required
)
```

### Connectors

#### `connectors_retrieve`

List all connector types.

```python
from roe import RoeClient

client = RoeClient()

result = client.connectors.list()
```

#### `connectors_retrieve_by_type`

Get connector details.

```python
from roe import RoeClient

client = RoeClient()

result = client.connectors.retrieve(
    connector_type="connector_type",  # required
)
```

### Discovery

#### `discovery_supported_models_list`

List supported model IDs

```python
from roe import RoeClient

client = RoeClient()

result = client.discovery.list_supported_models(
    capability="capability",  # optional
)
```

#### `discovery_agent_engine_types_list`

List supported agent engine types

```python
from roe import RoeClient

client = RoeClient()

result = client.discovery.list_agent_engine_types()
```

### Knowledge Base

#### `knowledge_base_list`

List all KBs for the org, or start a new draft.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.list()
```

#### `knowledge_base_create`

List all KBs for the org, or start a new draft.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.create()
```

#### `knowledge_base_catalog_retrieve`

Names-only typology+tactic catalog.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.catalog()
```

#### `knowledge_base_import_lens_create`

Import a finalized Atlas lens into roe-main by its atlas_lens_id.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.import_lens()
```

#### `knowledge_base_lens_retrieve`

Fetch a lens directly from Atlas by its atlas_lens_id and return the
names-only projection.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.lens_by_atlas_id()
```

#### `knowledge_base_destroy`

Get or delete a single KB.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.delete()
```

#### `knowledge_base_retrieve`

Get or delete a single KB.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.retrieve()
```

#### `knowledge_base_draft_retrieve`

Poll the atlas draft.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.poll_draft()
```

#### `knowledge_base_finalize_create`

Commit the agreed selection into a lens and mark the KB active.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.finalize()
```

#### `knowledge_base_regenerate_create`

Kick off another async generation round with feedback.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.regenerate()
```

#### `knowledge_base_resolve_create`

Approve or decline a pending regeneration proposal.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.resolve()
```

#### `knowledge_base_selection_partial_update`

Persist hand-edits to the working selection (typology + tactic opt-in/out).

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.patch_selection()
```

#### `knowledge_base_sync_create`

Standalone best-effort lens sync (display mode).

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.sync()
```

#### `knowledge_base_unlink_destroy`

Unlink a knowledge base: remove the local KnowledgeBase row only, leaving
the Atlas lens (and any in-progress draft) untouched.

```python
from roe import RoeClient

client = RoeClient()

result = client.knowledge_base.unlink()
```

### Policies

#### `policies_list`

List all policies and create a new policy.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.list(
    page=1,  # optional
    page_size=1,  # optional
)
```

#### `policies_create`

List all policies and create a new policy.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.create(
    name="name",  # required
    content={},  # required
    description="description",  # optional
    version_name="version_name",  # optional
)
```

#### `policies_destroy`

Retrieve, update, or delete a single policy by ID.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.delete(
    policy_id="policy_id",  # required
)
```

#### `policies_retrieve`

Retrieve, update, or delete a single policy by ID.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.retrieve(
    policy_id="policy_id",  # required
)
```

#### `policies_partial_update`

Retrieve, update, or delete a single policy by ID.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.update(
    policy_id="policy_id",  # required
    name="name",  # optional
    description="description",  # optional
)
```

#### `policies_update`

Retrieve, update, or delete a single policy by ID.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.replace(
    policy_id="policy_id",  # required
    name="name",  # required
    description="description",  # optional
)
```

#### `policies_versions_list`

Create a new policy version or list all versions of a specific policy.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.versions.list(
    policy_id="policy_id",
    page=1,
    page_size=10,
)
```

#### `policies_versions_create`

Create a new policy version or list all versions of a specific policy.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.versions.create(
    policy_id="policy_id",
    content={},
    version_name="version_name",
    base_version_id="base_version_id",
)
```

#### `policies_versions_retrieve`

Get a specific policy version by policy_id and version_id.

```python
from roe import RoeClient

client = RoeClient()

result = client.policies.versions.retrieve(
    policy_id="policy_id",
    version_id="version_id",
)
```

### Tables

#### `tables_list`

List Roe tables

```python
from roe import RoeClient

client = RoeClient()

result = client.tables.list()
```

#### `tables_query_create`

Run a read-only Roe table query

```python
from roe import RoeClient

client = RoeClient()

result = client.tables.query(
    sql="sql",  # required
    limit=1,  # optional
)
```

#### `tables_query_result_retrieve`

Get a Roe table query result

```python
from roe import RoeClient

client = RoeClient()

result = client.tables.query_result(
    table_query_id="table_query_id",  # required
)
```

#### `tables_destroy`

Delete a Roe table

```python
from roe import RoeClient

client = RoeClient()

result = client.tables.delete(
    table_name="table_name",  # required
)
```

#### `tables_describe_retrieve`

Describe a Roe table

```python
from roe import RoeClient

client = RoeClient()

result = client.tables.describe(
    table_name="table_name",  # required
)
```

#### `tables_preview_retrieve`

Preview a Roe table

```python
from roe import RoeClient

client = RoeClient()

result = client.tables.preview(
    table_name="table_name",  # required
    limit=1,  # optional
)
```

#### `upload_table`

Upload a CSV as a Roe table

```python
from roe import RoeClient

client = RoeClient()

result = client.tables.upload(
    table_name="table_name",
    file="file.csv",
    with_headers=True,
)
```

### Users

#### `users_current_user_retrieve`

Get the current user

```python
from roe import RoeClient

client = RoeClient()

result = client.users.me()
```

## Use Cases

These workflows assume `ROE_API_KEY` and `ROE_ORGANIZATION_ID` are set.
The first example provisions a policy and an agent from scratch; the later two
reuse an existing agent id so they stay focused on the run-and-fetch calls.

### Create a policy and run a policy-aware agent

```python
from roe import RoeClient

client = RoeClient()

policy = client.policies.create(
    name="AML Investigation Policy",
    content={
        "guidelines": {
            "categories": [
                {
                    "title": "Transaction Patterns",
                    "rules": [
                        {
                            "title": "Structuring below reporting thresholds",
                            "flag": "RED_FLAG",
                            "description": "Deposits just under CTR thresholds in a short window.",
                        }
                    ],
                }
            ]
        },
        "dispositions": {
            "classifications": [
                {"name": "SAR", "description": "File a Suspicious Activity Report."},
                {"name": "DISMISS", "description": "Close as non-suspicious."},
            ]
        },
    },
)

agent = client.agents.create(
    name="AML Investigation Agent",
    engine_class_id="AMLInvestigationEngine",
    input_definitions=[
        {
            "key": "alert_data",
            "data_type": "text/plain",
            "description": "Alert to investigate.",
        }
    ],
    engine_config={
        "policy_version_id": str(policy.current_version_id),
        "alert_data": "${alert_data}",
    },
)

job = client.agents.run(
    agent_id=str(agent.id),
    timeout_seconds=300,
    alert_data="Customer made 9 cash deposits of $9,500 over three days.",
)
result = job.wait(interval=5.0, timeout=300)

for output in result.outputs:
    print(f"{output.key}: {output.value}")
```

### Run an agent and download a saved reference

```python
import json
import os
from pathlib import Path

from roe import RoeClient

client = RoeClient()
agent_id = os.environ["ROE_URL_AGENT_ID"]

job = client.agents.run(
    agent_id=agent_id,
    timeout_seconds=300,
    url="https://www.roe-ai.com/",
    metadata={"use_case": "website-scan"},
)
result = job.wait(interval=5.0, timeout=300)

for output in result.outputs:
    try:
        payload = json.loads(output.value)
    except json.JSONDecodeError:
        continue
    for ref in payload.get("references", []):
        resource_id = ref.get("resource_id")
        if resource_id:
            content = client.agents.jobs.download_reference(job.id, resource_id)
            Path(f"{resource_id}.bin").write_bytes(content)
```

### Run a batch of inputs

```python
import os

from roe import RoeClient

client = RoeClient()
agent_id = os.environ["ROE_TEXT_AGENT_ID"]

batch = client.agents.run_many(
    agent_id=agent_id,
    batch_inputs=[
        {"text": "Summarize the customer complaint."},
        {"text": "Extract the requested follow-up action."},
    ],
    timeout_seconds=300,
)
results = batch.wait(interval=5.0, timeout=300)

for job_result in results:
    if job_result is None:
        continue
    for output in job_result.result or []:
        print(f"{output.key}: {output.value}")
```
