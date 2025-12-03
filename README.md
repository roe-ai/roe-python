# Roe AI Python SDK

A Python SDK for the Roe AI API.

## Installation

```bash
pip install roe-ai
# or
uv add roe-ai
```

## Quick Start

```python
from roe import RoeClient

client = RoeClient(
    api_key="your-api-key",
    organization_id="your-org-uuid"
)

# Run an existing agent
job = client.agents.run(agent_id="agent-uuid", text="Analyze this text")
result = job.wait()

for output in result.outputs:
    print(f"{output.key}: {output.value}")
```

Or use environment variables:

```bash
export ROE_API_KEY="your-api-key"
export ROE_ORGANIZATION_ID="your-org-uuid"
```

```python
client = RoeClient()  # Reads from environment
```

## Running Agents

### Async (Recommended)

```python
job = client.agents.run(agent_id="agent-uuid", text="Hello world")
result = job.wait()
```

### Sync

```python
outputs = client.agents.run_sync(agent_id="agent-uuid", text="Hello world")
```

### With Files

```python
# Local file path - automatically uploaded
job = client.agents.run(agent_id="agent-uuid", document="path/to/file.pdf")

# Existing Roe file ID
job = client.agents.run(agent_id="agent-uuid", document="file-uuid")
```

### Batch Processing

```python
batch = client.agents.run_many(
    agent_id="agent-uuid",
    batch_inputs=[
        {"document": "file1.pdf"},
        {"document": "file2.pdf"},
        {"document": "file3.pdf"},
    ]
)
results = batch.wait()
```

## Creating Agents

### Text Extraction Agent

```python
agent = client.agents.create_agent(
    name="Text Analyzer",
    engine_class_id="MultimodalExtractionEngine",
    input_definitions=[
        {"key": "text", "data_type": "text/plain", "description": "Text to analyze"}
    ],
    engine_config={
        "model": "gpt-4.1-2025-04-14",
        "text": "${text}",
        "instruction": "Summarize the key points.",
        "output_schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string", "description": "Summary"}
            }
        }
    }
)

job = client.agents.run(agent_id=str(agent.id), text="Your text here...")
```

### Document Extraction Agent

```python
agent = client.agents.create_agent(
    name="PDF Analyzer",
    engine_class_id="PDFExtractionEngine",
    input_definitions=[
        {"key": "pdf_files", "data_type": "application/pdf", "description": "PDF to analyze"}
    ],
    engine_config={
        "model": "gpt-4.1-2025-04-14",
        "pdf_files": "${pdf_files}",
        "instructions": "Extract the main topics from this document.",
        "output_schema": {
            "type": "object",
            "properties": {
                "topics": {"type": "array", "items": {"type": "string"}}
            }
        }
    }
)

job = client.agents.run(agent_id=str(agent.id), pdf_files="document.pdf")
```

### Web Insights Agent

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
        "instruction": "Extract company information.",
        "vision_mode": False,
        "crawl_config": {
            "save_html": True,
            "save_markdown": True,
            "save_screenshot": True
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "company_name": {"type": "string"},
                "description": {"type": "string"}
            }
        }
    }
)

job = client.agents.run(agent_id=str(agent.id), url="https://example.com")
```

### Perplexity Search Agent

```python
agent = client.agents.create_agent(
    name="Web Search",
    engine_class_id="PerplexitySearchEngine",
    input_definitions=[
        {"key": "prompt", "data_type": "text/plain", "description": "Search query"}
    ],
    engine_config={
        "prompt": "${prompt}"
    }
)

job = client.agents.run(agent_id=str(agent.id), prompt="What is the capital of France?")
```

### Maps Search Agent

```python
agent = client.agents.create_agent(
    name="Location Finder",
    engine_class_id="GoogleMapsEntityExtractionEngine",
    input_definitions=[
        {"key": "address", "data_type": "text/plain", "description": "Address to search"}
    ],
    engine_config={
        "address": "${address}",
        "instruction": "Get business details.",
        "model": "gpt-4.1-2025-04-14",
        "output_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "full_address": {"type": "string"}
            }
        }
    }
)

job = client.agents.run(agent_id=str(agent.id), address="Apple Park, Cupertino, CA")
```

## Agent Management

```python
# List agents
agents = client.agents.list_base_agents(page=1, page_size=10)

# Get agent
agent = client.agents.get_base_agent(agent_id="agent-uuid")

# Update agent
client.agents.update_agent(agent_id="agent-uuid", name="New Name")

