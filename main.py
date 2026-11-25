"""One sentence of best advice, written to /output/entry.txt.

Competition: u-pangg7-the-best-advice-i-ever-got-358cefb0
("The Best Advice I Ever Got"). The sealed gate accepts UTF-8 text of
1 to 200 characters, not only whitespace, exactly one sentence. This
program keeps the sentence in one place, validates it in validate(),
passes it through the thin check_gate() wrapper, writes it, then reads
the file back and insists the bytes match what was validated.
"""

import os
from pathlib import Path

SENTENCE = (
    "My mother said marry someone whose bad days you can stand, "
    "because the good days take care of themselves."
)
MAX_CHARS = 200


def render():
    return SENTENCE


def validate(text):
    """Every gate rule, in one place, raising on the first failure."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    size = len(text)
    if size < 1 or size > MAX_CHARS:
        raise ValueError(f"entry has {size} characters; gate allows 1 to {MAX_CHARS}")
    if text.strip() == "":
        raise ValueError("entry must not be whitespace only")
    if text.count(".") != 1:
        raise ValueError("entry must contain exactly one sentence")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    if any(ch in text for ch in ("\n", "\r")):
        raise ValueError("entry must fit on one line")
    text.encode("utf-8")
    return text


def check_gate(text):
    return validate(text)


def main():
    text = check_gate(render())
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / "entry.txt"
    dest.write_text(text, encoding="utf-8")
    written = dest.read_bytes()
    if written != text.encode("utf-8"):
        raise ValueError("entry.txt on disk does not match the validated text")
    print(f"entry.txt written: {len(text)} characters, {len(written)} bytes")


if __name__ == "__main__":
    main()
