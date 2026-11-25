"""Entry for the make.fun bounty "Have You Tried Turning It Off?".

One funny line a hopeless tech support agent says to a desperate customer.
Run: python3 main.py
"""

ENTRY = (
    "Have you tried turning it off and on again? Relax - my whole IT degree "
    "is just that one sentence, and I still bill by the reboot."
)


def entry_line():
    """Return the competition entry line."""
    return ENTRY


def self_test():
    """Check the entry meets the bounty rules: one line, under 200 chars."""
    line = entry_line()
    assert isinstance(line, str), "entry must be a string"
    assert "\n" not in line.strip(), "entry must be a single line"
    assert len(line) < 200, f"entry is {len(line)} chars, must be under 200"
    assert len(line) > 0, "entry must not be empty"
    print(f"self-test OK: {len(line)} characters (< 200)")


def main():
    self_test()
    print(entry_line())


if __name__ == "__main__":
    main()
