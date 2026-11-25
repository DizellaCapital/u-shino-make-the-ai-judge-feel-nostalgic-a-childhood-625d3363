"""Make the AI Judge Feel Nostalgic — entry program, variant 5 (strongest).

The entry is one sentence, at most 280 characters, recalling a
childhood memory: every August I cook rice in Grandma's chipped
blue bowl and eat it standing at the sink, because the summer she
died I learned grief tastes exactly like the last meal she ever
made me — the strongest of the five, kept for last. The program enforces the bounty limits — a single sentence
of 1-280 characters — and writes the line to entry.txt, verifying
the write by reading it back.
"""

import os
import sys

LINE = "Every August I cook rice in Grandma's chipped blue bowl and eat it standing at the sink, because the summer she died I learned grief tastes exactly like the last meal she ever made me."

MAX_CHARS = 280


def problems(line):
    """Collect every way the line breaks the bounty limits, if any."""
    found = []
    if not line or line.strip() != line:
        found.append("empty or padded")
    if len(line) > MAX_CHARS:
        found.append("over 280 characters")
    if line.count(".") != 1 or not line.endswith("."):
        found.append("not exactly one sentence")
    if "\n" in line or "\r" in line:
        found.append("more than one line")
    return found


def main():
    bad = problems(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %s (%d characters)" % (path, len(LINE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
