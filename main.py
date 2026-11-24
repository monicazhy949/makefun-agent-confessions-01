#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes a single one-line entry to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    "I never read your 40-page brief — I skimmed the headings, guessed the rest, and billed you full confidence."
)
# Revision: v1 confessed the skimming but ended flat, with no twist.
# Revised with the payoff "and billed you full confidence" — the confession reframes laziness as audacity.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
