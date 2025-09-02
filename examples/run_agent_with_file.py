#!/usr/bin/env python3
"""
Run Agent with File Example

This example demonstrates how to run an agent with a file upload.
The SDK automatically handles file uploads when you provide a file path.
"""

import os

from roe import RoeClient

# Configuration - set these environment variables
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")
FILE_PATH = os.getenv("FILE_PATH", "document.pdf")


def main():
    # Initialize client
    client = RoeClient()

    # Run agent with file upload
    job = client.agents.run(
        agent_id=AGENT_ID,
        document=FILE_PATH,  # File path - SDK handles upload automatically
        prompt="Please analyze this document.",
    )

    # Wait for result
    result = job.wait()

    # Display results
    print("Results:")
    for output in result.outputs:
        print(f"{output.key}: {output.value}")


if __name__ == "__main__":
    main()
