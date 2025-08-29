#!/usr/bin/env python3
"""
Run Agent Many Example

This example demonstrates how to run an agent with multiple inputs in a batch.
"""

import os

from roe import RoeClient

# Configuration - set these environment variables
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    # Initialize client
    client = RoeClient(base_url="http://localhost:8000/api/")

    # Batch inputs
    inputs_list = [
        {"text": "The quick brown fox jumps over the lazy dog.", "task": "sentiment"},
        {"text": "I absolutely love this product!", "task": "sentiment"},
        {"text": "This is terrible and I want my money back.", "task": "sentiment"},
        {"text": "The weather is okay today.", "task": "sentiment"},
    ]

    # Run agent with multiple inputs
    batch = client.agents.run_many(agent_id=AGENT_ID, inputs_list=inputs_list)

    # Wait for all jobs to complete
    results = batch.wait()

    # Display results
    print(f"Completed {len(results)} jobs:")
    for i, result in enumerate(results, 1):
        print(f"\nJob {i}:")
        for output in result.outputs:
            print(f"  {output.key}: {output.value}")


if __name__ == "__main__":
    main()
