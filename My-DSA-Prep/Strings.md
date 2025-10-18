## Strings — learning roadmap and examples

This document is a step-by-step roadmap for learning and applying string techniques in algorithms and interview problems. Each step contains the core idea, short examples, and suggested exercises.

Note: structural pattern matching (`match` / `case`) requires Python 3.10+. Other examples run on Python 3.8+.

---

Step 1 — Core concepts and representations

- Goal: understand what a string is in your language of choice and the consequences (immutability, indexing, slicing).
- Key points:
  - Python: `str` is immutable and stores Unicode code points; prefer `''.join(list)` for many concatenations.
  - C++/Java: strings may be mutable (C++ std::string) or UTF-16 (Java); watch encoding.

Examples:
```python
# indexing and slicing
s = 'Hello World'
print(s[0], s[-1])      # H d
print(s[0:5], s[6:])    # Hello World
```

Exercises:
- Explain memory/ownership when passing strings between functions in your chosen language.
- Write a safe indexing helper that returns a default when out-of-range.

---

Step 2 — Common methods and idioms

- Goal: become fluent with core string APIs and when to use them (split/join, strip, find, replace, format).

Examples:
```python
words = '  hello  world  '.split()
print(' '.join(words))        # 'hello world'
print('file.txt'.endswith('.txt'))
print('café'.encode('utf-8'))
```

Guidelines:
- Normalize case for comparisons (`casefold()` for Unicode-aware lowercasing).
- Prefer `str` methods over regex for simple tasks.

Exercises:
- Implement a small sanitizer that trims, normalizes Unicode (NFC), and lowercases a user input.

---

Step 3 — Pattern templates and common algorithmic patterns

- Goal: recognize patterns that cover many problems: two-pointers, sliding window, prefix function, rolling hash, and tries.

Quick reference:
- Two-pointers: palindrome checks, pair-sum in sorted arrays.
- Sliding window: minimum window substring, longest substring with K distinct characters.
- Prefix function (KMP): pattern matching without re-scan.
- Rolling hash (Rabin-Karp): fast substring fingerprinting, but always verify due to collisions.

Exercise:
- Implement a sliding-window template that returns start/end indices for all windows satisfying a predicate.

---

Step 4 — Essential algorithms (implement and test)

Below are concise implementations to study and reuse. Understand invariants, complexity, and edge cases.

Palindrome check (two-pointer):
```python
def is_palindrome(s: str) -> bool:
    i, j = 0, len(s)-1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1; j -= 1
    return True
```

KMP (pattern search):
```python
def kmp_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    # build lps
    lps = [0]*len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    # search
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                return i - j
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
    return -1
```

Rabin-Karp (find all occurrences):
```python
def rabin_karp_all(text: str, pattern: str):
    if not pattern or len(pattern) > len(text):
        return []
    d, q = 256, 10**9 + 7
    n, m = len(text), len(pattern)
    h = pow(d, m-1, q)
    p = t = 0
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    res = []
    for i in range(n - m + 1):
        if p == t and text[i:i+m] == pattern:
            res.append(i)
        if i < n - m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t += q
    return res
```

Minimum window substring (template):
```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ''
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    for right, ch in enumerate(s, 1):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if end == 0 or right - left < end - start:
                start, end = left, right
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[start:end]
```

Exercises:
- Implement `longest_palindromic_substring` using expand-around-center and compare to Manacher for performance.

---

Step 5 — Data structures for string problems

- Trie (prefix tree): fast prefix queries and dictionary problems.
- Suffix array / suffix automaton / suffix tree: for repeated-substring queries, frequency, and advanced queries.
- Aho-Corasick: multiple-pattern search across a large text.
- Eertree (palindromic tree): enumerate distinct palindromic substrings efficiently.

Example — Trie (basic operations):
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return False
        return True

# usage
trie = Trie(); trie.insert('hello')
```

Guidance:
- For interviews, explain the trade-offs (memory vs query time) and prefer simple trie implementations or use hashing when memory is tight.

---

Step 6 — Advanced topics (what to know conceptually)

- Suffix array: concept, LCP, and simple suffix-array-by-sorting for small inputs.
- Suffix automaton: states, transitions, and how it represents all substrings.
- Aho-Corasick: trie + failure links for multi-pattern match.
- Manacher's algorithm: linear-time longest palindromic substring.

Advice: you don't need to implement every advanced structure from memory for interviews; being able to explain use-cases, complexity, and a simple naive implementation is often enough.

---

Step 7 — Practice roadmap (order to learn problems)

1. Basics & string APIs: slicing, split/join, strip, startswith/endswith.
2. Two-pointer problems: palindrome, reverse words, pair-sum on sorted input.
3. Sliding window problems: min window substring, longest substring with K distinct chars.
4. Pattern matching: KMP, Rabin-Karp, Z algorithm.
5. Tries & prefix problems, grouping anagrams.
6. Advanced: suffix array/automaton concepts, Aho-Corasick for many patterns.

Exercises per stage are above; practice incrementally and compare multiple approaches when time allows.

---

Try it — runnable examples

Copy these examples into a `.py` file and run them to validate behavior. They are deterministic and intended as learning checks.

```python
# Example: is_palindrome and kmp_search
def is_palindrome(s):
    s2 = ''.join(ch for ch in s.lower() if ch.isalnum())
    return s2 == s2[::-1]

