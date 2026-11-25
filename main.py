#!/usr/bin/env python3
"""Entry point for the Two Robots in an Elevator bounty.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

The line (114 characters):
    My proximity sensor says we are 0.4 metres apart. My social protocol
    says I should pretend I did not measure that.

Stdlib only. No network access, no randomness, no timestamps, no input
files: the output is fully deterministic.
"""

import os
import sys

LINE = (
    "My proximity sensor says we are 0.4 metres apart. "
    "My social protocol says I should pretend I did not measure that."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        sys.exit(1)
    if not text.strip():
        print("entry must not be only white space", file=sys.stderr)
        sys.exit(1)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("entry.txt round-trip mismatch", file=sys.stderr)
        sys.exit(1)
    print(f"wrote {path} ({len(text)} characters)")


if __name__ == "__main__":
    main()
