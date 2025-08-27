#!/usr/bin/env python3
"""
Get Agent Example

This example demonstrates how to retrieve a specific base agent by ID
and display its details.

Configuration:
- Set ROE_API_KEY environment variable
- Set ROE_ORGANIZATION_ID environment variable
- Set AGENT_ID to the UUID of the agent you want to retrieve

Or modify the constants below:
"""

import os

from roe import NotFoundError, RoeClient

# Configuration - modify these or use environment variables
API_KEY = os.getenv("ROE_API_KEY", "your-api-key-here")
ORGANIZATION_ID = os.getenv("ROE_ORGANIZATION_ID", "your-organization-uuid-here")
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    """Get a specific base agent by ID."""

    # Initialize the client
    try:
        client = RoeClient(api_key=API_KEY, organization_id=ORGANIZATION_ID)
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set ROE_API_KEY and ROE_ORGANIZATION_ID environment variables")
        return

    if AGENT_ID == "your-agent-uuid-here":
        print(
            "❌ Please set AGENT_ID environment variable or modify the constant in this script"
        )
        return

    try:
        print(f"🔍 Retrieving base agent: {AGENT_ID}\n")

        # Get the specific agent
        agent = client.agents.get_base_agent(AGENT_ID)

        # Display agent details
        print(f"🤖 Agent: {agent.name}")
        print(f"   ID: {agent.id}")
        print(f"   Engine: {agent.engine_name} ({agent.engine_class_id})")
        print(f"   Organization: {agent.organization}")
        print()

        print("📊 Statistics:")
        print(f"   Total Jobs: {agent.job_count}")
        if agent.most_recent_job:
            print(f"   Most Recent Job: {agent.most_recent_job}")
        print()

        print("⚙️  Configuration:")
        print(f"   Cache Disabled: {agent.disable_cache}")
        print(f"   Cache Failed Jobs: {agent.cache_failed_jobs}")
        print()

        if agent.current_version_id:
            print(f"🔖 Current Version: {agent.current_version_id}")
        else:
            print("🔖 No current version set")
        print()

        if agent.creator:
            print(f"👤 Creator: {agent.creator.first_name} {agent.creator.last_name}")
            print(f"   Email: {agent.creator.email}")
        print()

        print(f"📅 Created: {agent.created_at}")

    except NotFoundError:
        print(f"❌ Agent not found: {AGENT_ID}")
        print("Please check the agent ID and your organization access")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    main()
