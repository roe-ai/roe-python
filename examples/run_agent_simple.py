#!/usr/bin/env python3
"""
Run Agent Simple Example

This example demonstrates how to run an agent with simple text inputs.
"""

import os

from roe import RoeClient

# Configuration - set these environment variables
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    # Initialize client
    client = RoeClient()

    # Run agent with dynamic inputs
    # Input keys depend on your agent's input_definitions (e.g., "text", "document", "url")
    job = client.agents.run(
        agent_id=AGENT_ID,
        text="Hello, please analyze this text.",
    )

    # Wait for result
    result = job.wait()

    # Display results
    print("Results:")
    for output in result.outputs:
        print(f"{output.key}: {output.value}")


if __name__ == "__main__":
    main()
