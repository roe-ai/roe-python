#!/usr/bin/env python3
"""
Run Agent with File Example

This example demonstrates how to run an agent with a file upload.
Uses the simple file path approach - the SDK handles the upload automatically.

Configuration:
- Set ROE_API_KEY environment variable
- Set ROE_ORGANIZATION_ID environment variable
- Set AGENT_ID to the UUID of the agent you want to run
- Set FILE_PATH to the path of the file you want to upload

Or modify the constants below:
"""

import os

from roe import NotFoundError, RoeClient

# Configuration - modify these or use environment variables
API_KEY = os.getenv("ROE_API_KEY", "your-api-key-here")
ORGANIZATION_ID = os.getenv("ROE_ORGANIZATION_ID", "your-organization-uuid-here")
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")
FILE_PATH = os.getenv("FILE_PATH", "sample.txt")

# Create a sample file if it doesn't exist
SAMPLE_TEXT = """This is a sample text file created for testing the Roe AI SDK.

It contains some example content that can be processed by AI agents.
The file includes multiple lines and various types of content to demonstrate
the file upload and processing capabilities.

Key features to test:
- Text extraction
- Content analysis
- File processing
- Multi-line handling

This should provide enough content for most agent testing scenarios."""


def create_sample_file():
    """Create a sample file for testing if it doesn't exist."""
    if not os.path.exists(FILE_PATH) and FILE_PATH == "sample.txt":
        with open(FILE_PATH, "w") as f:
            f.write(SAMPLE_TEXT)
        print(f"📄 Created sample file: {FILE_PATH}")


def main():
    """Run an agent with file upload."""

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

    # Create sample file if needed
    create_sample_file()

    # Check if file exists
    if not os.path.exists(FILE_PATH):
        print(f"❌ File not found: {FILE_PATH}")
        print("Please set FILE_PATH environment variable to an existing file")
        return

    try:
        print(f"🚀 Running agent: {AGENT_ID}")
        print(f"📄 With file: {FILE_PATH}\n")

        # Get file size for display
        file_size = os.path.getsize(FILE_PATH)
        print("📊 File info:")
        print(f"   Path: {FILE_PATH}")
        print(f"   Size: {file_size} bytes")
        print()

        # Run the agent with file upload
        # The SDK will automatically detect that FILE_PATH is a file path
        # and handle the upload for us
        print("⏳ Executing agent with file upload...")

        result = client.agents.run(
            agent_id=AGENT_ID,
            document=FILE_PATH,  # This will be auto-uploaded
            prompt="Please analyze this document and provide insights.",
        )

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
        print("- Agent doesn't accept file inputs")
        print("- File format not supported")
        print("- File too large")
        print("- Insufficient credits")
        print("- Network connectivity problems")

    finally:
        # Clean up sample file if we created it
        if FILE_PATH == "sample.txt" and os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
            print(f"🧹 Cleaned up sample file: {FILE_PATH}")

        client.close()


if __name__ == "__main__":
    main()
