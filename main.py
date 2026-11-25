"""Best advice, one sentence, to /output/entry.txt.

Competition: u-pangg7-the-best-advice-i-ever-got-358cefb0
("The Best Advice I Ever Got"). The gate wants UTF-8 text of 1 to 200
characters, not only whitespace, exactly one sentence. This program holds
the sentence as a constant, checks it, writes it out, then reads the file
back and compares the bytes so a half-written file can never pass silent.
"""

from pathlib import Path
import os

ADVICE = (
    "My mother said marry someone whose bad days you can stand, "
    "because the good days take care of themselves."
)


def check_entry(sentence):
    """Refuse anything the gate would refuse, with a plain reason."""
    if not isinstance(sentence, str):
        raise TypeError("entry must be text")
    if not 1 <= len(sentence) <= 200:
        raise ValueError(f"entry is {len(sentence)} characters, gate allows 1-200")
    if not sentence.strip():
        raise ValueError("entry must not be only whitespace")
    if sentence.count(".") != 1 or not sentence.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("entry must be a single line")
    sentence.encode("utf-8")
    return sentence


def main():
    sentence = check_entry(ADVICE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(sentence, encoding="utf-8")
    back = target.read_bytes()
    if back != sentence.encode("utf-8"):
        raise ValueError("entry.txt bytes differ from the checked sentence")
    print(f"wrote entry.txt: {len(sentence)} chars, {len(back)} bytes")


if __name__ == "__main__":
    main()
