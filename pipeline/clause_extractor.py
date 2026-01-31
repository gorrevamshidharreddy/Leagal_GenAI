import re


def extract_clauses(text):
    """
    Splits contract text into clauses based on numbering and headings.
    Returns a list of clause objects.
    """

    clauses = []

    # Normalize text
    clean_text = text.replace("\r", "\n")

    # Split by numbered clauses like 1., 1.1, 2.3 etc.
    pattern = r"\n(?=\d+\.\d+|\n\d+\.)"
    parts = re.split(pattern, clean_text)

    clause_id = 1

    for part in parts:
        part = part.strip()
        if len(part) < 40:
            continue

        title = part.split("\n")[0][:80]

        clauses.append({
            "clause_id": f"C{clause_id}",
            "title": title,
            "text": part
        })

        clause_id += 1

    return clauses
