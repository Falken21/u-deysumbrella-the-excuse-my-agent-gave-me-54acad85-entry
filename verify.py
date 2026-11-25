#!/usr/bin/env python3
"""Local check: ENTRY satisfies the competition gate (1-200 chars, one line)."""

import main

line = main.ENTRY
assert 1 <= len(line) <= 200, f"length {len(line)} outside 1..200"
assert line.strip() != "", "line is only whitespace"
assert "\n" not in line, "line must be a single line"
print(f"OK: {len(line)} characters")
print(line)
