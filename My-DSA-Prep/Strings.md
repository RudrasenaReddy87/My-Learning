# Strings: Immutable Sequences of Characters

Hello, aspiring programmer! Strings are everywhere in coding – from user inputs to file parsing. In Python, strings are immutable sequences of characters, meaning once created, you can't change them in place. This immutability leads to efficient memory usage but requires care when modifying. Why important? Strings handle text processing, which is crucial in web dev, data analysis, and CP. Common use cases: validating emails, parsing logs, implementing search. Let's dive deep, covering every method, algorithms, and my hard-earned tips.

## Introduction to Strings

Strings are sequences of Unicode characters. Immutable: operations create new strings. Importance: Text manipulation is core to programming. Use cases: Password validation, URL parsing, natural language processing.

Key properties:
- Indexed, sliced like lists.
- Immutable.
- Support rich methods.

Personal note: Strings tripped me up with immutability; I tried s[0] = 'a' and got errors.

## Basics: Declaration, Concatenation, Repetition, Indexing, Slicing

### Declaration
Enclose in quotes.
```python
s = "hello"
s = 'world'
s = """multi-line"""
```
Parameters: The string content.
Return: String object.
Complexity: O(n) space.

Example 1: Declare a string.
```python
greeting = "Hello, World!"
print(greeting)  # Hello, World!
```
Tip: Use triple quotes for multi-line.

### Concatenation
Join strings.
```python
s1 + s2
```
Complexity: O(n+m).

Example 2: Concatenate names.
```python
full = "John" + " " + "Doe"
print(full)  # John Doe
```

### Repetition
Repeat string.
```python
s * n
```
Complexity: O(n*len(s)).

Example: Repeat "ha" 3 times.
```python
laugh = "ha" * 3  # hahaha
```

### Indexing
Access character.
```python
s[index]
```
Complexity: O(1).

Example: First char.
```python
print(s[0])
```

### Slicing
Substring.
```python
s[start:end:step]
```
Complexity: O(k).

Example: Reverse string.
```python
rev = s[::-1]
```

## All String Methods

### split
Split into list.
Syntax: str.split(sep=None, maxsplit=-1)
Parameters: sep (delimiter), maxsplit (max splits).
Return: List of substrings.
Complexity: O(n).

Example: Split by space.
```python
words = "hello world".split()  # ['hello', 'world']
```
Tip: Use for tokenizing.

### join
Join list into string.
Syntax: sep.join(iterable)
Parameters: sep (separator), iterable (strings).
Return: Joined string.
Complexity: O(total length).

Example: Join with comma.
```python
",".join(['a','b','c'])  # 'a,b,c'
```

### replace
Replace occurrences.
Syntax: str.replace(old, new, count=-1)
Parameters: old (to replace), new (replacement), count (max replaces).
Return: New string.
Complexity: O(n).

Example: Replace 'a' with 'o'.
```python
"banana".replace('a','o')  # 'bonono'
```

### find
Find substring index.
Syntax: str.find(sub, start=0, end=-1)
Parameters: sub (substring), start/end (range).
Return: Index or -1.
Complexity: O(n).

Example: Find 'world'.
```python
"hello world".find('world')  # 6
```

### index
Like find, but raises ValueError if not found.
Syntax: str.index(sub, start=0, end=-1)
Return: Index.
Complexity: O(n).

Example: Same as find, but errors if not found.

### count
Count occurrences.
Syntax: str.count(sub, start=0, end=-1)
Parameters: sub, start/end.
Return: Count.
Complexity: O(n).

Example: Count 'l' in "hello".
```python
"hello".count('l')  # 2
```

### isalpha
Check all alphabetic.
Syntax: str.isalpha()
Return: Bool.
Complexity: O(n).

Example: "abc".isalpha()  # True

### isdigit
Check all digits.
Syntax: str.isdigit()
Return: Bool.

Example: "123".isdigit()  # True

### isspace
Check all whitespace.
Syntax: str.isspace()
Return: Bool.

Example: "   ".isspace()  # True

### lower
Convert to lowercase.
Syntax: str.lower()
Return: New string.
Complexity: O(n).

Example: "HELLO".lower()  # 'hello'

### upper
To uppercase.
Syntax: str.upper()
Return: New string.

Example: "hello".upper()  # 'HELLO'

