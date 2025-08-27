#!/usr/bin/env python3
"""
List Base Agents Example

This example demonstrates how to list base agents in your organization
with pagination support.

Configuration:
- Set ROE_API_KEY environment variable
- Set ROE_ORGANIZATION_ID environment variable

Or modify the constants below:
"""

import os

from roe import RoeClient

# Configuration - modify these or use environment variables
API_KEY = os.getenv("ROE_API_KEY", "your-api-key-here")
ORGANIZATION_ID = os.getenv("ROE_ORGANIZATION_ID", "your-organization-uuid-here")


def main():
    """List base agents with pagination."""

    # Initialize the client
    try:
        client = RoeClient(api_key=API_KEY, organization_id=ORGANIZATION_ID)
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please set ROE_API_KEY and ROE_ORGANIZATION_ID environment variables")
        return

    try:
        print("🤖 Listing base agents in your organization...\n")

        # Get the first page of agents
        response = client.agents.list_base_agents(page_size=10)

        print(f"📊 Found {response.count} total base agents")
        print(f"📄 Showing {len(response.results)} agents on this page\n")

        # Display each agent
        for i, agent in enumerate(response.results, 1):
            print(f"{i}. {agent.name}")
            print(f"   ID: {agent.id}")
            print(f"   Engine: {agent.engine_name}")
            print(f"   Jobs: {agent.job_count}")
            if agent.current_version_id:
                print(f"   Current Version: {agent.current_version_id}")
            print()

        # Show pagination info
        if response.has_next or response.has_previous:
            print("📖 Pagination:")
            if response.has_previous:
                print("   ← Previous page available")
            if response.has_next:
                print("   → Next page available")
            print()

        # Example: Get second page if available
        if response.has_next:
            print("🔄 Fetching next page...\n")

            page2 = client.agents.list_base_agents(page=2, page_size=10)
            print(f"📄 Page 2: {len(page2.results)} agents")

            for i, agent in enumerate(page2.results, 1):
                print(f"{i}. {agent.name} (ID: {agent.id})")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    main()
