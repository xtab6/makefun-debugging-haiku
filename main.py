#!/usr/bin/env python3
"""Write one debugging haiku (strict 5-7-5, <=200 chars) to /output/entry.txt.

Haiku:
  A breakpoint blinks red          (5: A-break-point-blinks-red)
  the log says nothing happened    (7: the-log-says-noth-ing-hap-pened)
  the bug wore my face             (5: the-bug-wore-my-face)
"""

import os

HAIKU = (
    "A breakpoint blinks red\n"
    "the log says nothing happened\n"
    "the bug wore my face\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clean only the contents of /output, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for f in files:
                    os.remove(os.path.join(root, f))
                for d in dirs:
                    os.rmdir(os.path.join(root, d))
            os.rmdir(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
