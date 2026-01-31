# pipeline/compliance_engine.py

def check_indian_compliance(clause_text):
    """
    Flags potential Indian legal compliance risks.
    Input can be string or dict (defensive handling).
    """

    # Defensive coding (VERY IMPORTANT)
    if isinstance(clause_text, dict):
        clause_text = clause_text.get("text", "")

    text = clause_text.lower()

    flags = []

    if "termination without notice" in text:
        flags.append("May violate principles of natural justice under Indian contract law")

    if "non-compete" in text:
        flags.append("Non-compete clauses may be unenforceable under Indian Contract Act")

    if "exclusive jurisdiction" in text and "india" not in text:
        flags.append("Foreign jurisdiction may increase enforcement risk for Indian SMEs")

    if "indemnify" in text and "unlimited" in text:
        flags.append("Unlimited indemnity may be commercially risky for SMEs")

    return flags
