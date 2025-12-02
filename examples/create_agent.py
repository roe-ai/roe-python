#!/usr/bin/env python3
"""
Create Agent Example

This example demonstrates how to create a new agent with configuration.
"""

from roe import RoeClient


def main():
    client = RoeClient()

    # Create a multimodal extraction agent
    agent = client.agents.create_agent(
        name="Document Summarizer",
        engine_class_id="MultimodalExtractionEngine",
        input_definitions=[
            {
                "key": "document",
                "data_type": "application/pdf",
                "description": "PDF document to summarize",
            },
        ],
        engine_config={
            "model": "gpt-4.1-2025-04-14",
            "instruction": "Summarize the key points of this document.",
            "output_schema": {
                "type": "object",
                "properties": {
                    "summary": {"type": "string", "description": "Document summary"},
                    "key_points": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Key points from the document",
                    },
                },
            },
        },
        version_name="v1",
        description="Initial version",
    )

    print(f"Created agent: {agent.name}")
    print(f"Agent ID: {agent.id}")
    print(f"Current version ID: {agent.current_version_id}")


if __name__ == "__main__":
    main()

