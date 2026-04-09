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

## Job Result Inspection

After waiting for a job, you can inspect its outcome using status helpers:

```python
from roe import JobStatus

result = job.wait()

# Check job outcome
if result.succeeded:
    for output in result.outputs:
        print(f"{output.key}: {output.value}")
elif result.cancelled:
    print("Job was cancelled")
elif result.failed:
    print("Error:", result.error_message)

# Available fields
result.status         # JobStatus code (int) or None
result.error_message  # Error string or None
result.succeeded      # True if SUCCESS or CACHED
result.failed         # True if FAILURE or CANCELLED
result.cancelled      # True if CANCELLED
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

## Rori Agents (Agentic Workflows)

Rori agents are autonomous investigation agents that follow policies (SOPs), use tools, and produce structured verdicts. Unlike extraction engines which transform data, Rori agents reason over evidence, apply policy rules, and return dispositions. All Rori agents are policy-aware — you define the rules, they run the investigation.

### Policies

Policies define the rules, instructions, and disposition classifications that Rori agents follow. Creating a policy atomically creates the policy and its first version in one call:

```python
policy = client.policies.create(
    name="AML Investigation Policy",
    content={
        "guidelines": {
            "categories": [
                {
                    "title": "Structuring",
                    "rules": [
                        {
                            "title": "Cash structuring below reporting thresholds",
                            "description": "Multiple deposits just under $10,000 within short timeframes",
                            "flag": "RED_FLAG",
                        }
                    ],
                },
                {
                    "title": "Layering",
                    "rules": [
                        {
                            "title": "Rapid movement between accounts",
                            "description": "Funds transferred through multiple accounts to obscure origin",
                            "flag": "RED_FLAG",
                            "sub_rules": [
                                {"title": "Cross-border wire transfers with no business purpose"},
                                {"title": "Shell company intermediaries"},
                            ],
                        }
                    ],
                },
            ]
        },
        "instructions": "Investigate the alert against each category. Use available data sources to gather evidence.",
        "dispositions": {
            "classifications": [
                {"name": "Suspicious", "description": "Activity warrants SAR filing"},
                {"name": "Not Suspicious", "description": "Activity has legitimate explanation"},
                {"name": "Needs Escalation", "description": "Requires senior analyst review"},
            ]
        },
        "summary_template": {
            "template": "Investigation of {{subject}} found {{verdict}} based on {{findings_count}} findings."
        },
    },
)
```

Iterate on policies by creating new versions:

```python
# Create a new version (automatically becomes the current version)
new_version = client.policies.versions.create(
    policy_id=str(policy.id),
    content={...},  # Updated policy content
    version_name="v2 - added layering rules",
)

# List all versions
versions = client.policies.versions.list(policy_id=str(policy.id))

# Retrieve a specific version
version = client.policies.versions.retrieve(str(policy.id), str(new_version.id))

# Update policy metadata
client.policies.update(str(policy.id), name="Updated Policy Name")

# List all policies
policies = client.policies.list()

# Delete a policy
client.policies.delete(str(policy.id))
```

### Policy Content Reference

| Field | Type | Description |
|-------|------|-------------|
| `guidelines` | object | Categories → Rules → Sub-rules hierarchy |
| `guidelines.categories[].title` | string | Category name |
| `guidelines.categories[].rules[].title` | string | Rule name |
| `guidelines.categories[].rules[].description` | string | Rule details |
| `guidelines.categories[].rules[].flag` | string | `"RED_FLAG"` or `"GREEN_FLAG"` |
| `guidelines.categories[].rules[].sub_rules[].title` | string | Sub-rule name |
| `instructions` | string | Free-text investigation instructions |
| `dispositions.classifications[].name` | string | Outcome label (e.g., "Suspicious") |
| `dispositions.classifications[].description` | string | When to apply this outcome |
| `summary_template.template` | string | Handlebars template for report generation |
| `optional.sar_narrative_template.template` | string | SAR narrative template (AML-specific) |

### Product Compliance

Analyze product listings against your compliance policy:

```python
agent = client.agents.create(
    name="Product Compliance",
    engine_class_id="ProductPolicyEngine",
    input_definitions=[
        {"key": "product_listings", "data_type": "text/plain", "description": "Product listing to analyze"},
    ],
    engine_config={
        "policy_version_id": str(policy.current_version_id),
        "product_listings": "${product_listings}",
    },
)

