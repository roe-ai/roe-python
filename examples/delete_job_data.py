#!/usr/bin/env python3
"""
Delete Job Data Example

This example demonstrates how to delete persisted job data.
"""

import os

from roe import RoeClient

JOB_ID = os.getenv("JOB_ID", "your-job-uuid-here")


def main():
    client = RoeClient()

    # Delete job data (inputs and sanitize outputs)
    # Only works for completed, failed, or cancelled jobs
    result = client.agents.delete_job_data(job_id=JOB_ID)

    print(f"Status: {result.status}")
    print(f"Files deleted: {result.deleted_count}")
    print(f"Files failed: {result.failed_count}")
    print(f"Outputs sanitized: {result.outputs_sanitized}")

    if result.errors:
        print("Errors:")
        for error in result.errors:
            print(f"  - {error}")


if __name__ == "__main__":
    main()

