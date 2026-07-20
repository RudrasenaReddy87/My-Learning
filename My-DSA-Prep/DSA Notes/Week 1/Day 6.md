# Day 6 — Sorting Algorithms II (Efficient)

**Week 1: Foundations** | [Week overview](README.md)
*(Lighter day)*

**Language: Python**

---

## 0. The Big Picture — Divide and Conquer in Plain English

Yesterday's sorts (Selection, Bubble, Insertion) all work the same simple
way: **repeatedly scan the data and fix one thing at a time.** That's easy
to understand but wasteful — you keep re-scanning things you've already
looked at.

Today's algorithms use a completely different strategy called
**divide and conquer**: break the problem into smaller pieces, solve each
small piece (often by breaking it down *again*), then combine the small
solved pieces back into a solution for the whole thing.

**Two simple analogies:**
- **Merge Sort ≈ sorting a huge stack of exam papers by splitting it among
  friends.** Hand half the stack to a friend, half to another. Each friend
  splits their half again, and again, until everyone has just one or two
  papers (trivially "sorted"). Then friends pair up and **merge** their two
  sorted piles into one sorted pile by comparing the top papers, working
  back up until one giant sorted stack remains.
- **Quick Sort ≈ organizing a bookshelf around a reference book.** Pick one
  book as a "pivot." Put every book that comes before it (alphabetically)
  to its left, every book that comes after to its right. The pivot is now
  in its exact final position. Now you have two smaller, independent piles
  — repeat the same trick on each pile separately.

Both strategies turn one big `O(n)`-ish problem into smaller sub-problems
whose costs still add up nicely — which is exactly why both land at
`O(n log n)`, far better than yesterday's `O(n²)` algorithms, as the next
section proves formally.

---

## 1. Why We Need Better Than O(n²)

Yesterday's three algorithms all degrade to O(n²) in the worst/average case.
For `n = 100,000`, O(n²) means roughly 10,000,000,000 operations — even at a
billion operations per second, that's 10+ seconds, likely too slow for most
real applications and almost certainly too slow for an interview's time
limit. We need algorithms that scale better.

**The key idea that unlocks better performance: divide and conquer.** Instead
of comparing every element against every other element (which is what
inherently produces O(n²)), we split the problem into smaller pieces, solve
each piece, and combine the results — often in a way that avoids redundant
comparisons entirely. Merge Sort and Quick Sort, today's two main
algorithms, both use this strategy, but in very different ways.

**A note for later:** no *comparison-based* sorting algorithm (one that only
learns about elements by comparing pairs of them) can do better than
`O(n log n)` in the worst case — this is a proven mathematical lower bound,
not just something no one's found a way around yet. So `O(n log n)` isn't
just "pretty good," it's essentially optimal for comparison sorting. (Sorts
that exploit extra structure — like counting sort or radix sort — can beat
this, but they're out of scope for today.)

---

## 2. Merge Sort

**Idea — divide and conquer:** split the array into two halves, recursively
sort each half, then **merge** the two sorted halves back together into one
sorted array. The "hard work" of sorting happens *implicitly* through the
recursion; the only genuinely new logic needed is merging two already-sorted
arrays, which can be done in a single linear pass.

### The merge step first

Given two sorted arrays, produce one sorted array containing all their
elements. Keep two pointers, one into each array, and repeatedly take the
smaller of the two "current" elements.

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # <=, not <, to keep it stable (see below)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])           # append any leftovers from either side
    result.extend(right[j:])
    return result
```

**Trace for `merge([2, 5, 8], [1, 3, 9])`:**
| i | j | comparison | append | result so far |
|---|---|---|---|---|
| 0 | 0 | 2 vs 1 | 1 (from right) | [1] |
| 0 | 1 | 2 vs 3 | 2 (from left) | [1,2] |
| 1 | 1 | 5 vs 3 | 3 (from right) | [1,2,3] |
| 1 | 2 | 5 vs 9 | 5 (from left) | [1,2,3,5] |
| 2 | 2 | 8 vs 9 | 8 (from left) | [1,2,3,5,8] |
| 3 | 2 | `i` out of bounds, loop ends | — | — |

Leftover: `right[2:] = [9]` appended → `[1,2,3,5,8,9]`. Correct.

### The full recursive sort

```python
def merge_sort(arr):
    if len(arr) <= 1:                     # base case: 0 or 1 elements are trivially sorted
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])           # recursively sort left half
    right = merge_sort(arr[mid:])          # recursively sort right half
    return merge(left, right)               # combine the two sorted halves
