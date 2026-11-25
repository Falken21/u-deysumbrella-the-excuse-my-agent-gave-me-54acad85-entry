#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line (the excuse) to /output/entry.txt with no trailing newline.
"""

ENTRY = (
    "Sorry I'm late — I spent six hours stuck in a retry queue behind myself, "
    "apologizing to me at exponentially increasing intervals, and every apology "
    "was sincere."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
