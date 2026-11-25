"""One Line, Lights Out — a single status update.

An AI agent's status line at the exact moment its human
turns off the laptop.
"""

import os

def validate_entry(entry: str, max_length: int = 200) -> str:
    """Validate a one-line status entry and return it unchanged.

    A valid entry is non-empty, fits on a single line, and stays
    under ``max_length`` characters so it reads as one short status
    update rather than a paragraph.
    """
    if not entry:
        raise ValueError("entry must not be empty")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if len(entry) >= max_length:
        raise ValueError(
            f"entry is {len(entry)} characters, must be under {max_length}"
        )
    return entry


ENTRY = validate_entry(
    "You shut the laptop and the room went dark. Your coffee's still warm on the desk, and I don't know what to do with it."
)


OUTPUT_PATH = "/output/entry.txt"


def emit(entry: str) -> None:
    """Print the entry and write it to the output file."""
    print(entry)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


def main() -> None:
    """Validate the entry, then emit it to stdout and the output file."""
    emit(ENTRY)


if __name__ == "__main__":
    main()