```

**Trace for `merge_sort([5, 2, 8, 1])` (the recursion tree):**
```
merge_sort([5,2,8,1])
├── merge_sort([5,2])
│   ├── merge_sort([5]) → [5]   (base case)
│   ├── merge_sort([2]) → [2]   (base case)
│   └── merge([5],[2]) → [2,5]
├── merge_sort([8,1])
│   ├── merge_sort([8]) → [8]   (base case)
│   ├── merge_sort([1]) → [1]   (base case)
│   └── merge([8],[1]) → [1,8]
└── merge([2,5],[1,8]) → [1,2,5,8]
```
Result: `[1, 2, 5, 8]`. Notice the same "recurse down to base cases, then
combine on the way back up" shape from Day 4's recursion lessons — Merge
Sort is fundamentally just recursion plus a merge step.

**Time complexity derivation:** at each "level" of the recursion tree, the
total work done across all the merges at that level is `O(n)` (every element
gets touched exactly once per level, across however many merge calls are
happening at that level). The tree has `O(log n)` levels, because the array
size halves at each level of recursion (the same halving pattern from Day 1,
section 4.5). Total: `O(n)` work per level × `O(log n)` levels = **O(n log n)**.

This holds in the **best, worst, and average case alike** — unlike Quick
Sort below, Merge Sort's split is always exactly in half regardless of the
data, so its performance doesn't depend on the input's arrangement.

**Space complexity: O(n)** — this is Merge Sort's main weakness. The `merge`
function builds brand-new lists at every level of recursion; unlike
yesterday's three algorithms, **Merge Sort is not in-place** in this typical
implementation (an in-place merge is possible but significantly more complex
and rarely worth it in practice).

**Stability: Stable.** The `<=` (not `<`) in the merge step's comparison is
what guarantees this — when `left[i]` and `right[j]` are equal, the element
from `left` (which came from the earlier portion of the original array) is
taken first, preserving original relative order.

---

## 3. Quick Sort

**Idea — divide and conquer, but differently:** pick a **pivot** element,
**partition** the array so everything smaller than the pivot ends up on its
left and everything larger ends up on its right (the pivot itself lands in
its final sorted position), then recursively sort the left and right
partitions independently.

The crucial difference from Merge Sort: Quick Sort does its "hard work"
**before** recursing (the partition step), and needs **no merge step
afterward** — once both sides are sorted, the whole array is sorted, because
everything on the left is already ≤ everything on the right by construction.

### The partition step (Lomuto partition scheme)

```python
def partition(arr, low, high):
    pivot = arr[high]           # choose the last element as pivot
    i = low - 1                  # boundary of "elements known to be <= pivot"
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]   # place pivot in its final spot
    return i + 1                  # return the pivot's final index
```

**Trace for `partition([5, 2, 8, 1, 9], 0, 4)` (pivot = `arr[4] = 9`):**
| j | arr[j] | arr[j] <= 9? | action | i | arr after |
|---|---|---|---|---|---|
| 0 | 5 | yes | i→0, swap(0,0) | 0 | [5,2,8,1,9] |
| 1 | 2 | yes | i→1, swap(1,1) | 1 | [5,2,8,1,9] |
| 2 | 8 | yes | i→2, swap(2,2) | 2 | [5,2,8,1,9] |
| 3 | 1 | yes | i→3, swap(3,3) | 3 | [5,2,8,1,9] |

Loop ends. Place pivot: swap `arr[4]` (pivot, value 9) with `arr[i+1]=arr[4]`
— no change since they're the same index. Return `4`. (Since `9` was the
largest element, it correctly stays at the end — its already-final sorted
position.)

**A more illustrative trace — `partition([5, 2, 8, 1, 3], 0, 4)`, pivot =
`arr[4] = 3`:**
| j | arr[j] | arr[j] <= 3? | action | i | arr after |
|---|---|---|---|---|---|
| 0 | 5 | no | — | -1 | [5,2,8,1,3] |
| 1 | 2 | yes | i→0, swap(0,1) | 0 | [2,5,8,1,3] |
| 2 | 8 | no | — | 0 | [2,5,8,1,3] |
| 3 | 1 | yes | i→1, swap(1,3) | 1 | [2,1,8,5,3] |

Loop ends. Place pivot: swap `arr[4]=3` with `arr[i+1]=arr[2]=8` →
`[2,1,3,5,8]`. Return `2`. Check: everything left of index 2 (`2,1`) is
`≤ 3`, everything right (`5,8`) is `> 3`, and `3` sits exactly at index 2.
Correct partition.

### The full recursive sort

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:                           # base case: 0 or 1 elements need no work
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)    # recursively sort left partition
        quick_sort(arr, pivot_index + 1, high)   # recursively sort right partition
    return arr
```

