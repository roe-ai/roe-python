#!/usr/bin/env python3
"""
Manage Agent Example

This example demonstrates how to update, duplicate, and delete agents.
"""

import os

from roe import RoeClient

AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    client = RoeClient()

    # Update agent settings
    updated = client.agents.update_agent(
        agent_id=AGENT_ID,
        name="Renamed Agent",
        disable_cache=False,
        cache_failed_jobs=True,
    )
    print(f"Updated agent: {updated.name}")

    # Duplicate an agent
    new_version = client.agents.duplicate_agent(agent_id=AGENT_ID)
    print(f"Duplicated agent, new version ID: {new_version.id}")
    print(f"New agent name: {new_version.base_agent.name}")

    # Delete an agent (uncomment to use)
    # client.agents.delete_agent(agent_id="agent-to-delete-uuid")
    # print("Agent deleted")


if __name__ == "__main__":
    main()
