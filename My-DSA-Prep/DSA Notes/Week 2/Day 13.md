# Day 13 — Counting & Intervals

**Week 2: Arrays Part 1–2** | [Week overview](README.md)
*(Lighter day)*

**Language: Python**

---

## 1. Count Subarrays With Sum Equal to K

**The problem:** given an array (which may include negative numbers) and a
target `k`, count how many contiguous subarrays sum to exactly `k`.

**Why not two-pointer?** The converging two-pointer technique (Day 8)
relies on a monotonic relationship — as one pointer moves, the sum changes
predictably in one direction. **That breaks down with negative numbers**:
adding an element could increase *or* decrease the running sum, so you can't
safely decide which pointer to move. We need a different tool: **prefix
sums combined with hashing** — directly extending the Two Sum hashing
pattern from Day 8 to subarrays.

**The key identity:** define `prefix_sum[i]` as the sum of all elements from
the start of the array up to index `i`. Then the sum of the subarray from
index `i+1` to `j` is `prefix_sum[j] - prefix_sum[i]`. We want this to equal
`k`, i.e. `prefix_sum[j] - k = prefix_sum[i]` — so at each position `j`, we
just need to know: **how many earlier positions had a prefix sum equal to
`prefix_sum[j] - k`?**

```python
def count_subarrays_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    freq = {0: 1}          # empty prefix (sum 0) has occurred once, before any elements
    for x in arr:
        prefix_sum += x
        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count
```

**Trace for `arr = [1, 1, 1], k = 2`:**
| x | prefix_sum | prefix_sum - k | in freq? | count | freq after |
|---|---|---|---|---|---|
| 1 | 1 | -1 | no | 0 | {0:1, 1:1} |
| 1 | 2 | 0 | yes (freq[0]=1) | 1 | {0:1, 1:1, 2:1} |
| 1 | 3 | 1 | yes (freq[1]=1) | 2 | {0:1, 1:1, 2:1, 3:1} |

Result: `count = 2`. Verify by hand: subarrays of `[1,1,1]` summing to `2`
are `[1,1]` (indices 0-1) and `[1,1]` (indices 1-2) — exactly 2. Correct.

**Why does `freq = {0: 1}` need that initial entry?** It represents "the
empty prefix, before any elements, has sum 0" — this lets a subarray that
starts from **index 0** be counted correctly (e.g., if `prefix_sum` itself
ever equals `k` exactly, we need `prefix_sum - k = 0` to find a match, and
that match must come from this initial entry, since no real element has
been processed yet at that point).

**Complexity:** **O(n) time** (single pass, O(1) average hashmap
operations), **O(n) space** (the `freq` dictionary can grow to size `n`).
This is a direct generalization of Day 8's Two Sum pattern — "have I seen
the complementary value before" — applied to running sums instead of raw
values.

---

## 2. Count Subarrays With XOR Equal to K

**Same overall shape, different operation.** XOR has a property that makes
this trick work just as well as it did for sum: **XOR is its own inverse**
— `a ^ a = 0`, and `a ^ b ^ b = a`. So if `prefix_xor[j]` is the XOR of all
elements from the start up to index `j`, then the XOR of the subarray from
`i+1` to `j` is `prefix_xor[j] ^ prefix_xor[i]` (XOR "cancels out" the
shared prefix, the same way subtraction cancels out a shared prefix *sum*).

We want `prefix_xor[j] ^ prefix_xor[i] = k`. XOR-ing both sides by
`prefix_xor[j]` (using the self-inverse property) gives:
`prefix_xor[i] = prefix_xor[j] ^ k`. So at each position `j`, check: how many
earlier positions had prefix XOR equal to `prefix_xor[j] ^ k`?

```python
def count_subarrays_xor_k(arr, k):
    count = 0
    prefix_xor = 0
    freq = {0: 1}
    for x in arr:
        prefix_xor ^= x
        needed = prefix_xor ^ k
        if needed in freq:
            count += freq[needed]
        freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
    return count
```