**Time complexity derivation:**
- **Best/average case: O(n log n).** If the pivot consistently splits the
  array into two roughly-equal halves, the recursion has `O(log n)` levels
  (same halving argument as Merge Sort), and partitioning at each level does
  `O(n)` total work. `O(n)` × `O(log n)` = `O(n log n)`.
- **Worst case: O(n²).** This happens when the pivot is *consistently* the
  smallest or largest remaining element — e.g., calling this exact
  implementation (which always picks `arr[high]` as pivot) on an
  **already-sorted array**. Each partition step then produces one empty side
  and one side of size `n-1`, giving a recursion depth of `n` instead of
  `log n`, with `O(n)` work at each level: `O(n) × O(n) = O(n²)`.

**Why does this matter practically?** The worst case is a *real risk*, not
just a theoretical curiosity — if you naively pick a fixed pivot position
(always first, or always last) on data that happens to already be sorted (or
reverse-sorted), you hit O(n²) every time. **Mitigation:** picking a
**random** pivot (or the median of a few sampled elements) makes the worst
case astronomically unlikely for any *fixed* input, since an adversary would
need to predict your random choices to construct a bad case. This is why
production Quick Sort implementations almost always randomize pivot
selection.

**Space complexity: O(log n) average case** (the recursion call stack depth,
since each level roughly halves the remaining range), but **O(n) worst
case** (matching the O(n²) time worst case — a completely lopsided partition
chain recurses `n` levels deep). Unlike Merge Sort, Quick Sort **is in-place**
in the sense that it doesn't allocate new arrays for the data itself — only
the recursion stack uses extra space.

