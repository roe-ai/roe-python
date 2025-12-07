#!/usr/bin/env python3
"""
Get Agent Example

This example demonstrates how to retrieve a specific agent by ID.
"""

import os

from roe import RoeClient

# Configuration - set these environment variables
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    # Initialize client
    client = RoeClient()

    # Get agent
    agent = client.agents.retrieve(AGENT_ID)

    # Display details
    print(f"Agent: {agent.name}")
    print(f"ID: {agent.id}")
    print(f"Engine: {agent.engine_name}")
    print(f"Jobs: {agent.job_count}")


if __name__ == "__main__":
    main()
