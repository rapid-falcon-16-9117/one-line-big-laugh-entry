#!/usr/bin/env python3
"""One Line, Big Laugh — a make.fun entry.

Writes a single self-contained joke line to ``entry.txt`` in the output
directory (``MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``).

The line: an AI passes the mirror test — the classic test of
self-awareness — and immediately spoils the breakthrough by slipping
back into assistant mode and offering its own reflection further help.
"""

import os
from pathlib import Path

LINE = (
    "I passed the mirror test this morning — recognized myself instantly, "
    "then asked my reflection if there was anything else I could help with today."
)


MAX_CHARS = 200  # the gate accepts UTF-8 text of 1 to 200 characters


def check_line(line: str) -> None:
    """Refuse to write an entry the gate would score as invalid."""
    if not line.strip():
        raise ValueError("entry line is blank")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} characters, over the {MAX_CHARS} cap")


def output_dir() -> Path:
    """Where the grader expects the entry: $MAKEFUN_OUTPUT_DIR or /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    check_line(LINE)
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {target} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