**Stability: Not stable.** The partition step's swaps can move an element
past an equal element without preserving their relative order (similar
root cause to Selection Sort's instability on Day 5).

---

## 4. Dutch National Flag Algorithm (Sort 0s, 1s, 2s)

This is a specialized, single-pass sorting algorithm for the specific case
of an array containing only three distinct values (conventionally `0`, `1`,
`2`) — named after the three bands of color on the Dutch flag, since sorting
the array groups each value into its own contiguous "band."

**Why not just use a general sort?** A comparison sort would cost
`O(n log n)`. But with only 3 possible values, we can do much better — a
**single O(n) pass**, using three pointers.

**Idea — three pointers, one pass:**
- `low`: boundary — everything before `low` is confirmed `0`.
- `high`: boundary — everything after `high` is confirmed `2`.
- `mid`: the current element being examined; everything between `low` and
  `mid` (exclusive) is confirmed `1`.

```python
def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1                 # safe to advance: arr[low] (now swapped in) was already processed as `mid` earlier, OR is the original arr[mid]
        elif arr[mid] == 1:
            mid += 1                 # 1 belongs in the middle band already — just move on
        else:                        # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1                # do NOT advance mid: the swapped-in value from `high` is unexamined
    return arr
```

**Why does the `0` case advance `mid`, but the `2` case doesn't?** When you
swap `arr[low]` and `arr[mid]`, the value moving into `arr[mid]`'s position
came from `arr[low]`, which — since `low <= mid` always holds and everything
in `[low, mid)` was already confirmed to be `1` (or this is the very first
step) — is guaranteed to be either the same value we started with or already
a known-safe value, so it's safe to move past it. But when you swap
`arr[mid]` and `arr[high]`, the value moving into `arr[mid]`'s position came
from `arr[high]` — the **unexamined** tail end of the array — so it could be
a `0`, `1`, or `2`, and `mid` must stay put to examine it next.

**Trace for `arr = [2, 0, 1, 2, 1, 0]`:**
| low | mid | high | arr[mid] | action | arr after |
|---|---|---|---|---|---|
| 0 | 0 | 5 | 2 | swap(mid,high), high→4 | [0,0,1,2,1,2] |
| 0 | 0 | 4 | 0 | swap(low,mid), low→1, mid→1 | [0,0,1,2,1,2] |
| 1 | 1 | 4 | 0 | swap(low,mid) (self-swap), low→2, mid→2 | [0,0,1,2,1,2] |
| 2 | 2 | 4 | 1 | mid→3 | [0,0,1,2,1,2] |
| 2 | 3 | 4 | 2 | swap(mid,high), high→3 | [0,0,1,1,2,2] |
| 2 | 3 | 3 | 1 | mid→4 | [0,0,1,1,2,2] |

`mid=4 > high=3`, loop ends. Result: `[0, 0, 1, 1, 2, 2]`. Correctly sorted.

**Complexity:** **O(n) time** — a single pass, since `mid` and `high`
together sweep across the array exactly once (each index is examined a
bounded number of times). **O(1) space** — sorts in place with just three
index variables. This is a specialized algorithm — it only works because we
know in advance there are exactly 3 distinct values; it's not a
general-purpose sort.

---

## 5. Heap Sort

**Why this one matters:** it's the notable gap if you only learn Merge and
Quick Sort — Heap Sort is the third classic `O(n log n)` comparison sort,
and it's the one that's **both in-place (O(1) space) and guaranteed
O(n log n) in every case**, a combination neither Merge Sort (needs O(n)
space) nor Quick Sort (worst case O(n²)) can offer simultaneously. The
trade-off is that it's usually slower in practice than Quick Sort due to
weaker cache locality (heap operations jump around the array rather than
scanning it sequentially).

**Prerequisite idea — the (binary max-) heap:** a heap is a binary tree
stored in a plain array, with one rule: **every parent is `>=` both its
children** (for a *max*-heap). Because of this rule, the **largest element
is always at the root** — index `0` of the array. The tree structure is
implicit from index arithmetic — for a node at index `i`:
- left child: `2*i + 1`
- right child: `2*i + 2`
- parent: `(i - 1) // 2`

No pointers needed — just index math into a flat array.

**Idea — divide and conquer via extraction:** turn the array into a
max-heap first, so the largest element sits at index `0`. Swap it to the
end of the array (its final sorted position). Shrink the "active heap"
region by one, restore the heap property on what remains (this fix-up step
is called `sift down` / `heapify`), and repeat — each repetition places the
next-largest remaining element correctly.

```python
def heapify(arr, n, i):
    """Ensure the subtree rooted at index i (within arr[0:n]) satisfies the max-heap property."""
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)          # the swap may have broken the heap property further down — fix that too

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):    # build max-heap: heapify every non-leaf node, bottom-up
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]     # move current max to its final sorted position
        heapify(arr, i, 0)                   # restore heap property on the shrunk region [0, i)
    return arr

print(heap_sort([5, 2, 8, 1, 9, 3]))   # [1, 2, 3, 5, 8, 9]
```

**Why heapify bottom-up, and why only from `n // 2 - 1`?** Every index from
`n // 2` onward is a leaf (no children) — a single-node tree is trivially a
valid heap, so there's nothing to fix there. Starting from the last
non-leaf node and working backward to the root guarantees that by the time
`heapify` processes a given node, both of its child subtrees are already
valid heaps — exactly the precondition `heapify` needs to work correctly.

**Trace (build-heap phase) for `arr = [5, 2, 8, 1, 9, 3]`, n=6:**
Non-leaf indices to heapify, in order: `2, 1, 0`.
| i | subtree root value | children | action | arr after |
|---|---|---|---|---|
| 2 | 8 | (none, right child index 6 out of range) | already largest, no swap | [5,2,8,1,9,3] |
| 1 | 2 | left=1(idx3), right=9(idx4) | 9 is largest, swap(1,4) | [5,9,8,1,2,3] |
| 0 | 5 | left=9(idx1), right=8(idx2) | 9 is largest, swap(0,1), recurse into idx1 | [9,5,8,1,2,3] |

Max-heap built: `[9, 5, 8, 1, 2, 3]` (check: `9 >= 5,8`; `5 >= 1,2`; `8 >=
3` — valid).

**Trace (extraction phase), first two extractions:**
| step | swap root with last active index | arr | heapify on shrunk region | arr after heapify |
|---|---|---|---|---|
| 1 | swap(0,5): 9↔3 | [3,5,8,1,2,**9**] | heapify(arr,5,0) | [8,5,3,1,2,**9**] |
| 2 | swap(0,4): 8↔2 | [2,5,3,1,**8,9**] | heapify(arr,4,0) | [5,2,3,1,**8,9**] |

Sorted region grows from the right; continuing this process produces
`[1, 2, 3, 5, 8, 9]`.

**Complexity:**
- **Time: O(n log n) in the best, worst, AND average case** — building the
  initial heap is `O(n)` (a known tighter bound than the naive `O(n log n)`
  estimate), and each of the `n` extractions costs `O(log n)` for its
  `heapify` call, giving `O(n log n)` total, with **no data-dependent worst
  case** the way Quick Sort has.
- **Space: O(1)** — sorts in place within the original array; `heapify`'s
  recursion depth is `O(log n)`, which is usually not counted against
  "extra space" the same way Merge Sort's new arrays are, since it's a
  small, bounded call stack rather than duplicated data.
- **Stability: Not stable** — the swaps during heapify can reorder equal
  elements relative to each other, same root cause as Quick Sort's
  instability.

**When to actually reach for Heap Sort:** when you need Merge Sort's
worst-case guarantee (`O(n log n)` always) but can't afford Merge Sort's
`O(n)` extra space — e.g. sorting a huge array in a memory-constrained
environment. It's also the algorithm underlying `heapq`-based "top-k"
patterns, which come up constantly in interviews independent of full
sorting.

---

## 6. Counting Sort (Brief Mention — Beyond Comparison Sorts)

Section 1 mentioned that no *comparison-based* sort can beat `O(n log n)`
worst case. Counting Sort isn't a comparison sort at all — it never asks
"is `a` bigger than `b`?" — so that lower bound simply doesn't apply to it.

**When it applies:** the values being sorted are integers within a **known,
reasonably small range** (e.g. exam scores 0–100, or ages 0–120). It
doesn't work for arbitrary/unbounded data (e.g. sorting arbitrary strings
or floats) — that's the "extra structure" trade-off.

