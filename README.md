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
export ROE_API_KEY="your-api-key"
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

## AML Investigation Example

Create an agent that investigates transaction alerts for potential money laundering.
The result includes a **verdict** (disposition), an executive **summary** with cited evidence,
and **findings** organized by policy category with red flags and green flags.

### Policy structure (created in the Roe AI dashboard)

A **Policy** is a JSON SOP with three sections — `guidelines`, `instructions`, and
`dispositions`.  Below is a condensed example showing just the shape; a real policy
will have many more categories and rules:

```json
{
  "guidelines": {
    "categories": [
      {
        "id": "1",
        "title": "Alert Intake and Classification",
        "description": "Initial steps for processing and classifying AML alerts",
        "rules": [
          {
            "id": "1.1",
            "title": "Alert Metadata Review",
            "description": "Review core alert information and context",
            "sub_rules": [
              { "id": "1.1.1", "title": "Alert Trigger Understanding",
                "description": "Review the alert type and the underlying rule that fired..." },
              { "id": "1.1.2", "title": "Customer Identification",
                "description": "Retrieve the customer identifier and basic profile..." }
            ]
          },
          {
            "id": "1.2",
            "title": "Investigation Type Classification",
            "description": "Classify investigation pathway based on alert source",
            "sub_rules": [
              { "id": "1.2.1", "title": "Transaction Monitoring Alert Pathway",
                "description": "Classify under TM pathway if triggered by automated detection..." },
              { "id": "1.2.2", "title": "Sanctions Screening Hit Pathway",
                "description": "Classify under Sanctions pathway if arising from a potential match..." }
            ]
          }
        ]
      },
      {
        "id": "2",
        "title": "Customer Due Diligence and Profile Review",
        "description": "Assess completeness and quality of CDD information",
        "rules": [ "..." ]
      }
    ]
  },
  "instructions": "You are an AML Investigator. Analyze transaction alerts by reviewing alert metadata, classifying the investigation type, performing CDD checks, and evaluating typology-specific indicators. Support every finding with evidence from internal systems and external sources. Determine the correct disposition and document clear, defensible reasoning.",
  "dispositions": {
    "classifications": [
      { "name": "File SAR", "description": "Sufficient indicators of suspicious activity" },
      { "name": "Escalate", "description": "Uncertain outcome or significant exposure — route to senior investigator" },
      { "name": "Close - No Issue", "description": "Activity has a reasonable, substantiated business explanation" }
    ]
  }
}
```

### Running the agent

```python
import json
from roe import RoeClient

client = RoeClient()

# Create an AML Investigation agent.
# `policy_version_id` references the Policy (SOP) you created above.
agent = client.agents.create(
    name="AML Investigator",
    engine_class_id="AMLInvestigationEngine",
    description="Investigate transaction alerts against our AML policy",
    input_definitions=[
        {"key": "alert_data", "data_type": "text/plain", "description": "Alert data JSON"},
        {"key": "transaction_data", "data_type": "text/plain", "description": "Transaction data JSON"},
    ],
    engine_config={
        "model": "gpt-5.2-2025-12-11",
        "policy_version_id": "your-policy-version-uuid",   # SOP with guidelines + dispositions
    },
)

# Run the agent with alert data
alert = {
    "transaction_id": "TXN-001",
    "amount": 50000,
    "currency": "USD",
    "flag": "structuring",
    "account_id": "ACC-12345",
}

job = client.agents.run(
    agent_id=str(agent.id),
    alert_data=json.dumps(alert),
)
result = job.wait()

# Parse the investigation output
for output in result.outputs:
    data = json.loads(output.value)

    # Verdict (disposition) — e.g. "Escalate", "Close - No Issue", "SAR Filing"
    print(f"Verdict: {data['result']['verdict']}")

    # Executive summary with evidence citations
    print(f"Summary: {data['result']['summary']}")

    # Walk each policy category's findings
    for category in data["result"].get("findings", []):
        print(f"\nCategory {category['category_id']}: {category.get('summary', '')}")

        for flag in category.get("red_flags", []):
            status = "HIT" if flag["hit"] else "NOT HIT"
            print(f"  [RED  {status}] {flag['title']}")
            for ev in flag.get("evidences", []):
                print(f"    - {ev['evidence_name']}: {ev['evidence_description']}")

        for flag in category.get("green_flags", []):
            status = "HIT" if flag["hit"] else "NOT HIT"
            print(f"  [GREEN {status}] {flag['title']}")

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
| Grok 4.1 Fast | `grok-4-1-fast-reasoning` |
| Grok 4 | `grok-4-0709` |
| Claude Sonnet 4.5 | `claude-sonnet-4-5-20250929` |
| Claude Sonnet 4 | `claude-sonnet-4-20250514` |
| Claude 3.7 Sonnet | `claude-3-7-sonnet-20250219` |
| Claude Haiku 4.5 | `claude-haiku-4-5-20251001` |
| Claude 3.5 Haiku | `claude-3-5-haiku-20241022` |
| Claude Opus 4.6 | `claude-opus-4-6` |
| Claude Opus 4.5 | `claude-opus-4-5-20251101` |
| Claude Opus 4.1 | `claude-opus-4-1-20250805` |
| Claude Opus 4 | `claude-opus-4-20250514` |
| Gemini 3 Pro | `gemini-3-pro-preview` |
| Gemini 3 Flash | `gemini-3-flash-preview` |
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
| Research | `ResearchEngine` |
| Maps Search | `GoogleMapsEntityExtractionEngine` |
| Social Media | `SocialScraperEngine` |
| AML Investigation | `AMLInvestigationEngine` |
| Fraud Investigation | `FraudInvestigationEngine` |
| Data Analysis | `DataAnalysisEngine` |
| Marketplace Storefront | `MarketplaceStorefrontAnalysisEngine` |
| Merchant Risk | `MerchantRiskAnalysisEngine` |
| Merchant Underwriting | `MerchantUnderwritingEngine` |
| Product Policy | `ProductPolicyEngine` |

## Links

- [Roe AI](https://www.roe-ai.com/)
- [API Docs](https://docs.roe-ai.com)
