#!/usr/bin/env python3
"""
Update Agent Example

This example demonstrates how to update, duplicate, and delete agents.
"""

import os

from roe import RoeClient

AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    client = RoeClient()

    # Update agent settings
    updated = client.agents.update(
        agent_id=AGENT_ID,
        name="Renamed Agent",
        disable_cache=False,
        cache_failed_jobs=True,
    )
    print(f"Updated agent: {updated.name}")

    # Duplicate an agent (creates a new agent and returns its current version)
    new_version = client.agents.duplicate(agent_id=AGENT_ID)
    print(f"Duplicated agent. New agent ID: {new_version.base_agent.id}")
    print(f"New agent's initial version ID: {new_version.id}")
    print(f"New agent name: {new_version.base_agent.name}")

    # Delete an agent (uncomment to use)
    # client.agents.delete(agent_id="agent-to-delete-uuid")
    # print("Agent deleted")


if __name__ == "__main__":
    main()
