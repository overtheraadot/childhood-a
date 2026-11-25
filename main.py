"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one single line evoking a childhood memory to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default "/output").

The memory: the dial-up modem's screech, the whole family yelling not to
pick up the phone, and a picture loading one slow line at a time.
"""

import os

ENTRY = (
    "The modem screamed its dial-up song while Mum yelled from the kitchen "
    "not to touch the phone, and I watched my favourite cartoon load one "
    "slow line at a time, praying nobody would pick up."
)

MAX_CHARS = 200


def verify(path: str, expected: str) -> None:
    """Re-read the written file and re-check every gate on its contents."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        raw = f.read()
    body = raw.rstrip("\n")
    if raw != expected + "\n":
        raise SystemExit("written file does not match the entry exactly")
    if not body or body != body.strip():
        raise SystemExit("entry is empty or has surrounding whitespace")
    if "\n" in body or "\r" in body:
        raise SystemExit("entry must be a single line")
    if len(body) > MAX_CHARS:
        raise SystemExit(f"entry is {len(body)} chars, over the {MAX_CHARS} limit")
    body.encode("utf-8")


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    verify(path, line)
    print(f"wrote {len(line)} chars to {path} (verified)")


if __name__ == "__main__":
    main()