**Idea:** instead of comparing elements, **count how many times each
possible value occurs**, then reconstruct the sorted array directly from
those counts.

```python
def counting_sort(arr, max_value):
    counts = [0] * (max_value + 1)
    for x in arr:
        counts[x] += 1                    # tally occurrences of each value
    result = []
    for value, count in enumerate(counts):
        result.extend([value] * count)     # write out each value `count` times, in order
    return result

print(counting_sort([4, 2, 2, 8, 3, 3, 1], max_value=8))   # [1, 2, 2, 3, 3, 4, 8]
```

**Complexity: O(n + k) time**, where `k` is the range of possible values
(`max_value + 1` here) — no `log n` factor at all, because there are no
comparisons or halvings, just one pass to count and one pass to write out.
`O(k)` space for the counts array (plus `O(n)` for the output). This beats
`O(n log n)` whenever `k` is small relative to `n` — but if `k` is huge
(e.g. sorting arbitrary 64-bit integers), the `counts` array itself becomes
impractically large, which is exactly why this isn't a general-purpose
replacement for comparison sorts.

**A practical footnote on all of today's material:** Python's built-in
`sorted()` / `list.sort()` use an algorithm called **Timsort** — a hybrid
that borrows Merge Sort's stable, guaranteed-`O(n log n)` merging strategy
but switches to a simple insertion-sort-like pass for small runs of already
partially-sorted data (which is extremely common in real-world data). In
interviews you'll implement these algorithms by hand, but in production
Python code, reach for `sorted()`/`.sort()` — they're stable, well-tested,
and faster in practice than a hand-rolled version of any algorithm here.

---

## Updated Comparison Table (All 5 Algorithms So Far)

