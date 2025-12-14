# Roe AI Python SDK

Python SDK for the [Roe AI](https://www.roe-ai.com/) API.

## Installation

```bash
uv add roe-ai
```

or

```bash
pip install roe-ai
```

## Quick Start

```python
from roe import RoeClient

client = RoeClient(
    api_key="your-api-key",
    organization_id="your-org-uuid",
)

# Run an agent
job = client.agents.run(agent_id="agent-uuid", text="Analyze this text")
result = job.wait()

for output in result.outputs:
    print(f"{output.key}: {output.value}")
```

Or use environment variables:

```bash
export ROE_ORGANIZATION_API_KEY="your-api-key"
export ROE_ORGANIZATION_ID="your-org-uuid"
```

## Full Example

Create an agent that extracts structured data from websites:

```python
from roe import RoeClient

client = RoeClient()

# Create a Web Insights agent
agent = client.agents.create(
    name="Company Analyzer",
    engine_class_id="URLWebsiteExtractionEngine",
    input_definitions=[
        {"key": "url", "data_type": "text/plain", "description": "Website URL"},
    ],
    engine_config={
        "url": "${url}",
        "model": "gpt-4.1-2025-04-14",
        "instruction": "Extract company information from this website.",
        "vision_mode": False,
        "crawl_config": {
            "save_html": True,
            "save_markdown": True,
            "save_screenshot": True,
        },
        "output_schema": {
            "type": "object",
            "properties": {
                "company_name": {"type": "string"},
                "description": {"type": "string"},
                "products": {"type": "array", "items": {"type": "string"}},
            }
        }
    }
)

# Run the agent
job = client.agents.run(agent_id=str(agent.id), url="https://www.roe-ai.com/")
result = job.wait()

# Print results
import json
for output in result.outputs:
    print(json.dumps(json.loads(output.value), indent=2))

# Download saved references (screenshots, HTML, markdown)
for ref in result.get_references():
    content = client.agents.jobs.download_reference(str(job.id), ref.resource_id)
    with open(ref.resource_id, "wb") as f:
        f.write(content)

# Cleanup
client.agents.delete(str(agent.id))
```

## API Reference

### Agents

```python
client.agents.list()                          # List agents
client.agents.retrieve("agent-uuid")          # Get agent
client.agents.create(name="...", ...)         # Create agent
client.agents.update("agent-uuid", ...)       # Update agent
client.agents.delete("agent-uuid")            # Delete agent
client.agents.duplicate("agent-uuid")         # Duplicate agent
```

### Running Agents

```python
client.agents.run(agent_id, **inputs)         # Async execution
client.agents.run_sync(agent_id, **inputs)    # Sync execution
client.agents.run_many(agent_id, batch_inputs)# Batch execution
client.agents.run_version(agent_id, version_id, **inputs)
```

### Versions

```python
client.agents.versions.list(agent_id)
client.agents.versions.retrieve(agent_id, version_id)
client.agents.versions.retrieve_current(agent_id)
client.agents.versions.create(agent_id, ...)
client.agents.versions.update(agent_id, version_id, ...)
client.agents.versions.delete(agent_id, version_id)
```

### Jobs

```python
client.agents.jobs.retrieve_status(job_id)
client.agents.jobs.retrieve_result(job_id)
client.agents.jobs.download_reference(job_id, resource_id)
client.agents.jobs.delete_data(job_id)
```

## Supported Models

| Model | Value |
|-------|-------|
| GPT-5.2 | `gpt-5.2-2025-12-11` |
| GPT-5.1 | `gpt-5.1-2025-11-13` |
| GPT-5 | `gpt-5-2025-08-07` |
| GPT-5 Mini | `gpt-5-mini-2025-08-07` |
| GPT-4.1 | `gpt-4.1-2025-04-14` |
| GPT-4.1 Mini | `gpt-4.1-mini-2025-04-14` |
| O3 Pro | `o3-pro-2025-06-10` |
| O3 | `o3-2025-04-16` |
| O4 Mini | `o4-mini-2025-04-16` |
| GPT-4o | `gpt-4o-2024-11-20` |
| Grok 4 | `grok-4-0709` |
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

| Engine | ID |
|--------|-----|
| Multimodal Extraction | `MultimodalExtractionEngine` |
| Document Insights | `PDFExtractionEngine` |
| Document Segmentation | `PDFPageSelectionEngine` |
| Web Insights | `URLWebsiteExtractionEngine` |
| Interactive Web | `InteractiveWebExtractionEngine` |
| Web Search | `URLFinderEngine` |
| Perplexity Search | `PerplexitySearchEngine` |
| Maps Search | `GoogleMapsEntityExtractionEngine` |
| Merchant Risk | `MerchantRiskAnalysisEngine` |
| Product Policy | `ProductPolicyEngine` |
| LinkedIn Crawler | `LinkedInScraperEngine` |
| Social Media | `SocialScraperEngine` |

## Links

- [Roe AI](https://www.roe-ai.com/)
- [API Docs](https://docs.roe-ai.com)
