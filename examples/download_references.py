#!/usr/bin/env python3
"""
Download References Example

This example demonstrates how to download reference files from job results.
Reference files include screenshots, HTML, and markdown from web crawling jobs.
"""

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

    # Use the get_references() helper to extract all reference URLs
    references = result.get_references()
    print(f"Found {len(references)} references")

    # Download each reference file
    for ref in references:
        content = client.agents.download_reference(
            job_id=str(job.id),
            resource_id=ref.resource_id,
        )

        # Save to file
        filename = f"downloaded_{ref.resource_id}"
        with open(filename, "wb") as f:
            f.write(content)
        print(f"Saved: {filename} ({len(content)} bytes)")

    # You can also download with the attachment flag for proper Content-Disposition
    # for ref in references:
    #     content = client.agents.download_reference(
    #         job_id=str(job.id),
    #         resource_id=ref.resource_id,
    #         as_attachment=True,
    #     )


if __name__ == "__main__":
    main()
