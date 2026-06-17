# Python SDK Examples

<!-- AUTO-GENERATED. Do not edit by hand. -->

## Examples

Copy-ready calls for every SDK operation. Required and optional inputs are shown inline in each code block.

### Agents

#### `agents_list`

List agents or create a new agent.

```python
from roe._generated.api.agents import agents_list
from uuid import UUID

result = agents_list.sync(
    client=client.raw,
    engine_class_id="engine_class_id",  # optional query
    exclude_engine_class_id="exclude_engine_class_id",  # optional query
    include_job_stats=True,  # optional query
    ordering="ordering",  # optional query
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # required query
    page=1,  # optional query
    page_size=1,  # optional query
    search="search",  # optional query
    tags=["value"],  # optional query
)
```

#### `agents_create`

Create a new base agent.

```python
from roe._generated.api.agents import agents_create
from uuid import UUID
from roe._generated.models.base_agent_create_request import BaseAgentCreateRequest

result = agents_create.sync(
    client=client.raw,
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=BaseAgentCreateRequest(
        name="name",  # required
        engine_class_id="engine_class_id",  # required
        organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional
        version_name="version_name",  # optional
        description="description",  # optional
        input_definitions="input_definitions",  # optional
        engine_config="engine_config",  # optional
    ),  # required body
)
```

#### `agents_jobs_results_create`

Get results for multiple agent jobs

```python
from roe._generated.api.agents import agents_jobs_results_create
from uuid import UUID
from roe._generated.models.agent_job_result_many_request import AgentJobResultManyRequest

result = agents_jobs_results_create.sync(
    client=client.raw,
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentJobResultManyRequest(
        job_ids=["value"],  # required
    ),  # required body
)
```

#### `agents_jobs_statuses_create`

Get status for multiple agent jobs

```python
from roe._generated.api.agents import agents_jobs_statuses_create
from uuid import UUID
from roe._generated.models.agent_job_status_many_request import AgentJobStatusManyRequest

result = agents_jobs_statuses_create.sync(
    client=client.raw,
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentJobStatusManyRequest(
        job_ids=["value"],  # required
    ),  # required body
)
```

#### `agents_jobs_references_retrieve`

Serve a reference file associated with an agent job.

```python
from roe._generated.api.agents import agents_jobs_references_retrieve
from uuid import UUID

result = agents_jobs_references_retrieve.sync(
    client=client.raw,
    agent_job_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    download=True,  # optional query
    resource_id="resource_id",  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_jobs_result_retrieve`

Get agent job result data.

```python
from roe._generated.api.agents import agents_jobs_result_retrieve
from uuid import UUID

result = agents_jobs_result_retrieve.sync(
    client=client.raw,
    agent_job_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_jobs_cancel_create`

Cancel an agent job

```python
from roe._generated.api.agents import agents_jobs_cancel_create
from uuid import UUID

result = agents_jobs_cancel_create.sync(
    client=client.raw,
    job_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_jobs_delete_data_create`

Delete agent job data

```python
from roe._generated.api.agents import agents_jobs_delete_data_create
from uuid import UUID

result = agents_jobs_delete_data_create.sync(
    client=client.raw,
    job_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_jobs_status_retrieve`

Get agent job status.

```python
from roe._generated.api.agents import agents_jobs_status_retrieve
from uuid import UUID

result = agents_jobs_status_retrieve.sync(
    client=client.raw,
    job_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_run`

Run agent synchronously

```python
from roe._generated.api.agents import agents_run
from uuid import UUID
from roe._generated.models.agent_execution_request import AgentExecutionRequest

result = agents_run.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentExecutionRequest(
        metadata={},  # optional
    ),  # optional body
)
```

#### `agents_run_async_create`

Run agent asynchronously.

```python
from roe._generated.api.agents import agents_run_async_create
from uuid import UUID
from roe._generated.models.agent_execution_request import AgentExecutionRequest

result = agents_run_async_create.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentExecutionRequest(
        metadata={},  # optional
    ),  # optional body
)
```

#### `agents_run_async_many`

Run agent asynchronously with multiple inputs

```python
from roe._generated.api.agents import agents_run_async_many
from uuid import UUID
from roe._generated.models.agent_run_async_many_request import AgentRunAsyncManyRequest

result = agents_run_async_many.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentRunAsyncManyRequest(
        inputs=["value"],  # required
    ),  # required body
)
```

