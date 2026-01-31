def generate_advice(clause_text, risk_level):
    text = clause_text.lower()

    if risk_level == "High":
        if "terminate" in text:
            return {
                "plain_explanation": "This clause allows the other party to end the contract suddenly.",
                "business_impact": "Your business may lose income or operations without notice.",
                "suggestion": "Ask for a minimum notice period (e.g., 30 or 60 days) before termination."
            }

        if "indemnify" in text:
            return {
                "plain_explanation": "You are responsible for covering losses caused to the other party.",
                "business_impact": "This could lead to heavy financial liability.",
                "suggestion": "Limit indemnity to direct damages and add a financial cap."
            }

        if "non-compete" in text:
            return {
                "plain_explanation": "This clause restricts you from working with competitors.",
                "business_impact": "It may block future business opportunities.",
                "suggestion": "Reduce duration, geography, or remove non-compete obligations."
            }

    if risk_level == "Medium":
        return {
            "plain_explanation": "This clause creates legal obligations that need attention.",
            "business_impact": "May increase compliance or operational burden.",
            "suggestion": "Clarify responsibilities and add reasonable limits."
        }

    return {
        "plain_explanation": "This clause is standard and low risk.",
        "business_impact": "No major business impact.",
        "suggestion": "No immediate action required."
    }
