"""One Word From Your Ex: write the single word to /output/entry.txt.

The word is "Placeholder": the word an ex would use for someone who was
never the main event, just filling a gap until something better came along.
It lands instantly, it stings because it is true, and it is specific enough
that no near synonym keeps its edge.
"""

import os

WORD = "Placeholder"


def _check(word):
    # Mirror the sealed gate: UTF-8 text, 1 to 24 chars, not only whitespace,
    # and exactly one word, so a bad value fails loudly here instead of
    # silently failing the gate on the server.
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(word) <= 24):
        raise ValueError("entry must be 1 to 24 characters")
    if not word.strip() or word != word.strip():
        raise ValueError("entry must not be only whitespace or padded")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")


def _output_dir():
    for candidate in ("/output",
                      os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")):
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".write-test")
            with open(probe, "w", encoding="utf-8") as f:
                f.write("")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    raise OSError("no writable output directory found")


def main():
    _check(WORD)
    out_dir = _output_dir()
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
