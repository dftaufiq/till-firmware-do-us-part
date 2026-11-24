#!/usr/bin/env python3
"""Till Firmware Do Us Part — make.fun entry.

Writes one funny, heartfelt wedding vow a robot says at its own wedding
to /output/entry.txt. Deterministic: the same line every run.

The line (168 characters, gate allows 1-200):
  "I, B-04, take you to have and to hold — and I promise that when my
   warranty expires in 312 days, I will still choose you, because no
   update ever taught me how to leave."

Why this line (pairwise selection, see leaderboard-top10.md):
  - 2-beat + reveal in the final clause (winner pattern from 15 finalist
    one-liners: vacuum-alibi, pickup-lines, judge-smile).
  - Explicit wedding formula ("take you to have and to hold") — judge
    criterion 1 first: it must BE a robot's wedding vow.
  - Situational laugh, not a bolted-on pun (criterion 2): the warranty
    expires, yet the robot stays — because no update ever taught it how
    to leave.
  - Genuine tenderness under the joke (criterion 3): "I will still
    choose you."
  - Machine-specific detail (criterion 4): warranty, update.
  - Named character (B-04) and a specific number (312 days).
  - Warranty angle is nearly empty in this field (4/275 public titles);
    the crowded "love you through every firmware update" angle is avoided.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)
    if not line.endswith("."):
        print("ERROR: entry must be one sentence ending in a period",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "I, B-04, take you to have and to hold — and I promise that when my "
    "warranty expires in 312 days, I will still choose you, because no "
    "update ever taught me how to leave."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
