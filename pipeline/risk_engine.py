# pipeline/risk_engine.py

HIGH_RISK_KEYWORDS = [
    "penalty",
    "indemnify",
    "indemnity",
    "unlimited liability",
    "non-compete",
    "liquidated damages",
    "termination without notice",
    "auto-renewal",
    "lock-in period",
    "exclusive jurisdiction"
]

MEDIUM_RISK_KEYWORDS = [
    "termination",
    "arbitration",
    "jurisdiction",
    "confidentiality",
    "governing law",
    "renewal"
]


def assess_clause_risk(clause_text: str) -> str:
    """
    Returns risk level for a clause: High / Medium / Low
    """

    text = clause_text.lower()

    for word in HIGH_RISK_KEYWORDS:
        if word in text:
            return "High"

    for word in MEDIUM_RISK_KEYWORDS:
        if word in text:
            return "Medium"

    return "Low"
