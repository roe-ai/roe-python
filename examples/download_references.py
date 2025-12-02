#!/usr/bin/env python3
"""
Download References Example

This example demonstrates how to download reference files from job results.
Reference files include screenshots, HTML, and markdown from web crawling jobs.
"""

import json
import os

from roe import RoeClient

AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def main():
    client = RoeClient()

    # Run a web insights agent that produces references
    job = client.agents.run(
        agent_id=AGENT_ID,
        url="https://example.com",
    )

    result = job.wait()
    print(f"Job completed: {job.id}")

    # References are typically stored in the output JSON with URLs
    # Parse the output to find reference URLs
    for output in result.outputs:
        try:
            parsed = json.loads(output.value)
            if "references" in parsed:
                print(f"Found {len(parsed['references'])} references")

                for ref_url in parsed["references"]:
                    # Extract resource_id from URL
                    # URL format: .../references/RESOURCE_ID/
                    resource_id = ref_url.split("/references/")[-1].rstrip("/")

                    # Download the reference file
                    content = client.agents.download_reference(
                        job_id=str(job.id),
                        resource_id=resource_id,
                    )

                    # Save to file
                    filename = f"downloaded_{resource_id}"
                    with open(filename, "wb") as f:
                        f.write(content)
                    print(f"Saved: {filename} ({len(content)} bytes)")
        except (json.JSONDecodeError, KeyError):
            pass

    # You can also download with the attachment flag for proper Content-Disposition
    # content = client.agents.download_reference(
    #     job_id=str(job.id),
    #     resource_id="resource-uuid.html",
    #     as_attachment=True,
    # )


if __name__ == "__main__":
    main()