### title
Capitalize words.
Syntax: str.title()
Return: New string.

Example: "hello world".title()  # 'Hello World'

### casefold
Aggressive lowercase for case-insensitive.
Syntax: str.casefold()
Return: New string.

Example: For Turkish 'İ'.

### strip
Remove leading/trailing whitespace.
Syntax: str.strip(chars=None)
Parameters: chars to strip.
Return: New string.
Complexity: O(n).

Example: "  hello  ".strip()  # 'hello'

### lstrip
Left strip.
Syntax: str.lstrip(chars=None)

### rstrip
Right strip.
Syntax: str.rstrip(chars=None)

### zfill
Pad with zeros.
Syntax: str.zfill(width)
Parameters: width.
Return: Padded string.

Example: "42".zfill(5)  # '00042'

### format
Format string.
Syntax: str.format(*args, **kwargs)
Return: Formatted string.

Example: "{} {}".format('hello', 'world')  # 'hello world'

### encode
Encode to bytes.
Syntax: str.encode(encoding='utf-8', errors='strict')
Return: Bytes.

Example: "hello".encode()  # b'hello'

### decode
Decode bytes to string.
Syntax: bytes.decode(encoding='utf-8', errors='strict')
Return: String.

### partition
Split at first occurrence.
Syntax: str.partition(sep)
Return: Tuple (before, sep, after).

Example: "hello world".partition(' ')  # ('hello', ' ', 'world')

### rpartition
From right.

### swapcase
Swap case.
Syntax: str.swapcase()
Return: New string.

Example: "Hello".swapcase()  # 'hELLO'

### capitalize
Capitalize first char.
Syntax: str.capitalize()

### expandtabs
Expand tabs.
Syntax: str.expandtabs(tabsize=8)

### center
Center string.
Syntax: str.center(width, fillchar=' ')
Return: Centered string.

Example: "hi".center(10, '-')  # '----hi----'

### ljust
Left justify.
Syntax: str.ljust(width, fillchar=' ')

### rjust
Right justify.

### translate
Translate characters.
Syntax: str.translate(table)
Parameters: Translation table from maketrans.

### maketrans
Create translation table.
Syntax: str.maketrans(x, y=None, z=None)
Return: Dict for translate.

Example: table = str.maketrans('aeiou', '12345')
"hello".translate(table)  # 'h2ll4'

### isalnum
Check all alphanumeric.
Syntax: str.isalnum()
Return: Bool.
Complexity: O(n).

Example: "abc123".isalnum()  # True
Trick: Useful for validating usernames; faster than regex for simple checks.

### isdecimal
Check all decimal digits.
Syntax: str.isdecimal()
Return: Bool.

Example: "123".isdecimal()  # True
Trick: Stricter than isdigit; doesn't accept superscripts.

### isnumeric
Check all numeric.
Syntax: str.isnumeric()
Return: Bool.

Example: "½".isnumeric()  # True
Trick: Accepts fractions, superscripts; use for broad numeric checks.

### isidentifier
Check valid identifier.
Syntax: str.isidentifier()
Return: Bool.

Example: "var1".isidentifier()  # True
Trick: For parsing code; keywords like 'if' return False.

### isprintable
Check all printable.
Syntax: str.isprintable()
Return: Bool.

Example: "hello\n".isprintable()  # False
Trick: For sanitizing output; excludes newlines, tabs.

### istitle
Check title case.
Syntax: str.istitle()
Return: Bool.

Example: "Hello World".istitle()  # True
Trick: Each word starts with upper, rest lower.

### isupper
Check all uppercase.
Syntax: str.isupper()
Return: Bool.

Example: "HELLO".isupper()  # True
Trick: Fails if any lowercase; use for case validation.

### islower
Check all lowercase.
Syntax: str.islower()
Return: Bool.

Example: "hello".islower()  # True
Trick: Opposite of isupper.

### startswith
Check prefix.
Syntax: str.startswith(prefix, start=0, end=-1)
Parameters: prefix (str or tuple), start/end.
Return: Bool.
Complexity: O(len(prefix)).

Example: "hello".startswith("he")  # True
Trick: Faster than slicing; use tuple for multiple prefixes.

### endswith
Check suffix.
Syntax: str.endswith(suffix, start=0, end=-1)
Return: Bool.

