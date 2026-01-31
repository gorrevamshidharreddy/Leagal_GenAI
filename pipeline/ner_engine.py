import re

def extract_entities(text):
    entities = {
        "parties": [],
        "dates": [],
        "amounts": []
    }

    # -------- Parties (simple heuristic) --------
    party_patterns = [
        r"between\s+([A-Z][A-Za-z0-9 &.,]+)",
        r"by\s+and\s+([A-Z][A-Za-z0-9 &.,]+)",
        r"([A-Z][A-Za-z0-9 &.,]+)\s+hereinafter"
    ]

    for pattern in party_patterns:
        matches = re.findall(pattern, text)
        entities["parties"].extend(matches)

    # -------- Dates --------
    date_pattern = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b"
    entities["dates"] = re.findall(date_pattern, text)

    # -------- Amounts --------
    amount_pattern = r"(₹|\$)\s?\d+(?:,\d+)*(?:\.\d+)?"
    entities["amounts"] = re.findall(amount_pattern, text)

    # Remove duplicates
    entities["parties"] = list(set(entities["parties"]))
    entities["dates"] = list(set(entities["dates"]))
    entities["amounts"] = list(set(entities["amounts"]))

    return entities
