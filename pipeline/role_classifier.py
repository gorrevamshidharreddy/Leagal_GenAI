def classify_clause_role(clause_text):
    text = clause_text.lower()

    if "shall not" in text or "must not" in text:
        return {
            "category": "Prohibition",
            "reason": "Clause restricts an action"
        }

    if "shall" in text or "must" in text:
        return {
            "category": "Obligation",
            "reason": "Clause imposes a mandatory duty"
        }

    if "may" in text or "entitled to" in text:
        return {
            "category": "Right",
            "reason": "Clause grants permission or benefit"
        }

    return {
        "category": "Other",
        "reason": "Informational or descriptive clause"
    }