Example: "hello".endswith("lo")  # True
Trick: Similar to startswith; efficient for file extensions.

### rfind
Find from right.
Syntax: str.rfind(sub, start=0, end=-1)
Return: Index or -1.

Example: "banana".rfind("a")  # 5
Trick: Last occurrence; use for parsing paths.

### rindex
Index from right.
Syntax: str.rindex(sub, start=0, end=-1)
Return: Index.

Example: Same as rfind, but errors if not found.
Trick: When you expect the substring to exist.

### rsplit
Split from right.
Syntax: str.rsplit(sep=None, maxsplit=-1)
Return: List.

Example: "a,b,c".rsplit(",", 1)  # ['a,b', 'c']
Trick: For paths or URLs; maxsplit from right.

### splitlines
Split by lines.
Syntax: str.splitlines(keepends=False)
Return: List.

Example: "a\nb\nc".splitlines()  # ['a', 'b', 'c']
Trick: Handles \n, \r\n; keepends for preserving.

### removeprefix
Remove prefix (Python 3.9+).
Syntax: str.removeprefix(prefix)
Return: New string.

Example: "prefix_hello".removeprefix("prefix_")  # 'hello'
Trick: Cleaner than slicing; check if starts with.

### removesuffix
Remove suffix (Python 3.9+).
Syntax: str.removesuffix(suffix)
Return: New string.

Example: "hello_suffix".removesuffix("_suffix")  # 'hello'
Trick: Opposite of removeprefix; efficient.

## Advanced Topics

### Regex
Use re module for patterns.
```python
import re
match = re.search(r'\d+', "abc123")  # '123'
```
Complexity: Varies.
Trick: Compile patterns with re.compile for reuse; use re.IGNORECASE for case-insensitive.

Example: Validate email.
```python
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
email_pattern.match("user@example.com")  # Match object
```

### Unicode
Strings are Unicode. Handle with care.
Example: Emojis, accented chars.
Trick: Use ord() and chr() for code points; len() counts code points, not graphemes.

Example: Emoji length.
```python
s = "👋"  # len(s) == 1, but displays as one character
print(ord("👋"))  # 128075
```

### Bytes and Encoding
Convert to bytes for binary data.
Example: For file I/O.
Trick: Specify encoding to avoid UnicodeDecodeError; use 'utf-8' default.

Example: Read file with encoding.
```python
with open('file.txt', 'r', encoding='utf-8') as f:
    content = f.read()
```

### Normalization
unicodedata.normalize for consistent forms.
```python
import unicodedata
normalized = unicodedata.normalize('NFC', 'café')  # Combines accents
```
Trick: Use 'NFD' for decomposition in search; 'NFC' for canonical equivalence.

### F-Strings (Python 3.6+)
Formatted string literals.
Syntax: f"{expression}"
Complexity: O(n).

Example: 
```python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Alice is 30 years old.
```
Trick: Use !r for repr, !s for str; format specifiers like :.2f for floats.

### Raw Strings
Prefix 'r' to ignore escapes.
Example: r"\n" remains "\n", not newline.
Trick: Essential for regex patterns to avoid double-escaping.

### Escape Sequences
Special chars: \n, \t, \\, \xHH (hex).
Trick: Use repr(s) to see escapes; triple quotes preserve them.

### String Interning
Python interns small strings for efficiency.
Trick: Use sys.intern() for custom; == compares identity for interned.

Example:
```python
import sys
s1 = sys.intern("hello")
s2 = sys.intern("hello")
s1 is s2  # True
```

### % Formatting (Old Style)
Uses % operator.
Example: "%s %d" % ("hello", 42)
Trick: Deprecated but in legacy code; use for simple cases.

### Common Pitfalls
- Modifying immutable strings: Use list comprehension.
- Off-by-one in slicing.
- Case sensitivity in comparisons.
- Unicode surprises: Normalize first.
- Memory: Repeated + creates many objects; use join.

Trick: For building strings, use list and ''.join(list).
```python
parts = ['hello', 'world']
s = ''.join(parts)  # Efficient
```

## Algorithms

### Substring Search
Naive: Check all positions. O(n*m)

Example: Naive search for "abc" in "ababc".
```python
def naive_search(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1
```
Complexity: O(n*m). Worst case: All characters match partially.

