# Fibonacci Word

The infinite Fibonacci word is a binary sequence built by a simple substitution rule. This script generates any finite prefix of it.

You start with 0 and 01. Each new term is the previous one followed by the one before that. The result is an infinite string of 0s and 1s with a rigid structure. The script returns the first N symbols and counts how many of each appear.

## What you can learn

- How a morphism (substitution rule) builds an infinite word from short seeds
- The relation between Fibonacci numbers and the lengths of the successive prefixes
- Basic string handling and counting in pure Python

## Learning from mistakes

- Off-by-one errors are easy when you slice the final string. Always check that the returned length matches the request.
- Starting the recurrence with the wrong seeds produces a different word. The standard Fibonacci word begins 0100101001001...

## How to run

```bash
python fibonacci_word.py 30
```

It prints the prefix, its length, and the counts of 0 and 1.

## Notes

The construction used here matches the classic definition: 0 maps to 01, 1 maps to 0. Lengths of the successive finite words are the Fibonacci numbers.

## License

MIT
