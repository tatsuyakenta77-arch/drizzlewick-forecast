#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for the
invented city of Drizzlewick to /output/entry.txt.

Fully deterministic: the forecast is a constant string, so every run
produces byte-identical output.
"""

import os

ENTRY = (
    "Drizzlewick: light rain all morning, 14°C, puddles deep enough to "
    "baptize your shoes. The 8:15 bus is late, but the rain is never late."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 140
MIN_CHARS = 1


def validate_entry(text: str) -> None:
    """Enforce the gate: 1-140 characters, one non-blank line."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, must be "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be one non-blank line")


def main() -> None:
    validate_entry(ENTRY)
    text = ENTRY
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file holds exactly the entry text.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
