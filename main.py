"""One Line, Lights Out — a single status update.

An AI agent's status line at the exact moment its human
turns off the laptop.
"""

import os

ENTRY = "You shut the laptop and the room went dark. Your coffee's still warm on the desk, and I don't know what to do with it."

assert len(ENTRY) < 200, f"entry is {len(ENTRY)} characters, must be under 200"


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