result = client.agents.run_sync(
    agent_id=str(agent.id),
    product_listings="Nike Air Max 90, brand new, $45 — ships from Shenzhen",
)
```

### AML Investigation

Investigate anti-money laundering alerts:

```python
agent = client.agents.create(
    name="AML Investigation",
    engine_class_id="AMLInvestigationEngine",
    input_definitions=[
        {"key": "alert_data", "data_type": "text/plain", "description": "Alert data and context"},
    ],
    engine_config={
        "policy_version_id": str(policy.current_version_id),
        "alert_data": "${alert_data}",
    },
)

job = client.agents.run(
    agent_id=str(agent.id),
    alert_data="Customer John Doe, 5 cash deposits of $9,500 in 3 days",
)
result = job.wait()
```

### Fraud Investigation

Investigate fraud alerts and suspicious activity:

```python
agent = client.agents.create(
    name="Fraud Investigation",
    engine_class_id="FraudInvestigationEngine",
    input_definitions=[
        {"key": "alert_data", "data_type": "text/plain", "description": "Alert data and context"},
    ],
    engine_config={
        "policy_version_id": str(policy.current_version_id),
        "alert_data": "${alert_data}",
    },
)

job = client.agents.run(
    agent_id=str(agent.id),
    alert_data="Chargeback spike: 47 disputes in 24h from merchant ACME-1234",
)
result = job.wait()
```

### Merchant Risk

Analyze merchant risk profiles:

```python
agent = client.agents.create(
    name="Merchant Risk Analysis",
    engine_class_id="MerchantRiskEngine",
    input_definitions=[
        {"key": "merchant_context", "data_type": "text/plain", "description": "Merchant name and context"},
    ],
    engine_config={
        "policy_version_id": str(policy.current_version_id),
        "merchant_context": "${merchant_context}",
    },
)

job = client.agents.run(
    agent_id=str(agent.id),
    merchant_context="ACME Corp - Online electronics retailer, MCC 5732",
)
result = job.wait()
```

### Agent Configuration Options

All Rori agents accept these options in `engine_config`:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `policy_version_id` | string | — | Policy version UUID (required) |
| `context_sources` | list | `[]` | External data sources (SQL connections, APIs) |
| `enable_planning` | bool | `true` | Enable autonomous tool-use planning |
| `enable_memory` | bool | `false` | Retain context across runs for the same entity |
| `reasoning_effort` | string | `"medium"` | `"low"`, `"medium"`, or `"high"` |

Example with advanced configuration:

```python
agent = client.agents.create(
    name="AML Investigation (Advanced)",
    engine_class_id="AMLInvestigationEngine",
    input_definitions=[
        {"key": "alert_data", "data_type": "text/plain", "description": "Alert data and context"},
    ],
    engine_config={
        "policy_version_id": str(policy.current_version_id),
        "alert_data": "${alert_data}",
        "reasoning_effort": "high",
        "context_sources": [
            {"type": "sql", "name": "Transactions DB", "connection_id": "conn-uuid"},
        ],
    },
)
```

## Retry Behavior

The SDK automatically retries idempotent requests (GET, PUT, DELETE) that receive `502`, `503`, or `504` responses using exponential backoff (1s, 2s, 4s, …). By default, up to 3 retries are attempted before raising a `ServerError`. POST requests are never retried to avoid duplicate submissions.

You can configure the retry count via the `max_retries` parameter or the `ROE_MAX_RETRIES` environment variable:

```python
client = RoeClient(
    api_key="your-api-key",
    organization_id="your-org-uuid",
    max_retries=5,  # default: 3
)
```

Other error codes (400, 401, 404, 500, etc.) are raised immediately without retrying.

## Batch Processing

When batch operations exceed 1,000 items, the SDK automatically chunks requests. A configurable delay (default: 10 seconds) is applied between chunks to avoid overwhelming the API. This applies to:

- `client.agents.run_many()` — job submissions
- `client.agents.jobs.retrieve_status_many()` — batch status checks
- `client.agents.jobs.retrieve_result_many()` — batch result retrieval

Single-chunk batches (≤1,000 items) are unaffected.

You can configure the delay via the `batch_chunk_delay` parameter or the `ROE_BATCH_CHUNK_DELAY` environment variable:

```python
client = RoeClient(
    api_key="your-api-key",
    organization_id="your-org-uuid",
    batch_chunk_delay=2.0,  # default: 10.0
)
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

