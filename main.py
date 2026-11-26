"""The Printer Finally Answers.

Writes the office printer's single-line reply to /output/entry.txt.
Standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "You have pressed Print 14 times in the last 40 seconds; "
    "I heard you the first time and I am still on page one."
)


def main() -> None:
    """Write the single-line entry to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
