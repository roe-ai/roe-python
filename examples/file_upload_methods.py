#!/usr/bin/env python3
"""
File Upload Methods Example

This example demonstrates all the different ways to provide files to agents:
1. File path (string) - automatic upload
2. File object - manual file handling
3. FileUpload object - explicit control
4. Roe file ID - reference existing file
5. In-memory file (BytesIO) - programmatically created content

Configuration:
- Set ROE_API_KEY environment variable
- Set ROE_ORGANIZATION_ID environment variable
- Set AGENT_ID to the UUID of the agent you want to run

Or modify the constants below:
"""

import io
import os

from roe import FileUpload, NotFoundError, RoeClient

# Configuration - modify these or use environment variables
API_KEY = os.getenv("ROE_API_KEY", "your-api-key-here")
ORGANIZATION_ID = os.getenv("ROE_ORGANIZATION_ID", "your-organization-uuid-here")
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")

# Sample content for testing
SAMPLE_CONTENT = """Sample Document Content

This is a test document created programmatically to demonstrate
different file upload methods with the Roe AI Python SDK.

The document contains:
- Multiple paragraphs
- Various text formats
- Sample data for processing

This content can be used to test document analysis agents."""


def demo_file_path_upload(client, agent_id):
    """Method 1: File path (string) - SDK handles file reading."""
    print("📁 Method 1: File path upload")

    # Create a temporary file
    test_file = "temp_upload_test.txt"
    with open(test_file, "w") as f:
        f.write(SAMPLE_CONTENT)

    try:
        # The SDK automatically detects this is a file path and uploads it
        result = client.agents.run(
            agent_id=agent_id,
            document=test_file,  # String path - auto-uploaded
            prompt="Analyze this document",
        )
        print(f"   ✅ Success! Got {len(result)} outputs")

    except Exception as e:
        print(f"   ❌ Error: {e}")

    finally:
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)

    print()


def demo_file_object_upload(client, agent_id):
    """Method 2: File object - manual file handling."""
    print("📂 Method 2: File object upload")

    # Create a temporary file
    test_file = "temp_object_test.txt"
    with open(test_file, "w") as f:
        f.write(SAMPLE_CONTENT)

    try:
        # Open file and pass the file object
        with open(test_file, "rb") as f:
            result = client.agents.run(
                agent_id=agent_id,
                document=f,  # File object
                prompt="Analyze this document",
            )
        print(f"   ✅ Success! Got {len(result)} outputs")

    except Exception as e:
        print(f"   ❌ Error: {e}")

    finally:
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)

    print()


def demo_explicit_file_upload(client, agent_id):
    """Method 3: FileUpload object - explicit control."""
    print("📋 Method 3: Explicit FileUpload object")

    # Create a temporary file
    test_file = "temp_explicit_test.txt"
    with open(test_file, "w") as f:
        f.write(SAMPLE_CONTENT)

    try:
        # Use FileUpload for explicit control over the upload
        file_upload = FileUpload(
            path=test_file,
            filename="custom_document_name.txt",  # Override filename
            mime_type="text/plain",  # Explicit MIME type
        )

        result = client.agents.run(
            agent_id=agent_id,
            document=file_upload,  # Explicit FileUpload object
            prompt="Analyze this document",
        )
        print(f"   ✅ Success! Got {len(result)} outputs")
        print(f"   📄 Uploaded as: {file_upload.effective_filename}")

    except Exception as e:
        print(f"   ❌ Error: {e}")

    finally:
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)

    print()


def demo_file_id_reference(client, agent_id):
    """Method 4: Roe file ID - reference existing file."""
    print("🔗 Method 4: Roe file ID reference")

    # This would use a file already uploaded to Roe
    # Replace with actual file ID from your Roe organization
    roe_file_id = "3c90c3cc-0d44-4b50-8888-8dd25736052a"

    try:
        # The SDK detects UUID strings as file references
        result = client.agents.run(
            agent_id=agent_id,
            document=roe_file_id,  # UUID string - treated as file reference
            prompt="Analyze this document",
        )
        print(f"   ✅ Success! Got {len(result)} outputs")

    except Exception as e:
        print(f"   ❌ Error: {e}")
        print(f"   (This is expected if file ID {roe_file_id} doesn't exist)")

    print()


def demo_in_memory_file(client, agent_id):
    """Method 5: In-memory file (BytesIO)."""
    print("💾 Method 5: In-memory file (BytesIO)")

    try:
        # Create file content in memory
        file_content = SAMPLE_CONTENT.encode("utf-8")
        file_obj = io.BytesIO(file_content)

        result = client.agents.run(
            agent_id=agent_id,
            document=file_obj,  # In-memory file object
            prompt="Analyze this in-memory document",
        )
        print(f"   ✅ Success! Got {len(result)} outputs")

    except Exception as e:
        print(f"   ❌ Error: {e}")

    print()


def main():
    """Demonstrate all file upload methods."""

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
        print(f"🚀 Testing file upload methods with agent: {AGENT_ID}\n")

        # Test each upload method
        demo_file_path_upload(client, AGENT_ID)
        demo_file_object_upload(client, AGENT_ID)
        demo_explicit_file_upload(client, AGENT_ID)
        demo_file_id_reference(client, AGENT_ID)
        demo_in_memory_file(client, AGENT_ID)

        print("🎉 File upload methods demonstration complete!")

    except NotFoundError:
        print(f"❌ Agent not found: {AGENT_ID}")
        print("Please check the agent ID and your organization access")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    main()