#### `agents_run_version`

Run agent version synchronously

```python
from roe._generated.api.agents import agents_run_version
from uuid import UUID
from roe._generated.models.agent_execution_request import AgentExecutionRequest

result = agents_run_version.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    agent_version_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentExecutionRequest(
        metadata={},  # optional
    ),  # optional body
)
```

#### `agents_run_versions_async_create`

Run agent version asynchronously.

```python
from roe._generated.api.agents import agents_run_versions_async_create
from uuid import UUID
from roe._generated.models.agent_execution_request import AgentExecutionRequest

result = agents_run_versions_async_create.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    agent_version_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentExecutionRequest(
        metadata={},  # optional
    ),  # optional body
)
```

#### `agents_destroy`

Delete a base agent.

```python
from roe._generated.api.agents import agents_destroy
from uuid import UUID

result = agents_destroy.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_retrieve`

Retrieve an agent.

```python
from roe._generated.api.agents import agents_retrieve
from uuid import UUID

result = agents_retrieve.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_partial_update`

Partially update an agent.

```python
from roe._generated.api.agents import agents_partial_update
from uuid import UUID
from roe._generated.models.patched_base_agent_update_request import PatchedBaseAgentUpdateRequest

result = agents_partial_update.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=PatchedBaseAgentUpdateRequest(
        name="name",  # optional
        disable_cache=True,  # optional
        cache_failed_jobs=True,  # optional
    ),  # optional body
)
```

#### `agents_update`

Update a base agent.

```python
from roe._generated.api.agents import agents_update
from uuid import UUID
from roe._generated.models.base_agent_update_request import BaseAgentUpdateRequest

result = agents_update.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=BaseAgentUpdateRequest(
        name="name",  # optional
        disable_cache=True,  # optional
        cache_failed_jobs=True,  # optional
    ),  # optional body
)
```

#### `agents_duplicate_create`

Duplicate an agent.

```python
from roe._generated.api.agents import agents_duplicate_create
from uuid import UUID

result = agents_duplicate_create.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_jobs_cancel_all_create`

Cancel all agent jobs

```python
from roe._generated.api.agents import agents_jobs_cancel_all_create
from uuid import UUID

result = agents_jobs_cancel_all_create.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_versions_list`

List agent versions.

```python
from roe._generated.api.agents import agents_versions_list
from uuid import UUID

result = agents_versions_list.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_versions_create`

Create a new agent version.

```python
from roe._generated.api.agents import agents_versions_create
from uuid import UUID
from roe._generated.models.agent_version_create_request import AgentVersionCreateRequest

result = agents_versions_create.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentVersionCreateRequest(
        version_name="version_name",  # optional
        description="description",  # optional
        input_definitions="input_definitions",  # optional
        engine_config="engine_config",  # optional
    ),  # optional body
)
```

#### `agents_versions_current_retrieve`

Retrieve the current version of an agent.

```python
from roe._generated.api.agents import agents_versions_current_retrieve
from uuid import UUID

result = agents_versions_current_retrieve.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    get_supports_eval=True,  # optional query
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_versions_destroy`

Delete an agent version.

```python
from roe._generated.api.agents import agents_versions_destroy
from uuid import UUID

result = agents_versions_destroy.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    agent_version_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_versions_retrieve`

Retrieve an agent version.

```python
from roe._generated.api.agents import agents_versions_retrieve
from uuid import UUID

result = agents_versions_retrieve.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    agent_version_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    get_supports_eval=True,  # optional query
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `agents_versions_partial_update`

Partially update an agent version.

```python
from roe._generated.api.agents import agents_versions_partial_update
from uuid import UUID
from roe._generated.models.patched_agent_version_update_request import PatchedAgentVersionUpdateRequest

result = agents_versions_partial_update.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    agent_version_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=PatchedAgentVersionUpdateRequest(
        version_name="version_name",  # optional
        description="description",  # optional
    ),  # optional body
)
```

#### `agents_versions_update`

Update an agent version.

```python
from roe._generated.api.agents import agents_versions_update
from uuid import UUID
from roe._generated.models.agent_version_update_request import AgentVersionUpdateRequest

result = agents_versions_update.sync(
    client=client.raw,
    agent_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    agent_version_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=AgentVersionUpdateRequest(
        version_name="version_name",  # optional
        description="description",  # optional
    ),  # optional body
)
```

### Connections

#### `connections_list`

List/create connections.

```python
from roe._generated.api.connections import connections_list
from uuid import UUID

