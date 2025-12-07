#!/usr/bin/env python3
"""
Run Agent with Timeout Example

This example demonstrates how to configure and handle timeouts to prevent
jobs from getting stuck indefinitely. This is especially useful for:
- Production environments where jobs need strict SLAs
- Long-running agents that may occasionally hang
- Batch processing where one stuck job shouldn't block the workflow
"""

import os
import time

from roe import RoeClient

# Configuration - set these environment variables
AGENT_ID = os.getenv("AGENT_ID", "your-agent-uuid-here")


def example_single_job_with_timeout():
    """Example 1: Single job with custom timeout"""
    print("\n=== Example 1: Single Job with Custom Timeout ===")

    client = RoeClient()

    # Run agent with 10-minute timeout (600 seconds)
    # Default is 7200 seconds (2 hours)
    job = client.agents.run(
        agent_id=AGENT_ID,
        timeout_seconds=600,  # 10 minutes
        prompt="Analyze this text for sentiment and key themes.",
    )

    print(f"Job started: {job.id}")
    print("Waiting for completion (max 10 minutes)...")

    try:
        # Wait for result with the configured timeout
        result = job.wait()

        print("✓ Job completed successfully!")
        print(f"  Input tokens: {result.input_tokens}")
        print(f"  Output tokens: {result.output_tokens}")

        for output in result.outputs:
            print(f"  {output.key}: {output.value}")

    except TimeoutError as e:
        print(f"✗ Job exceeded timeout: {e}")
        print("  The job may be stuck or taking longer than expected.")
        print("  You can check job status later or retry with a longer timeout.")


def example_default_timeout():
    """Example 2: Using default timeout (2 hours)"""
    print("\n=== Example 2: Default Timeout (7200 seconds / 2 hours) ===")

    client = RoeClient()

    # When timeout_seconds is not specified, defaults to 7200 seconds
    job = client.agents.run(
        agent_id=AGENT_ID,
        prompt="Process this document thoroughly.",
    )

    print(f"Job started: {job.id}")
    print("Waiting with default 2-hour timeout...")

    try:
        job.wait()
        print("✓ Job completed successfully!")

    except TimeoutError as e:
        print(f"✗ Job exceeded default timeout: {e}")


def example_batch_with_timeout():
    """Example 3: Batch jobs with timeout"""
    print("\n=== Example 3: Batch Jobs with Timeout ===")

    client = RoeClient()

    # Process multiple inputs with 15-minute timeout
    batch_inputs = [
        {"text": "Analyze sentiment: I love this product!"},
        {"text": "Analyze sentiment: This is terrible."},
        {"text": "Analyze sentiment: It's okay, nothing special."},
    ]

    batch = client.agents.run_many(
        agent_id=AGENT_ID,
        batch_inputs=batch_inputs,
        timeout_seconds=900,  # 15 minutes for all jobs
    )

    print(f"Batch started with {len(batch.job_ids)} jobs")
    print("Waiting for all jobs to complete (max 15 minutes)...")

    try:
        results = batch.wait()

        print(f"✓ All {len(results)} jobs completed successfully!")
        for i, result in enumerate(results, 1):
            print(f"\n  Job {i}:")
            for output in result.outputs:
                print(f"    {output.key}: {output.value}")

    except TimeoutError as e:
        print(f"✗ Batch exceeded timeout: {e}")
        print("  Some jobs may still be running on the server.")


def example_override_timeout_in_wait():
    """Example 4: Override timeout when calling wait()"""
    print("\n=== Example 4: Override Timeout in wait() ===")

    client = RoeClient()

    # Create job with 10-minute default timeout
    job = client.agents.run(
        agent_id=AGENT_ID, timeout_seconds=600, prompt="Quick analysis task"
    )

    print(f"Job started: {job.id}")
    print("Default timeout: 600 seconds")

    try:
        # But override with shorter 2-minute timeout when waiting
        print("Overriding with 2-minute timeout for this wait...")
        job.wait(timeout=120)  # 2 minutes

        print("✓ Job completed within 2 minutes!")

    except TimeoutError as e:
        print(f"✗ Job didn't complete within 2 minutes: {e}")
        print("  You could retry with the original 10-minute timeout:")

        try:
            # Retry with original timeout
            job.wait(timeout=600)
            print("✓ Job completed with longer timeout!")
        except TimeoutError:
            print("✗ Job still didn't complete")


def example_production_use_case():
    """Example 5: Production use case with error handling"""
    print("\n=== Example 5: Production Use Case ===")

    client = RoeClient()

    # In production, you might have strict SLAs
    MAX_PROCESSING_TIME = 300  # 5 minutes SLA

    job = client.agents.run(
        agent_id=AGENT_ID,
        timeout_seconds=MAX_PROCESSING_TIME,
        prompt="Time-sensitive production task",
    )

    print(f"Job started: {job.id}")
    start_time = time.time()

    try:
        job.wait()
        elapsed = time.time() - start_time

        print(f"✓ Job completed in {elapsed:.1f} seconds")

        # Check if we met SLA (with buffer)
        if elapsed < MAX_PROCESSING_TIME * 0.9:
            print("  ✓ Met SLA with headroom")
        else:
            print("  ⚠ Met SLA but close to timeout - consider optimization")

    except TimeoutError:
        elapsed = time.time() - start_time
        print(f"✗ Job exceeded {MAX_PROCESSING_TIME}s SLA (took >{elapsed:.1f}s)")

        # In production, you might:
        # 1. Log the timeout for monitoring
        # 2. Send an alert
        # 3. Retry with different parameters
        # 4. Return a fallback result
        print("  → Logging timeout event for monitoring...")
        print("  → Could retry or use fallback strategy")


def example_checking_status_manually():
    """Example 6: Manual status checking with timeout awareness"""
    print("\n=== Example 6: Manual Status Checking ===")

    client = RoeClient()

    job = client.agents.run(
        agent_id=AGENT_ID, timeout_seconds=300, prompt="Task with manual monitoring"
    )

    print(f"Job started: {job.id}")
    print("Monitoring status manually...")

    start_time = time.time()
    timeout = 60  # Check for 1 minute

    while (time.time() - start_time) < timeout:
        status = job.retrieve_status()
        elapsed = time.time() - start_time

        print(f"  [{elapsed:.1f}s] Status: {status.status}")

        if status.status in (2, 6):  # SUCCESS or CACHED
            job.retrieve_result()
            print("✓ Job completed successfully!")
            break
        elif status.status in (3, 4):  # FAILURE or CANCELLED
            print("✗ Job failed or was cancelled")
            break

        time.sleep(5)  # Check every 5 seconds
    else:
        print(f"✗ Job didn't complete within {timeout} seconds")
        print("  Job may still be running on the server")


def main():
    """Run all examples"""
    print("=" * 70)
    print("ROE AI SDK - Timeout Configuration Examples")
    print("=" * 70)

    # Run examples
    example_single_job_with_timeout()
    example_default_timeout()
    example_batch_with_timeout()
    example_override_timeout_in_wait()
    example_production_use_case()
    example_checking_status_manually()

    print("\n" + "=" * 70)
    print("Examples completed!")
    print("\nKey Takeaways:")
    print("- Default timeout is 7200 seconds (2 hours)")
    print("- Set timeout_seconds when calling run() or run_many()")
    print("- TimeoutError is raised when jobs exceed the timeout")
    print("- Timeouts prevent indefinite waiting on stuck jobs")
    print("- Production systems should set appropriate timeouts for their SLAs")
    print("=" * 70)


if __name__ == "__main__":
    main()
