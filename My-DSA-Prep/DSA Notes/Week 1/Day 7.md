# Day 7 — Searching + Weekly Wrap-up

**Week 1: Foundations** | [Week overview](README.md)
*(Lighter day)*

**Language: Python**

---

## 0. The Big Picture — What "Searching" Actually Means (Plain-English Primer)

Before any code: searching just means **"is this value in my collection,
and if so, where?"** Every search algorithm answers that question, but they
differ enormously in *how much they're allowed to assume about the data* —
and that assumption is what determines the speed.

**A simple analogy — looking up a name:**
- **Linear search** is like flipping through a stack of unsorted index
  cards one at a time until you find the name you want. No shortcuts
  possible, because the cards aren't in any particular order.
- **Binary search** is like using a **phone book** (or a dictionary). You
  don't start at page 1 — you flip to the middle. If the name you want
  comes alphabetically before what you see, you know it can only be in the
  first half, so you throw away the second half entirely and repeat on what
  remains. You never have to check most of the book.

That's the entire idea behind everything in this file: **linear search
trades no setup cost for slow lookups; binary search demands the data be
sorted first, but pays that cost back many times over with dramatically
faster lookups.**

**Simple mental math:** with 1,000,000 sorted items, linear search might
check up to 1,000,000 of them. Binary search checks at most `log2(1,000,000)
≈ 20`. That's the difference between reading a phone book cover to cover and
finding a name in about 20 flips.

---

## 1. Linear Search (Recap)

Covered on Day 3 — included again here for completeness before contrasting
it with Binary Search.

```python
def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1
```

**Complexity:** O(n) worst case, O(1) space. Works on **any** array, sorted
or not — it makes no assumptions about ordering.

---

## 2. Binary Search — Iterative

**The precondition that changes everything: the array must be sorted.**
Once you know that, you can eliminate **half** of the remaining search space
with every single comparison, instead of checking one element at a time.

**Idea:** maintain a search window `[low, high]`. Look at the middle
element. If it's the target, done. If the target is smaller, the target
(if present) must be in the left half — discard the right half. If the
target is larger, discard the left half. Repeat until found or the window is
empty.

```python
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2    # avoids potential overflow vs (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1                 # target must be in the right half
        else:
            high = mid - 1                # target must be in the left half
    return -1
```

**Why `low + (high - low) // 2` instead of the more obvious
`(low + high) // 2`?** In languages with fixed-size integers (C++, Java),
`low + high` can overflow if both are large, silently producing a wrong
(often negative) `mid`. `low + (high - low) // 2` computes the same value
without ever letting the sum exceed `high`. Python integers don't overflow,
so this specific bug can't happen here — but **write it this way anyway**,
because it's the version that's correct in every language, and interviewers
watch for this exact detail.

**Trace for `binary_search_iterative([1, 3, 5, 7, 9, 11, 13], 7)`:**
| low | high | mid | arr[mid] | comparison | action |
|---|---|---|---|---|---|
| 0 | 6 | 3 | 7 | equal | **return 3** |

Found immediately — lucky first guess. Let's trace a case that takes longer:

**Trace for `binary_search_iterative([1, 3, 5, 7, 9, 11, 13], 3)`:**
| low | high | mid | arr[mid] | comparison | action |
|---|---|---|---|---|---|
| 0 | 6 | 3 | 7 | 7 > 3 | high = 2 |
| 0 | 2 | 1 | 3 | equal | **return 1** |

Two comparisons found it, versus up to 2 comparisons for linear search on
this small example — the gap becomes dramatic as `n` grows (recall Day 1's
table: for `n=1000`, linear search can take 1000 steps, binary search takes
~10).

**Complexity:** **O(log n) time** — this is exactly the halving-loop pattern
from Day 1, section 4.5: the search window's size roughly halves every
iteration. **O(1) space.**

**A critical edge-case habit:** always mentally test with a 0-element array,
a 1-element array, and a target that isn't present, before considering a
binary search implementation done. E.g. `binary_search_iterative([], 5)`:
`low=0, high=-1`, loop condition `0 <= -1` is `False` immediately, returns
`-1` — correct, no crash.

