# Roe AI Python SDK

A Python SDK for interacting with the Roe AI API.

## Installation

```bash
uv add roe-ai
```

## Quick Start

### Authentication

Set your API credentials as environment variables:

```bash
export ROE_API_KEY="your-api-key-here"
export ROE_ORGANIZATION_ID="your-organization-uuid-here"
```

### Basic Usage

```python
from roe import RoeClient

# Initialize client
client = RoeClient()

# List agents
agents = client.agents.list_base_agents()
print(f"Found {agents.count} agents")

# Run an agent
job = client.agents.run(
    agent_id="your-agent-uuid",
    prompt="Hello world"
)
result = job.wait()

# Process results
for output in result.outputs:
    print(f"{output.key}: {output.value}")
```

### Batch Processing

```python
# Run multiple jobs
batch = client.agents.run_many(
    agent_id="agent-uuid",
    inputs_list=[
        {"prompt": "Analyze sentiment: I love this!"},
        {"prompt": "Analyze sentiment: This is terrible."},
        {"prompt": "Analyze sentiment: It's okay."},
    ]
)

# Wait for all to complete
results = batch.wait()
for result in results:
    print(result.outputs)
```

### File Uploads

```python
# File path (auto-upload)
job = client.agents.run(
    agent_id="agent-uuid",
    document="path/to/file.pdf",
    prompt="Analyze this document"
)

# Existing Roe file ID
job = client.agents.run(
    agent_id="agent-uuid",
    document="file-uuid-here",
    prompt="Analyze this document"
)
```

## Examples

For detailed examples, see the [examples/](examples/) directory:

- `run_agent_simple.py` - Basic agent execution
- `run_agent_with_file.py` - File upload handling
- `run_agent_many.py` - Batch processing
- `list_agents.py` - List available agents
- `get_agent.py` - Get agent details
- `agent_versions.py` - Work with agent versions
- `file_upload_methods.py` - Different file upload methods

## Configuration

The client can be configured via environment variables or constructor parameters:

- `ROE_API_KEY` - Your API key (required)
- `ROE_ORGANIZATION_ID` - Your organization ID (required)
- `ROE_BASE_URL` - API base URL (optional)
- `ROE_TIMEOUT` - Request timeout (optional)
- `ROE_MAX_RETRIES` - Max retries (optional)

## Documentation

- **API Docs**: https://docs.roe-ai.com
- **Issues**: https://github.com/roe-ai/roe-python/issues
