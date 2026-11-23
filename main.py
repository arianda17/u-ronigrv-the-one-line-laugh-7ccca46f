"""The One-Line Laugh entrypoint.

Writes the competition entry line to /output/entry.txt.
"""

LINE = "I bought a $14 salad and the app asked if I wanted to round up for charity — yes, please round it down to free."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.endswith(".") and LINE.count(".") == 1, "line must be a single sentence"
    assert LINE.strip(), "line must not be only whitespace"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
