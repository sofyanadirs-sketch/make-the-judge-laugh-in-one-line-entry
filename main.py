"""Make the Judge Laugh in One Line.

Writes one funny line (69 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3.13 standard library only, no network, no randomness, no clock:
every run writes byte-identical output.
"""

import os

LINE = "I asked AI to write my will; it left everything to my search history."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
