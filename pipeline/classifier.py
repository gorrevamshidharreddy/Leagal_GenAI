from pipeline.config import USE_LLM

def classify_contract(text):
    if not USE_LLM:
        text_lower = text.lower()

        if "employment" in text_lower:
            return {
                "contract_type": "Employment Agreement",
                "confidence": "0.82"
            }
        elif "lease" in text_lower or "rent" in text_lower:
            return {
                "contract_type": "Lease Agreement",
                "confidence": "0.79"
            }
        elif "service" in text_lower:
            return {
                "contract_type": "Service Contract",
                "confidence": "0.76"
            }
        else:
            return {
                "contract_type": "General Commercial Contract",
                "confidence": "0.70"
            }