**Trace for `arr = [4, 2, 2, 6, 4], k = 6`:**
| x | prefix_xor | needed = prefix_xor^k | in freq? | count | freq after |
|---|---|---|---|---|---|
| 4 | 4 | 4^6=2 | no | 0 | {0:1, 4:1} |
| 2 | 6 | 6^6=0 | yes (freq[0]=1) | 1 | {0:1, 4:1, 6:1} |
| 2 | 4 | 4^6=2 | no | 1 | {0:1, 4:2, 6:1} |
| 6 | 2 | 2^6=4 | yes (freq[4]=2) | 1+2=3 | {0:1, 4:2, 6:1, 2:1} |
| 4 | 6 | 6^6=0 | yes (freq[0]=1) | 3+1=4 | {0:1, 4:2, 6:2, 2:1} |

Result: `count = 4`. Verified independently: the subarrays with XOR exactly
`6` are `(indices 0-1)`, `(indices 0-4)`, `(indices 1-3)`, and `(index 3
alone)` — 4 total. Correct.

**Complexity:** **O(n) time**, **O(n) space** — structurally identical to
the sum version, just swapping `+`/`-` for `^` throughout, since XOR's
self-inverse property plays the same role that subtraction's inverse
relationship to addition plays for the sum version.

---

## 3. Merge Overlapping Intervals

**The problem:** given a collection of intervals (each `[start, end]`),
merge all overlapping intervals into their union, returning the minimal set
of non-overlapping intervals that covers the same ranges.

**Example:** `[[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]`
(`[1,3]` and `[2,6]` overlap since `2 <= 3`, so they merge into `[1,6]`).

**Idea:** first **sort the intervals by start value** — once sorted, any
interval that could possibly overlap with the "current" merged interval must
appear immediately next in the sorted order (since everything later starts
even further right). This turns an otherwise messy comparison problem into
a simple single left-to-right scan.

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda interval: interval[0])   # sort by start
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:                # overlaps (or touches) the last merged interval
            merged[-1] = [last_start, max(last_end, end)]
        else:
            merged.append([start, end])       # no overlap — starts a new interval
    return merged
```

**Trace for `intervals = [[1,3],[2,6],[8,10],[15,18]]`** (already sorted by
start):
| current | last merged | overlap? (`start <= last_end`) | action | merged after |
|---|---|---|---|---|
| [1,3] | — | — | initialize | [[1,3]] |
| [2,6] | [1,3] | 2 <= 3, yes | extend to [1, max(3,6)=6] | [[1,6]] |
| [8,10] | [1,6] | 8 <= 6? no | append new | [[1,6],[8,10]] |
| [15,18] | [8,10] | 15 <= 10? no | append new | [[1,6],[8,10],[15,18]] |

Result: `[[1,6],[8,10],[15,18]]`. Matches the expected output.

**Why `max(last_end, end)` instead of just `end` when merging?** Consider
`[[1,10],[2,3]]` — sorted, `[1,10]` comes first. The second interval `[2,3]`
is fully **contained inside** the first, so the merged end must stay `10`,
not shrink to `3`. `max(last_end, end)` correctly handles both "extends
past the current merge" and "fully contained within it."

**Complexity:** **O(n log n) time** — dominated by the initial sort; the
merge pass itself is a single O(n) scan. **O(n) space** for the output (or
O(log n) to O(n) additional space depending on the sort algorithm's
internals — not a concern to optimize further here).

---

## 4. Merge Two Sorted Arrays Without Extra Space

**The problem:** given two sorted arrays, merge them into sorted order — but
you must do it **in-place across both arrays**, without allocating a third
array. (Contrast with the `merge` helper from Day 6's Merge Sort, which
freely built a brand-new result list — that's exactly the O(n) space this
problem forbids.)

**Why is this hard?** A normal merge (two pointers, one per array, always
taking the smaller front element) needs somewhere to *put* the merged
result — normally a third array. Without one, whenever you'd want to
"insert" an element from the second array into its correct position in the
first, you'd need to shift a bunch of elements — which can cascade
expensively if done naively (repeatedly, per misplaced element, that's
`O(n*m)` in the worst case).

**The efficient trick — the "gap method" (inspired by Shell Sort):**
instead of comparing *adjacent* elements, compare elements that are a
certain **gap** distance apart (treating the two arrays as one continuous
virtual sequence), swapping them if out of order — then shrink the gap
(roughly halving it each round) and repeat, finishing when the gap reaches 0.
This is the exact same "compare-and-swap at shrinking distances" idea Shell
Sort uses to sort a single array efficiently, applied here across two
arrays treated as one.

```python
def merge_without_extra_space(arr1, arr2):
    n, m = len(arr1), len(arr2)

    def get(index):                     # read from the "virtual" combined array
        return arr1[index] if index < n else arr2[index - n]

    def set_value(index, value):        # write to the "virtual" combined array
        if index < n:
            arr1[index] = value
        else:
            arr2[index - n] = value

    def next_gap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)    # ceiling division by 2

    gap = next_gap(n + m)
    while gap > 0:
        i = 0
        j = gap
        while j < n + m:
            if get(i) > get(j):
                vi, vj = get(i), get(j)
                set_value(i, vj)
                set_value(j, vi)
            i += 1
            j += 1
        gap = next_gap(gap)
    return arr1, arr2