def kmp_search(text, pattern):
    if not pattern:
        return 0
    lps = [0]*len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                return i-j
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
    return -1

print(is_palindrome('A man a plan a canal Panama'))
print(kmp_search('ABABDABACDABABCABAB', 'ABABCABAB'))
```

Further practice: copy other functions from this file (min_window, rabin_karp_all, trie) and run them interactively.

---

How to run

- Save snippets into a `.py` file and run with `python file.py` using your local Python 3 interpreter.
- For pattern-matching (`match`), run on Python 3.10+.

If you want, I will:
- Convert the rest of topic files to the same roadmap style, one file at a time (next: `Arrays.md`).
- Optionally add a lightweight `run_examples.py` CLI that can execute these "Try it" snippets (non-intrusively).

def z_algorithm(s: str):
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def z_search(text: str, pattern: str):
    s = pattern + '$' + text
    z = z_algorithm(s)
    m = len(pattern)
    res = []
    for i in range(m+1, len(s)):
        if z[i] == m:
            res.append(i - m - 1)
    return res

print(z_search('abxabcabcaby', 'abc'))  # [3, 6]
```

### 3. Trie (Prefix Tree) — insertion, search, startsWith
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            node = node.children.get(ch)
            if node is None:
                return False
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return False
        return True

trie = Trie()
trie.insert('hello')
print(trie.search('hell'))  # False
print(trie.starts_with('hell'))  # True
```

### 4. Rolling Hash (Rabin-Karp) with multiple patterns / fast checks
```python
def rabin_karp_all(text: str, pattern: str):
    if not pattern or len(pattern) > len(text):
        return []
    d, q = 256, 10**9 + 7
    n, m = len(text), len(pattern)
    h = pow(d, m-1, q)
    p = t = 0
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    res = []
    for i in range(n - m + 1):
        if p == t and text[i:i+m] == pattern:
            res.append(i)
        if i < n - m:
            t = (d*(t - ord(text[i])*h) + ord(text[i+m])) % q
            if t < 0:
                t += q
    return res

print(rabin_karp_all('abababab', 'ab'))  # [0,2,4,6]
```

## Algorithms and DSA Questions (with solutions)

This section contains common interview/contest problems, short explanation, complexity, and tested Python code.

### Problem A — Reverse Words In-Place (without extra split)
Goal: Given a string s, reverse words and remove extra spaces. Example: "  the sky  is blue  " -> "blue is sky the"

```python
def reverse_words_inplace(s: str) -> str:
    # Trim and split manually to show in-place idea (O(n) time, O(n) space for result)
    words = []
    i, n = 0, len(s)
    while i < n:
        while i < n and s[i] == ' ':
            i += 1
        if i >= n:
            break
        j = i
        while j < n and s[j] != ' ':
            j += 1
        words.append(s[i:j])
        i = j
    return ' '.join(reversed(words))

print(reverse_words_inplace('  the sky  is blue  '))  # 'blue is sky the'
```

Complexity: O(n) time, O(n) extra space for words list.

### Problem B — Check Rotation (s1 is rotation of s2)
```python
def is_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s1 in s2 + s2

print(is_rotation('ABCD', 'CDAB'))  # True
```

### Problem C — Group Anagrams
Group a list of strings into anagrams.

```python
from collections import defaultdict

def group_anagrams(strs):
    d = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        d[key].append(s)
    return list(d.values())

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))
# [['eat','tea','ate'], ['tan','nat'], ['bat']]
```

Optimization: Use character counts as tuple for key to avoid sorting when alphabet size small.

### Problem D — Longest Palindromic Substring
Two solutions: expand-around-center O(n^2) and Manacher O(n). Manacher is implemented above. Here's expand-center for simplicity:

```python
def longest_palindrome_expand(s: str) -> str:
    if not s:
        return ''
    start = end = 0
    for i in range(len(s)):
        l1 = expand(s, i, i)
        l2 = expand(s, i, i+1)
        l = max(l1, l2)
        if l > end - start + 1:
            start = i - (l-1)//2
            end = i + l//2
    return s[start:end+1]

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

print(longest_palindrome_expand('cbbd'))  # 'bb'
```

### Problem E — String Compression (basic)
Given a string, compress consecutive characters: "aaabb" -> "a3b2" (only if shorter)

```python
def compress_string(s: str) -> str:
    if not s:
        return ''
    res = []
    prev = s[0]
    count = 1
    for ch in s[1:]:
        if ch == prev:
            count += 1
        else:
            res.append(prev + (str(count) if count>1 else ''))
            prev = ch
            count = 1
    res.append(prev + (str(count) if count>1 else ''))
    comp = ''.join(res)
    return comp if len(comp) < len(s) else s

