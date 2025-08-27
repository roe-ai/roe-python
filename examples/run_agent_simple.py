#!/usr/bin/env python3
"""
Run Agent Simple Example

This example demonstrates how to run an agent with simple text inputs only.
No file uploads - just text, numbers, and other basic data types.

Configuration:
- Set ROE_API_KEY environment variable
- Set ROE_ORGANIZATION_ID environment variable
- Set AGENT_ID to the UUID of the agent you want to run

Or modify the constants below:
"""

import os

from roe import NotFoundError, RoeClient

# Configuration - modify these or use environment variables
API_KEY = os.getenv("ROE_API_KEY", "your-api-key-here")
ORGANIZATION_ID = os.getenv("ROE_ORGANIZATION_ID", "your-organization-uuid-here")
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")

# Example inputs - modify these based on your agent's requirements
EXAMPLE_INPUTS = {
    "prompt": "Hello, this is a test message. Please process this text.",
    "temperature": 0.7,
    "max_tokens": 100,
}


def main():
    """Run an agent with simple text inputs."""

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
        print(f"🚀 Running agent: {AGENT_ID}\n")

        # Display the inputs we're sending
        print("📤 Inputs:")
        for key, value in EXAMPLE_INPUTS.items():
            print(f"   {key}: {value}")
        print()

        # Run the agent
        print("⏳ Executing agent...")
        result = client.agents.run(agent_id=AGENT_ID, **EXAMPLE_INPUTS)

        # Display the results
        print("\n✅ Agent completed successfully!\n")
        print("📥 Results:")

        for datum in result:
            print(f"🔹 {datum.key}: {datum.description}")
            print(f"   Type: {datum.data_type}")
            print(f"   Value: {datum.value}")
            if datum.cost:
                print(f"   Cost: ${datum.cost}")
            print()

        if not result:
            print("   No output data returned")

    except NotFoundError:
        print(f"❌ Agent not found: {AGENT_ID}")
        print("Please check the agent ID and your organization access")

    except Exception as e:
        print(f"❌ Error running agent: {e}")
        print("This might be due to:")
        print("- Invalid inputs for this agent")
        print("- Agent configuration issues")
        print("- Insufficient credits")
        print("- Network connectivity problems")

    finally:
        client.close()


if __name__ == "__main__":
    main()
