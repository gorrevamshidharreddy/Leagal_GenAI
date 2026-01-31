def normalize_text(text, language):
    """
    For hackathon:
    - English → returned as-is
    - Hindi → placeholder normalization (future translation hook)
    """

    if language.lower() == "hindi":
        return (
            "[Translated from Hindi]\n\n" + text
        )

    return text
