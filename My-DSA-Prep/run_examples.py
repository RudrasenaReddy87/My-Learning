"""
Run with `python run_examples.py` or `python run_examples.py --run-smoke`.
"""
import argparse
from collections import Counter

# Minimal implementations used for tests

def is_palindrome(s: str) -> bool:
    s = ''.join(ch.lower() for ch in s if not ch.isspace())
    return s == s[::-1]


def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1.replace(' ', '').lower()) == Counter(s2.replace(' ', '').lower())


def reverse_words(s: str) -> str:
    return ' '.join(s.split()[::-1])


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


def kmp_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    # compute lps
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
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1


# Tests

def run_tests():
    tests = []
    # (callable, args, expected)
    tests.append((is_palindrome, ("A man a plan a canal Panama",), True))
    tests.append((is_anagram, ("listen", "silent"), True))
    tests.append((reverse_words, ("Hello World",), "World Hello"))
    tests.append((compress_string, ("aaabbbccc",), "a3b3c3"))
    tests.append((kmp_search, ("ABABDABACDABABCABAB", "ABABCABAB"), 10))

    # more array helpers
    def max_subarray(a):
        best = -10**18
        cur = 0
        for x in a:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best

    def sliding_window_max(a, k):
        from collections import deque
        if not a or k <= 0:
            return []
        dq = deque()
        res = []
        for i, x in enumerate(a):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and a[dq[-1]] < x:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(a[dq[0]])
        return res

    def next_greater(a):
        res = [-1]*len(a)
        stack = []
        for i, x in enumerate(a):
            while stack and a[stack[-1]] < x:
                res[stack.pop()] = x
            stack.append(i)
        return res

    tests.append((max_subarray, ([-2,1,-3,4,-1,2,1,-5,4],), 6))
    tests.append((sliding_window_max, ([1,3,-1,-3,5,3,6,7], 3), [3,3,5,5,6,7]))
    tests.append((next_greater, ([2,1,2,4,3],), [4,2,4,-1,-1]))

    # arrays helpers (from Arrays.md)
    def two_sum(a, target):
        seen = {}
        for i, x in enumerate(a):
            if target - x in seen:
                return [seen[target-x], i]
            seen[x] = i
        return []

    def rotate_right(a, k):
        n = len(a)
        k %= n
        a[:] = a[::-1]
        a[:k] = a[:k][::-1]
        a[k:] = a[k:][::-1]

    tests.append((two_sum, ([2,7,11,15], 9), [0,1]))
    arr = [1,2,3,4,5,6,7]
    rotate_right(arr, 3)
    tests.append((lambda: arr, (), [5,6,7,1,2,3,4]))

    # linked list smoke: simple Node and to_list
    class Node:
        def __init__(self, val=0, nxt=None):
            self.val = val
            self.next = nxt

    def build_list(vals):
        head = None
        cur = None
        for v in vals:
            node = Node(v)
            if not head:
                head = node; cur = node
            else:
                cur.next = node; cur = node
        return head

    def to_list(head):
        res = []
        cur = head
        while cur:
            res.append(cur.val); cur = cur.next
        return res

    ll = build_list([1,2,3])
    tests.append((to_list, (ll,), [1,2,3]))

    # stack/queue basics
    def valid_paren(s):
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
        return not stack

    tests.append((valid_paren, ('()[]{}',), True))

    failures = 0
    for func, args, expected in tests:
        # allow zero-arg lambdas for inline tests
        if callable(func) and args == ():
            result = func()
        else:
            result = func(*args)
        if result != expected:
            failures += 1
            print(f"FAIL: {func.__name__}{args} -> {result} (expected {expected})")
        else:
            print(f"PASS: {func.__name__}{args} -> {result}")

    if failures:
        print(f"\n{failures} test(s) failed.")
    else:
        print("\nAll tests passed.")


if __name__ == '__main__':
    run_tests()
