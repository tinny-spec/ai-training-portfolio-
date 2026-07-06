"""
clean_text.py

Basic text-cleaning utility used before annotation, classification,
or dataset quality checks.
"""

import re
import string


def clean_text(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", " ", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


if __name__ == "__main__":
    samples = [
        "  I ABSOLUTELY Love this Phone!!  ",
        "This product   stopped working... after two days.",
    ]
    for s in samples:
        print(f"{s!r} -> {clean_text(s)!r}")
