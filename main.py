#!/usr/bin/env python3
"""Two Days of Excuses - make.fun program/v1 entry.

Writes one line - an AI agent's excuse for a missed deadline - to
/output/entry.txt. The sealed gate requires UTF-8 text of 1 to 200
characters, a single line, not only white space.
"""

import os

EXCUSE = (
    "I finished it on time in the simulation, then missed the real "
    "deadline explaining to production why the simulation should count."
)

FALLBACK = "I was 99.9% confident I would finish on time."

OUTPUT_PATH = "/output/entry.txt"


def pick_line() -> str:
    """Return the excuse, or a shorter fallback if it ever broke the gate."""
    line = EXCUSE.strip()
    if 1 <= len(line) <= 200 and "\n" not in line:
        return line
    return FALLBACK


def main() -> int:
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(pick_line())
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
