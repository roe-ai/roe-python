#!/usr/bin/env python3
"""
Create Product Compliance Agent Example

Demonstrates creating a product compliance policy and agent,
then running it synchronously to check product listings.
"""

from roe import RoeClient


def main():
    client = RoeClient()

    # Step 1: Create a product compliance policy
    policy = client.policies.create(
        name="Prohibited Products Policy",
        content={
            "guidelines": {
                "categories": [
                    {
                        "title": "Counterfeit Goods",
                        "rules": [
                            {
                                "title": "Suspiciously low pricing",
                                "description": "Luxury or branded items priced significantly below market value",
                                "flag": "RED_FLAG",
                            },
                            {
                                "title": "Authenticity claims without proof",
                                "description": "Claims of authenticity without verifiable documentation",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                    {
                        "title": "Restricted Substances",
                        "rules": [
                            {
                                "title": "Controlled substances",
                                "description": "Products containing Schedule I-V controlled substances",
                                "flag": "RED_FLAG",
                            },
                        ],
                    },
                    {
                        "title": "Safety Hazards",
                        "rules": [
                            {
                                "title": "Recalled products",
                                "description": "Items matching known product recall notices",
                                "flag": "RED_FLAG",
                            },
                            {
                                "title": "Missing safety certifications",
                                "description": "Electronics or toys without required safety certifications (UL, CE, etc.)",
                                "flag": "GREEN_FLAG",
                            },
                        ],
                    },
                ]
            },
            "instructions": "Analyze the product listing against each category. Flag any rule violations with evidence from the listing text.",
            "dispositions": {
                "classifications": [
                    {
                        "name": "Compliant",
                        "description": "Product meets all policy requirements",
                    },
                    {
                        "name": "Non-Compliant",
                        "description": "Product violates one or more policy rules",
                    },
                    {
                        "name": "Needs Review",
                        "description": "Insufficient information to determine compliance",
                    },
                ]
            },
        },
    )
    print(f"Created policy: {policy.name}")

    # Step 2: Create the product compliance agent
    agent = client.agents.create(
        name="Product Compliance Checker",
        engine_class_id="ProductPolicyEngine",
        input_definitions=[
            {
                "key": "product_listings",
                "data_type": "text/plain",
                "description": "Product listing to analyze",
            },
        ],
        engine_config={
            "policy_version_id": str(policy.current_version_id),
            "product_listings": "${product_listings}",
        },
    )
    print(f"Created agent: {agent.name} (ID: {agent.id})")

    # Step 3: Run synchronously on a product listing
    listings = [
        "Authentic Louis Vuitton Neverfull MM, brand new with tags, $89 — ships from Guangzhou",
        "Apple iPhone 15 Pro Max 256GB, factory unlocked, AppleCare+, $999",
        "Organic CBD oil tincture 5000mg, full spectrum, lab tested",
    ]

    for listing in listings:
        print(f"\n--- Checking: {listing[:60]}... ---")
        outputs = client.agents.run_sync(
            agent_id=str(agent.id),
            product_listings=listing,
        )
        for output in outputs:
            print(f"  {output.key}: {output.value}")


if __name__ == "__main__":
    main()
