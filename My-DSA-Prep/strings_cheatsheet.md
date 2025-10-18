# Strings Cheatsheet: Comprehensive Quick Reference

Immutable sequences of Unicode chars. Key: Immutability means new strings for changes. Use lists for mods.

## Basics

- **Declaration**: `"hello"`, `'world'`, `"""multi-line"""` (O(n) space)
- **Concatenation**: `s1 + s2` (O(n+m))
- **Repetition**: `s * n` (O(n*len(s)))
- **Indexing**: `s[i]` (O(1))
- **Slicing**: `s[start:end:step]` (O(k)) – e.g., `s[::-1]` reverse

## All String Methods

| Method | Syntax | Return | Example | Trick |
|--------|--------|--------|---------|-------|
| split | str.split(sep=None, maxsplit=-1) | List[str] | `"a b".split()` → ['a', 'b'] | Tokenize; sep=None for whitespace |
| join | sep.join(iterable) | str | `",".join(['a','b'])` → 'a,b' | Efficient for building strings |
| replace | str.replace(old, new, count=-1) | str | `"abc".replace('a','x')` → 'xbc' | count=-1 for all |
| find | str.find(sub, start=0, end=-1) | int or -1 | `"abc".find('b')` → 1 | No error if not found |
| index | str.index(sub, start=0, end=-1) | int | `"abc".index('b')` → 1 | Raises ValueError if not found |
| count | str.count(sub, start=0, end=-1) | int | `"aaa".count('a')` → 3 | Range optional |
| isalpha | str.isalpha() | bool | `"abc".isalpha()` → True | All alphabetic |
| isdigit | str.isdigit() | bool | `"123".isdigit()` → True | All digits |
| isspace | str.isspace() | bool | `"   ".isspace()` → True | All whitespace |
| lower | str.lower() | str | `"ABC".lower()` → 'abc' | Case-insensitive |
| upper | str.upper() | str | `"abc".upper()` → 'ABC' | |
| title | str.title() | str | `"hello world".title()` → 'Hello World' | Capitalize words |
| casefold | str.casefold() | str | `"HELLO".casefold()` → 'hello' | Aggressive lower for Turkish etc. |
| strip | str.strip(chars=None) | str | `"  abc  ".strip()` → 'abc' | Remove leading/trailing |
| lstrip | str.lstrip(chars=None) | str | `"  abc".lstrip()` → 'abc' | Left only |
| rstrip | str.rstrip(chars=None) | str | `"abc  ".rstrip()` → 'abc' | Right only |
| zfill | str.zfill(width) | str | `"42".zfill(5)` → '00042' | Zero-pad to width |
| format | str.format(*args, **kwargs) | str | `"{} {}".format('a','b')` → 'a b' | Positional/keyword |
| encode | str.encode(encoding='utf-8', errors='strict') | bytes | `"abc".encode()` → b'abc' | To binary |
| decode | bytes.decode(encoding='utf-8', errors='strict') | str | `b'abc'.decode()` → 'abc' | From binary |
| partition | str.partition(sep) | tuple | `"a b".partition(' ')` → ('a', ' ', 'b') | First occurrence |
| rpartition | str.rpartition(sep) | tuple | `"a b c".rpartition(' ')` → ('a b', ' ', 'c') | Last occurrence |
| swapcase | str.swapcase() | str | `"AbC".swapcase()` → 'aBc' | Swap upper/lower |
| capitalize | str.capitalize() | str | `"hello".capitalize()` → 'Hello' | First char upper |
| expandtabs | str.expandtabs(tabsize=8) | str | `"a\tb".expandtabs()` → 'a       b' | Tabs to spaces |
| center | str.center(width, fillchar=' ') | str | `"hi".center(5,'-')` → '--hi-' | Center with fill |
| ljust | str.ljust(width, fillchar=' ') | str | `"hi".ljust(5,'-')` → 'hi---' | Left justify |
| rjust | str.rjust(width, fillchar=' ') | str | `"hi".rjust(5,'-')` → '---hi' | Right justify |
 | translate | str.translate(table) | str | `"abc".translate(table)` → mapped | Use maketrans |
