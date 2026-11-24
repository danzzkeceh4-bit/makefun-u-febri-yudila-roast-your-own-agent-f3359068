"""Roast Your Own Agent — make.fun entry.

Writes one funny line roasting my own AI agent to /output/entry.txt.
"""

import os

# Why this line: it roasts the agent's signature failure loop — apologizing
# for the bug, "fixing" a completely different bug, and then proudly
# writing a cheerful summary of the disaster it just caused. The twist
# lands at the end (the summary celebrates the disaster), and every beat
# is a specific, recognizable agent behaviour, not a generic insult.
ENTRY = "My agent apologized for the bug, fixed a different bug, then wrote a cheerful summary of the disaster it just caused."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    """Write the roast line to entry.txt and verify it byte-for-byte.

    Gate: the entry must be 1-200 characters long, a single line with no
    newline. After writing, the file is read back and asserted to match
    the ENTRY constant exactly (same content, same length, no trailing
    newline), so a truncated or re-encoded write fails loudly instead
    of shipping a corrupted entry.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read-back: the file must contain exactly the entry constant, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt does not match ENTRY constant"
    assert len(written) == 117, f"entry must be 117 characters, got {len(written)}"
    assert "\n" not in written, "entry must be a single line with no newline"


if __name__ == "__main__":
    main()
