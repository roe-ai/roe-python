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

    # Duplicate an agent (creates a new agent with different ID)
    new_agent = client.agents.duplicate(agent_id=AGENT_ID)
    print(f"Duplicated agent, new agent ID: {new_agent.id}")
    print(f"New agent name: {new_agent.name}")

    # Delete an agent (uncomment to use)
    # client.agents.delete(agent_id="agent-to-delete-uuid")
    # print("Agent deleted")


if __name__ == "__main__":
    main()
