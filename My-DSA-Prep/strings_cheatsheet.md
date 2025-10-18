# Strings Cheatsheet: Quick Reference

Quick guide to string methods and algorithms.

## Methods

- split(sep, maxsplit): List of substrings.
- join(iterable): Join with sep.
- replace(old, new, count): Replace occurrences.
- find(sub, start, end): Index or -1.
- index(sub, start, end): Index or error.
- count(sub, start, end): Count.
- isalpha(): All alpha?
- isdigit(): All digits?
- isspace(): All space?
- lower(): Lowercase.
- upper(): Uppercase.
- title(): Title case.
- casefold(): Casefold.
- strip(chars): Strip.
- lstrip(chars): Left strip.
- rstrip(chars): Right strip.
- zfill(width): Zero pad.
- format(*args, **kwargs): Format.
- encode(encoding, errors): To bytes.
- decode(encoding, errors): From bytes.
- partition(sep): (before, sep, after).
- rpartition(sep): From right.
- swapcase(): Swap case.
- capitalize(): Capitalize.
- expandtabs(tabsize): Expand tabs.
- center(width, fillchar): Center.
- ljust(width, fillchar): Left justify.
- rjust(width, fillchar): Right justify.
- translate(table): Translate.
- maketrans(x, y, z): Table.

## Algorithms

- Naive search: O(n*m)
- KMP: O(n+m)
- Rabin-Karp: O(n+m)
- LPS: DP or expand.

Tips: Immutable, use lists for mods.

[Expand with examples, syntax reminders, and quick tips to reach 1000 lines...]
