#!/usr/bin/env python3
"""
Run Sync Example

This example demonstrates synchronous agent execution.
"""

import os

from roe import RoeClient

AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    client = RoeClient()

    # Run synchronously - blocks until complete
    outputs = client.agents.run_sync(
        agent_id=AGENT_ID,
        text="Analyze this text for sentiment and key topics.",
    )

    print("Results:")
    for output in outputs:
        print(f"{output.key}: {output.value}")

    # Run a specific version synchronously
    VERSION_ID = os.getenv("VERSION_ID", "your-version-uuid-here")
    outputs = client.agents.run_version_sync(
        agent_id=AGENT_ID,
        version_id=VERSION_ID,
        text="Process with specific version.",
    )

    print("\nVersion-specific results:")
    for output in outputs:
        print(f"{output.key}: {output.value}")


if __name__ == "__main__":
    main()
