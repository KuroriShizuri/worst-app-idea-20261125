#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (at most 240 chars) pitching the worst, most useless
app imaginable to /output/entry.txt. Gate: 1-240 UTF-8 characters, not only
whitespace, single sentence.
"""

import sys
from pathlib import Path

ENTRY = (
    "Uber for sighing: an app that dispatches a certified stranger to your "
    "house to sigh loudly beside you, because sighing alone simply does not "
    "scale."
)

MAX_CHARS = 240
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} gate")
    if "\n" in text.strip():
        raise SystemExit("entry must be a single line of text")


def main(argv: list[str]) -> int:
    validate(ENTRY)
    if "--self-test" in argv or "--check" in argv:
        print(f"self-test OK: {len(ENTRY)} chars, within {MAX_CHARS}")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    # Read the file back and verify it is byte-identical to the entry.
    written = OUTPUT.read_text(encoding="utf-8")
    if written != ENTRY:
        raise SystemExit("read-back mismatch: /output/entry.txt != ENTRY")
    validate(written)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT} (read-back verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
