# Day 8 — Two-Pointer & Sorting-Based Patterns

**Week 2: Arrays Part 1–2** | [Week overview](README.md)

**Language: Python**

---

## 1. The Two-Pointer Technique — Formalized

You've already used pieces of this technique without the formal name: Day 3's
array reversal (two pointers converging from the ends) and remove-duplicates
/ move-zeros (two pointers moving in the same direction at different speeds).
Today we name the pattern explicitly and apply it to a new class of problems:
**finding pairs (or groups) of elements that satisfy some condition.**

**The core insight:** on an **unsorted** array, checking every pair for a
condition (like "do these two sum to a target?") naively costs `O(n²)` — a
nested loop over all pairs. But if the array is **sorted**, you can use two
pointers — one starting at the left end, one at the right end — and *move
them intelligently* based on a comparison, eliminating large chunks of the
search space with each step, much like Binary Search eliminates half the
array with each comparison.

**General template for the converging two-pointer pattern on a sorted array:**
```python
left, right = 0, len(arr) - 1
while left < right:
    current = combine(arr[left], arr[right])   # e.g. arr[left] + arr[right]
    if current == target:
        # found it — record/return
    elif current < target:
        left += 1     # need a bigger combined value — move left pointer right
    else:
        right -= 1    # need a smaller combined value — move right pointer left
```

**Why moving `left` right always increases `current` (for a sum), and why
that's safe:** because the array is sorted ascending, `arr[left]` only ever
gets larger as `left` increases — so if the current sum is too small, moving
`left` forward is the *only* way to potentially reach the target without
overshooting from the other direction. This monotonic relationship between
pointer movement and value movement is precisely what makes the two-pointer
approach correct — it can only work when you have some sorted/monotonic
structure to exploit.

---

## 2. Two Sum (Return Indices) — Hashing Approach

**The problem:** given an array and a target value, find the **indices** of
two elements that sum to the target.

**Why not the two-pointer approach here?** Two-pointer requires a *sorted*
array, but this problem asks for the **original indices** — sorting the
array would scramble those indices, and mapping back is extra work.
Fortunately, there's an approach that works directly on the unsorted array
and is just as fast: **hashing**.

**Idea:** walk through the array once. For each element `x`, check whether
`target - x` (the value that would complete the pair) has **already been
seen**. If yes, you've found your pair. If no, record `x`'s index in a
hash map (Python `dict`) for future lookups, and keep going.

```python
def two_sum(arr, target):
    seen = {}                       # maps value -> index, for values seen so far
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []                        # no valid pair found
```

**Trace for `two_sum([2, 7, 11, 15], target=9)`:**
| i | x | complement | complement in seen? | action | seen after |
|---|---|---|---|---|---|
| 0 | 2 | 7 | no | record | {2: 0} |
| 1 | 7 | 2 | **yes** (seen[2]=0) | return [0, 1] | — |

Result: `[0, 1]` — `arr[0] + arr[1] = 2 + 7 = 9`. Correct.

**Complexity:** **O(n) time** — a single pass, and dict lookups/insertions
are O(1) average case. **O(n) space** — the `seen` dictionary can grow to
hold up to `n` entries. This is a direct trade: we spend O(n) *extra space*
to avoid the O(n²) nested-loop brute force (check every pair directly) or
the awkwardness of sorting (which would cost O(n log n) and lose original
indices).

**This "have I seen the complement/target value before" hashing pattern is
one of the highest-value patterns in all of interview DSA** — it converts an
apparent O(n²) pairwise-checking problem into O(n), and reappears constantly
(you'll see close variants throughout this plan, including Day 16's subarray
sum problems).

---

## 3. Move All Negative Numbers to One Side

**The problem:** rearrange an array in-place so all negative numbers come
before all non-negative numbers. (Order *within* each group doesn't need to
be preserved — this is a relaxation of Day 3's "move zeros to the end,"
which did need to preserve order.)

**Idea:** this is the same **slow/fast, same-direction two-pointer pattern**
from Day 3's `move_zeros_to_end` — but because order doesn't need to be
preserved here, we can use an even simpler **converging two-pointer**
approach instead, similar in spirit to the Dutch National Flag partitioning
from Day 6.

```python
def move_negatives_to_left(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] < 0:
            left += 1                 # already negative, correctly placed — move on
        elif arr[right] >= 0:
            right -= 1                 # already non-negative, correctly placed — move on
        else:
            arr[left], arr[right] = arr[right], arr[left]   # swap misplaced pair
            left += 1
            right -= 1
    return arr
```

