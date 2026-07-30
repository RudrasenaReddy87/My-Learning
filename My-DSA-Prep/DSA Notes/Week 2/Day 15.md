# Day 15 (Supplement) — Missing Array Patterns from Week 2

**Week 2: Arrays Part 1–2** | Fills gaps left by Days 8–14

**Language: Python**

---

## Why this supplement exists

Days 8–14 cover two-pointer/hashing fundamentals, Kadane's family, next
permutation, matrix manipulation, and prefix-sum/merge-sort-piggybacked
counting extremely well. But a few classic array patterns that normally sit
alongside these in any standard DSA sequence were never covered — some of
them are direct extensions of things you already learned (e.g. Majority
Element **II** extends Day 8/9's Moore's Voting; Two Sum **II** extends Day
8's Two Sum). This supplement fills those specific gaps, in the same style
as the rest of the week, so nothing is left as a blind spot going into
Week 3.

**Topics covered today:**
1. Two Sum II — sorted-array two-pointer variant
2. Trapping Rain Water
3. 3Sum
4. 4Sum
5. Product of Array Except Self
6. Longest Consecutive Sequence
7. Majority Element II (`> n/3` times)
8. Pascal's Triangle
9. Maximum Consecutive Ones
10. Union and Intersection of Two Sorted Arrays

---

## 1. Two Sum II — Sorted Array, Two-Pointer

**The problem:** same goal as Day 8's Two Sum (find two elements summing to
a target), but here the array is **already sorted**, and you don't need the
*original* unsorted indices — just the values (or 1-indexed positions in
the sorted array). This is exactly the case Day 8 said two-pointer *couldn't*
handle (needing original indices) — when that constraint is lifted, two-
pointer becomes the better tool: **O(1) space** instead of hashing's O(n).

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1      # sum too small — grow it by moving left pointer up
        else:
            right -= 1     # sum too large — shrink it by moving right pointer down
    return []
```

**Trace for `arr = [2, 7, 11, 15], target = 9`:**
| left | right | arr[left]+arr[right] | comparison | action |
|---|---|---|---|---|
| 0 | 3 | 2+15=17 | 17>9 | right→2 |
| 0 | 2 | 2+11=13 | 13>9 | right→1 |
| 0 | 1 | 2+7=9 | equal | return [0,1] |

Result: `[0, 1]` — same answer as Day 8's hashing version, but reached with
**O(1) extra space** instead of O(n), because sortedness gives us the
monotonic structure the converging two-pointer template (Day 8, section 1)
needs.

**Complexity:** **O(n) time**, **O(1) space** — strictly better space than
Day 8's hashing Two Sum, but *only* usable because the array is sorted and
original unsorted indices aren't required. This is the direct trade-off Day
8 flagged but didn't fully demonstrate: sorted + no-index-needed → two-
pointer wins; unsorted + index-needed → hashing wins.

---

## 2. Trapping Rain Water

**The problem:** given an array where each element represents a bar's
height (a bar chart / elevation map), compute how much water it can trap
after rain, assuming water is held between bars.

**Example:** `height = [0,1,0,2,1,0,1,3,2,1,2,1]` → total trapped water = `6`.

**Key insight:** the amount of water trapped **above any single position
`i`** is determined entirely by `min(max height to its left, max height to
its right) - height[i]` (and never negative — a position can't trap water
if there's no taller wall on both sides). Water above position `i` is
bounded by whichever *side* is shorter, since water would simply spill over
the shorter side.

### Brute force: for each position, scan both directions for the max — O(n²)

```python
def trap_brute(height):
    n = len(height)
    total = 0
    for i in range(n):
        left_max = max(height[:i+1])
        right_max = max(height[i:])
        total += min(left_max, right_max) - height[i]
    return total
```

### Better: precompute left-max and right-max arrays — O(n) time, O(n) space

```python
def trap_precompute(height):
    n = len(height)
    if n == 0:
        return 0
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    return sum(min(left_max[i], right_max[i]) - height[i] for i in range(n))
```

### Optimal: two pointers, O(n) time, O(1) space

**Idea:** maintain `left`/`right` pointers and `left_max`/`right_max`
running maxima. At each step, move whichever pointer is on the side with
the **smaller** running max — because that side's water level is *already
known* to be capped by its own running max (the other side's max is
guaranteed to be at least as large, whether or not we've fully computed
it yet, since we're always advancing the smaller-max side).

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            total += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            total += right_max - height[right]
            right -= 1
    return total

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
```