result = connections_list.sync(
    client=client.raw,
    connector_type="connector_type",  # optional query
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    page=1,  # optional query
    page_size=1,  # optional query
    search="search",  # optional query
)
```

#### `connections_create`

List/create connections.

```python
from roe._generated.api.connections import connections_create
from uuid import UUID
from roe._generated.models.create_connection_request import CreateConnectionRequest

result = connections_create.sync(
    client=client.raw,
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=CreateConnectionRequest(
        connector_type="connector_type",  # required
        name="name",  # required
        description="description",  # optional
        config={},  # required
        auth_config={},  # optional
        organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional
    ),  # required body
)
```

#### `connections_test_credentials_create`

Test credentials without storing them.

```python
from roe._generated.api.connections import connections_test_credentials_create
from roe._generated.models.test_connection_credentials_request import TestConnectionCredentialsRequest

result = connections_test_credentials_create.sync(
    client=client.raw,
    body=TestConnectionCredentialsRequest(
        connector_type="connector_type",  # required
        config={},  # required
        auth_config={},  # optional
    ),  # required body
)
```

#### `connections_destroy`

Manage connection.

```python
from roe._generated.api.connections import connections_destroy
from uuid import UUID

result = connections_destroy.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `connections_retrieve`

Manage connection.

```python
from roe._generated.api.connections import connections_retrieve
from uuid import UUID

result = connections_retrieve.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `connections_partial_update`

Manage connection.

```python
from roe._generated.api.connections import connections_partial_update
from uuid import UUID
from roe._generated.models.patched_update_connection_request import PatchedUpdateConnectionRequest

result = connections_partial_update.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=PatchedUpdateConnectionRequest(
        name="name",  # optional
        description="description",  # optional
        config={},  # optional
        auth_config={},  # optional
    ),  # optional body
)
```

#### `connections_update`

Manage connection.

```python
from roe._generated.api.connections import connections_update
from uuid import UUID
from roe._generated.models.update_connection_request import UpdateConnectionRequest

result = connections_update.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=UpdateConnectionRequest(
        name="name",  # optional
        description="description",  # optional
        config={},  # optional
        auth_config={},  # optional
    ),  # optional body
)
```

#### `connections_test_create`

Test connection.

```python
from roe._generated.api.connections import connections_test_create
from uuid import UUID

result = connections_test_create.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

### Connectors

#### `connectors_retrieve`

List all connector types.

```python
from roe._generated.api.connectors import connectors_retrieve

result = connectors_retrieve.sync(
    client=client.raw,
)
```

#### `connectors_retrieve_by_type`

Get connector details.

```python
from roe._generated.api.connectors import connectors_retrieve_by_type

result = connectors_retrieve_by_type.sync(
    client=client.raw,
    connector_type="connector_type",  # required path
)
```

### Discovery

#### `discovery_supported_models_list`

List supported model IDs

```python
from roe._generated.api.discovery import discovery_supported_models_list

result = discovery_supported_models_list.sync(
    client=client.raw,
    capability="capability",  # optional query
)
```

#### `discovery_agent_engine_types_list`

List supported agent engine types

```python
from roe._generated.api.discovery import discovery_agent_engine_types_list

result = discovery_agent_engine_types_list.sync(
    client=client.raw,
)
```

### Policies

#### `policies_list`

List all policies and create a new policy.

```python
from roe._generated.api.policies import policies_list
from uuid import UUID

result = policies_list.sync(
    client=client.raw,
    ordering="ordering",  # optional query
    page=1,  # optional query
    page_size=1,  # optional query
    search="search",  # optional query
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `policies_create`

List all policies and create a new policy.

```python
from roe._generated.api.policies import policies_create
from uuid import UUID
from roe._generated.models.create_policy_request import CreatePolicyRequest

result = policies_create.sync(
    client=client.raw,
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=CreatePolicyRequest(
        name="name",  # required
        description="description",  # optional
        content="content",  # required
        version_name="version_name",  # optional
    ),  # required body
)
```

#### `policies_destroy`

Retrieve, update, or delete a single policy by ID.

```python
from roe._generated.api.policies import policies_destroy
from uuid import UUID

result = policies_destroy.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `policies_retrieve`

Retrieve, update, or delete a single policy by ID.