**Trace for `arr = [1, -2, 3, -4, 5, -6]`:**
| left | right | arr[left] | arr[right] | action | arr after |
|---|---|---|---|---|---|
| 0 | 5 | 1 | -6 | both misplaced, swap | [-6,-2,3,-4,5,1] |
| 1 | 4 | -2 | 5 | arr[left]<0, left→2 | [-6,-2,3,-4,5,1] |
| 2 | 4 | 3 | 5 | both misplaced, swap | [-6,-2,5,-4,3,1] |
| 3 | 3 | — | — | loop stops (left==right) | — |

Result: `[-6, -2, 5, -4, 3, 1]`. Check: negatives (`-6,-2,-4`) all appear
before non-negatives (`5,3,1`) — correct, even though the relative order
within each group changed (`-4` moved past `5`), which is allowed here since
we only need grouping, not order preservation.

**Complexity:** O(n) time (each pointer moves at most n times total),
O(1) space — the same converging two-pointer shape as Day 3's array
reversal, applied to a partitioning condition instead of a full reversal.

**If order-preservation is required instead** (harder version), you'd need
the same-direction slow/fast pattern from Day 3's `move_zeros_to_end`
instead — the converging approach above sacrifices order for a simpler,
still-O(n)/O(1) implementation. Recognizing *which* variant a problem is
asking for (order matters vs. doesn't) is part of correctly picking your
pattern.

---

## 4. Moore's Voting Algorithm — Intuition (Full Problem on Day 9)

**The problem it solves:** given an array, find the element that appears
**more than n/2 times** (the "majority element"), if one exists — in
**O(n) time and O(1) space** (no hash map counting, which would also work
but costs O(n) space).

**The core intuition — "cancellation":** think of each occurrence of the
current candidate majority element as a `+1` vote, and every other element as
a `-1` vote against it. If you walk through the array maintaining a running
`count`, incrementing for the current candidate and decrementing otherwise,
here's the key fact: **a true majority element (appearing more than n/2
times) can never be fully "cancelled out" to zero and then displaced for
good**, because it fundamentally outnumbers every other element combined.

Concretely: maintain a `candidate` and a `count`. If `count` hits 0, pick a
new `candidate` (the current element) and reset `count` to 1. Otherwise,
increment `count` if the current element matches `candidate`, or decrement
it if it doesn't.

**A miniature trace, informally, for `[2, 2, 1, 1, 1]`** (majority element
is `1`, appearing 3 out of 5 times):
- Start: `candidate=2, count=1` (first element).
- See `2`: matches candidate, `count=2`.
- See `1`: doesn't match, `count=1`.
- See `1`: doesn't match, `count=0` → **candidate switches to `1`**, `count=1`.
- See `1`: matches new candidate, `count=2`.
- End: `candidate = 1` — correct!

Notice the true majority element (`1`) survived the "cancellation war" and
ended up as the final candidate, even though it wasn't the *first* element
seen. You'll implement this fully, with the full code and a formal
correctness discussion, on **Day 9** — today's goal is just to plant this
intuition so the algorithm doesn't feel like a magic trick when you meet the
code tomorrow.

---

## 5. Dutch National Flag — Quick Revisit

You fully covered this algorithm on **Day 6, section 4** — sorting an array
of only `0`s, `1`s, and `2`s in a single O(n) pass using three pointers
(`low`, `mid`, `high`). It's listed again in today's practice set purely for
spaced repetition, since it's exactly the kind of "clicks once, then must be
reinforced" algorithm that's easy to forget without a second pass. If the
three-pointer logic doesn't come back to you immediately, re-read Day 6
section 4 before attempting the practice question below — don't just
re-copy the code from memory without re-deriving *why* `mid` advances after
a `0`-swap but not after a `2`-swap.

---

## Worked Examples — Trace These Yourself First

**Example A:** Why does the Two Sum hashing approach check `complement in
seen` **before** adding the current element `x` to `seen`, rather than
after?
<details><summary>Answer</summary>
If you added `x` to `seen` first, an element could incorrectly "pair with
itself" — e.g. for `target=4` and current element `x=2`, if `2` were already
in `seen` (added on this same iteration before the check), the function
would wrongly report indices `[i, i]` using the same index twice. Checking
the complement *before* inserting `x` ensures a match can only use a
*different*, earlier-seen index.
</details>

**Example B:** In `move_negatives_to_left`, why is the converging two-pointer
approach able to use O(1) space, while a version that builds two separate
lists (one for negatives, one for non-negatives) and concatenates them would
use O(n) space?
<details><summary>Answer</summary>
The converging two-pointer approach only ever swaps elements *within* the
existing array — no new list is ever created, so auxiliary space is O(1). A
"build two separate lists" approach allocates new memory proportional to the
input size to hold the split-out groups before combining them, which is
O(n) auxiliary space. This is the same time/space trade-off theme from
Day 3, Example C — same O(n) time, different space complexity depending on
whether you mutate in place or allocate new structures.
</details>

