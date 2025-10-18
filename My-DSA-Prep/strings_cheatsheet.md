# Strings — one-page cheatsheet

Compact reference for interviews: quick concepts, common patterns, important methods, complexities, and bite-size snippets.
Core ideas
- Python `str` is immutable and sequence-like (0-based indices). Use lists + `''.join()` for heavy concatenation.
- Encode/decode for bytes: `s.encode()` / `b.decode()`.
- Normalize Unicode when comparing: `unicodedata.normalize('NFC', s)`.
Common patterns (pick the right one)
- Two-pointers: palindromes, compare ends — O(n), O(1) extra.
- Sliding window: min-window substring, longest no-repeat substring — typical O(n) with hashmap.
- Rolling hash (Rabin-Karp): substring search, beware collisions.
Important methods (fast lookup)
- len(s) — O(1) | s[i:j] — O(k) to copy | s[::-1] creates reversed copy
- `s.split()`, `'sep'.join(seq)` (use join for concatenation)
- `s.find(sub)` / `s.index(sub)` / `s.count(sub)`
Complexity quick map
- scan / count / simple match: O(n)
- freq-map (Counter): O(n)
- sort chars (anagram key): O(n log n)
Mini snippets (one-liners)
- Reverse words: `' '.join(s.split()[::-1])`
- Rotation check: `s1 in (s2 + s2)`
- Group anagrams: `d[''.join(sorted(s))].append(s)` or use a char-count tuple as key
Interview checklist & pitfalls
- Sanitize inputs (strip, case/Unicode). Mention constraints (alphabet size, expected length).
- Edge cases: empty string, single char, all-equal, unicode/grapheme issues.
- Pitfalls: repeated `in` checks inside loops (O(n) each), forgot to normalize Unicode, off-by-one in slices.
When to reach for advanced tools
- Use KMP/Z when you need guaranteed O(n) pattern search.
- Use rolling hash for simple implementations or probabilistic checks (combine with verification to avoid false positives).
- Use tries for many prefix queries; suffix arrays/automata for heavy substring frequency queries.
Keep this page synced with `Strings.md` for runnable examples and deeper explanations.

---

Try-it (quick sanity checks)
```python
assert 'aba'[::-1] == 'aba'
assert 'ab' in ('cd' + 'ab')
print('strings_cheatsheet quick checks passed')
```

# Strings Cheatsheet — One Page

A compact reference for interview prep. Keep this printable sheet handy.

---

Key concepts

- Representation: Python `str` = sequence of Unicode code points. Indexing 0-based.
- Immutability: `str` is immutable; use list + `''.join()` for heavy concatenation.
- Bytes vs str: `s.encode(encoding)` -> bytes; `b.decode(encoding)` -> str.
- Unicode normalization: `unicodedata.normalize('NFC', s)` before comparisons for canonical equivalence.
- Grapheme vs code point: user-perceived char may be multiple code points.

Common patterns

- Two-pointers: palindromes, reverse, compare from both ends. O(n), O(1) extra.
- Sliding window: substring problems (min window, longest substring without repeat). O(n) with hashmap.
- Hashing (Rabin-Karp): rolling hash for substring search, O(n) average.
- Prefix-function (KMP): O(n) exact pattern search.
- Tries: prefix operations, insert/search in O(length) per word.
- Suffix arrays/automata: repeated substring / frequency queries (advanced).

Important `str` methods (quick)

- len(s) — O(1)
- s[i:j], s[::-1] — slicing O(k) to create new string
- s.split(), s.join(iterable) — split/join; prefer join for concatenation
- s.find(sub), s.index(sub) — find/index
- s.replace(old, new) — O(n) new string
- s.startswith(), s.endswith()
- s.count(sub)
- s.strip(), s.lstrip(), s.rstrip()
- s.lower(), s.upper(), s.casefold() (use for Unicode-insensitive)
- s.encode(), bytes.decode()
- str.maketrans() + translate() for bulk replace
- str.removeprefix()/removesuffix() (3.9+)

Complexities (common)