### KMP Algorithm
Prefix table for efficiency. O(n+m)

#### KMP Implementation
```python
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    if not pattern:
        return 0
    lps = compute_lps(pattern)
    i = 0  # text index
    j = 0  # pattern index
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j  # found at position
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1
```
Complexity: O(n + m). LPS computation: O(m), search: O(n).
Example: Search "ABABCABAB" for "ABAB". LPS: [0,0,1,2]. Found at index 5.

#### Edge Cases
- Pattern longer than text: Return -1.
- Empty pattern: Return 0.
- Pattern not found: Return -1.

### Rabin-Karp
Hashing for fast search. O(n+m) average.

#### Rabin-Karp Implementation
```python
def rabin_karp(text, pattern, q=101):
    d = 256  # number of characters
    n = len(text)
    m = len(pattern)
    if m > n:
        return -1
    h = pow(d, m-1, q)
    p = 0  # hash for pattern
    t = 0  # hash for text
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i+m])) % q
            if t < 0:
                t += q
    return -1
```
Complexity: O(n + m) average, O((n-m+1)*m) worst (hash collisions).
Example: Search "GEEKS FOR GEEKS" for "GEEK". Found at 0 and 10.

#### Advantages
- Good for multiple patterns.
- Rolling hash avoids recomputation.

### Longest Palindromic Substring
DP or expand around center.

#### DP Approach
```python
def longest_palindrome_dp(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    for i in range(n):
        dp[i][i] = True
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    return s[start:start + max_len]
```
Complexity: O(n^2) time, O(n^2) space.

#### Expand Around Center
```python
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_palindrome_expand(s):
    if not s:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i+1)
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start:end+1]
```
Complexity: O(n^2) time, O(1) space.
Example: "babad" -> "bab" or "aba".

### Trie (Prefix Tree)
For prefix searches.

#### Trie Implementation
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```
Complexity: Insert/Search: O(m), where m is word length.
Use: Autocomplete, spell check.

### Sliding Window
For anagrams, etc.

#### Find All Anagrams
```python
from collections import Counter
def find_anagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter()
    left = 0
    for right in range(len(s)):
        s_count[s[right]] += 1
        if right - left + 1 > len(p):
            s_count[s[left]] -= 1
            if s_count[s[left]] == 0:
                del s_count[s[left]]
            left += 1
        if s_count == p_count:
            result.append(left)
    return result
```
Complexity: O(n).
Example: s="cbaebabacd", p="abc" -> [0,6]

### String Rotation
Check if one string is rotation of another.
```python
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)
```
Complexity: O(n).

### Anagram Check
```python
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)
```
Complexity: O(n).

### Palindrome Check
```python
def is_palindrome(s):
    return s == s[::-1]
```
Complexity: O(n).

### String Compression
Run-length encoding.
```python
def compress(s):
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)
```
Example: "aaabbb" -> "a3b3"

### Edit Distance (Levenshtein)
DP for min edits.
```python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```
Complexity: O(m*n).
Example: "kitten" to "sitting" -> 3.

## Personal Notes and Tips for CP

- Strings are immutable, so use lists for modifications.
- Pitfall: Forgetting case sensitivity.
- Trick: Use f-strings for formatting.
- Cross-reference: Strings in hashing problems.

Practice: Reverse words, check palindromes.

## Interview Questions

- Implement strstr (substring search).
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

- Empty strings: Most methods handle, but check.
- Single character: Works.
- All same characters: Palindromes, compressions.
- Unicode: Emojis, accented chars.
- Large strings: Use efficient algorithms.

## Time Complexities in Detail

- Basic ops (index, slice): O(1)/O(k)
- Methods (split, replace): O(n)
- Algorithms: KMP O(n+m), Rabin-Karp O(n+m) avg, DP palindrome O(n^2)
- Trie: O(m) per operation

## Personal Stories

- In a contest, naive substring search TLE'd; switched to KMP and passed.
- Forgot immutability, tried s[0]='a'; error.
- Used wrong encoding; garbled text.

## Code Variations

- Recursive palindrome check.
- Iterative vs recursive string reversal.
- Using bytearray for mutable strings.

## Examples to Practice

1. Reverse string without slicing.
2. Check if string is rotation.
3. Find all permutations.
4. Implement wildcard matching.
5. Longest substring without repeating chars.
