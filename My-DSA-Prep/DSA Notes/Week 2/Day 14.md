# Day 14 — Combinatorics on Arrays + Weekly Wrap-up

**Week 2: Arrays Part 1–2** | [Week overview](README.md)
*(Lighter day)*

**Language: Python**

---

## 1. Find the Repeating and Missing Number

**The problem:** an array of size `n` is supposed to contain every integer
from `1` to `n` exactly once — but instead, one number is **missing** and
another number is **duplicated** (appearing twice) in its place. Find both
the repeating number and the missing number.

**Example:** `[3, 1, 2, 5, 3]` (`n=5`) — every number 1-5 should appear once,
but `3` appears twice and `4` is missing. Repeating = `3`, Missing = `4`.

### Approach 1 — Math (sum and sum of squares)

**Setup:** let `R` = the repeating number, `M` = the missing number.

- The **expected sum** of `1..n` is `S = n(n+1)/2`.
- The **actual sum** of the array is `S' = S - M + R` (we're missing `M`
  from the ideal sum, but we have an extra `R` in its place).
- So: `S' - S = R - M`. Call this difference `D1 = R - M`.

That's one equation with two unknowns — we need a second, independent
equation to solve for `R` and `M` individually. Sum of **squares** gives us
that:

- Expected sum of squares: `S2 = 1² + 2² + ... + n² = n(n+1)(2n+1)/6`.
- Actual sum of squares: `S2' = S2 - M² + R²`.
- So: `S2' - S2 = R² - M² = (R-M)(R+M)`. Since we already know
  `D1 = R - M`, we can solve: `(R+M) = (S2' - S2) / D1`. Call this `D2`.

Now we have two equations: `R - M = D1` and `R + M = D2`. Solving
simultaneously: `R = (D1 + D2) / 2`, `M = (D2 - D1) / 2`.

```python
def find_repeating_and_missing_math(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6

    actual_sum = sum(arr)
    actual_sq_sum = sum(x * x for x in arr)

    d1 = actual_sum - expected_sum              # R - M
    d2 = (actual_sq_sum - expected_sq_sum) // d1  # R + M

    repeating = (d1 + d2) // 2
    missing = (d2 - d1) // 2
    return repeating, missing
```

**Trace for `arr = [3, 1, 2, 5, 3]` (`n=5`):**
- `expected_sum = 5*6//2 = 15`. `actual_sum = 3+1+2+5+3 = 14`.
  `d1 = 14 - 15 = -1` (i.e. `R - M = -1`).
- `expected_sq_sum = 5*6*11//6 = 55`. `actual_sq_sum = 9+1+4+25+9 = 48`.
  `d2 = (48 - 55) // -1 = 7` (i.e. `R + M = 7`).
- `repeating = (-1 + 7) // 2 = 3`. `missing = (7 - (-1)) // 2 = 4`.

Result: `(repeating=3, missing=4)`. Matches the expected answer.

**Complexity:** **O(n) time** (two linear passes to compute sums, or one
combined pass), **O(1) space**.

### Approach 2 — XOR (conceptual overview)

**Idea:** XOR-ing every array element together with every number from `1` to
`n` cancels out every value that appears exactly the expected number of
times (any value appearing in both the array and the range exactly once
cancels to 0 via `a^a=0`). What's left is `R ^ M` — the repeating value
contributes an *extra* copy (appears twice in the array + once in the range
= 3 total occurrences = an odd count = survives XOR), and the missing value
contributes one *fewer* copy (0 in the array + 1 in the range = 1
occurrence = also survives).