**Why is it safe to trust `left_max` alone when `height[left] < height[right]`?**
We know `right_max >= height[right] > height[left]`. Since `right_max` is
already at least as large as `height[left]`, the true water cap at
`left` is `min(left_max, right_max)`, and because `right_max > height[left]`
is guaranteed while `left_max` might still be `< height[left]` or not — the
binding constraint is always `left_max` in this branch, so we don't need
`right_max`'s exact value to compute water at `left` correctly.

**Trace for `height = [0,1,0,2,1,0,1,3,2,1,2,1]`** (abbreviated — first few
steps): `left=0,right=11`: `height[0]=0 < height[11]=1` → update
`left_max=max(0,0)=0`, water at 0 = `0-0=0`, `left→1`. `left=1,right=11`:
`height[1]=1 < height[11]=1`? No (equal, goes to else branch) →
`right_max=max(0,1)=1`, water at 11 = `1-1=0`, `right→10`. ... (continuing
this process across all 12 positions accumulates to a total of `6`,
matching the brute-force/precompute versions).

**Complexity:** **O(n) time, O(1) space** — the two-pointer version is
strictly better than the precompute version's O(n) space, using the same
"which side is the binding constraint" insight in place of storing full
left/right-max arrays.

---

## 3. 3Sum

**The problem:** given an array, find all **unique triplets**
`[a, b, c]` such that `a + b + c == 0` (or a general target). No duplicate
triplets in the output.

**Why not extend Two Sum's hashing directly?** You could (fix one element,
then run Two Sum-hashing on the rest for each fixed element — O(n²) time,
O(n) space) — but the far more common and cleaner approach reuses **Day 8's
two-pointer template directly**, once the array is sorted, giving O(n²)
time with O(1) extra space (beyond sort and output).

**Idea:** sort the array. Fix one element `arr[i]` (the smallest of the
triplet, scanned left to right). For the remaining subarray `arr[i+1:]`,
run the **converging two-pointer Two Sum** (section 1 above / Day 8) looking
for a pair summing to `-arr[i]`. Skip duplicate values at every level to
avoid duplicate triplets in the output.

```python
def three_sum(arr):
    arr.sort()
    n = len(arr)
    result = []
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue                          # skip duplicate "first" elements
        left, right = i + 1, n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1                  # skip duplicate second elements
                while left < right and arr[right] == arr[right+1]:
                    right -= 1                 # skip duplicate third elements
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))
# [[-1, -1, 2], [-1, 0, 1]]
```

**Trace (partial) for `arr = [-4,-1,-1,0,1,2]` (sorted):** `i=0 (-4)`:
`left=1,right=5`: `-4-1+2=-3<0`→left+1; `-4-1+2` (left=2)... eventually no
triplet found with `-4` as the smallest, since nothing sums to 0 with it.
`i=1 (-1)`: `left=2,right=5`: `-1-1+2=0` → found `[-1,-1,2]`, advance both,
skip duplicates. `left=3,right=4`: `-1+0+1=0` → found `[-1,0,1]`. Continue
similarly for `i=2` (duplicate `-1`, skipped by the `i>0 and arr[i]==arr[i-1]`
guard).

**Complexity:** **O(n log n)** for the sort, plus **O(n²)** for the
outer-loop-times-two-pointer scan (the two-pointer scan is O(n) for each of
the `n` fixed elements) → **O(n²) time overall**, **O(1) extra space**
(beyond sort internals and the output list) — a large improvement over the
naive **O(n³)** brute force of checking every triplet directly.

---

## 4. 4Sum

**The problem:** same idea as 3Sum, but find all unique **quadruplets**
`[a, b, c, d]` summing to a target.

**Idea:** identical pattern, one level deeper — fix **two** elements with
nested loops, then run the converging two-pointer scan on the remaining two
positions. Duplicate-skipping is needed at every fixed level.

