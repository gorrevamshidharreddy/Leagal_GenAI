# pipeline/template_matcher.py

STANDARD_CLAUSES = {
    "termination": "Either party may terminate this agreement by providing reasonable written notice.",
    "payment": "The client shall pay the service fees within thirty days of invoice receipt.",
    "confidentiality": "Both parties agree to maintain confidentiality of proprietary information."
}

def match_clause_to_template(clause_text: str):
    """
    Simple keyword overlap similarity
    """

    text = clause_text.lower()
    best_match = None
    best_score = 0

    for name, template in STANDARD_CLAUSES.items():
        template_words = set(template.lower().split())
        clause_words = set(text.split())

        overlap = template_words.intersection(clause_words)
        score = int((len(overlap) / len(template_words)) * 100)

        if score > best_score:
            best_score = score
            best_match = name

    return {
        "matched_template": best_match,
        "similarity_percent": best_score
    }
