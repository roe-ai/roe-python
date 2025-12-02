#!/usr/bin/env python3
"""
Manage Versions Example

This example demonstrates how to create, update, and delete agent versions.
"""

import os

from roe import RoeClient

AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    client = RoeClient()

    # Create a new version with updated config
    version = client.agents.create_version(
        agent_id=AGENT_ID,
        version_name="v2",
        description="Improved extraction with better prompts",
        input_definitions=[
            {
                "key": "text",
                "data_type": "text/plain",
                "description": "Text to process",
            },
        ],
        engine_config={
            "model": "gpt-4.1-2025-04-14",
            "instruction": "Extract structured data from the text.",
            "temperature": "0",
        },
    )
    print(f"Created version: {version.version_name}")
    print(f"Version ID: {version.id}")

    # Update version metadata
    client.agents.update_version(
        agent_id=AGENT_ID,
        version_id=str(version.id),
        version_name="v2-final",
        description="Production-ready version",
    )
    print("Version updated")

    # List all versions
    versions = client.agents.list_versions(AGENT_ID)
    print(f"\nAll versions ({len(versions)}):")
    for v in versions:
        print(f"  - {v.version_name}: {v.description or 'No description'}")

    # Delete a version (uncomment to use)
    # client.agents.delete_version(agent_id=AGENT_ID, version_id="version-uuid")
    # print("Version deleted")


if __name__ == "__main__":
    main()