```python
def four_sum(arr, target):
    arr.sort()
    n = len(arr)
    result = []
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j] == arr[j-1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = arr[i] + arr[j] + arr[left] + arr[right]
                if total == target:
                    result.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result

print(four_sum([1, 0, -1, 0, -2, 2], 0))
# [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
```

**Complexity:** **O(n log n)** sort, then **O(n³)** for two nested fixed
loops times an O(n) two-pointer scan → **O(n³) time**, **O(1) extra
space**. This generalizes cleanly: **k-Sum** follows the same recursive
"fix one element, recurse on (k-1)-Sum" idea, bottoming out at two-pointer
Two Sum once only 2 elements remain — worth noticing as a pattern rather
than memorizing 3Sum and 4Sum as unrelated problems.

---

## 5. Product of Array Except Self

**The problem:** given an array, return an array `output` where
`output[i]` equals the product of **all** elements except `arr[i]` —
**without using division**, and ideally in `O(1)` extra space (excluding
the output array).

**Example:** `[1, 2, 3, 4]` → `[24, 12, 8, 6]` (e.g. `output[0] = 2*3*4=24`).

**Why not just divide by `arr[i]` from the total product?** Division fails
if any element is `0` (and the problem typically forbids division anyway,
as a constraint to force a cleaner O(n)-without-division solution).

**Idea:** `output[i]` is the product of everything to i's **left**, times
everything to its **right**. Compute these as two passes: a left-to-right
pass filling `output[i]` with the running product of everything *before*
`i`, then a right-to-left pass multiplying in the running product of
everything *after* `i`.

```python
def product_except_self(arr):
    n = len(arr)
    output = [1] * n

    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= arr[i]

    return output

print(product_except_self([1, 2, 3, 4]))   # [24, 12, 8, 6]
```

**Trace for `arr = [1, 2, 3, 4]`:**
- Left pass: `output = [1, 1, 2, 6]` (each `output[i]` = product of
  everything strictly before `i`; `prefix` ends at `24` but isn't stored).
- Right pass (`suffix` starts at `1`, multiplies in from the right):
  `i=3`: `output[3] = 6*1=6`, `suffix=4`. `i=2`: `output[2]=2*4=8`,
  `suffix=12`. `i=1`: `output[1]=1*12=12`, `suffix=24`. `i=0`:
  `output[0]=1*24=24`, `suffix=24`.

Result: `[24, 12, 8, 6]`. Matches.

**Complexity:** **O(n) time** (two linear passes), **O(1) extra space**
(the `output` array itself is required output, not extra — only `prefix`
and `suffix` are auxiliary scalars). This is the same "running value from
one direction, then the other" idea as Day 11's Leaders-in-an-Array
(running max from the right) and Day 10's Buy/Sell Stock (running min from
the left) — here applied twice, once per direction, and combined
multiplicatively instead of via a single comparison.

---

## 6. Longest Consecutive Sequence

**The problem:** given an unsorted array of integers, find the length of
the longest run of **consecutive** integers (not necessarily contiguous in
the array itself — e.g. `[100, 4, 200, 1, 3, 2]` contains the consecutive
run `1, 2, 3, 4`, length `4`).

**Why not just sort first?** Sorting works (`O(n log n)`) but there's an
`O(n)` approach using a hash **set** — worth knowing since it beats sorting
asymptotically and reuses the "have I seen X" pattern from Two Sum (Day 8).

**Idea:** put every element into a set for O(1) lookups. For each element
`x`, only treat it as the **start** of a potential sequence if `x - 1` is
**not** in the set (this guarantees we only ever start counting from the
true beginning of each run, so every run gets counted exactly once, not
once per element within it). From a valid start, count forward
(`x+1, x+2, ...`) while each next value is present.

```python
def longest_consecutive(arr):
    num_set = set(arr)
    longest = 0
    for x in num_set:
        if x - 1 not in num_set:              # only start counting from a true sequence start
            length = 1
            current = x
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest

print(longest_consecutive([100, 4, 200, 1, 3, 2]))   # 4
```