- Scanning / counting / simple match: O(n)
- Sorting characters (anagram key): O(n log n) per string
- Frequency map (Counter): O(n)
- KMP / Z / Manacher: O(n)
- Suffix array naive: O(n^2 log n), optimized: O(n log n) or O(n)

Mini snippets (memory-compact)

- Reverse words: `' '.join(s.split()[::-1])`
- Check rotation: `s1 in s2 + s2`
- Group anagrams: `d[''.join(sorted(s))].append(s)` or use char-count tuple
- Longest palindrome (expand center): O(n^2) simple
- Manacher: O(n) optimal

Interview tips

- Sanitize inputs: strip whitespace, normalize case or Unicode when needed.
- Always state complexity and edge cases (empty string, single char, unicode).
- Prefer `str` methods over regex for simple tasks — clearer and often faster.
- For heavy text processing, consider streaming or chunked processing to save memory.

---

Quick edge cases checklist (always run through these in interviews):
- Empty inputs: `''`, []
- Single element / single char
- All-equal elements (e.g., 'aaaa')
- Case sensitivity and Unicode (accented characters)
- Very large inputs — streaming vs in-memory

Common pitfalls:
- Off-by-one in slices and loop bounds
- Using `in` on long strings repeatedly (O(n) per check) inside loops — prefer hashing or index search
- Assuming ASCII only — use `encode()`/`decode()` carefully

Keep this sheet synced with `Strings.md` for examples and deeper explanations.
# Strings Cheatsheet — One Page

A compact reference for interview prep. Keep this printable sheet handy.

---

Key concepts

- Representation: Python `str` = sequence of Unicode code points. Indexing 0-based.
- Immutability: `str` is immutable; use list + `''.join()` for heavy concatenation.
- Bytes vs str: `s.encode(encoding)` -> bytes; `b.decode(encoding)` -> str.
- Unicode normalization: `unicodedata.normalize('NFC', s)` before comparisons for canonical equivalence.
- Grapheme vs code point: user-perceived char may be multiple code points.

Common patterns

- Two-pointers: palindromes, reverse, compare from both ends. O(n), O(1) extra.
- Sliding window: substring problems (min window, longest substring without repeat). O(n) with hashmap.
- Hashing (Rabin-Karp): rolling hash for substring search, O(n) average.
- Prefix-function (KMP): O(n) exact pattern search.
- Tries: prefix operations, insert/search in O(length) per word.
- Suffix arrays/automata: repeated substring / frequency queries (advanced).

Important `str` methods (quick)

- len(s) — O(1)
- s[i:j], s[::-1] — slicing O(k) to create new string
- s.split(), s.join(iterable) — split/join; prefer join for concatenation
- s.find(sub), s.index(sub) — find/index
- s.replace(old, new) — O(n) new string
- s.startswith(), s.endswith()
- s.count(sub)
- s.strip(), s.lstrip(), s.rstrip()
- s.lower(), s.upper(), s.casefold() (use for Unicode-insensitive)
- s.encode(), bytes.decode()
- str.maketrans() + translate() for bulk replace
- str.removeprefix()/removesuffix() (3.9+)

Complexities (common)

- Scanning / counting / simple match: O(n)
- Sorting characters (anagram key): O(n log n) per string
- Frequency map (Counter): O(n)
- KMP / Z / Manacher: O(n)
- Suffix array naive: O(n^2 log n), optimized: O(n log n) or O(n)

Mini snippets (memory-compact)

- Reverse words: `' '.join(s.split()[::-1])`
- Check rotation: `s1 in s2 + s2`
- Group anagrams: `d[''.join(sorted(s))].append(s)` or use char-count tuple
- Longest palindrome (expand center): O(n^2) simple
- Manacher: O(n) optimal

Interview tips

- Sanitize inputs: strip whitespace, normalize case or Unicode when needed.
- Always state complexity and edge cases (empty string, single char, unicode).
- Prefer `str` methods over regex for simple tasks — clearer and often faster.
- For heavy text processing, consider streaming or chunked processing to save memory.

---

Reference: expand in `My-DSA-Prep/Strings.md` for full examples and explanations.