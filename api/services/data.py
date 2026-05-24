DOCUMENTS = [
    {
        "id": "AML-001",
        "type": "AML Policy",
        "title": "Structuring and Unusual Velocity",
        "text": (
            "Transactions should be escalated when multiple transfers are intentionally kept below "
            "reporting thresholds, when payment velocity changes abruptly, or when counterparties "
            "are linked to high-risk jurisdictions. Analysts must cite specific transaction evidence "
            "and avoid claiming criminal intent without corroboration."
        ),
    },
    {
        "id": "KYC-014",
        "type": "KYC Guideline",
        "title": "Customer Due Diligence Refresh",
        "text": (
            "KYC refresh is required when customer behavior materially changes, beneficial ownership "
            "information becomes stale, or identity documents expire. Reviews should distinguish "
            "missing documentation from confirmed sanctions exposure."
        ),
    },
    {
        "id": "TX-1049",
        "type": "Transaction",
        "title": "High Velocity Wire Cluster",
        "text": (
            "TX-1049 is a 9,850 EUR outbound wire sent after four same-day transfers between "
            "9,400 and 9,950 EUR. The beneficiary is newly added, the device fingerprint changed "
            "two hours before submission, and the destination bank is in a jurisdiction listed as "
            "enhanced due diligence required."
        ),
    },
    {
        "id": "SUPPORT-087",
        "type": "Conversation",
        "title": "Customer Disputed Transfer",
        "text": (
            "The customer reported that two same-day wire transfers were expected, but a third "
            "transfer to a new beneficiary was not recognized. The agent advised temporary account "
            "controls while the case was reviewed."
        ),
    },
]

MODEL_BENCHMARKS = [
    {"model": "GPT-4.1", "accuracy": 94, "faithfulness": 91, "latency": 620, "compliance": 93},
    {"model": "Llama 3.1", "accuracy": 86, "faithfulness": 83, "latency": 810, "compliance": 84},
    {"model": "Mistral Large", "accuracy": 89, "faithfulness": 86, "latency": 740, "compliance": 88},
    {"model": "Gemma 2", "accuracy": 78, "faithfulness": 76, "latency": 880, "compliance": 79},
]
