#!/usr/bin/env python3
"""
Manage Policies Example

Demonstrates the full policy lifecycle: create, list, retrieve,
create new versions, update metadata, and delete.
"""

from roe import RoeClient


def main():
    client = RoeClient()

    # Create a policy with an initial version
    policy = client.policies.create(
        name="Fraud Investigation SOP",
        description="Standard operating procedure for fraud alert investigation",
        content={
            "guidelines": {
                "categories": [
                    {
                        "title": "Transaction Patterns",
                        "rules": [
                            {
                                "title": "Velocity anomaly",
                                "description": "Unusual spike in transaction frequency",
                                "flag": "RED_FLAG",
                            },
                            {
                                "title": "Amount anomaly",
                                "description": "Transaction amounts significantly above historical average",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                    {
                        "title": "Account Behavior",
                        "rules": [
                            {
                                "title": "New account rapid activity",
                                "description": "High transaction volume within first 30 days of account opening",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                ]
            },
            "instructions": "Investigate the alert against each category. Gather evidence from available data sources. Cite specific transactions and patterns.",
            "dispositions": {
                "classifications": [
                    {
                        "name": "Fraudulent",
                        "description": "Confirmed fraud indicators found",
                    },
                    {
                        "name": "Legitimate",
                        "description": "Activity has legitimate explanation",
                    },
                    {"name": "Escalate", "description": "Needs senior analyst review"},
                ]
            },
            "summary_template": {
                "template": "Investigation of {{subject}} resulted in {{verdict}}. {{findings_count}} findings identified."
            },
        },
    )
    print(f"Created policy: {policy.name} (ID: {policy.id})")
    print(f"Current version: {policy.current_version_id}")

    # List all policies
    all_policies = client.policies.list()
    print(f"\nTotal policies: {all_policies.count}")
    for p in all_policies.results:
        print(f"  - {p.name} ({p.id})")

    # Retrieve the policy
    retrieved = client.policies.retrieve(str(policy.id))
    print(f"\nRetrieved: {retrieved.name}")

    # List versions (paginated)
    versions = client.policies.versions.list(str(policy.id))
    print(f"\nVersions ({versions.count}):")
    for v in versions.results:
        print(f"  - {v.version_name} ({v.id})")

    # Create a new version (automatically becomes current)
    new_version = client.policies.versions.create(
        policy_id=str(policy.id),
        content={
            "guidelines": {
                "categories": [
                    {
                        "title": "Transaction Patterns",
                        "rules": [
                            {
                                "title": "Velocity anomaly",
                                "description": "Unusual spike in transaction frequency",
                                "flag": "RED_FLAG",
                            },
                            {
                                "title": "Amount anomaly",
                                "description": "Transaction amounts significantly above historical average",
                                "flag": "RED_FLAG",
                            },
                            {
                                "title": "Geographic anomaly",
                                "description": "Transactions from unexpected or high-risk geographies",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                ]
            },
            "instructions": "Investigate the alert against each category. Gather evidence from available data sources. Cite specific transactions and patterns. Pay special attention to geographic indicators.",
            "dispositions": {
                "classifications": [
                    {
                        "name": "Fraudulent",
                        "description": "Confirmed fraud indicators found",
                    },
                    {
                        "name": "Legitimate",
                        "description": "Activity has legitimate explanation",
                    },
                    {"name": "Escalate", "description": "Needs senior analyst review"},
                ]
            },
        },
        version_name="v2 - added geographic anomaly rule",
    )
    print(f"\nCreated new version: {new_version.version_name} ({new_version.id})")

    # Retrieve a specific version
    retrieved_version = client.policies.versions.retrieve(
        str(policy.id), str(new_version.id)
    )
    print(f"Retrieved version: {retrieved_version.version_name}")

    # Update policy metadata
    updated = client.policies.update(str(policy.id), name="Fraud Investigation SOP v2")
    print(f"\nUpdated policy name: {updated.name}")

    # Clean up
    client.policies.delete(str(policy.id))
    print("Deleted policy")


if __name__ == "__main__":
    main()
