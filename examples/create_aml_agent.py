#!/usr/bin/env python3
"""
Create AML Investigation Agent Example

Demonstrates the end-to-end workflow: create a policy, create an AML
investigation agent, run it, interpret results, then update the policy.
"""

from roe import RoeClient


def main():
    client = RoeClient()

    # Step 1: Create the AML investigation policy
    policy = client.policies.create(
        name="AML Investigation Policy",
        content={
            "guidelines": {
                "categories": [
                    {
                        "title": "Structuring",
                        "rules": [
                            {
                                "title": "Cash structuring below reporting thresholds",
                                "description": "Multiple deposits just under $10,000 within short timeframes to avoid CTR filing",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                    {
                        "title": "Layering",
                        "rules": [
                            {
                                "title": "Rapid movement between accounts",
                                "description": "Funds transferred through multiple accounts to obscure origin",
                                "flag": "RED_FLAG",
                                "sub_rules": [
                                    {
                                        "title": "Cross-border wire transfers with no business purpose"
                                    },
                                    {"title": "Shell company intermediaries"},
                                ],
                            },
                        ],
                    },
                ]
            },
            "instructions": "Investigate the alert by analyzing transaction patterns, account relationships, and customer profile. Use available data sources to corroborate or refute each finding.",
            "dispositions": {
                "classifications": [
                    {
                        "name": "Suspicious",
                        "description": "Activity warrants SAR filing",
                    },
                    {
                        "name": "Not Suspicious",
                        "description": "Activity has legitimate business explanation",
                    },
                    {
                        "name": "Needs Escalation",
                        "description": "Requires senior BSA analyst review",
                    },
                ]
            },
            "summary_template": {
                "template": "AML investigation of {{subject}} concluded with disposition: {{verdict}}. {{findings_count}} findings were identified across {{categories_reviewed}} categories."
            },
            "optional": {
                "sar_narrative_template": {
                    "template": "On {{date}}, suspicious activity was identified involving {{subject}}. {{narrative}}"
                }
            },
        },
    )
    print(f"Created policy: {policy.name} (version: {policy.current_version_id})")

    # Step 2: Create the AML investigation agent
    agent = client.agents.create(
        name="AML Investigation Agent",
        engine_class_id="AMLInvestigationEngine",
        input_definitions=[
            {
                "key": "alert_data",
                "data_type": "text/plain",
                "description": "Alert data and context for AML investigation",
            },
        ],
        engine_config={
            "policy_version_id": str(policy.current_version_id),
            "alert_data": "${alert_data}",
        },
    )
    print(f"Created agent: {agent.name} (ID: {agent.id})")

    # Step 3: Run the agent
    job = client.agents.run(
        agent_id=str(agent.id),
        alert_data="Customer John Doe (ID: CUST-9182), 5 cash deposits of $9,500 each over 3 business days at different branch locations. Customer has no prior history of cash transactions.",
    )
    print("Running investigation...")
    result = job.wait()

    # Step 4: Interpret results
    print("\n--- Investigation Results ---")
    for output in result.outputs:
        print(f"\n{output.key}:")
        print(f"  {output.value}")

    # Step 5: Update the policy with a new version
    new_version = client.policies.versions.create(
        policy_id=str(policy.id),
        content={
            "guidelines": {
                "categories": [
                    {
                        "title": "Structuring",
                        "rules": [
                            {
                                "title": "Cash structuring below reporting thresholds",
                                "description": "Multiple deposits just under $10,000 within short timeframes to avoid CTR filing",
                                "flag": "RED_FLAG",
                            },
                            {
                                "title": "Smurfing",
                                "description": "Using multiple individuals to make deposits below reporting thresholds",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                    {
                        "title": "Layering",
                        "rules": [
                            {
                                "title": "Rapid movement between accounts",
                                "description": "Funds transferred through multiple accounts to obscure origin",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                ]
            },
            "instructions": "Investigate the alert by analyzing transaction patterns, account relationships, and customer profile. Pay special attention to potential smurfing networks.",
            "dispositions": {
                "classifications": [
                    {
                        "name": "Suspicious",
                        "description": "Activity warrants SAR filing",
                    },
                    {
                        "name": "Not Suspicious",
                        "description": "Activity has legitimate business explanation",
                    },
                    {
                        "name": "Needs Escalation",
                        "description": "Requires senior BSA analyst review",
                    },
                ]
            },
        },
        version_name="v2 - added smurfing detection",
    )
    print(f"\nUpdated policy to: {new_version.version_name}")

    # Step 6: Update agent to use new policy version and re-run
    client.agents.versions.create(
        agent_id=str(agent.id),
        input_definitions=[
            {
                "key": "alert_data",
                "data_type": "text/plain",
                "description": "Alert data and context for AML investigation",
            },
        ],
        engine_config={
            "policy_version_id": str(new_version.id),
            "alert_data": "${alert_data}",
        },
        version_name="v2 - updated policy",
    )

    job = client.agents.run(
        agent_id=str(agent.id),
        alert_data="Customer John Doe (ID: CUST-9182), 5 cash deposits of $9,500 each over 3 business days at different branch locations.",
    )
    print("Re-running with updated policy...")
    result = job.wait()

    print("\n--- Updated Investigation Results ---")
    for output in result.outputs:
        print(f"\n{output.key}:")
        print(f"  {output.value}")


if __name__ == "__main__":
    main()