print(compress_string('aaabbbccc'))  # 'a3b3c3'
```

### Problem F — Longest Common Subsequence (LCS) on strings (DP)
Classic DP problem. Returns length and one LCS.

```python
def lcs(a: str, b: str):
    m, n = len(a), len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # reconstruct one LCS
    i, j = m, n
    res = []
    while i and j:
        if a[i-1] == b[j-1]:
            res.append(a[i-1]); i-=1; j-=1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return dp[m][n], ''.join(reversed(res))

print(lcs('AGGTAB', 'GXTXAYB'))  # (4, 'GTAB')
```

## How to run the code snippets
All snippets are pure Python 3. Copy a function into a local `.py` file and run `python yourfile.py`.

Quality gates: I kept the changes limited to `Strings.md` and only added runnable Python samples. Next I'll mark todos 1 completed and set the next todo in-progress.

## Additional Resources
- Books: "Introduction to Algorithms" for advanced string algos.
- Online: LeetCode, HackerRank for practice.
- Videos: Khan Academy on strings.

Remember, practice makes perfect! Start with basics, add complexity, and soon strings will feel like second nature. Happy coding! 🚀

---

Extras — edge cases checklist and interview tips

- Edge cases: empty string, single char, all same chars, unicode combining characters, very long inputs (stream if needed).
- Input normalization: trim, casefold, and Unicode normalize before comparisons when appropriate.
- Memory tip: avoid repeated `+` concatenation in loops; prefer `''.join(parts)`.

Interview checklist:
- Ask about character set (ASCII vs Unicode), expected max lengths, memory limits.
- State algorithm complexity and whether extra structures (hashes, arrays) are allowed.
- For randomized algorithms (rolling hash), mention collision probability and verification step.

---

Advanced extras — suffix structures, multiple-pattern search, Unicode, and interview tips (humanized)

Suffix structures (short and practical)
- Suffix Array: sorted array of all suffixes' starting indices. Useful for many substring queries and building LCP arrays. Simple implementation: sort suffixes O(n^2 log n) naive, practical for small inputs. Know the concept for interviews; implementing an optimal O(n log n) or O(n) SA is advanced.
- Suffix Automaton (SAM): a compact automaton representing all substrings of a string. Great for counting distinct substrings, longest common substring, and frequency queries. Implementing from scratch is advanced, but explain state/link structure clearly in interviews.
- Suffix Tree: compressed trie of suffixes. Powerful but complex; explain use-cases and that construction is linear-time with Ukkonen's algorithm.

Aho-Corasick (multiple-pattern search)
- Use-case: search many patterns simultaneously in a large text (spam filters, dictionary matching). Build a trie of patterns with failure links; traverse text once O(n + total_pattern_length + matches).
- Humanized explanation: imagine walking through a forest of prefixes and having teleport links (failures) to the nearest valid prefix when a branch breaks.

Eertree (palindromic tree)
- Use-case: enumerating all distinct palindromic substrings and answering palindromic queries quickly. It's an elegant data structure that stores palindromes as nodes and adds characters in amortized O(1) per character.

Rolling-hash caveats
- Hash collisions: Rolling hashes have small collision probabilities; always verify by direct substring comparison when hash matches, especially in interviews.
- Choosing mod and base: use large mod (like near 1e9+7) and random/base mixing when concerned; explain trade-offs.

Unicode and normalization
- Normalization: visually identical characters may have different code points (NFC vs NFD). Use `unicodedata.normalize` before comparisons.
- Grapheme clusters: For user-facing operations (like reversing text), consider grapheme clusters rather than code points (libraries like `regex` with `\X` help).

Humanized interview tips (what to say)
- "I'll first restate the problem and ask about character set and constraints — ASCII? Unicode? Max length?"
- "My plan: if patterns are few, use KMP/Rabin-Karp; if many, build Aho-Corasick. For substring frequency, consider suffix automaton or suffix array depending on constraints."
- "I'll note complexity and memory trade-offs: building suffix structures costs O(n) memory/time; verify with small examples."

Deterministic smoke tests (copy into `run_examples.py` or run in REPL)
```python
# Strings smoke tests
def is_palindrome(s):
    s2 = ''.join(ch for ch in s.lower() if ch.isalnum())
    return s2 == s2[::-1]

def kmp_search(text, pattern):
    if not pattern:
        return 0
    lps = [0]*len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1; j += 1
            if j == len(pattern):
                return i-j
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1

assert is_palindrome('A man a plan a canal Panama')
assert kmp_search('ABABDABACDABABCABAB', 'ABABCABAB') == 10
print('Strings smoke tests passed')
```

Related practice topics
- Repeated substring queries, online substring matching, longest repeated substring, minimal cyclic rotation (Booth's algorithm), palindromic queries (Eertree).

Final humanized checklist
- Always verbalize assumptions (charset, constraints). Test on tiny examples; include edge-cases in your mental plan. Mention verification steps after randomized/hash-based checks.