**Example C:** In Moore's Voting intuition, what would happen if you ran the
algorithm on an array that has **no** true majority element (e.g.
`[1, 2, 3, 4]`, where nothing appears more than 2 times)? Would the returned
`candidate` still be meaningful?
<details><summary>Answer</summary>
The algorithm will still run and produce *some* candidate — but it would be
meaningless/incorrect, since no true majority exists. Moore's Voting
Algorithm only *guarantees* correctness when a majority element is known (or
verified) to exist; if that's not guaranteed by the problem, you need an
extra verification pass afterward (count the candidate's actual occurrences
and check it's really `> n/2`) before trusting the result. You'll see this
verification step explicitly in Day 9's full implementation.
</details>

---

## Practice Questions

### Question 1 — Sort an Array of 0s, 1s, and 2s (Dutch National Flag)
**Question:** Given an array containing only `0`, `1`, and `2`, sort it
in-place in a single O(n) pass. (Full explanation: Day 6, section 4.)
**Input:** `arr = [2, 0, 2, 1, 1, 0]`
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

print(sort_012([2, 0, 2, 1, 1, 0]))   # [0, 0, 1, 1, 2, 2]
```
Three pointers (`low`/`mid`/`high`) partition the array into three known
bands in one pass. Complexity: `O(n)` time, `O(1)` space.

### Question 2 — Move All Negative Numbers to One Side
**Question:** Given an array of positive and negative integers, rearrange it
in-place so all negatives come before all non-negatives (relative order
within each group doesn't need to be preserved).
**Input:** `arr = [1, -2, 3, -4, 5, -6]`
**Output:** `[-6, -2, 5, -4, 3, 1]` (one valid arrangement — any arrangement
with all negatives before all non-negatives is acceptable)
**Solution:**
```python
def move_negatives_to_left(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] < 0:
            left += 1
        elif arr[right] >= 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

print(move_negatives_to_left([1, -2, 3, -4, 5, -6]))   # [-6, -2, 5, -4, 3, 1]
```
Converging two-pointer partition: advance `left` past already-negative
elements, `right` past already-non-negative elements, and swap misplaced
pairs. Complexity: `O(n)` time, `O(1)` space (section 3).

### Question 3 — Two Sum (Return Indices) — Hashing Approach
**Question:** Given an array and a target sum, return the indices of two
elements that add up to the target.
**Input:** `arr = [2, 7, 11, 15], target = 9`
**Output:** `[0, 1]`
**Solution:**
```python
def two_sum(arr, target):
    seen = {}
    for i, x in enumerate(arr):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
```
Single pass, checking whether the value needed to complete the pair
(`target - x`) has already been seen, using a hash map for O(1) average
lookups. Complexity: `O(n)` time, `O(n)` space (section 2).

## Revision

- Quick recall (5 min): re-implement Binary Search (Week 1, Day 7) from
  memory — iterative version, watch the `mid` formula and loop condition.

## Key Takeaways

- The **converging two-pointer pattern** solves pair-finding problems in
  `O(n)` on a **sorted** array by exploiting the monotonic relationship
  between pointer movement and value movement — it can't be applied to
  unsorted data without first sorting (which costs `O(n log n)` and may
  destroy needed information like original indices).
- The **"have I seen X before" hashing pattern** (Two Sum) converts an
  apparent `O(n²)` pairwise-checking problem into `O(n)` time at the cost of
  `O(n)` space — and works directly on unsorted data while preserving
  original indices, unlike the two-pointer approach.
- Whether a problem requires **preserving relative order** (like Day 3's
  move-zeros) or not (like today's move-negatives) determines whether you
  need the same-direction slow/fast pattern or can use the simpler
  converging two-pointer pattern.
- **Moore's Voting Algorithm** uses a "cancellation" intuition — a true
  majority element can never be permanently cancelled out — to find a
  majority element in `O(n)` time, `O(1)` space; it requires a verification
  pass if the existence of a majority element isn't guaranteed. Full
  implementation on Day 9.

---

## Additional Topics — Filling Gaps in Day 8's Scope

Two more classic two-pointer problems that belong alongside today's Two Sum
and Move-Negatives — both are extremely common interview questions that use
the exact converging/same-direction two-pointer templates from section 1.

### 6. Container With Most Water

**The problem:** given an array `height` where `height[i]` is the height of
a vertical line at position `i`, find two lines that, together with the
x-axis, form a container holding the **maximum amount of water**. The
container's area is `min(height[left], height[right]) * (right - left)` —
bounded by the **shorter** of the two lines (water can't rise above the
shorter wall) and the **distance** between them.

**Brute force:** check every pair of lines — `O(n²)`.

**Optimal — converging two-pointer:** start with the **widest** possible
container (`left=0, right=n-1`) and shrink inward. **Key insight:** at each
step, the container's height is capped by the **shorter** line — so moving
the pointer at the **taller** line inward can only ever *shrink* the width
without any chance of increasing the height cap (the shorter side still
bounds it, or bounds it even more if the new line is shorter still). Moving
the pointer at the **shorter** line, however, might find a taller line,
potentially increasing the height cap enough to offset the reduced width.
So: **always move the pointer at the shorter line.**

```python
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, h * (right - left))
        if height[left] < height[right]:
            left += 1      # shorter side — move it, hoping for a taller line
        else:
            right -= 1
    return best

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 49
```

**Trace for `height = [1,8,6,2,5,4,8,3,7]`:**
| left | right | h=min | width | area | move |
|---|---|---|---|---|---|
| 0(1) | 8(7) | 1 | 8 | 8 | left (shorter) |
| 1(8) | 8(7) | 7 | 7 | 49 | right (shorter) |
| 1(8) | 7(3) | 3 | 6 | 18 | right |
| 1(8) | 6(8) | 8 | 5 | 40 | left or right (tie, either) |

Best area found: `49` (between index 1, height 8, and index 8, height 7).
Matches.

**Why is it safe to permanently discard the shorter line's position without
checking it against every other line?** Any container using the shorter
line paired with something **even further away** than the current partner
would still be capped by that same short height (or an even shorter one it
finds) — since we've already paired it with its farthest possible partner
(the widest container available at this step), no future pairing involving
this exact line can beat the area just computed. This is the same
"eliminate large chunks of the search space per comparison" logic Day 8's
original two-pointer template (section 1) and Binary Search both rely on.

**Complexity:** **O(n) time** (single converging pass), **O(1) space**.

### 7. Squares of a Sorted Array

**The problem:** given an array sorted in **non-decreasing** order (which
may contain negative numbers), return a new array of the squares of each
element, **also sorted** in non-decreasing order.

**Example:** `[-4, -1, 0, 3, 10]` → `[0, 1, 9, 16, 100]`.

**Why not just square everything and re-sort?** That works (`O(n log n)`),
but there's an `O(n)` two-pointer approach: since the input is sorted, the
**largest-magnitude** values sit at the two **ends** of the array (very
negative on the left, very positive on the right) — the middle holds the
smallest-magnitude values. So the **largest squares** are always found by
comparing the two end pointers, and we can fill the result array **from the
back** (largest to smallest).

```python
def sorted_squares(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1
    for pos in range(n - 1, -1, -1):        # fill from the largest position backward
        if abs(arr[left]) > abs(arr[right]):
            result[pos] = arr[left] ** 2
            left += 1
        else:
            result[pos] = arr[right] ** 2
            right -= 1
    return result

print(sorted_squares([-4, -1, 0, 3, 10]))   # [0, 1, 9, 16, 100]
```

**Trace for `arr = [-4, -1, 0, 3, 10]`:**
| pos | left(val) | right(val) | abs compare | placed | left/right after |
|---|---|---|---|---|---|
| 4 | 0(-4) | 4(10) | 4 < 10 | 100 | right→3 |
| 3 | 0(-4) | 3(3) | 4 > 3 | 16 | left→1 |
| 2 | 1(-1) | 3(3) | 1 < 3 | 9 | right→2 |
| 1 | 1(-1) | 2(0) | 1 > 0 | 1 | left→2 |
| 0 | 2(0) | 2(0) | equal | 0 | either advances, loop ends |

Result: `[0, 1, 9, 16, 100]`. Matches.

**Complexity:** **O(n) time** (single pass, filling result directly rather
than sorting), **O(n) space** for the output — beats the "square then sort"
approach's `O(n log n)` time.

## Additional Key Takeaways (Day 8 Supplement)

- **Container With Most Water** always moves the pointer at the **shorter**
  line inward — moving the taller line can only shrink the container with
  no chance of raising its height cap, so it's provably never useful.
- **Squares of a Sorted Array** exploits the fact that a sorted array's
  largest-magnitude values sit at its two ends — filling the result
  **from the back** using a converging two-pointer avoids the need to
  re-sort after squaring.
