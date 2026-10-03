import re


def clean_text(text: str) -> str:

    # Remove extra whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # Remove leading/trailing spaces
    text = text.strip()

    return text