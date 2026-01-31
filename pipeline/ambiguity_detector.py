# pipeline/ambiguity_detector.py

AMBIGUOUS_TERMS = [
    "reasonable",
    "as applicable",
    "from time to time",
    "sole discretion",
    "may be determined",
    "if required",
    "as decided",
    "as mutually agreed"
]

def detect_ambiguity(clause_text: str):
    """
    Returns ambiguity flag and reasons
    """

    text = clause_text.lower()
    found = []

    for term in AMBIGUOUS_TERMS:
        if term in text:
            found.append(term)

    return {
        "is_ambiguous": len(found) > 0,
        "terms": found
    }
