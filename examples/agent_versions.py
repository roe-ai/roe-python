#!/usr/bin/env python3
"""
Agent Versions Example

This example demonstrates how to work with agent versions:
- List all versions of a base agent
- Get the current version with input definitions
- Run a specific version

Configuration:
- Set ROE_API_KEY environment variable
- Set ROE_ORGANIZATION_ID environment variable
- Set AGENT_ID to the UUID of the agent you want to explore

Or modify the constants below:
"""

import os

from roe import NotFoundError, RoeClient

# Configuration - modify these or use environment variables
API_KEY = os.getenv("ROE_API_KEY", "your-api-key-here")
ORGANIZATION_ID = os.getenv("ROE_ORGANIZATION_ID", "your-organization-uuid-here")
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    """Explore agent versions."""

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
        print(f"🔍 Exploring versions for agent: {AGENT_ID}\n")

        # Step 1: Get the base agent info
        print("1️⃣ Getting base agent information...")
        base_agent = client.agents.get_base_agent(AGENT_ID)
        print(f"   Agent: {base_agent.name}")
        print(f"   Engine: {base_agent.engine_name}")
        if base_agent.current_version_id:
            print(f"   Current Version ID: {base_agent.current_version_id}")
        print()

        # Step 2: List all versions
        print("2️⃣ Listing all versions...")
        versions = client.agents.list_versions(AGENT_ID)
        print(f"   Found {len(versions)} versions:\n")

        for i, version in enumerate(versions, 1):
            print(f"   {i}. {version.version_name}")
            print(f"      ID: {version.id}")
            print(f"      Created: {version.created_at}")
            print(f"      Readonly: {version.readonly}")
            if version.description:
                print(f"      Description: {version.description}")
            print()

        # Step 3: Get current version with input definitions
        print("3️⃣ Getting current version details...")
        try:
            current_version = client.agents.get_current_version(AGENT_ID)
            print(f"   Current Version: {current_version.version_name}")
            print(f"   Version ID: {current_version.id}")
            print()

            # Show input definitions
            if current_version.input_definitions:
                print("   📝 Input Definitions:")
                for input_def in current_version.input_definitions:
                    print(f"      • {input_def.key} ({input_def.data_type})")
                    print(f"        {input_def.description}")
                    if input_def.example:
                        print(f"        Example: {input_def.example}")
                    if input_def.accepts_multiple_files:
                        print("        Accepts multiple files: Yes")
                    print()
            else:
                print("   📝 No input definitions found")

            # Show engine configuration
            if current_version.engine_config:
                print("   ⚙️  Engine Config:")
                for key, value in current_version.engine_config.items():
                    print(f"      {key}: {value}")
                print()

        except Exception as e:
            print(f"   ❌ Could not get current version: {e}")
            print()

        # Step 4: Demonstrate running different versions
        if versions:
            print("4️⃣ Example: Running the current version...")
            print("   (This would use the base agent's current version)")
            print(f"   Command: client.agents.run(agent_id='{AGENT_ID}', ...)")
            print()

            print("   Alternative: Running a specific version...")
            first_version = versions[0]
            print(
                f"   Command: version = client.agents.get_version('{AGENT_ID}', '{first_version.id}')"
            )
            print("   Then: version.run(...)")
            print()

    except NotFoundError:
        print(f"❌ Agent not found: {AGENT_ID}")
        print("Please check the agent ID and your organization access")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    main()