Once you have `xor_all = R ^ M`, find any bit where they **differ** (e.g.
the rightmost set bit of `xor_all`), and use that bit to split both the
array and the range `1..n` into two groups — one group where that bit is
set, one where it's not. `R` and `M` necessarily land in *different* groups
(since that's a bit where they differ), so XOR-ing each group separately
isolates `R` and `M` into two separate values. A final pass checking which
one actually appears in the original array (twice) tells you which is `R`
and which is `M`.

This approach is also **O(n) time, O(1) space**, and has the advantage of
using only integer XOR (no risk of large-number overflow from squaring,
though this isn't a practical concern in Python). It's presented here
conceptually rather than with full code — the math approach above is
generally easier to implement correctly under interview time pressure, but
recognizing the XOR approach exists (and why it works) is valuable, since
some interviewers specifically ask for a non-arithmetic-overflow-prone
alternative.

---

## 2. Count Inversions in an Array

**The problem:** count the number of pairs `(i, j)` with `i < j` but
`arr[i] > arr[j]` (i.e., pairs that are "out of order" relative to fully
sorted order). This is a measure of how far an array is from being sorted —
a fully sorted array has 0 inversions; a fully reverse-sorted array has the
maximum possible, `n(n-1)/2`.

**Example:** `arr = [2, 4, 1, 3, 5]` → inversions: `(2,1)` at indices
`(0,2)`, `(4,1)` at `(1,2)`, `(4,3)` at `(1,3)` — **3 inversions** total.

**Brute force:** check every pair — `O(n²)`.

**The optimal trick — piggyback on Merge Sort.** Recall Merge Sort's `merge`
step (Day 6) combines two already-sorted halves by repeatedly taking the
smaller of the two current front elements. **Key insight:** whenever the
merge step takes an element from the **right** half (because it's smaller
than the current left element), that element forms an inversion with
**every remaining element still left in the left half** — because the left
half is sorted, so if the current left element is bigger than this right
element, so is every element after it in the left half.

```python
def count_inversions(arr):
    temp = [0] * len(arr)

    def merge_and_count(left, mid, right):
        i, j, k = left, mid + 1, left
        count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                count += (mid - i + 1)   # arr[i..mid] are ALL > arr[j] — that's this many inversions
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]; i += 1; k += 1
        while j <= right:
            temp[k] = arr[j]; j += 1; k += 1
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
        return count

    def sort_and_count(left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += sort_and_count(left, mid)
            count += sort_and_count(mid + 1, right)
            count += merge_and_count(left, mid, right)
        return count

    return sort_and_count(0, len(arr) - 1)
```

**Trace for `arr = [2, 4, 1, 3, 5]`** (focusing on the key merge step that
finds inversions — the full recursive breakdown follows Day 6's Merge Sort
pattern exactly):

Eventually, `merge_and_count` is called to merge the sorted left half
`[2, 4]` (from original indices 0-1) with the sorted right half `[1, 3]`
(from original indices 2-3):
- `i=0(val 2), j=0(val 1)`: `2 > 1` → take `1` from right, count +=
  `(mid - i + 1)` = 2 remaining left elements (`2, 4`) both form inversions
  with this `1`. `count = 2`. `j` advances.
- `i=0(val 2), j=1(val 3)`: `2 <= 3` → take `2` from left, no new inversion.
  `i` advances.
- `i=1(val 4), j=1(val 3)`: `4 > 3` → take `3` from right, count +=
  `(mid - i + 1)` = 1 remaining left element (`4`). `count += 1` → `count=3`.
- Left exhausted after taking `4`.

This single merge call alone found `2 + 1 = 3` inversions — matching the
expected total (and in this particular example, these happen to be exactly
all 3 inversions in the whole array, though in general inversions are found
across every level of the recursion, accumulated via the `count +=` calls
in `sort_and_count`).

**Why does `count += (mid - i + 1)` correctly count inversions, without
double-counting or missing any?** Because the left and right halves were
**already recursively sorted** before this merge call — any inversion
*within* the left half or *within* the right half was already counted by
the earlier recursive calls (`sort_and_count(left, mid)` and
`sort_and_count(mid+1, right)`). This merge step only needs to count
inversions **across** the two halves — and `mid - i + 1` is exactly the
count of remaining (unprocessed) left-half elements, all of which are `>`
the current right-half element being placed (since the left half is
sorted ascending).

**Complexity:** **O(n log n) time** — identical shape to Merge Sort itself
(Day 6), since we're just adding O(1) extra bookkeeping (`count +=`) to each
existing merge comparison. **O(n) space** for the `temp` array, same as
standard Merge Sort.

---

## 3. Reverse Pairs (Harder Inversion-Count Variant)

**The problem:** count pairs `(i, j)` with `i < j` where
**`arr[i] > 2 * arr[j]`** — a stricter, scaled condition than plain
inversions.

**Why can't you reuse `count_inversions` directly?** The condition involves
a factor of `2`, which breaks the simple "take from right, count remaining
left elements" trick used above — that trick relied on the comparison being
the *same* comparison used to decide the merge order (`arr[i] > arr[j]`).
Here, the counting condition (`arr[i] > 2*arr[j]`) is different from the
merge-order condition (`arr[i] > arr[j]`), so counting must happen as a
**separate pass**, using a **two-pointer sweep** over the two (already
individually sorted) halves, done *before* the normal merge overwrites them.

```python
def reverse_pairs(arr):
    temp = [0] * len(arr)

    def merge_and_count(left, mid, right):
        # Count cross-pairs BEFORE merging, while both halves are still
        # individually sorted (but not yet merged into one).
        count = 0
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += (j - (mid + 1))

        # Standard merge (same as count_inversions / Day 6's Merge Sort).
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]; i += 1
            else:
                temp[k] = arr[j]; j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]; i += 1; k += 1
        while j <= right:
            temp[k] = arr[j]; j += 1; k += 1
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
        return count

    def sort_and_count(left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += sort_and_count(left, mid)
            count += sort_and_count(mid + 1, right)
            count += merge_and_count(left, mid, right)
        return count

    return sort_and_count(0, len(arr) - 1)
```

**Why does the two-pointer counting sweep (`j` never resetting between
different `i` values) correctly find all pairs, in O(n) per merge level
rather than O(n²)?** Because `arr[left..mid]` is sorted **ascending**, as
`i` increases, `arr[i]` only grows — so the threshold `2 * arr[j]` needed to
satisfy `arr[i] > 2*arr[j]` becomes easier to exceed with a larger `arr[i]`,
meaning **`j` never needs to move backward** once it has advanced for a
smaller `i`. This monotonic relationship (identical in spirit to the
two-pointer arguments from Day 8) is what keeps this counting pass linear
instead of quadratic.

**Complexity:** the counting sweep adds O(n) work per merge call (same
order as the merge itself), so the overall complexity stays
**O(n log n) time**, **O(n) space** — same class as plain inversion
counting, just with a different (scaled) comparison being counted.

**Sanity-check example:** for `arr = [1, 3, 2, 3, 1]`, brute-force checking
all pairs `(i,j)`, `i<j`, `arr[i] > 2*arr[j]` finds exactly 2 such pairs:
`(index 1, index 4)`: `3 > 2*1=2`, yes; `(index 3, index 4)`: `3 > 2*1=2`,
yes. `reverse_pairs([1,3,2,3,1])` returns `2`, matching.

---

## Worked Examples — Trace These Yourself First

**Example A:** In the math approach for Find Repeating/Missing, why is a
*single* equation (`R - M = D1`) not enough to solve for both `R` and `M`,
and why does bringing in the sum of squares fix that?
<details><summary>Answer</summary>
One linear equation with two unknowns (`R` and `M`) has infinitely many
solutions (e.g. `R=5,M=6` and `R=10,M=11` both satisfy `R-M=-1`) — you need a
**second, independent** equation to pin down a unique solution. The sum of
squares provides exactly that: `R² - M² = (R-M)(R+M)`, which, combined with
the already-known `D1 = R-M`, lets you solve for `R+M` too — two independent
equations (`R-M` and `R+M`) uniquely determine both `R` and `M`.
</details>

**Example B:** In `count_inversions`, why is the total inversion count the
**sum** of the counts from `sort_and_count(left, mid)`,
`sort_and_count(mid+1, right)`, and `merge_and_count(left, mid, right)`,
rather than needing some other combination?
<details><summary>Answer</summary>
Every inversion in the whole array falls into exactly one of three
non-overlapping categories: both elements are in the left half (counted by
the recursive call on the left half), both are in the right half (counted
by the recursive call on the right half), or one is in each half (counted
by the cross-half counting during the merge step). Since these three
categories are mutually exclusive and collectively exhaustive, simply
summing their counts gives the exact total with no double-counting or gaps.
</details>

**Example C:** Why must the reverse-pairs counting sweep happen **before**
the merge step overwrites `arr[left..right]`, rather than being combined
into the same loop as the merge?
<details><summary>Answer</summary>
The counting sweep relies on `arr[left..mid]` and `arr[mid+1..right]` each
being **independently sorted** (a guarantee from the prior recursive calls)
— but the merge step's job is to interleave and overwrite those two ranges
into one combined sorted range. If counting were interleaved with the
merge's own overwriting, the values being compared could already be
corrupted (overwritten) partway through, breaking the sorted-halves
assumption the two-pointer counting sweep depends on. Counting first, using
the still-pristine sorted halves, then merging afterward, keeps the two
steps correctly independent.
</details>

---

## Practice Questions

### Question 1 — Find the Repeating and Missing Number
**Question:** Given an array of size `n` containing numbers from `1` to `n`
with one number missing and one duplicated, find both.
**Input:** `arr = [3, 1, 2, 5, 3]`
**Output:** `(repeating=3, missing=4)`
**Solution:**
```python
def find_repeating_and_missing_math(arr):
    n = len(arr)
    expected_sum = n * (n + 1) // 2
    expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6

    actual_sum = sum(arr)
    actual_sq_sum = sum(x * x for x in arr)

    d1 = actual_sum - expected_sum
    d2 = (actual_sq_sum - expected_sq_sum) // d1

    repeating = (d1 + d2) // 2
    missing = (d2 - d1) // 2
    return repeating, missing

print(find_repeating_and_missing_math([3, 1, 2, 5, 3]))   # (3, 4)
```
Use sum and sum-of-squares differences to form two equations (`R-M` and
`R+M`) and solve simultaneously. Complexity: `O(n)` time, `O(1)` space
(section 1).

### Question 2 — Count Inversions in an Array
**Question:** Count the number of pairs `(i, j)` with `i < j` and
`arr[i] > arr[j]`.
**Input:** `arr = [2, 4, 1, 3, 5]`
**Output:** `3`
**Solution:**
```python
def count_inversions(arr):
    temp = [0] * len(arr)

    def merge_and_count(left, mid, right):
        i, j, k = left, mid + 1, left
        count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]; i += 1
            else:
                temp[k] = arr[j]
                count += (mid - i + 1)
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]; i += 1; k += 1
        while j <= right:
            temp[k] = arr[j]; j += 1; k += 1
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
        return count

    def sort_and_count(left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += sort_and_count(left, mid)
            count += sort_and_count(mid + 1, right)
            count += merge_and_count(left, mid, right)
        return count

    return sort_and_count(0, len(arr) - 1)

print(count_inversions([2, 4, 1, 3, 5]))   # 3
```
Piggyback on Merge Sort: whenever the merge step takes an element from the
right half, every remaining left-half element forms an inversion with it.
Complexity: `O(n log n)` time, `O(n)` space (section 2).

### Question 3 — Reverse Pairs
**Question:** Count pairs `(i, j)` with `i < j` and `arr[i] > 2 * arr[j]`.
**Input:** `arr = [1, 3, 2, 3, 1]`
**Output:** `2`
**Solution:**
```python
def reverse_pairs(arr):
    temp = [0] * len(arr)

    def merge_and_count(left, mid, right):
        count = 0
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += (j - (mid + 1))

        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]; i += 1
            else:
                temp[k] = arr[j]; j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]; i += 1; k += 1
        while j <= right:
            temp[k] = arr[j]; j += 1; k += 1
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]
        return count

    def sort_and_count(left, right):
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += sort_and_count(left, mid)
            count += sort_and_count(mid + 1, right)
            count += merge_and_count(left, mid, right)
        return count

    return sort_and_count(0, len(arr) - 1)

print(reverse_pairs([1, 3, 2, 3, 1]))   # 2
```
A two-pointer sweep counts cross-half pairs satisfying the scaled condition
*before* the merge overwrites the (still individually sorted) halves; the
sweep is linear because `arr[i]` only grows as `i` increases, so `j` never
needs to move backward. Complexity: `O(n log n)` time, `O(n)` space
(section 3).

---

## Weekly Wrap-up — Timed Mixed Practice

Redo these 3 problems from this week from scratch, timed, no notes, to
confirm the patterns have stuck before moving to Week 3:
- **Maximum Subarray Sum** (Kadane's, Day 9) — should take under 3 minutes.
- **Two Sum** (hashing, Day 8) — should take under 3 minutes.
- **Merge Overlapping Intervals** (Day 13) — should take under 5 minutes,
  including remembering to sort first.

If Maximum Product Subarray (Day 9) still feels shaky, that's the one
problem this week most worth a second pass — the max/min swap-on-negative
logic is easy to half-remember incorrectly.

## Revision (of Week 1)

- **Sieve of Eratosthenes** (Week 1, Day 2) — re-implement from memory (it
  resurfaces in graph/number-theory problems later).
- **Sort an array of 0s, 1s, 2s** (Dutch National Flag, Week 1 Day 6 /
  reinforced Day 8) — re-solve cold.

**Mistakes log check-in:** review anything you logged in Week 1 and confirm
you no longer make that mistake. This week introduced several "trick"
patterns (prefix sum/XOR hashing, merge-sort-piggybacked counting) — if any
of those still feel like memorized magic rather than derivable logic, that's
worth flagging in your log specifically, since Week 3 builds directly on
this week's two-pointer and hashing fluency.

## Key Takeaways

- **Find Repeating and Missing** is solved with two independent equations
  (from sum and sum-of-squares differences) — a reminder that one linear
  relationship often isn't enough to separate two unknowns; you need a
  second, genuinely independent source of information.
- **Count Inversions** piggybacks on Merge Sort's existing merge step —
  whenever the merge "reaches across" and takes from the right half early,
  every remaining left-half element is an inversion with it, all countable
  with `O(1)` extra arithmetic per merge comparison, preserving Merge Sort's
  `O(n log n)` time.
- **Reverse Pairs** needs a *separate* two-pointer counting pass (not
  reusable from the merge comparison itself), because its condition
  (`arr[i] > 2*arr[j]`) differs from the merge's own ordering condition
  (`arr[i] > arr[j]`) — but the same sorted-halves monotonicity still keeps
  that separate pass linear, preserving `O(n log n)` overall.
- This week's throughline: **two-pointer patterns need monotonic structure
  to work** (sorted arrays, or sorted halves mid-merge-sort) — recognizing
  *why* a pattern applies (not just pattern-matching to "this looks like a
  two-pointer problem") is what lets you adapt it correctly to variants
  like Reverse Pairs.

---

## Additional Topics — Filling Gaps in Day 14's Scope

Day 14's theme is "combinatorics on arrays" via clever counting (sum/XOR
identities, merge-sort-piggybacked inversion counting). One major companion
technique in this family was missing: finding the **Kth smallest/largest**
element without fully sorting.

### 4. Kth Smallest / Kth Largest Element (Quickselect)

**The problem:** given an unsorted array, find the `k`-th smallest (or
largest) element — **without** fully sorting the array.

**Why not just sort and index?** Sorting works and is simple
(`O(n log n)`), and is a perfectly reasonable answer under time pressure —
but there's an approach that does better **on average**: `O(n)` expected
time, using the same **partitioning** idea as Quick Sort (which you should
already be familiar with from Week 1), but only **recursing into the one
side that could contain the answer**, instead of both sides.

**Key insight — this is "half of Quick Sort":** Quick Sort partitions
around a pivot, then recursively sorts **both** halves. **Quickselect**
partitions around a pivot, checks whether the pivot's final sorted position
matches the target rank `k`, and if not, recurses into **only the one side**
that could contain the `k`-th element — discarding the other half entirely,
the same way Binary Search discards half the search space per step.

```python
import random

def quickselect_kth_smallest(arr, k):
    arr = arr[:]                              # avoid mutating the caller's array
    def partition(l, r, pivot_idx):
        pivot = arr[pivot_idx]
        arr[pivot_idx], arr[r] = arr[r], arr[pivot_idx]   # move pivot to the end
        store = l
        for i in range(l, r):
            if arr[i] < pivot:
                arr[store], arr[i] = arr[i], arr[store]
                store += 1
        arr[store], arr[r] = arr[r], arr[store]            # move pivot to its final position
        return store

    left, right = 0, len(arr) - 1
    target = k - 1                              # convert 1-indexed k to 0-indexed target position
    while True:
        if left == right:
            return arr[left]
        pivot_idx = random.randint(left, right)   # random pivot avoids worst-case O(n^2) on adversarial input
        pivot_idx = partition(left, right, pivot_idx)
        if pivot_idx == target:
            return arr[pivot_idx]
        elif pivot_idx < target:
            left = pivot_idx + 1                    # answer is in the right partition
        else:
            right = pivot_idx - 1                   # answer is in the left partition

print(quickselect_kth_smallest([3, 2, 1, 5, 6, 4], 2))   # 2 (2nd smallest)
```

**For Kth largest:** either reverse the comparison in `partition`, or —
more simply — reuse `quickselect_kth_smallest` with an adjusted target:
the `k`-th largest is the `(n - k + 1)`-th smallest.

```python
def quickselect_kth_largest(arr, k):
    n = len(arr)
    return quickselect_kth_smallest(arr, n - k + 1)

print(quickselect_kth_largest([3, 2, 6, 5, 1, 4], 2))   # 5 (2nd largest)
```

**Trace (conceptual) for `arr = [3, 2, 1, 5, 6, 4], k = 2`** (looking for
the element that would land at 0-indexed position `1` if sorted):
partitioning around a random pivot (say `4`, at index 5) rearranges the
array so everything `< 4` is on the left and everything `>= 4` is on the
right, with `4` landing at its correct sorted index (`3`, since 3 elements
`3,2,1` are smaller). Since `3 > target(1)`, recurse into the **left**
partition only (`[3,2,1]`, ignoring `[5,6,4]` entirely) — repeating this
process narrows down to the answer `2` without ever fully sorting the
right side, or fully sorting the left side beyond what's needed.

**Why does discarding one whole side at each step still work correctly?**
After partitioning, the pivot sits at its **true final sorted position** —
so if the target rank `k` is less than the pivot's position, the `k`-th
smallest element **must** be somewhere in the left partition (everything in
the right partition is provably larger than the pivot, hence larger than
the target); symmetrically for the right partition. This is exactly the
same "eliminate half (or some fraction) of the search space per
comparison" logic behind Binary Search and the converging two-pointer
template (Day 8) — just applied via **partitioning** instead of direct
index comparison.

**Complexity:** **O(n) expected time** (each partitioning pass processes a
shrinking portion of the array, geometrically decreasing on average, giving
a total expected cost of `O(n) + O(n/2) + O(n/4) + ... = O(n)`) — but
**O(n²) worst case** (e.g., if pivots are consistently chosen poorly,
similar to Quick Sort's worst case from Week 1) — the **random** pivot
choice used here makes the worst case astronomically unlikely in practice.
**O(1) extra space** (in-place partitioning, beyond the O(n) copy taken to
avoid mutating the input). A guaranteed-`O(n)`-worst-case version exists
(the "median of medians" pivot-selection strategy) but is rarely needed or
expected in a standard interview setting — knowing Quickselect with random
pivoting is the expected level of depth.

**Why is this the natural companion to Day 14's other problems?** Both
`count_inversions` (section 2) and Quickselect **reuse a sorting algorithm's
core mechanic** (Merge Sort's merge step; Quick Sort's partition step) for
a **different purpose** than sorting itself (counting cross-half pairs;
finding a single rank without full ordering) — reinforcing this week's
throughline that these classic O(n log n) algorithms are reusable building
blocks, not just standalone sorting routines.

## Additional Key Takeaways (Day 14 Supplement)

- **Quickselect** finds the Kth smallest/largest element in `O(n)`
  *expected* time by partitioning (like Quick Sort) but recursing into only
  the **one side** that can contain the target rank — the same "eliminate
  large chunks of the search space" logic as Binary Search, applied via
  partitioning instead of index comparison.
- **Random pivot selection** is what keeps Quickselect's expected
  performance close to `O(n)` in practice, since it makes the `O(n²)` worst
  case (adversarially bad pivots every time) statistically negligible,
  mirroring the same concern from Quick Sort in Week 1.
- Across Day 14 (inversions, reverse pairs, and now Quickselect): **reusing
  a classic sort's internal mechanic for a non-sorting purpose** — counting
  cross-half pairs during a merge, or finding one rank during a
  partition — is a recurring, transferable idea worth recognizing whenever
  a problem "smells like" sorting but doesn't actually need a fully sorted
  result.
