#!/usr/bin/env python3
"""
List Agents Example

This example demonstrates how to list base agents in your organization.
"""

from roe import RoeClient


def main():
    # Initialize client
    client = RoeClient()

    # List agents
    response = client.agents.list(page_size=5)

    # Display results
    print(f"Found {response.count} agents:")
    for agent in response.results:
        print(f"- {agent.name} (ID: {agent.id})")


if __name__ == "__main__":
    main()
