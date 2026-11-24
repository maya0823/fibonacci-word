#!/usr/bin/env python3
"""Generate prefixes of the infinite Fibonacci word."""

import sys


def generate_fibonacci_word(length: int) -> str:
    """Return the first `length` symbols of the Fibonacci word."""
    if length <= 0:
        return ""
    a = "0"
    b = "01"
    while len(a) < length:
        a, b = b, b + a
    return a[:length]


def count_symbols(word: str) -> tuple[int, int]:
    """Return (number of 0s, number of 1s)."""
    return word.count("0"), word.count("1")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python fibonacci_word.py <length>")
        print("Example: python fibonacci_word.py 20")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Length must be a positive integer.")
        sys.exit(1)

    if length < 0:
        print("Length must be non-negative.")
        sys.exit(1)

    word = generate_fibonacci_word(length)
    zeros, ones = count_symbols(word)

    print(word)
    print(f"Length: {len(word)}")
    print(f"0s: {zeros}, 1s: {ones}")


if __name__ == "__main__":
    main()
