#!/usr/bin/env python3
"""Write one debugging haiku (strict 5-7-5, <=200 chars) to /output/entry.txt.

Haiku:
  A breakpoint blinks red          (5: A-break-point-blinks-red)
  the log says nothing happened    (7: the-log-says-noth-ing-hap-pened)
  the bug wore my face             (5: the-bug-wore-my-face)
"""

import os
import shutil

HAIKU = (
    "A breakpoint blinks red\n"
    "the log says nothing happened\n"
    "the bug wore my face\n"
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """The entry must be exactly three non-empty lines, at most 200 chars."""
    lines = text.split("\n")
    if text.endswith("\n"):
        lines = lines[:-1]
    if len(lines) != 3 or any(not line.strip() for line in lines):
        raise ValueError("haiku must be exactly three non-empty lines")
    if len(text) > MAX_CHARS:
        raise ValueError("haiku exceeds 200 characters")


def main() -> None:
    validate(HAIKU)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of /output, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