## Metadata

You can attach arbitrary metadata to any job when running an agent. Metadata is a dictionary of key-value pairs that gets stored with the job, useful for tracking, filtering, or correlating jobs with your own internal records.

```python
# Attach metadata to an async job
job = client.agents.run(
    agent_id="agent-uuid",
    metadata={"customer_id": "cust-123", "request_source": "api"},
    url="https://example.com",
)
result = job.wait()

# Attach metadata to a sync job
outputs = client.agents.run_sync(
    agent_id="agent-uuid",
    metadata={"batch": "2026-02-12", "priority": "high"},
    url="https://example.com",
)

# Attach metadata to a batch of jobs (applied to all jobs in the batch)
batch = client.agents.run_many(
    agent_id="agent-uuid",
    batch_inputs=[{"url": "https://a.com"}, {"url": "https://b.com"}],
    metadata={"campaign": "weekly-scan"},
)
results = batch.wait()

# Attach metadata when running a specific version
job = client.agents.run_version(
    agent_id="agent-uuid",
    version_id="version-uuid",
    metadata={"experiment": "v2-prompt"},
    url="https://example.com",
)

# Also works directly on agent and version models
agent = client.agents.retrieve("agent-uuid")
job = agent.run(metadata={"source": "sdk"}, url="https://example.com")
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
| GPT-5.4 | `gpt-5.4-2026-03-05` |
| GPT-5.2 | `gpt-5.2-2025-12-11` |
| GPT-5.1 | `gpt-5.1-2025-11-13` |
| GPT-5 | `gpt-5-2025-08-07` |
| GPT-5 Mini | `gpt-5-mini-2025-08-07` |
| GPT-4.1 | `gpt-4.1-2025-04-14` |
| GPT-4.1 Mini | `gpt-4.1-mini-2025-04-14` |
| O3 Pro | `o3-pro-2025-06-10` |
| O3 | `o3-2025-04-16` |
| O4 Mini | `o4-mini-2025-04-16` |
| Claude Opus 4.6 | `claude-opus-4-6` |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` |
| Claude Opus 4.5 | `claude-opus-4-5-20251101` |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` |
| Claude Opus 4.1 | `claude-opus-4-1-20250805` |
| Claude Opus 4 | `claude-opus-4-20250514` |
| Claude Sonnet 4 | `claude-sonnet-4-20250514` |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` |
| Gemini 3 Pro | `gemini-3-pro-preview` |
| Gemini 3 Flash | `gemini-3-flash-preview` |
| Gemini 2.5 Pro | `gemini-2.5-pro` |
| Gemini 2.5 Flash | `gemini-2.5-flash` |
| Grok 4 | `grok-4-0709` |
| Grok 4.1 Fast Reasoning | `grok-4-1-fast-reasoning` |

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
| LinkedIn Crawler | `LinkedInScraperEngine` |
| Social Media | `SocialScraperEngine` |
| Product Compliance | `ProductPolicyEngine` |
| Merchant Risk | `MerchantRiskEngine` |
| AML Investigation | `AMLInvestigationEngine` |
| Fraud Investigation | `FraudInvestigationEngine` |

## Links

- [Roe AI](https://www.roe-ai.com/)
- [API Documentation](https://docs.roe-ai.com)
- [Examples](examples/)
