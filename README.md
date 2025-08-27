# Roe AI Python SDK

A Python SDK for interacting with the Roe AI API.

## Installation

```bash
pip install roe-ai
```

## Quick Start

### 1. Set up authentication

Set your API credentials as environment variables:

```bash
export ROE_API_KEY="your-api-key-here"
export ROE_ORGANIZATION_ID="your-organization-uuid-here"
```

Or pass them directly to the client:

```python
from roe import RoeClient

client = RoeClient(
    api_key="your-api-key",
    organization_id="your-organization-uuid"
)
```

### 2. List your base agents

```python
# List all base agents in your organization
agents = client.agents.list_base_agents()

print(f"Found {agents.count} base agents:")
for agent in agents.results:
    print(f"- {agent.name} (ID: {agent.id})")
```

### 3. Run an agent

```python
# Run an agent with dynamic inputs
result = client.agents.run(
    agent_id="your-agent-uuid",
    # Dynamic inputs based on your agent's configuration
    document="path/to/file.pdf",  # File path - auto-uploaded
    prompt="Analyze this document",
    temperature=0.7,
)

# Process results
for output in result:
    print(f"{output.key}: {output.value}")
```

## File Handling

The SDK provides multiple ways to handle file inputs:

### 1. File Paths (Auto-upload)

```python
result = client.agents.run(
    agent_id="agent-uuid",
    document="path/to/file.pdf",  # Automatically uploaded
    prompt="Process this file"
)
```

### 2. File Objects

```python
with open("document.pdf", "rb") as f:
    result = client.agents.run(
        agent_id="agent-uuid",
        document=f,  # File object
        prompt="Process this file"
    )
```

### 3. Roe File IDs

```python
result = client.agents.run(
    agent_id="agent-uuid",
    document="3c90c3cc-0d44-4b50-8888-8dd25736052a",  # Existing file UUID
    prompt="Process this file"
)
```

### 4. Explicit FileUpload

```python
from roe import FileUpload

file_upload = FileUpload(
    path="document.pdf",
    filename="custom_name.pdf",
    mime_type="application/pdf"
)

result = client.agents.run(
    agent_id="agent-uuid",
    document=file_upload,
    prompt="Process this file"
)
```

## Advanced Usage

### Pagination

```python
# Iterate through all base agents
page = 1
while True:
    response = client.agents.list_base_agents(page=page, page_size=10)

    for agent in response.results:
        print(f"Processing: {agent.name}")

    if not response.has_next:
        break

    page += 1
```

### Agent Object Methods

```python
# Get a specific base agent and run it
agent = client.agents.get_base_agent("base-agent-uuid")
print(f"Base Agent: {agent.name}")

# Run using the agent object (uses current version)
result = agent.run(
    prompt="Hello from the agent object!",
    document="file.pdf"
)

# Get current version with input definitions
current_version = agent.get_current_version()
if current_version:
    print(f"Current version: {current_version.version_name}")
    print(f"Input definitions: {current_version.input_definitions}")
```

### Agent Versions

```python
# List all versions of a base agent
versions = client.agents.list_versions("base-agent-uuid")
for version in versions:
    print(f"Version: {version.version_name} (ID: {version.id})")

# Get a specific version
version = client.agents.get_version("base-agent-uuid", "version-uuid")
print(f"Version: {version.version_name}")

# Run a specific version
result = version.run(
    prompt="Hello from specific version!",
    document="file.pdf"
)
```

### Context Manager

```python
# Automatically close HTTP connections
with RoeClient() as client:
    result = client.agents.run(
        agent_id="agent-uuid",
        prompt="Hello world"
    )
    # Client is automatically closed
```

### Error Handling

```python
from roe import (
    RoeClient,
    AuthenticationError,
    InsufficientCreditsError,
    NotFoundError
)

try:
    client = RoeClient()
    result = client.agents.run(
        agent_id="invalid-uuid",
        prompt="Test"
    )
except AuthenticationError:
    print("Invalid API key")
except InsufficientCreditsError:
    print("Not enough credits")
except NotFoundError:
    print("Agent not found")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Configuration

### Environment Variables

- `ROE_API_KEY`: Your Roe AI API key (required)
- `ROE_ORGANIZATION_ID`: Your organization UUID (required)
- `ROE_BASE_URL`: API base URL (optional, defaults to https://api.roe-ai.com)
- `ROE_TIMEOUT`: Request timeout in seconds (optional, defaults to 60.0)
- `ROE_MAX_RETRIES`: Maximum retries (optional, defaults to 3)

### Configuration Options

```python
client = RoeClient(
    api_key="your-api-key",
    organization_id="your-org-uuid",
    base_url="https://api.roe-ai.com",  # Custom base URL
    timeout=30.0,  # 30 second timeout
    max_retries=5  # Retry failed requests up to 5 times
)
```

## API Reference

### RoeClient

Main client for interacting with the Roe AI API.

**Methods:**

- `agents` - Access to the agents API

### AgentsAPI

**Methods:**

- `list_base_agents(page=None, page_size=None)` - List base agents with pagination
- `get_base_agent(agent_id)` - Get a specific base agent by ID
- `list_versions(base_agent_id)` - List all versions of a base agent
- `get_version(base_agent_id, version_id)` - Get a specific agent version
- `get_current_version(base_agent_id)` - Get the current version of a base agent
- `run(agent_id, **inputs)` - Run an agent with dynamic inputs (base agent or version)

### Models

- `BaseAgent` - Base agent configuration and metadata
- `AgentVersion` - Agent version with input definitions and engine config
- `AgentInputDefinition` - Definition of agent input parameters
- `AgentDatum` - Agent execution result
- `PaginatedResponse[T]` - Paginated API response
- `FileUpload` - Explicit file upload with metadata

### Exceptions

- `RoeAPIException` - Base exception for all API errors
- `AuthenticationError` (401) - Invalid API key
- `InsufficientCreditsError` (402) - Not enough credits
- `ForbiddenError` (403) - Access denied
- `NotFoundError` (404) - Resource not found
- `BadRequestError` (400) - Invalid request
- `ServerError` (500+) - Server errors

## Examples

See the [examples/](examples/) directory:

- `list_agents.py` - List base agents with pagination
- `get_agent.py` - Get a specific agent by ID
- `run_agent_simple.py` - Run an agent with text inputs only
- `run_agent_with_file.py` - Run an agent with file upload
- `agent_versions.py` - Work with agent versions
- `file_upload_methods.py` - Compare all file upload approaches

## Support

- **Documentation**: https://docs.roe-ai.com/introduction
- **Issues**: https://github.com/roe-ai/roe-python/issues
- **Email**: support@roe-ai.com

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.