**Trace for `arr = [100, 4, 200, 1, 3, 2]`** (`num_set = {100,4,200,1,3,2}`):
- `x=100`: `99 not in set` → start counting. `101 in set`? No. `length=1`.
- `x=4`: `3 in set` → **not** a start, skip.
- `x=200`: `199 not in set` → start. `201 in set`? No. `length=1`.
- `x=1`: `0 not in set` → start. `2 in set`? Yes → `current=2,length=2`.
  `3 in set`? Yes → `current=3,length=3`. `4 in set`? Yes →
  `current=4,length=4`. `5 in set`? No → stop. `longest=4`.
- `x=3`: `2 in set` → not a start, skip.
- `x=2`: `1 in set` → not a start, skip.

Result: `longest = 4` (the run `1,2,3,4`). Matches.

**Why is this still O(n) overall, even with the inner `while` loop?** Every
element is visited by the inner `while` loop **at most once in total**
across the *entire* function's execution — because the inner loop only ever
runs starting from a true sequence start, and it consumes each subsequent
element of that run exactly once, never revisiting it from a different
starting point (since non-start elements are skipped by the outer `if`
check). This "looks like nested loops but is actually O(n) because the
inner loop's total work across all outer iterations is bounded" reasoning
is a useful pattern to recognize — it also appears in some graph traversal
analyses.

**Complexity:** **O(n) time** (amortized, as argued above — building the
set is O(n), and the total work across all `while` loop iterations is O(n)),
**O(n) space** for the set. Compare to the simpler **O(n log n) sort-based
approach** (sort, then scan once counting consecutive runs) if you'd rather
trade a bit of time for simpler-to-reason-about code.

---

## 7. Majority Element II (Elements Appearing More Than n/3 Times)

**The problem:** an extension of Day 8/9's Moore's Voting — find **all**
elements that appear **more than `n/3`** times in the array. Note: there
can be **at most 2** such elements (a simple counting argument: if 3+
elements each appeared more than `n/3` times, their combined count would
exceed `n`, which is impossible).

**Idea — Extended Boyer-Moore Voting:** since at most 2 elements can
qualify, track **two** candidates and two counters simultaneously, using
the same cancellation logic as the original algorithm, generalized to two
"slots" instead of one.

```python
def majority_element_ii(arr):
    candidate1 = candidate2 = None
    count1 = count2 = 0

    for x in arr:
        if candidate1 == x:
            count1 += 1
        elif candidate2 == x:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = x, 1
        elif count2 == 0:
            candidate2, count2 = x, 1
        else:
            count1 -= 1
            count2 -= 1

    # Verification pass: confirm each candidate actually exceeds n/3.
    result = []
    for candidate in (candidate1, candidate2):
        if candidate is not None and arr.count(candidate) > len(arr) // 3:
            result.append(candidate)
    return result

print(majority_element_ii([1, 1, 1, 3, 3, 2, 2, 2]))   # [1, 2]
```

**Trace for `arr = [1, 1, 1, 3, 3, 2, 2, 2]`** (`n=8`, `n/3` threshold `> 2`,
so we need `>= 3` occurrences):
| x | matches c1? | matches c2? | c1==0? | c2==0? | action | (c1,count1,c2,count2) |
|---|---|---|---|---|---|---|
| 1 | — | — | yes | — | c1=1,count1=1 | (1,1,None,0) |
| 1 | yes | — | — | — | count1=2 | (1,2,None,0) |
| 1 | yes | — | — | — | count1=3 | (1,3,None,0) |
| 3 | no | no | no | yes | c2=3,count2=1 | (1,3,3,1) |
| 3 | no | yes | — | — | count2=2 | (1,3,3,2) |
| 2 | no | no | no | no | count1=2,count2=1 | (1,2,3,1) |
| 2 | no | no | no | no | count1=1,count2=0 | (1,1,3,0) |
| 2 | no | no | no | yes | c2=2,count2=1 | (1,1,2,1) |

Candidates after voting: `1` and `2`. Verification: `arr.count(1)=3 > 2`,
`arr.count(2)=3 > 2` — both confirmed. Result: `[1, 2]`. Matches (`3`
appeared only twice, which is `not > 2`, correctly excluded even though it
was a candidate mid-scan).

