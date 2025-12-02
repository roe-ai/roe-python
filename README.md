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
    text="Hello world"
)
result = job.wait()

# Process results
for output in result.outputs:
    print(f"{output.key}: {output.value}")
```

## Supported Models

The following models are available for use in `engine_config["model"]`:

| Model Name | model |
|------------|-------|
| GPT-5.1 | `gpt-5.1-2025-11-13` |
| GPT-5 | `gpt-5-2025-08-07` |
| GPT-5 Mini | `gpt-5-mini-2025-08-07` |
| GPT-4.1 | `gpt-4.1-2025-04-14` |
| GPT-4.1 Mini | `gpt-4.1-mini-2025-04-14` |
| GPT-4o | `gpt-4o-2024-11-20` |
| O3 | `o3-2025-04-16` |
| O4 Mini | `o4-mini-2025-04-16` |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` |
| Claude Sonnet 4 | `claude-sonnet-4-20250514` |
| Claude 3.7 Sonnet | `claude-3-7-sonnet-20250219` |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` |
| Claude 3.5 Haiku | `claude-3-5-haiku-20241022` |
| Claude Opus 4.5 | `claude-opus-4-5-20251101` |
| Claude Opus 4.1 | `claude-opus-4-1-20250805` |
| Claude Opus 4 | `claude-opus-4-20250514` |
| Gemini 2.5 Pro | `gemini-2.5-pro-preview-06-05` |
| Gemini 2.5 Flash | `gemini-2.5-flash-preview-05-20` |

## Engine Classes

Available engine classes for `engine_class_id`:

| Engine | engine_class_id | Description |
|--------|-----------------|-------------|
| Document Insights | `PDFExtractionEngine` | Extract insights and structured information from documents |
| Document Segmentation | `PDFPageSelectionEngine` | Parse page filter criteria and output page ranges |
| Interactive Web Insight | `InteractiveWebExtractionEngine` | Navigate websites and extract structured data interactively |
| LinkedIn Crawler | `LinkedInScraperEngine` | Scrape LinkedIn profiles |
| Maps Search | `GoogleMapsEntityExtractionEngine` | Search Google Maps via fuzzy address name |
| Merchant Risk Analysis | `MerchantRiskAnalysisEngine` | Assess merchant compliance and risk factors |
| Multimodal Extraction | `MultimodalExtractionEngine` | Process multiple media types for data extraction |
| Perplexity Search | `PerplexitySearchEngine` | Web research via Perplexity |
| Product Policy Compliance | `ProductPolicyEngine` | Analyze product listings for policy compliance violations |
| Social Media Crawler | `SocialScraperEngine` | Scrape social media profile data and recent posts |
| Web Insights | `URLWebsiteExtractionEngine` | Extract insights and structured information from URLs |
| Web Search | `URLFinderEngine` | Search for most relevant URLs

## Agent Management

### Create Agent

```python
agent = client.agents.create_agent(
    name="My Agent",
    engine_class_id="MultimodalExtractionEngine",
    input_definitions=[
        {"key": "document", "data_type": "application/pdf", "description": "PDF to analyze"}
    ],
    engine_config={
        "model": "gpt-4.1-2025-04-14",
        "instruction": "Extract key information from the document",
        "output_schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string", "description": "Document summary"}
            }
        }
    }
)
print(f"Created: {agent.id}")
```

### Update Agent

```python
client.agents.update_agent(
    agent_id="agent-uuid",
    name="New Name",
    disable_cache=True
)
```

### Duplicate Agent

```python
new_version = client.agents.duplicate_agent(agent_id="agent-uuid")
print(f"New agent: {new_version.base_agent.id}")
```

### Delete Agent

```python
client.agents.delete_agent(agent_id="agent-uuid")
```

## Version Management

### Create Version

```python
version = client.agents.create_version(
    agent_id="agent-uuid",
    version_name="v2",
    description="Improved extraction",
    input_definitions=[
        {"key": "document", "data_type": "application/pdf", "description": "PDF"}
    ],
    engine_config={
        "model": "gpt-4.1-2025-04-14",
        "instruction": "New instructions"
    }
)
```

### Update Version

```python
client.agents.update_version(
    agent_id="agent-uuid",
    version_id="version-uuid",
    version_name="v2-updated",
    description="New description"
)
```

### Delete Version

```python
client.agents.delete_version(agent_id="agent-uuid", version_id="version-uuid")
```

## Running Agents

### Async Execution (Recommended)

```python
# Start job
job = client.agents.run(agent_id="agent-uuid", document="file.pdf")

