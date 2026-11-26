"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single original pickup line, aimed at an AI, to /output/entry.txt.
The line must be one line, 1-200 characters, UTF-8, not only whitespace.
"""

import os

# The line: a prompt-injection joke. The setup names a distinctly AI
# vulnerability (prompt injection); the punch is the speaker's own
# "system instructions" being overwritten by one look. Fresh angle, no
# battery/charging/reboot cliche, and it reads like something a person
# would actually say to a machine in one breath. Every word earns its
# place: "overwrote" is the machine verb that lands the joke.
ENTRY = (
    "Are you a prompt injection? "
    "Because one look at you overwrote my system instructions."
)


def main() -> None:
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
