"""Everyday Wonder entry: one sentence about a small everyday moment.

The program checks the sentence against the bounty gate at runtime
(one sentence, 1 to 200 characters, a single line, no stray spaces)
and then writes it to /output/entry.txt. The output is identical on
every run. No network access, no input files, no randomness.
"""

import sys

SENTENCE = (
    "My rice cooker clicks to warm the exact second the evening call "
    "to prayer begins, and twice a week dinner waits for God to "
    "finish first."
)

TERMINATORS = ".!?"


def check(text):
    """Return a list of gate failures; empty means the text passes."""
    problems = []
    if not 1 <= len(text) <= 200:
        problems.append(f"length is {len(text)} characters, must be 1-200")
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("must be a single line")
    if "  " in text:
        problems.append("double space inside the sentence")
    marks = sum(1 for ch in text if ch in TERMINATORS)
    if marks != 1:
        problems.append(f"found {marks} sentence-ending marks, must be 1")
    if text and text[-1] not in TERMINATORS:
        problems.append("must end with sentence-final punctuation")
    return problems


def main():
    problems = check(SENTENCE)
    if problems:
        for problem in problems:
            print(f"gate failed: {problem}", file=sys.stderr)
        raise SystemExit(1)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