```python
from roe._generated.api.policies import policies_retrieve
from uuid import UUID

result = policies_retrieve.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `policies_partial_update`

Retrieve, update, or delete a single policy by ID.

```python
from roe._generated.api.policies import policies_partial_update
from uuid import UUID
from roe._generated.models.patched_update_policy_request import PatchedUpdatePolicyRequest

result = policies_partial_update.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=PatchedUpdatePolicyRequest(
        name="name",  # optional
        description="description",  # optional
    ),  # optional body
)
```

#### `policies_update`

Retrieve, update, or delete a single policy by ID.

```python
from roe._generated.api.policies import policies_update
from uuid import UUID
from roe._generated.models.update_policy_request import UpdatePolicyRequest

result = policies_update.sync(
    client=client.raw,
    id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=UpdatePolicyRequest(
        name="name",  # required
        description="description",  # optional
    ),  # required body
)
```

#### `policies_versions_list`

Create a new policy version or list all versions of a specific policy.

```python
from roe._generated.api.policies import policies_versions_list
from uuid import UUID

result = policies_versions_list.sync(
    client=client.raw,
    page=1,  # optional query
    page_size=1,  # optional query
    policy_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

#### `policies_versions_create`

Create a new policy version or list all versions of a specific policy.

```python
from roe._generated.api.policies import policies_versions_create
from uuid import UUID
from roe._generated.models.create_policy_version_request import CreatePolicyVersionRequest

result = policies_versions_create.sync(
    client=client.raw,
    policy_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
    body=CreatePolicyVersionRequest(
        version_name="version_name",  # optional
        content="content",  # required
        base_version_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional
    ),  # required body
)
```

#### `policies_versions_retrieve`

Get a specific policy version by policy_id and version_id.

```python
from roe._generated.api.policies import policies_versions_retrieve
from uuid import UUID

result = policies_versions_retrieve.sync(
    client=client.raw,
    policy_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    version_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
    organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional query
)
```

### Tables

#### `tables_list`

List Roe tables

```python
from roe._generated.api.tables import tables_list

result = tables_list.sync(
    client=client.raw,
)
```

#### `tables_query_create`

Run a read-only Roe table query

```python
from roe._generated.api.tables import tables_query_create
from roe._generated.models.table_query_request import TableQueryRequest

result = tables_query_create.sync(
    client=client.raw,
    body=TableQueryRequest(
        sql="sql",  # required
        limit=1,  # optional
    ),  # required body
)
```

#### `tables_query_result_retrieve`

Get a Roe table query result

```python
from roe._generated.api.tables import tables_query_result_retrieve
from uuid import UUID

result = tables_query_result_retrieve.sync(
    client=client.raw,
    table_query_id=UUID("00000000-0000-0000-0000-000000000000"),  # required path
)
```

#### `tables_destroy`

Delete a Roe table

```python
from roe._generated.api.tables import tables_destroy

result = tables_destroy.sync(
    client=client.raw,
    table_name="table_name",  # required path
)
```

#### `tables_describe_retrieve`

Describe a Roe table

```python
from roe._generated.api.tables import tables_describe_retrieve

result = tables_describe_retrieve.sync(
    client=client.raw,
    table_name="table_name",  # required path
)
```

#### `tables_preview_retrieve`

Preview a Roe table

```python
from roe._generated.api.tables import tables_preview_retrieve

result = tables_preview_retrieve.sync(
    client=client.raw,
    limit=1,  # optional query
    table_name="table_name",  # required path
)
```

#### `upload_table`

Upload a CSV as a Roe table

```python
from roe._generated.api.tables import upload_table
from uuid import UUID
from roe._generated.models.table_upload_request import TableUploadRequest
from roe._generated.types import File

result = upload_table.sync(
    client=client.raw,
    body=TableUploadRequest(
        table_name="table_name",  # required
        file=File(payload=open("file.csv", "rb"), file_name="file.csv", mime_type="text/csv"),  # required
        with_headers=True,  # optional
        organization_id=UUID("00000000-0000-0000-0000-000000000000"),  # optional
    ),  # required body
)
```

### Users

#### `users_current_user_retrieve`

Get the current user

```python
from roe._generated.api.users import users_current_user_retrieve

result = users_current_user_retrieve.sync(
    client=client.raw,
)
```

## Use Cases

These workflows assume `ROE_API_KEY` and `ROE_ORGANIZATION_ID` are set.

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
