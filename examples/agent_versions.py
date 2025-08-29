#!/usr/bin/env python3
"""
Agent Versions Example

This example demonstrates how to work with agent versions.
"""

import os

from roe import RoeClient

# Configuration - set these environment variables
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    # Initialize client
    client = RoeClient()

    # List versions
    versions = client.agents.list_versions(AGENT_ID)
    print(f"Found {len(versions)} versions:")
    for version in versions:
        print(f"- {version.version_name} (ID: {version.id})")

    # Get current version with input definitions
    current = client.agents.get_current_version(AGENT_ID)
    print(f"\nCurrent version: {current.version_name}")
    print("Input definitions:")
    for input_def in current.input_definitions:
        print(f"- {input_def.key}: {input_def.description}")


if __name__ == "__main__":
    main()
