# Roe AI Python SDK

A Python SDK for the [Roe AI](https://www.roe-ai.com/) API.

## Installation

```bash
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

Or set environment variables:

```bash
export ROE_ORGANIZATION_API_KEY="your-api-key"
export ROE_ORGANIZATION_ID="your-org-uuid"
```

## Agent Examples

### Multimodal Extraction

Extract structured data from text and images:

```python
agent = client.agents.create(
    name="Listing Analyzer",
    engine_class_id="MultimodalExtractionEngine",
    input_definitions=[
        {"key": "text", "data_type": "text/plain", "description": "Item description"},
    ],
    engine_config={
        "model": "gpt-4.1-2025-04-14",
        "text": "${text}",
        "instruction": "Analyze this product listing. Is it counterfeit?",
        "output_schema": {
            "type": "object",
            "properties": {
                "is_counterfeit": {"type": "boolean", "description": "Whether likely counterfeit"},
                "confidence": {"type": "number", "description": "Confidence score 0-1"},
                "reasoning": {"type": "string", "description": "Explanation"},
            }
        }
    }
)

job = client.agents.run(
    agent_id=str(agent.id),
    text="Authentic Louis Vuitton bag, brand new, $50"
)
result = job.wait()
```

### Document Insights

Extract structured information from PDFs:

```python
agent = client.agents.create(
    name="Resume Parser",
    engine_class_id="PDFExtractionEngine",
    input_definitions=[
        {"key": "pdf_files", "data_type": "application/pdf", "description": "Resume PDF"},
    ],
    engine_config={
        "model": "gpt-4.1-2025-04-14",
        "pdf_files": "${pdf_files}",
        "instructions": "Extract candidate information from this resume.",
        "output_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "email": {"type": "string"},
                "skills": {"type": "array", "items": {"type": "string"}},
            }
        }
    }
)

job = client.agents.run(agent_id=str(agent.id), pdf_files="resume.pdf")
result = job.wait()
```

### Web Insights

Extract data from websites with automatic screenshot/HTML/markdown capture:

```python
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

# Download saved references (screenshots, HTML, markdown)
for ref in result.get_references():
    content = client.agents.jobs.download_reference(str(job.id), ref.resource_id)
    with open(ref.resource_id, "wb") as f:
        f.write(content)
```

### Interactive Web

Navigate websites and perform actions:

```python
agent = client.agents.create(
    name="Meeting Booker",
    engine_class_id="InteractiveWebExtractionEngine",
    input_definitions=[
        {"key": "url", "data_type": "text/plain", "description": "Website URL"},
        {"key": "action", "data_type": "text/plain", "description": "Action to perform"},
    ],
    engine_config={
        "url": "${url}",
        "action": "${action}",
        "output_schema": {
            "type": "object",
            "properties": {
                "calendar_link": {"type": "string", "description": "Booking link found"},
                "steps_taken": {"type": "array", "items": {"type": "string"}},
            }
        }
    }
)

job = client.agents.run(
    agent_id=str(agent.id),
    url="https://www.roe-ai.com/",
    action="Find the founder's calendar link to book a meeting"
)
result = job.wait()
```

## Running Agents

```python
# Async (recommended)
job = client.agents.run(agent_id="uuid", text="input")
result = job.wait()

# Sync
outputs = client.agents.run_sync(agent_id="uuid", text="input")

# With files (auto-uploaded)
job = client.agents.run(agent_id="uuid", document="file.pdf")

# Batch processing
batch = client.agents.run_many(
    agent_id="uuid",
    batch_inputs=[{"text": "input1"}, {"text": "input2"}]
)
results = batch.wait()
```

## Agent Management

```python
# List / Retrieve
agents = client.agents.list()
agent = client.agents.retrieve("uuid")

# Update / Delete
client.agents.update("uuid", name="New Name")
client.agents.delete("uuid")

# Duplicate
new_agent = client.agents.duplicate("uuid")
```

## Version Management

```python
# List and retrieve versions
versions = client.agents.versions.list("agent-uuid")
current = client.agents.versions.retrieve_current("agent-uuid")
version = client.agents.versions.retrieve("agent-uuid", "version-uuid")

# Create, update, delete versions
version = client.agents.versions.create(
    agent_id="agent-uuid",
    version_name="v2",
    input_definitions=[...],
    engine_config={...}
)

client.agents.versions.update("agent-uuid", "version-uuid", version_name="v2-updated")
client.agents.versions.delete("agent-uuid", "version-uuid")

# Run specific versions
job = client.agents.run_version("agent-uuid", "version-uuid", text="input")
result = job.wait()
```

## Job Management

```python
# Retrieve job status and results
status = client.agents.jobs.retrieve_status(job_id)
result = client.agents.jobs.retrieve_result(job_id)

# Batch operations
statuses = client.agents.jobs.retrieve_status_many([job_id1, job_id2])
results = client.agents.jobs.retrieve_result_many([job_id1, job_id2])

# Download references from jobs (screenshots, HTML, markdown)
content = client.agents.jobs.download_reference(job_id, resource_id)

# Delete job data
client.agents.jobs.delete_data(job_id)
```

## Supported Models

| Model | Value |
|-------|-------|
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

| Engine | ID |
|--------|----|
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
- [API Documentation](https://docs.roe-ai.com)
- [Examples](examples/)