```

**Trace for `arr1 = [1, 4, 7, 8, 10], arr2 = [2, 3, 9]`** (`n=5, m=3`,
combined virtual length 8; indices 0-4 map to `arr1`, indices 5-7 map to
`arr2`):

**Round 1, `gap = next_gap(8) = 4`:**
- `(i=0,j=4)`: `get(0)=1` vs `get(4)=10` → no swap.
- `(i=1,j=5)`: `get(1)=4` vs `get(5)=2` (`arr2[0]`) → `4>2`, swap →
  `arr1=[1,2,7,8,10]`, `arr2=[4,3,9]`.
- `(i=2,j=6)`: `get(2)=7` vs `get(6)=3` (`arr2[1]`) → `7>3`, swap →
  `arr1=[1,2,3,8,10]`, `arr2=[4,7,9]`.
- `(i=3,j=7)`: `get(3)=8` vs `get(7)=9` (`arr2[2]`) → no swap.

State: `arr1=[1,2,3,8,10]`, `arr2=[4,7,9]`.

**Round 2, `gap = next_gap(4) = 2`:**
- `(i=0,j=2)`: `1` vs `3` → no swap.
- `(i=1,j=3)`: `2` vs `8` → no swap.
- `(i=2,j=4)`: `3` vs `10` → no swap.
- `(i=3,j=5)`: `get(3)=8` vs `get(5)=4` (`arr2[0]`) → `8>4`, swap →
  `arr1=[1,2,3,4,10]`, `arr2=[8,7,9]`.
- `(i=4,j=6)`: `get(4)=10` vs `get(6)=7` (`arr2[1]`) → `10>7`, swap →
  `arr1=[1,2,3,4,7]`, `arr2=[8,10,9]`.

State: `arr1=[1,2,3,4,7]`, `arr2=[8,10,9]`.

**Round 3, `gap = next_gap(2) = 1`:**
- `(i=0,j=1)` through `(i=5,j=6)` all check out in order **except**:
  `(i=6,j=7)`: `get(6)=10` (`arr2[1]`) vs `get(7)=9` (`arr2[2]`) → `10>9`,
  swap → `arr2=[8,9,10]`.

State: `arr1=[1,2,3,4,7]`, `arr2=[8,9,10]`. `gap = next_gap(1) = 0`, loop
ends.

**Final result:** `arr1=[1,2,3,4,7]`, `arr2=[8,9,10]` — fully merged and
sorted across both arrays (reading `arr1` then `arr2` gives
`1,2,3,4,7,8,9,10`, correctly sorted).

**Complexity:** **O((n+m) log(n+m)) time** (the gap shrinks by roughly half
each round, giving `O(log(n+m))` rounds, each doing `O(n+m)` comparisons) —
worse than a normal O(n+m) merge with extra space, but this is the
fundamental trade-off for achieving **O(1) extra space** (beyond the two
input arrays themselves, no third array or hashmap is ever allocated).

---

## Worked Examples — Trace These Yourself First

**Example A:** Why does the subarray-sum-K counting trick (section 1) break
down if you tried to adapt the **converging two-pointer** approach instead,
for an array that includes negative numbers?
<details><summary>Answer</summary>
The converging two-pointer approach (Day 8) relies on knowing which
direction to move a pointer based on whether the current combined value is
too small or too large — which only works if moving a pointer changes the
value in a *predictable, monotonic* direction. With negative numbers in the
array, extending a subarray by one more element could *decrease* the sum
just as easily as increase it, so there's no reliable rule for "move this
pointer to increase, move that one to decrease" — the monotonic structure
two-pointer depends on simply isn't there.
</details>

**Example B:** In `count_subarrays_xor_k`, why is `needed = prefix_xor ^ k`
(not `prefix_xor - k`, and not `k ^ prefix_xor` reversed some other way)
the correct value to look up?
<details><summary>Answer</summary>
We derived `prefix_xor[i] = prefix_xor[j] ^ k` algebraically from
`prefix_xor[j] ^ prefix_xor[i] = k`, using the fact that XOR-ing both sides
by `prefix_xor[j]` cancels it out on the left (`prefix_xor[j] ^ prefix_xor[j]
= 0`), isolating `prefix_xor[i]`. (Note XOR is commutative, so
`prefix_xor ^ k` and `k ^ prefix_xor` are actually the same value — the
"direction" doesn't matter here, unlike subtraction, which is one of the
conceptual differences between the sum and XOR versions worth noticing.)
</details>

**Example C:** In the gap-method merge, why must `next_gap` use **ceiling**
division (`(gap // 2) + (gap % 2)`) rather than plain floor division
(`gap // 2`)?
<details><summary>Answer</summary>
If the gap sequence used floor division, a gap of `1` would produce a next
gap of `0` directly — but a gap of, say, `3` would floor to `1`, which is
fine; the real risk is with certain sequences never actually reaching every
necessary comparison distance before hitting 0 prematurely, similarly to
how Shell Sort's gap sequence must eventually include `1` to guarantee full
correctness (a final pass with gap=1 is equivalent to one full adjacent-pair
bubble-style pass, which is what finally guarantees complete correctness).
Ceiling division guarantees the gap sequence always eventually passes
through exactly `1` before reaching `0`, ensuring that crucial final
adjacent-comparison pass isn't skipped.
</details>

---

## Practice Questions

### Question 1 — Count Subarrays With Sum Equal to K
**Question:** Given an array (possibly with negative numbers) and a target
`k`, count how many contiguous subarrays sum to exactly `k`.
**Input:** `arr = [1, 1, 1], k = 2`
**Output:** `2`
**Solution:**
```python
def count_subarrays_sum_k(arr, k):
    count = 0
    prefix_sum = 0
    freq = {0: 1}
    for x in arr:
        prefix_sum += x
        if prefix_sum - k in freq:
            count += freq[prefix_sum - k]
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
    return count

print(count_subarrays_sum_k([1, 1, 1], 2))   # 2
```
Track running prefix sums in a hashmap; at each step, check how many earlier
prefixes are exactly `k` less than the current one. Complexity: `O(n)` time,
`O(n)` space (section 1).

### Question 2 — Count Subarrays With XOR Equal to K
**Question:** Given an array and a target `k`, count how many contiguous
subarrays have XOR exactly `k`.
**Input:** `arr = [4, 2, 2, 6, 4], k = 6`
**Output:** `4`
**Solution:**
```python
def count_subarrays_xor_k(arr, k):
    count = 0
    prefix_xor = 0
    freq = {0: 1}
    for x in arr:
        prefix_xor ^= x
        needed = prefix_xor ^ k
        if needed in freq:
            count += freq[needed]
        freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
    return count

print(count_subarrays_xor_k([4, 2, 2, 6, 4], 6))   # 4
```
Same hashmap-of-prefixes pattern as Question 1, using XOR's self-inverse
property (`a^a=0`) instead of subtraction. Complexity: `O(n)` time, `O(n)`
space (section 2).

### Question 3 — Merge Overlapping Intervals
**Question:** Given a list of intervals, merge all overlapping ones.
**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`
**Solution:**
```python
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = [last_start, max(last_end, end)]
        else:
            merged.append([start, end])
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
# [[1, 6], [8, 10], [15, 18]]
```
Sort by start value, then scan once, extending the last merged interval
whenever the next one overlaps it. Complexity: `O(n log n)` time (sort
dominates), `O(n)` output space (section 3).

### Question 4 — Merge Two Sorted Arrays Without Extra Space
**Question:** Given two sorted arrays, merge them into sorted order across
both arrays, without allocating a third array.
**Input:** `arr1 = [1, 4, 7, 8, 10], arr2 = [2, 3, 9]`
**Output:** `arr1 = [1, 2, 3, 4, 7], arr2 = [8, 9, 10]`
**Solution:**
```python
def merge_without_extra_space(arr1, arr2):
    n, m = len(arr1), len(arr2)

    def get(index):
        return arr1[index] if index < n else arr2[index - n]

    def set_value(index, value):
        if index < n:
            arr1[index] = value
        else:
            arr2[index - n] = value

    def next_gap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    gap = next_gap(n + m)
    while gap > 0:
        i, j = 0, gap
        while j < n + m:
            if get(i) > get(j):
                vi, vj = get(i), get(j)
                set_value(i, vj)
                set_value(j, vi)
            i += 1
            j += 1
        gap = next_gap(gap)
    return arr1, arr2

arr1, arr2 = [1, 4, 7, 8, 10], [2, 3, 9]
print(merge_without_extra_space(arr1, arr2))
# ([1, 2, 3, 4, 7], [8, 9, 10])
```
The "gap method" (Shell-Sort-inspired): compare and swap elements a shrinking
`gap` distance apart across the two arrays treated as one virtual sequence,
until `gap` reaches 0. Complexity: `O((n+m) log(n+m))` time, `O(1)` extra
space (section 4).

## Revision (of Week 1)

- Re-implement binary search from memory (no bugs).
- Re-derive time complexity of merge sort's merge step.
- Solve 2 recursion problems from Week 1's list cold (e.g., sum of digits,
  Fibonacci).

## Key Takeaways

- **Prefix sum/XOR + hashmap** extends the "have I seen the complement
  before" pattern (Day 8's Two Sum) from pairs to **subarrays**, solving
  count-subarrays-with-target-sum/XOR in `O(n)` time even with negative
  numbers, where two-pointer approaches break down due to lost monotonicity.
- **Merging overlapping intervals** becomes a simple linear scan once you
  **sort by start value** first — sorting is what guarantees any possible
  overlap partner appears immediately next in the scan order.
- The **gap method** merges two sorted arrays in-place, without a third
  array, by comparing elements at a shrinking distance apart — trading
  `O(n+m)` time (achievable with extra space) for `O((n+m) log(n+m))` time
  in exchange for `O(1)` extra space.
- Recognizing when a problem's structure (negative numbers breaking
  monotonicity, a hard space constraint) rules out your first-instinct
  approach — and knowing the next-best pattern to reach for — is the real
  skill being built this week, more than memorizing any single algorithm.

---

## Additional Topics — Filling Gaps in Day 13's Scope

Day 13 covered merging **overlapping** intervals from scratch. Two related
interval problems are commonly asked alongside it: inserting a **new**
interval into an already-merged list, and finding the **minimum number of
removals** needed to eliminate all overlaps.

### 5. Insert Interval

**The problem:** given a list of **already non-overlapping, sorted**
intervals, and a new interval to insert, insert it and merge as necessary
so the result stays non-overlapping and sorted.

**Example:** `intervals = [[1,3],[6,9]], new_interval = [2,5]` →
`[[1,5],[6,9]]` (the new interval `[2,5]` overlaps `[1,3]`, merging into
`[1,5]`, but doesn't reach `[6,9]`).

**Idea — three phases in one linear scan**, exploiting the fact that the
input is already sorted (no need to re-sort, unlike Day 13's general
`merge_intervals`, section 3):
1. Append every interval that ends **before** the new interval starts (no
   overlap possible — entirely to the left).
2. **Merge** every interval that overlaps the new interval into it
   (expanding the new interval's bounds as needed), stopping once an
   interval starts *after* the (possibly-expanded) new interval ends.
3. Append the new interval, then append everything remaining (all entirely
   to the right).

```python
def insert_interval(intervals, new_interval):
    result = []
    i, n = 0, len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval = [min(new_interval[0], intervals[i][0]),
                         max(new_interval[1], intervals[i][1])]
        i += 1

    result.append(new_interval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result

print(insert_interval([[1,3],[6,9]], [2,5]))   # [[1, 5], [6, 9]]
```

**Trace for `intervals = [[1,3],[6,9]], new_interval = [2,5]`:**
- Phase 1: `intervals[0]=[1,3]`, is `3 < 2`? No → phase 1 loop doesn't
  execute at all (nothing entirely to the left).
- Phase 2: `intervals[0]=[1,3]`, is `1 <= 5`? Yes → merge:
  `new_interval = [min(2,1), max(5,3)] = [1,5]`. `i→1`.
  `intervals[1]=[6,9]`, is `6 <= 5`? No → stop phase 2.
- Append `new_interval = [1,5]` → `result = [[1,5]]`.
- Phase 3: append remaining `intervals[1]=[6,9]` → `result = [[1,5],[6,9]]`.

Result: `[[1, 5], [6, 9]]`. Matches.

**Complexity:** **O(n) time** — a single pass through the input (no sort
needed, since it's already sorted, unlike Day 13's general
`merge_intervals`), **O(n) output space**.

### 6. Non-overlapping Intervals (Minimum Removals to Eliminate Overlaps)

**The problem:** given a list of intervals (possibly overlapping, in **any**
order), find the **minimum number of intervals to remove** so that none of
the remaining intervals overlap.

**Example:** `[[1,2],[2,3],[3,4],[1,3]]` → remove `[1,3]` (it overlaps both
`[1,2]` and `[2,3]`) → `1` removal needed.

**Why this is a greedy "activity selection" problem, not a merge problem:**
unlike Day 13's `merge_intervals` (which *combines* overlapping intervals),
here we must *keep as many intervals as possible while removing the rest*
— this is the classic **interval scheduling** greedy problem: **sort by
end time**, and greedily keep an interval whenever it starts at or after
the previously **kept** interval's end.

**Why sort by end time (not start time, unlike section 3's merge
problem)?** Keeping the interval that **ends earliest** among any group of
overlapping intervals leaves the **most room** for future intervals to
also be kept without conflict — this is the standard greedy-choice
argument behind activity-selection-style problems.

```python
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])       # sort by END time, not start
    count = 0                                  # number of intervals removed
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start < prev_end:                    # overlaps the last KEPT interval
            count += 1                           # must remove this one
        else:
            prev_end = end                       # no overlap — keep it, update the "last kept end"
    return count