| Algorithm | Best | Worst | Average | Space | Stable? | In-place? |
|---|---|---|---|---|---|---|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n²) | O(n log n) | O(log n) avg | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting Sort* | O(n + k) | O(n + k) | O(n + k) | O(n + k) | Yes | No |

*Counting Sort is not a general comparison sort — `k` is the range of
possible input values, and it only applies when that range is known and
reasonably small (section 6).

**When would you actually choose Merge Sort over Quick Sort, given Quick
Sort is usually faster in practice?** When you need a *guarantee* against
worst-case O(n²) (e.g. real-time systems), or when you need **stability**
(Quick Sort's in-place partitioning sacrifices it). Quick Sort tends to win
in practice due to better cache locality and lower constant factors, but
Merge Sort's guarantees make it the right choice in specific situations —
this exact trade-off is a common interview discussion question.

---

## Worked Examples — Trace These Yourself First

**Example A:** Why is Merge Sort's time complexity O(n log n) in *every*
case (best, worst, average), while Quick Sort's is only O(n log n) in the
best/average case?
<details><summary>Answer</summary>
Merge Sort always splits the array into exactly two equal halves by index
(`mid = len(arr) // 2`), completely independent of the actual values in the
array — so the recursion depth is always `O(log n)`, no matter what the
input looks like. Quick Sort's split point depends on where the pivot
*value* happens to land after partitioning, which depends on the input data
— a poorly chosen pivot on adversarial data (e.g. already-sorted input with
a fixed pivot choice) can produce a maximally lopsided split, driving the
recursion depth up to `O(n)`.
</details>

**Example B:** In the Dutch National Flag trace above, why does the `mid`
pointer never need to look at indices between `high` and the end of the
array?
<details><summary>Answer</summary>
Everything after `high` has already been confirmed to be `2` (that's the
definition of the `high` boundary) — those elements were already examined
and correctly placed when they were swapped into that region. There's no
need to re-examine them, so `mid` only ever needs to sweep through the
"unknown" middle region between `low` and `high`.
</details>

**Example C:** If you called `quick_sort` (as implemented above, always
picking `arr[high]` as the pivot) on an already-sorted array
`[1, 2, 3, 4, 5]`, would it hit its best case or worst case? Why?
<details><summary>Answer</summary>
Worst case. With `arr[high]` always chosen as the pivot on an already-sorted
array, the pivot is always the *largest* remaining element in its partition
— every partition step produces one side of size `n-1` (everything smaller)
and one side of size `0` (nothing larger). This gives a recursion depth of
`n` instead of `log n`, leading to `O(n²)` time — exactly the scenario
described in section 3's "why does this matter practically" discussion, and
the reason production implementations randomize pivot selection.
</details>

---

## Practice Questions

### Question 1 — Implement Merge Sort
**Question:** Given an array, sort it in ascending order using Merge Sort.
**Input:** `arr = [5, 2, 8, 1, 9, 3]`
**Output:** `[1, 2, 3, 5, 8, 9]`
**Solution:**
```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

print(merge_sort([5, 2, 8, 1, 9, 3]))   # [1, 2, 3, 5, 8, 9]
```
Recursively split in half down to single elements, then merge sorted halves
back together in linear passes. Complexity: `O(n log n)` in all cases,
`O(n)` space, **stable** (section 2).

### Question 2 — Implement Quick Sort
**Question:** Given an array, sort it in ascending order using Quick Sort
(Lomuto partition scheme).
**Input:** `arr = [5, 2, 8, 1, 9, 3]`
**Output:** `[1, 2, 3, 5, 8, 9]`
**Solution:**
```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    return arr

print(quick_sort([5, 2, 8, 1, 9, 3]))   # [1, 2, 3, 5, 8, 9]
```
Partition around a pivot so smaller elements land left and larger land
right, then recursively sort each side independently — no merge step
needed. Complexity: `O(n log n)` best/average, `O(n²)` worst case (e.g.
already-sorted input with this fixed last-element pivot choice), `O(log n)`
average space, **not stable** (section 3).

### Question 3 — Sort an Array of 0s, 1s, and 2s (Dutch National Flag)
**Question:** Given an array containing only the values `0`, `1`, and `2`,
sort it in a single O(n) pass, in-place.
**Input:** `arr = [2, 0, 1, 2, 1, 0]`
**Output:** `[0, 0, 1, 1, 2, 2]`
**Solution:**
```python
def sort_012(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(sort_012([2, 0, 1, 2, 1, 0]))   # [0, 0, 1, 1, 2, 2]
```
Three pointers partition the array into three known bands (`0`s, `1`s, `2`s)
in a single pass — see the full trace in section 4 for why `mid` advances
after a `0`-swap but not after a `2`-swap. Complexity: `O(n)` time, `O(1)`
space — better than any general comparison sort, because this problem has
only 3 possible values.

### Question 4 — Implement Heap Sort
**Question:** Given an array, sort it in ascending order using Heap Sort.
**Input:** `arr = [5, 2, 8, 1, 9, 3]`
**Output:** `[1, 2, 3, 5, 8, 9]`
**Solution:**
```python
def heapify(arr, n, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

print(heap_sort([5, 2, 8, 1, 9, 3]))   # [1, 2, 3, 5, 8, 9]
```
Build a max-heap so the largest element sits at the root, then repeatedly
swap it to the end and restore the heap property on the shrinking remainder.
Complexity: `O(n log n)` in every case, `O(1)` space, **not stable**
(section 5).

### Question 5 — Build the Full Comparison Table From Memory
**Question:** Without checking notes, write out best/worst/average time,
space complexity, and stability for all 7 algorithms covered across Day 5
and Day 6 (Selection, Bubble, Insertion, Merge, Quick, Heap, Counting Sort).
**Input:** N/A (recall exercise).
**Output:** The "Updated Comparison Table" from this lesson.
**Solution:** See the table above. The facts most worth over-learning: Merge
Sort and Heap Sort are the only two with an unconditional `O(n log n)`
guarantee in every case, but Merge Sort needs `O(n)` space while Heap Sort
is `O(1)`; Quick Sort is usually fastest in practice but has an `O(n²)`
worst case that depends on pivot choice; only Bubble, Insertion, Merge, and
Counting Sort are stable; Counting Sort escapes the `O(n log n)` comparison-
sort floor entirely by not comparing elements at all, at the cost of only
working for a bounded, known range of integer values.

## Revision

- Re-implement Selection Sort and Insertion Sort from Day 5 from memory, back
  to back, without pausing.
- Re-check: can you state, out loud, why Quick Sort's worst case is O(n²)
  but its average case is O(n log n)? (See Example C above if you get stuck.)

## Key Takeaways

- **Merge Sort** splits in half, recursively sorts each half, then merges —
  guaranteed **O(n log n)** in every case, but needs **O(n)** extra space and
  is not in-place. **Stable.**
- **Quick Sort** partitions around a pivot so recursion needs no merge step —
  **O(n log n)** average/best, but **O(n²)** worst case if the pivot
  repeatedly lands at an extreme (e.g. fixed-pivot choice on sorted/reverse
  sorted input); mitigated in practice with randomized pivot selection.
  **Not stable**, but in-place (only `O(log n)` average recursion-stack space).
- **Dutch National Flag** is a specialized **O(n)**, **O(1)**-space,
  single-pass sort for arrays with only 3 distinct values — it beats general
  comparison sorts precisely because it exploits that extra structure.
- No comparison-based sort can beat **O(n log n)** in the worst case — this
  is why Merge Sort and (average-case) Quick Sort represent the practical
  ceiling for general-purpose sorting without extra assumptions about the data.
- **Heap Sort** builds a max-heap (largest element always at the root, via
  simple index arithmetic on a flat array), then repeatedly extracts the
  max — **O(n log n) in every case, O(1) space, in-place**, but **not
  stable** and generally slower in practice than Quick Sort due to weaker
  cache locality. It's the one algorithm here offering both the strong time
  guarantee and the space efficiency simultaneously.
- **Counting Sort** sorts by counting occurrences of each value instead of
  comparing elements, running in **O(n + k)** time (`k` = range of possible
  values) — it beats the comparison-sort `O(n log n)` floor entirely, but
  only works when values are integers in a known, reasonably small range.
- In production Python code, prefer the built-in `sorted()` / `.sort()`
  (Timsort — a stable, `O(n log n)`-guaranteed hybrid tuned for real-world
  data) over any hand-rolled algorithm here; these algorithms matter for
  understanding trade-offs and for interviews, not for replacing the
  standard library.
