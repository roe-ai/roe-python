#!/usr/bin/env python3
"""
File Upload Methods Example

This example demonstrates different ways to provide files to agents.
"""

import io
import os

from roe import FileUpload, RoeClient

# Configuration - set these environment variables
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    # Initialize client
    client = RoeClient()

    print("Testing different file upload methods:")

    # Method 1: File path (string) - SDK handles upload automatically
    print("\n1. File path upload:")
    job = client.agents.run(
        agent_id=AGENT_ID,
        document="document.pdf",  # File path
        prompt="Analyze this document",
    )
    result = job.wait()
    print(f"Completed with {len(result.outputs)} outputs")

    # Method 2: FileUpload object - explicit control
    print("\n2. FileUpload object:")
    file_upload = FileUpload(
        path="document.pdf", filename="custom_name.pdf", mime_type="application/pdf"
    )
    job = client.agents.run(
        agent_id=AGENT_ID, document=file_upload, prompt="Analyze this document"
    )
    result = job.wait()
    print(f"Completed with {len(result.outputs)} outputs")

    # Method 3: In-memory file
    print("\n3. In-memory file:")
    content = b"Sample document content for testing"
    file_obj = io.BytesIO(content)
    job = client.agents.run(
        agent_id=AGENT_ID, document=file_obj, prompt="Analyze this content"
    )
    result = job.wait()
    print(f"Completed with {len(result.outputs)} outputs")

    # Method 4: Existing Roe file ID
    print("\n4. Roe file ID reference:")
    roe_file_id = "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    job = client.agents.run(
        agent_id=AGENT_ID,
        document=roe_file_id,  # UUID string references existing file
        prompt="Analyze this document",
    )
    result = job.wait()
    print(f"Completed with {len(result.outputs)} outputs")


if __name__ == "__main__":
    main()
