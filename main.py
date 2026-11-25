"""Have You Tried Turning It Off? — one hopeless tech-support line.

Reads the entry line from entry.txt next to this file and prints it.
"""

from pathlib import Path


def load_line() -> str:
    path = Path(__file__).resolve().parent / "entry.txt"
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise SystemExit("entry.txt is empty — nothing for support to say")
    if len(line) >= 200:
        raise SystemExit("entry line exceeds the 200-character limit")
    return line


def main() -> None:
    line = load_line()
    print(line)


if __name__ == "__main__":
    main()
