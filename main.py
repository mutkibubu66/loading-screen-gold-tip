#!/usr/bin/env python3
"""Write one original loading-screen tip, at most 200 characters.

Pure standard library, no network. Writes the tip to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE = (
    "Loading tip: the bar isn't stuck \u2014 it's on a union-mandated "
    "break. Please hold while it files the paperwork."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