---

## 3. Binary Search — Recursive

Same logic, expressed recursively instead of with a `while` loop — directly
applying Day 4's recursion template (base case + recursive case that shrinks
the problem).

```python
def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:                        # base case: search window is empty
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:                # base case: found it
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)   # search right half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)    # search left half
```

**Complexity:** O(log n) time — same as the iterative version. **Space:
O(log n)**, not O(1) — this is an important contrast to notice (the same
pattern you saw with recursive vs. iterative "is sorted" back on Day 4): each
recursive call adds a stack frame, and since the search window halves each
call, the recursion depth is `O(log n)`. **This is exactly why the iterative
version is generally preferred in production code** — same time complexity,
but O(1) space instead of O(log n).

---

## 4. Lower Bound / Upper Bound — Finding First and Last Occurrence

When an array has **duplicate** values, plain binary search only guarantees
finding *some* occurrence of the target — not necessarily the first or last.
Two closely related, very common variants:

- **Lower bound**: the index of the **first** element that is `>= target`
  (if `target` is present, this is its first occurrence).
- **Upper bound**: the index of the **first** element that is `> target`
  (one past the target's last occurrence, if present).

**Idea:** modify binary search so that instead of stopping the instant you
find a match, you **keep searching left** (toward earlier indices) to find
an even earlier match, remembering the best one found so far.

```python
def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid          # record this match...
            high = mid - 1         # ...but keep searching the LEFT half for an earlier one
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def find_last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid          # record this match...
            low = mid + 1          # ...but keep searching the RIGHT half for a later one
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
```

**Trace for `find_first_occurrence([2, 4, 4, 4, 4, 8, 9], 4)`:**
| low | high | mid | arr[mid] | action | result |
|---|---|---|---|---|---|
| 0 | 6 | 3 | 4 | match! record, search left: high=2 | 3 |
| 0 | 2 | 1 | 4 | match! record, search left: high=0 | 1 |
| 0 | 0 | 0 | 2 | 2 < 4, low=1 | 1 |

`low=1 > high=0`, loop ends. Result: `1` — the first `4` is indeed at index 1.

**Complexity:** still **O(log n) time** (same halving pattern — we never
revisit already-eliminated territory, we just don't stop at the *first*
match found), **O(1) space**.

### Count Occurrences of an Element

Once you have first and last occurrence, counting is a one-liner:

```python
def count_occurrences(arr, target):
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0                # target not present at all
    last = find_last_occurrence(arr, target)
    return last - first + 1
```

For `[2, 4, 4, 4, 4, 8, 9]` and `target=4`: `first=1`, `last=4`,
count = `4 - 1 + 1 = 4`. Correct.

**Complexity:** O(log n) time (two binary searches), O(1) space.

---

## 5. Searching in a Rotated Sorted Array

**Why this deserves its own section:** this is one of the single most
common binary-search interview questions, and it's the natural next step
once plain binary search feels comfortable — the array is *still* sorted,
just not starting from the smallest element.

**Setup:** a sorted array has been "rotated" at some unknown pivot point.
E.g. `[4, 5, 6, 7, 0, 1, 2]` is `[0, 1, 2, 4, 5, 6, 7]` rotated so it starts
at index 4. We don't know where the rotation point is in advance.

**The key insight (simple version):** even though the *whole* array isn't
sorted anymore, **at least one of the two halves around any `mid` always
is.** So at each step:
1. Compute `mid` as usual.
2. Figure out which half (`[low, mid]` or `[mid, high]`) is the sorted one
   — check `arr[low] <= arr[mid]`.
3. Check whether `target` falls inside that sorted half's range. If yes,
   search that half. If no, the target must be in the *other* half — search
   there instead.

This is exactly ordinary binary search's halving logic, with one extra "which
half is sorted?" check bolted on before deciding which way to go.

```python
def search_rotated(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:                   # left half [low, mid] is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1                       # target is inside the sorted left half
            else:
                low = mid + 1                        # target must be in the right half
        else:                                        # right half [mid, high] is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1                        # target is inside the sorted right half
            else:
                high = mid - 1                        # target must be in the left half
    return -1
```

**Trace for `search_rotated([4, 5, 6, 7, 0, 1, 2], 0)`:**
| low | high | mid | arr[mid] | which half sorted? | target in it? | action |
|---|---|---|---|---|---|---|
| 0 | 6 | 3 | 7 | left `[4,5,6,7]` sorted | 0 not in `[4,7)` | low = 4 |
| 4 | 6 | 5 | 1 | left `[0,1]` sorted | 0 in `[0,1)` | high = 4 |
| 4 | 4 | 4 | 0 | equal | — | **return 4** |

**Complexity:** **O(log n) time** — we still discard half the search space
every step, we just spend one extra comparison figuring out which half to
trust. **O(1) space.**

**Common mistake to avoid:** using `<` instead of `<=` in `arr[low] <=
arr[mid]` breaks the case where the left half has only one element
(`low == mid`) — that single-element half is trivially sorted, and `<=`
correctly captures that; `<` alone would misroute it.

---

## 6. Searching in a Row-and-Column Sorted 2D Matrix

**Setup:** each row is sorted left-to-right, and each column is sorted
top-to-bottom, e.g.:
```
[ 1,  4,  7, 11]
[ 2,  5,  8, 12]
[ 3,  6,  9, 16]
[10, 13, 14, 17]
```
**Naive idea (don't do this):** run binary search on each row separately —
`O(rows * log(cols))`. Works, but there's a neat `O(rows + cols)` trick that
uses the 2D sorted structure directly instead of treating it as many
separate 1D problems.

**The "staircase" idea:** start at the **top-right** corner. At each step:
- If the current value equals the target, done.
- If the current value is **bigger** than the target, the whole column
  below it is even bigger (columns increase downward) — so it's useless;
  move **left**.
- If the current value is **smaller** than the target, the whole row to its
  left is even smaller (rows increase rightward) — so it's useless; move
  **down**.

Each move eliminates an entire row or an entire column, so this takes at
most `rows + cols` steps — starting from the top-left or bottom-right corner
does *not* work the same way, since a move can't eliminate a full row/column
from those corners (try tracing it to see why).

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return (-1, -1)
    row, col = 0, len(matrix[0]) - 1     # start top-right
    while row < len(matrix) and col >= 0:
        current = matrix[row][col]
        if current == target:
            return (row, col)
        elif current > target:
            col -= 1                      # eliminate this column
        else:
            row += 1                      # eliminate this row
    return (-1, -1)
```

**Trace for `search_matrix(matrix, 8)` on the matrix above:**
| row | col | current | comparison | action |
|---|---|---|---|---|
| 0 | 3 | 11 | 11 > 8 | col=2 |
| 0 | 2 | 7 | 7 < 8 | row=1 |
| 1 | 2 | 8 | equal | **return (1, 2)** |

**Complexity:** **O(rows + cols) time** — far better than `O(rows *
log(cols))` for large matrices. **O(1) space.**

---

## 7. Binary Search on the Answer (Search Space)

This is the pattern flagged back in the End-of-Week self-check as
resurfacing constantly from Week 5 onward — worth a first look now while
plain binary search is fresh.

**The reframe:** so far, binary search has been applied to an actual array.
But the *real* underlying trick is more general: **binary search works on
any monotonic yes/no question over a range of numbers** — the array is just
one example of such a range. If you can write a function `is_ok(x)` that is
`False` for small `x` and then flips to `True` (and stays `True`) for all
larger `x` — a single "flip point" — you can binary search directly on `x`
itself to find that flip point, even if no array is involved at all.

**Toy example — smallest number whose square is `>= n`:**
```python
def smallest_square_root(n):
    low, high = 0, n
    result = n
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid >= n:            # is_ok(mid): "is mid big enough?"
            result = mid                # record candidate answer
            high = mid - 1              # try to find a smaller one that still works
        else:
            low = mid + 1                # mid too small, need bigger
    return result

print(smallest_square_root(10))   # 4  (4*4=16 >= 10, 3*3=9 < 10)
```

Notice the shape is **identical** to `find_first_occurrence` from section
4 — "record a candidate, then keep narrowing toward a better one" — just
applied to a computed condition (`mid * mid >= n`) instead of an array
comparison (`arr[mid] == target`). This is the generalization: **wherever
you can binary-search an array for the first index where some condition
becomes true, you can binary-search a numeric range for the first value
where some condition becomes true.**

**Why this matters:** problems like "minimum number of days to ship all
packages," "smallest capacity so a ferry can carry all cargo in `k` trips,"
or "kth smallest element in a sorted matrix" don't look like search
problems at first glance — there's no array to binary search *over*. But
each has a monotonic condition ("is capacity `x` large enough?") that flips
from `False` to `True` exactly once, which is the signal to binary search
on the answer instead of brute-forcing every candidate value.

**Complexity:** depends on the range size and the cost of `is_ok(x)` —
generically `O(log(range) * cost_of_is_ok)`.

---

## 8. Exponential Search (Brief Mention)

**When it's useful:** you have a sorted collection but **don't know its
size** in advance (e.g., searching a stream, or an array exposed only
through an iterator/API with no `len()`), so you can't set `high = len(arr)
- 1` the normal way.

**Idea:** find a valid upper bound for the search window first, by doubling
a bound (`1, 2, 4, 8, 16, ...`) until it either overshoots the target or the
end of the data — then run ordinary binary search inside that bound.

```python
def exponential_search(arr, target):
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2                       # double the bound each time
    low = bound // 2
    high = min(bound, len(arr) - 1)
    # ordinary binary search within [low, high]
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**Complexity:** **O(log i) time**, where `i` is the position of the target
— the doubling phase takes `O(log i)` steps, and the binary search phase
inside a window of size `O(i)` also takes `O(log i)`. For a target near the
start of a huge array, this beats plain binary search's `O(log n)` because
it never has to "know" `n` at all.

---

## Worked Examples — Trace These Yourself First

**Example A:** Why does `find_first_occurrence` set `high = mid - 1` (not
`low = mid + 1`) immediately after recording a match?
<details><summary>Answer</summary>
Because we're looking for the *first* occurrence — after finding a match at
`mid`, there might be an even earlier match somewhere in `[low, mid-1]` (the
left half), but everything in `[mid+1, high]` (the right half) is guaranteed
to be at indices *after* this match, so it can't contain an earlier one.
Narrowing to the left half is what lets the search keep looking for a
better (earlier) answer without losing the one already found (which is
saved in `result` before narrowing).
</details>

**Example B:** What does `find_first_occurrence(arr, target)` return if
`target` isn't in `arr` at all? Why is that a safe sentinel value?
<details><summary>Answer</summary>
It returns `-1`, because `result` is initialized to `-1` and is only ever
updated when `arr[mid] == target` actually happens — if that never happens,
the initial `-1` is returned unchanged. `-1` is a safe sentinel here because
it's never a valid array index, so any caller can immediately distinguish
"not found" from a real position.
</details>

**Example C:** Both the iterative and recursive Binary Search have O(log n)
*time* complexity. Which has better *space* complexity, and why does that
make it the generally preferred choice?
<details><summary>Answer</summary>
The iterative version has O(1) space (just a few scalar variables, updated
in place across loop iterations), while the recursive version has O(log n)
space (one stack frame per recursive call, and the recursion depth matches
the number of halvings, i.e. log n). Since both give identical time
complexity, the iterative version is strictly better on space with no
downside — which is why it's the default choice in most real code, with the
recursive version mainly useful for teaching/clarity or when a problem's
structure makes recursion more natural.
</details>

---

## Practice Questions

### Question 1 — Binary Search (Iterative and Recursive)
**Question:** Given a sorted array and a target value, return the target's
index, or `-1` if not present. Implement both iteratively and recursively.
**Input:** `arr = [1, 3, 5, 7, 9, 11, 13], target = 9`
**Output:** `4`
**Solution:**
```python
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search_iterative(arr, 9))   # 4
print(binary_search_recursive(arr, 9))   # 4
```
Halve the search window each step by comparing against the middle element.
Complexity: `O(log n)` time for both; `O(1)` space iterative vs. `O(log n)`
space recursive (section 2–3).

### Question 2 — First and Last Occurrence in a Sorted Array
**Question:** Given a sorted array with possible duplicates and a target,
return the first and last indices at which the target appears (or `[-1,-1]`
if absent).
**Input:** `arr = [2, 4, 4, 4, 4, 8, 9], target = 4`
**Output:** `[1, 4]`
**Solution:**
```python
def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def find_last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

arr = [2, 4, 4, 4, 4, 8, 9]
print([find_first_occurrence(arr, 4), find_last_occurrence(arr, 4)])   # [1, 4]
```
Modified binary search that keeps narrowing toward one side after finding a
match, instead of stopping immediately. Complexity: `O(log n)` time (each
function), `O(1)` space (section 4).

### Question 3 — Count Occurrences of an Element in a Sorted Array
**Question:** Given a sorted array and a target, return how many times the
target appears.
**Input:** `arr = [2, 4, 4, 4, 4, 8, 9], target = 4`
**Output:** `4`
**Input 2:** `arr = [2, 4, 4, 4, 4, 8, 9], target = 5`
**Output 2:** `0`
**Solution:**
```python
def count_occurrences(arr, target):
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    last = find_last_occurrence(arr, target)
    return last - first + 1

arr = [2, 4, 4, 4, 4, 8, 9]
print(count_occurrences(arr, 4))   # 4
print(count_occurrences(arr, 5))   # 0
```
Built directly on Question 2's two functions: if the target isn't found at
all (`first == -1`), return `0` immediately; otherwise the count is simply
`last - first + 1`. Complexity: `O(log n)` time (two binary searches),
`O(1)` space.

### Question 4 — Search in a Rotated Sorted Array
**Question:** Given a sorted array that's been rotated at an unknown pivot,
and a target, return its index or `-1`.
**Input:** `arr = [4, 5, 6, 7, 0, 1, 2], target = 0`
**Output:** `4`
**Solution:**
```python
def search_rotated(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))   # 4
```
At each step, one of the two halves around `mid` is guaranteed to be
normally sorted — identify which one, then check if the target's value
falls in that half's range before deciding which side to keep. Complexity:
`O(log n)` time, `O(1)` space (section 5).

### Question 5 — Search a 2D Sorted Matrix
**Question:** Given a matrix sorted ascending across each row and down each
column, find the `(row, col)` of `target`, or `(-1, -1)` if absent.
**Input:**
```
matrix = [[1,4,7,11],
          [2,5,8,12],
          [3,6,9,16],
          [10,13,14,17]], target = 8
```
**Output:** `(1, 2)`
**Solution:**
```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return (-1, -1)
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        current = matrix[row][col]
        if current == target:
            return (row, col)
        elif current > target:
            col -= 1
        else:
            row += 1
    return (-1, -1)

matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
print(search_matrix(matrix, 8))   # (1, 2)
```
Start at the top-right corner; each comparison eliminates a full row or a
full column, so this reaches the answer (or exhausts the matrix) in at most
`rows + cols` steps. Complexity: `O(rows + cols)` time, `O(1)` space
(section 6).

### Question 6 — Binary Search on the Answer: Smallest Divisor
**Question:** Given an array of positive integers and a `threshold`, find
the smallest positive integer `d` such that if every element is divided by
`d` (rounding up) the sum of the results is `<= threshold`.
**Input:** `arr = [1, 2, 5, 9], threshold = 6`
**Output:** `5`
**Solution:**
```python
import math

def smallest_divisor(arr, threshold):
    def total_with_divisor(d):
        return sum(math.ceil(x / d) for x in arr)

    low, high = 1, max(arr)
    result = high
    while low <= high:
        mid = low + (high - low) // 2
        if total_with_divisor(mid) <= threshold:   # is_ok(mid)
            result = mid                              # candidate divisor works; try smaller
            high = mid - 1
        else:
            low = mid + 1                              # too small a divisor, sum too big; go bigger
    return result

print(smallest_divisor([1, 2, 5, 9], 6))   # 5
```
There's no array to search *over* — instead, `is_ok(d)` ("does divisor `d`
keep the sum within threshold?") is `False` for small `d` and flips to
`True` and stays `True` as `d` grows, so we binary search directly on the
candidate divisor values `1..max(arr)`. Same "record a candidate, keep
narrowing" shape as `find_first_occurrence`. Complexity: `O(n * log(max(arr)))`
time (each of the `O(log(max(arr)))` binary-search steps costs `O(n)` to
compute the sum), `O(1)` space (section 7).

---

## End-of-Week 1 Self-Check

Before moving to Week 2, work through these from a blank page, **timed**,
with no notes:

1. Implement Binary Search (iterative) — target: under 3 minutes, zero bugs
   on the first try (watch the `mid` formula and `low <= high` condition).
2. State the time complexity of any nested-loop snippet shown to you in
   under 10 seconds.
3. Explain recursion using the call-stack/frame model (Day 4, section 2),
   not just "it calls itself."
4. Implement Merge Sort's `merge` step without looking it up.
5. State, from memory, the full 5-algorithm comparison table from Day 6
   (best/worst/average time, space, stability for Selection, Bubble,
   Insertion, Merge, Quick Sort).
6. Explain, in one or two sentences, why Rotated Sorted Array search still
   works even though the array as a whole isn't sorted (section 5).
7. State the "binary search on the answer" pattern in your own words: what
   property must `is_ok(x)` have for this technique to apply (section 7)?

If any of these feel shaky, spend an extra day here before Week 2 —
everything after this compounds on these fundamentals: Week 2's array
problems assume fluent Big-O reasoning and comfortable two-pointer/loop
patterns; Binary Search resurfaces heavily from Week 5 onward (including
"binary search on the answer," a pattern built directly on today's material).

## Revision (of Weeks 1)

- Reverse a Linked List, sum of digits, and Fibonacci (Day 4) — pick one and
  re-solve cold.
- Selection Sort and Insertion Sort (Day 5) — re-implement both back to back.

## Key Takeaways

- Binary Search requires a **sorted** array, and works by eliminating half
  the remaining search space each comparison — **O(log n)** time.
- Iterative Binary Search is **O(1)** space; recursive is **O(log n)**
  space (call stack) — same time complexity, so iterative is generally
  preferred when there's no other reason to prefer recursion.
- **Lower bound / first occurrence** and **upper bound / last occurrence**
  are binary search variants that keep narrowing toward one side *after*
  finding a match, instead of stopping immediately — both still **O(log n)**.
- Counting occurrences of a value in a sorted array reduces to
  `last_occurrence - first_occurrence + 1`, computed with two O(log n)
  searches instead of an O(n) scan.
- **Rotated sorted array search** still runs in **O(log n)**: at every
  `mid`, one of the two halves is guaranteed normally sorted — identify it,
  check whether the target's value falls in its range, and recurse into the
  correct half either way.
- **2D matrix search** (sorted by row and column) runs in **O(rows + cols)**
  by starting at a corner (e.g. top-right) where each comparison eliminates
  an entire row or column — much better than binary-searching every row
  separately.
- **Binary search on the answer** generalizes the whole technique beyond
  arrays: any monotonic yes/no condition over a numeric range (`False` then
  flipping permanently to `True`) can be binary searched directly, using the
  exact same "narrow the window, record the best candidate" shape as
  `find_first_occurrence`. This is the pattern behind many problems that
  don't look like search problems at first glance.
- **Exponential search** finds a valid search bound by doubling (`1, 2, 4,
  8, ...`) before running ordinary binary search inside it — useful when the
  collection's size isn't known up front, running in **O(log i)** where `i`
  is the target's position.