| maketrans | str.maketrans(x, y=None, z=None) | dict | `str.maketrans('a','x')` → {97:120} | Translation table |
| isalnum | str.isalnum() | bool | `"abc123".isalnum()` → True | Alpha + numeric |
| isdecimal | str.isdecimal() | bool | `"123".isdecimal()` → True | Decimal digits only |
| isnumeric | str.isnumeric() | bool | `"½".isnumeric()` → True | Numeric chars |
| isidentifier | str.isidentifier() | bool | `"var1".isidentifier()` → True | Valid var name |
| isprintable | str.isprintable() | bool | `"abc\n".isprintable()` → False | No control chars |
| istitle | str.istitle() | bool | `"Hello World".istitle()` → True | Title case |
| isupper | str.isupper() | bool | `"ABC".isupper()` → True | All upper |
| islower | str.islower() | bool | `"abc".islower()` → True | All lower |
| startswith | str.startswith(prefix, start=0, end=-1) | bool | `"abc".startswith('a')` → True | Prefix check |
| endswith | str.endswith(suffix, start=0, end=-1) | bool | `"abc".endswith('c')` → True | Suffix check |
| rfind | str.rfind(sub, start=0, end=-1) | int or -1 | `"aba".rfind('a')` → 2 | Last index |
| rindex | str.rindex(sub, start=0, end=-1) | int | `"aba".rindex('a')` → 2 | Last index, error if none |
| rsplit | str.rsplit(sep=None, maxsplit=-1) | list | `"a b c".rsplit(' ',1)` → ['a b', 'c'] | Split from right |
| splitlines | str.splitlines(keepends=False) | list | `"a\nb".splitlines()` → ['a', 'b'] | By lines |
| removeprefix | str.removeprefix(prefix) | str | `"pre_abc".removeprefix('pre_')` → 'abc' | Python 3.9+ |
| removesuffix | str.removesuffix(suffix) | str | `"abc_suf".removesuffix('_suf')` → 'abc' | Python 3.9+ |

## Advanced Concepts

- **Regex**: `import re; re.search(r'\d+', "abc123")` → Match. Compile: `re.compile(r'pattern')`. Flags: `re.IGNORECASE`.
- **Unicode**: `ord('a')` → 97, `chr(97)` → 'a'. Len counts code points. Normalize: `unicodedata.normalize('NFC', s)`.
- **Bytes/Encoding**: `s.encode('utf-8')` → bytes. `b.decode('utf-8')` → str. Specify encoding to avoid errors.
- **F-Strings**: `f"{var:.2f}"` (Python 3.6+). Use `!r` for repr, `!s` for str.
- **Raw Strings**: `r"\n"` → literal. For regex to avoid double escapes.
- **Escape Sequences**: `\n` newline, `\t` tab, `\\` backslash, `\xHH` hex.
- **String Interning**: `sys.intern(s)` interns string. `s1 is s2` for identity.
- **% Formatting**: `"%s %d" % ("a", 1)` → 'a 1'. Deprecated, use f-strings.
- **Common Pitfalls**: Immutability – use lists. Off-by-one slicing. Case sensitivity. Unicode normalize. Memory: Use `''.join(list)` for building.

## Algorithms Cheatsheet

### Substring Search
- **Naive**: Loop positions, check match. O(n*m). Worst: Partial matches.
- **KMP**: LPS table. O(n+m). Compute LPS: Prefix suffixes.
- **Rabin-Karp**: Hash rolling. O(n+m) avg, O(n*m) worst (collisions).

### Other Algorithms
- **Longest Palindromic Substring**: DP O(n^2) space, Expand O(n^2) time O(1) space.
- **Trie**: Insert/Search O(m). For prefixes.
- **Sliding Window**: Anagrams O(n). Use Counter.
- **String Rotation**: `s2 in s1+s1` O(n).
- **Anagram Check**: `Counter(s1) == Counter(s2)` O(n).
- **Palindrome Check**: `s == s[::-1]` O(n).
- **Compression**: Run-length O(n).
- **Edit Distance**: DP O(m*n).

## Time Complexities

- Index/Slice: O(1)/O(k)
- Methods (split, replace): O(n)
- Algorithms: KMP O(n+m), Rabin-Karp O(n+m) avg, DP LPS O(n^2)

## Interview Questions

- Implement strstr (find substring).
- Longest palindromic substring.
- Group anagrams.
- Valid anagram.
- String to integer (atoi).
- Longest common prefix.
- Valid palindrome.
- Implement strStr.
- Count and say.
- Multiply strings.

## Edge Cases

- Empty string: Methods handle, but check.
- Single char: Works.
- All same: Palindromes, compress.
- Unicode: Emojis, accents.
- Large strings: Efficient algos.

## Practice Problems

1. Reverse string without slicing.
2. Check rotation.
3. Find permutations.
4. Wildcard matching.
5. Longest substring no repeat.
6. Valid parentheses (string).
7. Roman to integer.
8. Integer to Roman.
9. Zigzag conversion.
10. Minimum window substring.

## Tips and Tricks

- Immutability: Use lists for mods, then ''.join.
- Case: lower() for insensitive.
- Building: Avoid + in loops; use join.
- Regex: Compile for reuse.
- Unicode: Normalize for consistency.
- Memory: Intern small strings.
- CP: KMP for TLE-prone searches.
- F-strings: Fast, readable.
- Raw: For patterns.
- Escape: repr() to see.
- Pitfalls: Slicing bounds, encoding errors.