print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))   # 1
```

**Trace for `intervals = [[1,2],[2,3],[3,4],[1,3]]`, sorted by end time →
`[[1,2],[2,3],[1,3],[3,4]]`:**
| current | prev_end | start < prev_end? | action | count | prev_end after |
|---|---|---|---|---|---|
| [1,2] | — | — | initialize | 0 | 2 |
| [2,3] | 2 | 2<2? no | keep | 0 | 3 |
| [1,3] | 3 | 1<3? **yes** | remove | 1 | 3 (unchanged) |
| [3,4] | 3 | 3<3? no | keep | 1 | 4 |

Result: `count = 1`. Matches — removing `[1,3]` leaves `[1,2],[2,3],[3,4]`,
which are non-overlapping.

**Complexity:** **O(n log n) time** (sort dominates), **O(1) extra space**
(beyond sort internals) — a genuinely different algorithmic shape from
`merge_intervals` (section 3) despite superficially similar input, because
the *goal* differs (combine everything vs. keep the maximum non-conflicting
subset).

## Additional Key Takeaways (Day 13 Supplement)

- **Insert Interval** is a specialized, faster variant of general interval
  merging — because the input is already sorted and non-overlapping, a
  single three-phase linear scan suffices, with no sort needed.
- **Non-overlapping Intervals** is a **greedy activity-selection** problem,
  not a merge problem — sorting by **end time** (not start time) and
  greedily keeping the earliest-ending non-conflicting interval at each
  step maximizes how many intervals can be kept, directly minimizing
  removals.
- The three interval problems this week (merge, insert, and minimum
  removal) look similar on the surface but solve **different goals**
  (combine everything / insert into a sorted list / keep a maximum
  compatible subset) — matching the goal to the right sort key (start time
  vs. end time) and the right scan strategy is the actual skill being
  tested, not "intervals" as a single monolithic pattern.