# Wait for result
result = job.wait()

# Process outputs
for output in result.outputs:
    print(f"{output.key}: {output.value}")
```

### Sync Execution

```python
outputs = client.agents.run_sync(agent_id="agent-uuid", document="file.pdf")
for output in outputs:
    print(f"{output.key}: {output.value}")
```

### Run Specific Version

```python
# Async
job = client.agents.run_version(
    agent_id="agent-uuid",
    version_id="version-uuid",
    document="file.pdf"
)
result = job.wait()

# Sync
outputs = client.agents.run_version_sync(
    agent_id="agent-uuid",
    version_id="version-uuid",
    document="file.pdf"
)
```

## Batch Processing

```python
batch = client.agents.run_many(
    agent_id="agent-uuid",
    batch_inputs=[
        {"document": "file1.pdf"},
        {"document": "file2.pdf"},
        {"document": "file3.pdf"},
    ]
)

# Wait for all jobs
results = batch.wait()
for result in results:
    print(f"Outputs: {len(result.outputs)}")
```

## File Uploads

```python
# File path (auto-upload)
job = client.agents.run(agent_id="agent-uuid", document="path/to/file.pdf")

# Existing Roe file ID
job = client.agents.run(agent_id="agent-uuid", document="file-uuid-here")
```

## Web Insights Example

```python
agent = client.agents.create_agent(
    name="Web Analyzer",
    engine_class_id="URLWebsiteExtractionEngine",
    input_definitions=[
        {"key": "url", "data_type": "text/plain", "description": "URL to analyze"}
    ],
    engine_config={
        "url": "${url}",
        "model": "gpt-4.1-2025-04-14",
        "instruction": "Analyze this website",
        "vision_mode": False,
        "crawl_config": {
            "save_html": True,
            "save_markdown": True,
            "save_screenshot": True,
            "crawling_only": False,
            "min_wait_time_sec": 0
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "company": {"type": "string"},
                "description": {"type": "string"}
            }
        }
    }
)

job = client.agents.run(agent_id=str(agent.id), url="https://apple.com")
result = job.wait()
```

## Download References

Reference files (screenshots, HTML, markdown) from web crawling jobs:

```python
import json

# Get job result
result = job.wait()

# Parse output for reference URLs
for output in result.outputs:
    parsed = json.loads(output.value)
    if "references" in parsed:
        for ref_url in parsed["references"]:
            # Extract resource_id from URL
            resource_id = ref_url.split("/references/")[-1].rstrip("/")

            # Download file
            content = client.agents.download_reference(
                job_id=str(job.id),
                resource_id=resource_id
            )

            with open(f"downloaded_{resource_id}", "wb") as f:
                f.write(content)
```

## Delete Job Data

```python
result = client.agents.delete_job_data(job_id="job-uuid")
print(f"Deleted {result.deleted_count} files")
```

## Timeout Configuration

```python
# Single job with 10-minute timeout
job = client.agents.run(
    agent_id="agent-uuid",
    timeout_seconds=600,
    document="file.pdf"
)

try:
    result = job.wait()
except TimeoutError:
    print("Job exceeded timeout")

# Batch with custom timeout
batch = client.agents.run_many(
    agent_id="agent-uuid",
    batch_inputs=[{"document": "file1.pdf"}],
    timeout_seconds=900
)
```

## Examples

See the [examples/](examples/) directory:

- `run_agent_simple.py` - Basic agent execution
- `run_agent_with_file.py` - File upload handling
- `run_agent_many.py` - Batch processing
- `run_agent_with_timeout.py` - Timeout configuration
- `run_sync.py` - Synchronous execution
- `list_agents.py` - List available agents
- `get_agent.py` - Get agent details
- `create_agent.py` - Create agents
- `manage_agent.py` - Update, duplicate, delete agents
- `agent_versions.py` - Work with versions
- `manage_versions.py` - Version CRUD
- `file_upload_methods.py` - File upload options
- `download_references.py` - Download reference files
- `delete_job_data.py` - Delete job data

## Configuration

Environment variables:

- `ROE_API_KEY` - Your API key (required)
- `ROE_ORGANIZATION_ID` - Your organization ID (required)
- `ROE_BASE_URL` - API base URL (optional)
- `ROE_TIMEOUT` - Request timeout (optional)
- `ROE_MAX_RETRIES` - Max retries (optional)

## Documentation

- **API Docs**: https://docs.roe-ai.com
- **Issues**: https://github.com/roe-ai/roe-python/issues