# Duplicate agent
new_agent = client.agents.duplicate_agent(agent_id="agent-uuid")

# Delete agent
client.agents.delete_agent(agent_id="agent-uuid")
```

## Version Management

```python
# List versions
versions = client.agents.list_versions(agent_id="agent-uuid")

# Get current version
current = client.agents.get_current_version(agent_id="agent-uuid")

# Create new version
version = client.agents.create_version(
    agent_id="agent-uuid",
    version_name="v2",
    input_definitions=[...],
    engine_config={...}
)

# Run specific version
job = client.agents.run_version(
    agent_id="agent-uuid",
    version_id="version-uuid",
    text="Input"
)

# Delete version
client.agents.delete_version(agent_id="agent-uuid", version_id="version-uuid")
```

## Job Management

```python
# Get job status
status = client.agents.get_job_status(job_id="job-uuid")

# Get job result
result = client.agents.get_job_result(job_id="job-uuid")

# Batch status/results
statuses = client.agents.get_job_status_many(job_ids=["job-1", "job-2"])
results = client.agents.get_job_result_many(job_ids=["job-1", "job-2"])
```

## Download References

Web crawling jobs can save screenshots, HTML, and markdown. Download them:

```python
import json

result = job.wait()

for output in result.outputs:
    data = json.loads(output.value)
    if "references" in data:
        for ref_url in data["references"]:
            resource_id = ref_url.split("/references/")[-1].rstrip("/")
            content = client.agents.download_reference(
                job_id=str(job.id),
                resource_id=resource_id
            )
            with open(f"{resource_id}", "wb") as f:
                f.write(content)
```

## Supported Models

| Model | `model` value |
|-------|---------------|
| GPT-5.1 | `gpt-5.1-2025-11-13` |
| GPT-5 | `gpt-5-2025-08-07` |
| GPT-5 Mini | `gpt-5-mini-2025-08-07` |
| GPT-4.1 | `gpt-4.1-2025-04-14` |
| GPT-4.1 Mini | `gpt-4.1-mini-2025-04-14` |
| O3 Pro | `o3-pro-2025-06-10` |
| O3 | `o3-2025-04-16` |
| O4 Mini | `o4-mini-2025-04-16` |
| GPT-4o | `gpt-4o-2024-11-20` |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` |
| Claude Sonnet 4 | `claude-sonnet-4-20250514` |
| Claude 3.7 Sonnet | `claude-3-7-sonnet-20250219` |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` |
| Claude 3.5 Haiku | `claude-3-5-haiku-20241022` |
| Claude Opus 4.5 | `claude-opus-4-5-20251101` |
| Claude Opus 4.1 | `claude-opus-4-1-20250805` |
| Claude Opus 4 | `claude-opus-4-20250514` |
| Gemini 3 Pro | `gemini-3-pro-preview` |
| Gemini 2.5 Pro | `gemini-2.5-pro` |
| Gemini 2.5 Flash | `gemini-2.5-flash` |

## Engine Classes

| Engine | `engine_class_id` | Description |
|--------|-------------------|-------------|
| Multimodal Extraction | `MultimodalExtractionEngine` | Extract data from text and images |
| Document Insights | `PDFExtractionEngine` | Extract insights from PDFs |
| Document Segmentation | `PDFPageSelectionEngine` | Select pages from PDFs by description |
| Web Insights | `URLWebsiteExtractionEngine` | Extract data from websites |
| Interactive Web | `InteractiveWebExtractionEngine` | Navigate and interact with websites |
| Web Search | `URLFinderEngine` | Find relevant URLs |
| Perplexity Search | `PerplexitySearchEngine` | Web research via Perplexity |
| Maps Search | `GoogleMapsEntityExtractionEngine` | Search Google Maps locations |
| Merchant Risk | `MerchantRiskAnalysisEngine` | Assess merchant risk |
| Product Policy | `ProductPolicyEngine` | Check product policy compliance |
| LinkedIn Crawler | `LinkedInScraperEngine` | Scrape LinkedIn profiles |
| Social Media | `SocialScraperEngine` | Scrape social media profiles |

## Configuration

| Environment Variable | Description |
|---------------------|-------------|
| `ROE_API_KEY` | API key (required) |
| `ROE_ORGANIZATION_ID` | Organization ID (required) |
| `ROE_BASE_URL` | API base URL (optional) |

## Links

- [Examples](examples/)
- [API Documentation](https://docs.roe-ai.com)
- [Issues](https://github.com/roe-ai/roe-python/issues)