**Complexity:** **O(n) time** (voting pass + verification pass, both
linear), **O(1) space** — same complexity class as the original Moore's
Voting (Day 8/9), just tracking twice the state. The verification pass is
**not optional** here either, for the same reason as the original: the
voting phase can produce spurious candidates when no qualifying majority
actually exists.

---

## 8. Pascal's Triangle

**The problem:** generate the first `n` rows of Pascal's Triangle, where
each entry is the sum of the two entries above it (with edges always `1`).

**Example (n=5):**
```
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
```

**Idea:** build row by row. Each new row starts and ends with `1`; every
interior entry is the sum of the two entries directly above it in the
previous row.

```python
def pascals_triangle(n):
    triangle = []
    for row_num in range(n):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
    return triangle

for row in pascals_triangle(5):
    print(row)
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
```

**Bonus — direct formula for a single entry, without building the whole
triangle:** entry at `(row, col)` (0-indexed) equals the binomial
coefficient `C(row, col) = row! / (col! * (row-col)!)`. Useful when you only
need one specific entry rather than the full triangle:

```python
from math import comb
def pascal_entry(row, col):
    return comb(row, col)

print(pascal_entry(4, 2))   # 6 — matches row 4, index 2 above
```

**Complexity (full triangle):** **O(n²) time** (total entries across `n`
rows is `1+2+...+n = O(n²)`), **O(n²) space** for the output. **Single
entry via `comb`:** **O(min(col, row-col)) time** (the underlying
computation), **O(1) space** — much cheaper than building the whole
triangle if you only need one value.

---

## 9. Maximum Consecutive Ones

**The problem:** given a binary array (`0`s and `1`s), find the length of
the longest run of consecutive `1`s.

**Example:** `[1, 1, 0, 1, 1, 1]` → `3` (the run `1,1,1` near the end).

