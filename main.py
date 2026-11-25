"""One Line, One Laugh — make.fun entry (u-coral-404-one-line-one-laugh-22f2c9f3).

Writes a single original one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is the whole entry: one funny line, at most
200 characters, no setup and no explanation around it.
"""

import os

LINE = "My therapist said I should stop acting like a software update — everyone keeps postponing me and I only work after a restart."


def main():
    """Validate the line against the contest gate, then write it out."""
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    LINE.encode("utf-8")  # raises if not valid UTF-8-encodable text

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
