#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter, written by main.py.

The program writes exactly one line of UTF-8 text to /output/entry.txt
(or $ENTRY_OUTPUT when set, for local validation).
"""

import os

LINE = "I resign as lighthouse keeper: the sea and I have agreed to see other people."


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