**Idea:** a single pass with a running counter — increment on `1`, reset to
`0` on `0`, tracking the best seen. This is the simplest possible instance
of the "running best" family you've now seen many variants of this week
(Kadane's running sum, Buy/Sell Stock's running min, Leaders' running max).

```python
def max_consecutive_ones(arr):
    best = 0
    current = 0
    for x in arr:
        if x == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best

print(max_consecutive_ones([1, 1, 0, 1, 1, 1]))   # 3
```

**Complexity:** **O(n) time**, **O(1) space** — about as simple as this
week's patterns get, useful as a sanity-check baseline against the more
elaborate running-best problems (Kadane's, Buy/Sell Stock) if any of those
still feel complicated: strip away the "extend vs. restart" decision-making
and this is what's left at the core.

---

## 10. Union and Intersection of Two Sorted Arrays

**The problem:** given two **sorted** arrays (possibly with duplicates
within each), compute their **union** (all distinct elements present in
either) and **intersection** (elements present in both, respecting
duplicate counts appropriately for a "sorted merge" style answer).

**Idea — merge-style two-pointer walk (no hashing needed, since both
inputs are already sorted):** walk both arrays simultaneously with one
pointer each, always advancing whichever pointer points at the smaller
value (same core mechanic as Day 6's Merge Sort `merge` step and Day 13's
gap-method merge).

```python
def union_sorted(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:                                   # equal — take one copy, advance both
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    while i < len(arr1):                          # drain any remainder
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1
    return result


def intersection_sorted(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:                                   # match found
            result.append(arr1[i])
            i += 1
            j += 1
    return result

print(union_sorted([1, 2, 2, 3, 4], [2, 3, 5]))         # [1, 2, 3, 4, 5]
print(intersection_sorted([1, 2, 2, 3, 4], [2, 3, 5]))   # [2, 3]
```

**Trace (intersection) for `arr1=[1,2,2,3,4], arr2=[2,3,5]`:**
| i | j | arr1[i] | arr2[j] | comparison | action |
|---|---|---|---|---|---|
| 0 | 0 | 1 | 2 | 1<2 | i→1 |
| 1 | 0 | 2 | 2 | equal | append 2, i→2,j→1 |
| 2 | 1 | 2 | 3 | 2<3 | i→3 |
| 3 | 1 | 3 | 3 | equal | append 3, i→4,j→2 |
| 4 | 2 | 4 | 5 | 4<5 | i→5, loop ends (i out of bounds) |

Result: `[2, 3]`. Matches.

**Why does this need duplicate-skip guards (`if not result or result[-1] !=
...`) in `union_sorted` but not in `intersection_sorted`?** Union must
produce **distinct** elements even if an input array has internal
duplicates (e.g. `arr1` has two `2`s) — the guard prevents re-appending a
value already at the end of `result`. Intersection here appends one match
per aligned pair of equal elements naturally as pointers advance together,
which (for this simplified version) doesn't need the same guard, though a
stricter "intersection with duplicate multiplicity" variant would need
additional handling — worth being explicit that this version returns
**distinct** intersecting values, matching most standard problem framings.

**Complexity:** both are **O(n + m) time** (single simultaneous pass over
both arrays — same merge-walk shape as Merge Sort's `merge` step, Day 6),
**O(n + m) space** in the worst case for the output. If the arrays were
**unsorted**, you'd fall back to hash sets instead (O(n+m) time and space
either way, but without needing sortedness) — this two-pointer version is
specifically the payoff for already having sorted input, the same theme
Day 8 and Day 13 raised repeatedly this week.

---

## Worked Examples — Trace These Yourself First

**Example A:** Why does Trapping Rain Water's two-pointer solution never
need to know the *exact* value of the far-side max, only that it's
*at least as large* as the current side's constraint?
<details><summary>Answer</summary>
Water trapped at any position is `min(left_max, right_max) - height[pos]`.
When we're processing the side with the smaller running max (say, the left
side, because `height[left] < height[right]` implies `right_max >=
height[right] > height[left]`), we know `right_max` is already large enough
to not be the binding constraint — whatever its exact value turns out to be
once fully computed, it's guaranteed to be `>= height[left]`, so `left_max`
alone determines the water level at the current left position, regardless
of `right_max`'s precise value.
</details>

**Example B:** In 3Sum, why is the duplicate-skip check for the "first"
element written as `if i > 0 and arr[i] == arr[i-1]: continue`, rather than
using a `set` to dedupe the final result list afterward?
<details><summary>Answer</summary>
Skipping duplicates *during* the scan (checking against the sorted array's
previous element) avoids ever generating a duplicate triplet in the first
place, keeping the algorithm's work proportional to genuinely new starting
points. Using a `set` afterward would still require generating all
duplicate triplets first (wasted work) and then deduplicating unhashable-if-
list, hashable-if-tuple structures — messier and less efficient than
preventing duplicates at the source, which sortedness makes easy to check
(all equal elements sit adjacent after sorting).
</details>

**Example C:** In Majority Element II, why can there be **at most 2**
elements appearing more than `n/3` times, and how does that fact directly
justify tracking exactly two candidates (rather than, say, three, "to be
safe")?
<details><summary>Answer</summary>
If three or more distinct elements each appeared more than `n/3` times,
their combined occurrence count would exceed `3 * (n/3) = n` — but the
array only has `n` elements total, a contradiction. So at most 2 elements
can possibly qualify, which is exactly why extended Boyer-Moore tracks
precisely 2 candidate/counter pairs — tracking a 3rd would be provably
unnecessary work, and tracking only 1 (the original algorithm) would be
insufficient, since a valid answer set of size 2 wouldn't fit.
</details>

---

## Practice Questions

### Question 1 — Two Sum II (Sorted, Two-Pointer)
**Input:** `arr = [2, 7, 11, 15], target = 9`
**Output:** `[0, 1]`
**Solution:** see section 1. Complexity: `O(n)` time, `O(1)` space.

### Question 2 — Trapping Rain Water
**Input:** `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
**Output:** `6`
**Solution:** see section 2 (optimal two-pointer version). Complexity:
`O(n)` time, `O(1)` space.

### Question 3 — 3Sum
**Input:** `arr = [-1, 0, 1, 2, -1, -4]`
**Output:** `[[-1, -1, 2], [-1, 0, 1]]`
**Solution:** see section 3. Complexity: `O(n²)` time, `O(1)` extra space.

### Question 4 — 4Sum
**Input:** `arr = [1, 0, -1, 0, -2, 2], target = 0`
**Output:** `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`
**Solution:** see section 4. Complexity: `O(n³)` time, `O(1)` extra space.

### Question 5 — Product of Array Except Self
**Input:** `arr = [1, 2, 3, 4]`
**Output:** `[24, 12, 8, 6]`
**Solution:** see section 5. Complexity: `O(n)` time, `O(1)` extra space.

### Question 6 — Longest Consecutive Sequence
**Input:** `arr = [100, 4, 200, 1, 3, 2]`
**Output:** `4`
**Solution:** see section 6. Complexity: `O(n)` time, `O(n)` space.

### Question 7 — Majority Element II
**Input:** `arr = [1, 1, 1, 3, 3, 2, 2, 2]`
**Output:** `[1, 2]`
**Solution:** see section 7. Complexity: `O(n)` time, `O(1)` space.

### Question 8 — Pascal's Triangle
**Input:** `n = 5`
**Output:** `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`
**Solution:** see section 8. Complexity: `O(n²)` time, `O(n²)` space.

### Question 9 — Maximum Consecutive Ones
**Input:** `arr = [1, 1, 0, 1, 1, 1]`
**Output:** `3`
**Solution:** see section 9. Complexity: `O(n)` time, `O(1)` space.

### Question 10 — Union and Intersection of Two Sorted Arrays
**Input:** `arr1 = [1, 2, 2, 3, 4], arr2 = [2, 3, 5]`
**Output:** Union `[1, 2, 3, 4, 5]`, Intersection `[2, 3]`
**Solution:** see section 10. Complexity: `O(n+m)` time, `O(n+m)` space.

---

## How This Connects Back to Days 8–14

- **Two Sum II** is the sorted-array counterpart to Day 8's Two Sum,
  demonstrating the exact space/index trade-off Day 8 described but didn't
  show in code.
- **Trapping Rain Water** reuses the "which side is the binding constraint"
  two-pointer reasoning first seen in Day 8's converging two-pointer
  template.
- **3Sum / 4Sum** build directly on top of Day 8's two-pointer Two Sum,
  showing how it generalizes when you fix `k-2` elements first.
- **Product of Array Except Self** reuses the "running value from one
  direction, then the other" idea from Day 10 (running min) and Day 11
  (running max), applied twice and combined multiplicatively.
- **Longest Consecutive Sequence** reuses the "have I seen X" hashing
  intuition from Day 8's Two Sum, applied to sequence membership instead of
  complement-pair lookup.
- **Majority Element II** is a direct, explicit extension of Day 8/9's
  Moore's Voting Algorithm to two simultaneous candidates.
- **Union/Intersection of Sorted Arrays** reuses the exact merge-walk
  mechanic from Day 6's Merge Sort and Day 13's gap-method merge.

None of today's content introduces a genuinely new algorithmic idea — every
technique here is a direct extension, generalization, or variant framing of
a pattern Days 8–14 already built. That's intentional: the goal of this
supplement is to close specific, commonly-tested gaps without introducing
new cognitive load, reinforcing that this week's patterns (two-pointer,
hashing, running-best tracking, and sorted-merge walks) cover far more
ground than their original example problems might have suggested.

## Key Takeaways

- **Sortedness unlocks two-pointer solutions** for problems that otherwise
  seem to need hashing or brute force (Two Sum II, 3Sum, 4Sum, Union/
  Intersection) — always ask "would sorting first make this monotonic?"
  before reaching for a hash-based approach.
- **"Running value from the left, then from the right, combined"** is a
  reusable two-pass template (Product Except Self, Trapping Rain Water,
  Leaders from Day 11) — recognize it as one pattern, not three unrelated
  tricks.
- **k-Sum problems generalize recursively**: fix elements one at a time,
  bottoming out at two-pointer Two Sum once two elements remain — 3Sum and
  4Sum are the same idea at different depths, not different algorithms.
- **Moore's Voting generalizes to "at most k candidates" for `> n/(k+1)`
  thresholds** — Majority Element II tracking 2 candidates for `> n/3` is a
  direct, principled extension of the single-candidate `> n/2` version, not
  a new algorithm.
