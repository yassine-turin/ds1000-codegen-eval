import re

def clean_code(raw: str) -> str:
    """
    Remove ```python fences, HTML tags, and trailing whitespace.
    """
    if raw is None:
        return ""

    # Remove code fences
    raw = re.sub(r"```(?:python)?", "", raw)
    raw = raw.replace("```", "")

    # Remove HTML-like tags
    raw = re.sub(r"<.*?>", "", raw)

    return raw.strip()

