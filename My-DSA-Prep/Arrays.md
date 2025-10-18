
# Arrays — learning roadmap and examples

This file is an ordered learning roadmap for arrays in algorithms and interviews. Work through the steps in order: core concepts → Python types → complexity rules → helpers → core algorithms → advanced topics → practice roadmap → runnable examples.

---

Step 1 — Core concepts and storage model

- Goal: understand what an array is at a memory and API level and why operations have their costs.
- Key points:
  - Arrays offer O(1) random access and O(n) insertion/deletion in the middle.
  - Python `list` stores pointers to objects; resizing is amortized O(1) for append.

Examples:
```python
# random access
a = [10, 20, 30, 40]
print(a[2])  # 30

# append is amortized O(1)
a.append(50)
```

Exercises:
- Explain why inserting at index 0 requires O(n) work.
- Measure appends amortized cost by timing many appends in a loop.

---

Step 2 — Array-like types in Python and when to use them

- Python `list`: general-purpose, stores references; preferred for interview solutions.
- `array.array`: compact numeric arrays when memory matters.
- `collections.deque`: O(1) append/pop from both ends; not random-access friendly.
- `numpy.ndarray`: use for heavy numeric work (vectorized operations, BLAS-backed speed).

Examples:
```python
from collections import deque
from array import array

lst = [1,2,3]
arr = array('i', [1,2,3])
dq = deque([1,2,3])
dq.appendleft(0)
```

Guideline: unless the problem requires C-style memory or extreme numeric performance, `list` is the default choice for interviews.

---

Step 3 — Complexity rules and common operations

- Indexing: O(1)
- Append/pop at end: O(1) amortized
- Insert/pop at arbitrary index: O(n)
- Iteration: O(n)
- Slicing and concatenation: O(k) / O(n+m)

Tip: always mention whether you're counting amortized time when you say "append is O(1)".

---

Step 4 — Reusable helpers and idioms

- Swap: `a[i], a[j] = a[j], a[i]`
- Binary search: use `bisect` for insertion points.
- Prefix sums: `ps = [0]; for x in a: ps.append(ps[-1]+x)` — useful for many subarray queries.

Helpers:
```python
import bisect
def prefix_sums(a):
    ps = [0]
    for x in a:
        ps.append(ps[-1] + x)
    return ps

print(prefix_sums([1,2,3]))  # [0,1,3,6]
```

Exercises:
- Implement a function that returns k-th prefix sum quickly using the prefix array.

---

Step 5 — Core algorithms (implement, understand invariants)

Study and implement these algorithms. For each, know input constraints and edge cases.

1) Linear search — simple scan
```python
def linear_search(a, x):
    for i, val in enumerate(a):
        if val == x:
            return i
    return -1
```

2) Binary search (closed-interval template)
```python
def binary_search(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

3) Two-sum (hashmap) — O(n)
```python
def two_sum_indices(a, target):
    seen = {}
    for i, val in enumerate(a):
        need = target - val
        if need in seen:
            return (seen[need], i)
        seen[val] = i
    return None
```

4) Kadane's algorithm — maximum subarray
```python
def max_subarray(a):
    best = -10**18
    cur = 0
    for x in a:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

5) LIS (n log n) — patience/tails method
```python
import bisect
def lis_length(a):
    tails = []
    for x in a:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

6) Sliding-window maximum (deque)
```python
from collections import deque
def sliding_window_max(a, k):
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
```

7) Quickselect (expected O(n)) — pivot selection and partitioning (prefer in-place for large data)
```python
import random
def quickselect(a, k):
    if not 0 <= k < len(a):
        raise IndexError('k out of range')
    def select(arr, k):
        if len(arr) == 1:
            return arr[0]
        pivot = random.choice(arr)
        lows = [x for x in arr if x < pivot]
        highs = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]
        if k < len(lows):
            return select(lows, k)
        elif k < len(lows) + len(pivots):
            return pivot
        else:
            return select(highs, k - len(lows) - len(pivots))
    return select(a, k)
```

8) Merge sort (stable)
```python
def merge_sort(a):
    if len(a) <= 1:
        return a[:]
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res
```

9) Count inversions (merge-sort variation)
```python
def count_inversions(a):
    def merge_count(left, right):
        i = j = 0
        merged = []
        inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                inv += len(left) - i
        merged.extend(left[i:]); merged.extend(right[j:])
        return merged, inv
    def sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a)//2
        l, li = sort_count(a[:mid])
        r, ri = sort_count(a[mid:])
        merged, mi = merge_count(l, r)
        return merged, li + ri + mi
    _, inv = sort_count(a)
    return inv
```

Exercises:
- Implement Quickselect in-place with Lomuto/Hoare partitioning.
- Write tests for sliding-window maximum and compare to a naive O(nk) solution for small inputs.

---

Step 6 — Advanced topics (overview and when to use)

- Fenwick Tree (Binary Indexed Tree): prefix sums with O(log n) updates and queries. Use for frequency/inversion problems.
- Segment Tree: range queries and range updates; lazy propagation for range updates.
- Sparse Table: immutable RMQ with O(1) queries after O(n log n) build (min/max/gcd).
- Mo's Algorithm: offline sqrt-decomposition for many range queries over static arrays.

Guidance: explain use-cases and trade-offs in interviews; implement Fenwick for frequency counts during practice.

---

Step 7 — Practice roadmap and ordering

1. Master indexing, slicing, and iteration patterns.
2. Solve two-pointer and sliding-window problems.
3. Learn prefix-sum techniques and hashing for subarray queries.
4. Implement sorting and selection algorithms (merge sort, quickselect).
5. Study trees/bit/segment structures for range queries.

---

Try it — runnable examples

Copy these snippets into a `.py` file and run them to verify behavior. They are small checks to confirm the implementations.

```python
def two_sum(a, target):
    seen = {}
    for i, x in enumerate(a):
        if target - x in seen:
            return [seen[target-x], i]
        seen[x] = i
    return []

def rotate_right(a, k):
    if not a:
        return
    n = len(a)
    k %= n
    a[:] = a[::-1]
    a[:k] = a[:k][::-1]
    a[k:] = a[k:][::-1]

def max_subarray(a):
    best = -10**18
    cur = 0
    for x in a:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

print(two_sum([2,7,11,15], 9))
arr = [1,2,3,4,5]
rotate_right(arr, 2)
print(arr)
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
```

---



