# Day 11 — Next Permutation & Leaders

**Week 2: Arrays Part 1–2** | [Week overview](README.md)

**Language: Python**

---

## 1. Next Permutation

**The problem:** given an array of numbers, rearrange it into the **next
lexicographically greater permutation** — the next arrangement that would
appear if you listed *all* permutations of these numbers in sorted (dictionary)
order. If the current arrangement is already the last (fully descending)
permutation, wrap around to the first (fully ascending) one.

**Example:** `[1, 2, 3]` → next permutation is `[1, 3, 2]`. And
`[3, 2, 1]` (the last permutation) wraps around to `[1, 2, 3]` (the first).

**Building intuition — what makes one permutation "next" after another?**
Think of permutations of `[1,2,3]` listed in lexicographic order:
`123, 132, 213, 231, 312, 321`. Notice: to get from one to the next, we want
the **smallest possible change that still increases the value**, and that
change should happen as far **right** as possible (changing something on the
left "spends" a bigger increase than necessary). This intuition drives the
whole algorithm.

### The algorithm, step by step

**Step 1 — find the pivot.** Scan from the **right**, looking for the first
index `i` (i.e., the *rightmost* such index) where `arr[i] < arr[i+1]` — this
is the rightmost place where increasing something is still possible without
touching anything further left. Everything to the right of `i` is, by
definition of this search, in non-increasing order (a descending run).

**Step 2 — find the successor.** If a pivot was found, scan from the right
again, looking for the first index `j > i` where `arr[j] > arr[i]` — the
smallest value in the descending right-hand run that's still bigger than
`arr[i]`. This is the "smallest possible increase."

**Step 3 — swap.** Swap `arr[i]` and `arr[j]`.

**Step 4 — reverse the suffix.** Everything after index `i` was (and, after
the swap, still is) in descending order — reverse it to make it ascending.
Since we want the **smallest** permutation greater than the current one, the
"tail" (everything after the pivot) should be as small as possible, and the
smallest arrangement of a set of values is their ascending order.

**If no pivot is found in Step 1** (the entire array is non-increasing, e.g.
`[3, 2, 1]`), this *is* the last permutation — simply reverse the whole
array to wrap around to the first (fully ascending) permutation.

```python
def next_permutation(arr):
    n = len(arr)

    # Step 1: find the pivot (rightmost i where arr[i] < arr[i+1])
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: find the rightmost j > i where arr[j] > arr[i]
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Step 3: swap
        arr[i], arr[j] = arr[j], arr[i]

    # Step 4: reverse everything after index i (or the whole array if i == -1)
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr
```

**Trace for `arr = [1, 2, 3]`:**
- Step 1: `i=1`: `arr[1]=2 < arr[2]=3`? Yes → pivot found at `i=1`.
- Step 2: `j=2`: `arr[2]=3 > arr[1]=2`? Yes → `j=2`.
- Step 3: swap `arr[1]` and `arr[2]` → `[1, 3, 2]`.
- Step 4: reverse `arr[2:]` (just `[2]`, a single element — no visible change).

Result: `[1, 3, 2]`. Matches the expected next permutation.

**A richer trace — `arr = [1, 3, 5, 4, 2]`:**
- Step 1: scan from the right: `arr[3]=4 vs arr[4]=2` → `4 >= 2`, keep
  going. `arr[2]=5 vs arr[3]=4` → `5 >= 4`, keep going. `arr[1]=3 vs arr[2]=5`
  → `3 < 5` → pivot found at `i=1`.
- Step 2: scan from the right for the first value `> arr[1]=3`: `arr[4]=2`?
  no. `arr[3]=4`? yes → `j=3`.
- Step 3: swap `arr[1]` and `arr[3]` → `[1, 4, 5, 3, 2]`.
- Step 4: reverse `arr[2:]` (`[5, 3, 2]` → `[2, 3, 5]`) → `[1, 4, 2, 3, 5]`.

Result: `[1, 4, 2, 3, 5]`. This is indeed the next permutation lexicographically
greater than `[1, 3, 5, 4, 2]` — the smallest possible increase (`3`→`4` at
position 1) followed by the smallest possible arrangement of the remaining
digits (`2,3,5` ascending).

**Trace for the wrap-around case, `arr = [3, 2, 1]`:**
- Step 1: `i=1`: `arr[1]=2 >= arr[2]=1`, keep going. `i=0`: `arr[0]=3 >=
  arr[1]=2`, keep going. `i=-1`: loop condition `i >= 0` fails → no pivot found.
- Step 4 (Step 2/3 skipped since `i < 0`): reverse the whole array (`arr[0:]`)
  → `[1, 2, 3]`.

Result: `[1, 2, 3]` — correctly wraps around to the first permutation.

**Complexity:** each step (finding the pivot, finding the successor,
reversing the suffix) is a single linear scan, so **O(n) time** total. The
swap and reversal happen in-place → **O(1) space**.

---

## 2. Leaders in an Array

**The problem:** an element is a **leader** if it is **strictly greater than
every element to its right** (the last element is always a leader by
default, since it has nothing to its right to compare against). Return all
leaders, in their original left-to-right order.

**Example:** `[16, 17, 4, 3, 5, 2]` → leaders are `[17, 5, 2]` (`17` beats
everything after it; `4` and `3` don't, since `5` is later and bigger; `5`
beats everything after it (`2`); `2` is the last element, automatically a
leader).

**Brute force:** for each element, scan everything to its right and check if
it's the max — `O(n²)`.

**Better approach — scan from the right, tracking the running maximum:**
if you scan right to left, "everything to the right" of the current position
is exactly everything you've already scanned. So maintain a running max: an
element is a leader exactly when it's **greater than the running max seen so
far** (from the right).

```python
def find_leaders(arr):
    leaders = []
    max_from_right = float('-inf')
    for x in reversed(arr):
        if x > max_from_right:
            leaders.append(x)
            max_from_right = x
    leaders.reverse()   # we collected them right-to-left; reverse for original order
    return leaders
```

**Trace for `arr = [16, 17, 4, 3, 5, 2]`, scanning in reverse (`2, 5, 3, 4, 17, 16`):**
| x | x > max_from_right? | leaders (collected so far) | max_from_right after |
|---|---|---|---|
| 2 | 2 > -inf, yes | [2] | 2 |
| 5 | 5 > 2, yes | [2, 5] | 5 |
| 3 | 3 > 5? no | [2, 5] | 5 |
| 4 | 4 > 5? no | [2, 5] | 5 |
| 17 | 17 > 5, yes | [2, 5, 17] | 17 |
| 16 | 16 > 17? no | [2, 5, 17] | 17 |

Collected (right-to-left order): `[2, 5, 17]`. Reverse to restore original
left-to-right order: `[17, 5, 2]`. Matches the expected answer.

**Complexity:** **O(n) time** (single reverse pass, plus the final reverse
of the small `leaders` list which is at most O(n) itself but doesn't change
the overall class), **O(k) space** for the output where `k` is the number of
leaders (unavoidable, since we must return them) — the auxiliary tracking
itself is O(1) beyond the output. This is the same "running best, scanned
from the informative direction" pattern as Best Time to Buy/Sell Stock (Day
10) — the key realization there was to track a running *minimum from the
left*; here it's a running *maximum from the right*. Recognizing "which
direction should I scan from, based on what information I need to have
already seen" is a transferable skill across many array problems.

---

## 3. Find All Duplicates in an Array (Without Extra Space) — Stretch

**The problem:** given an array of `n` integers where every value is in the
range `[1, n]` and some values appear **twice** while others appear once,
find all the values that appear twice — **without using extra space** beyond
the output list itself (i.e., O(1) *auxiliary* space, not counting the
result).

**The trick — use the array itself as a hash table, via sign-marking.**
Since every value is guaranteed to be in `[1, n]`, each value `v` can be
mapped to a valid index `v - 1`. Walk through the array; for each value `v`
(using its absolute value, since we'll be flipping signs), go to index
`|v| - 1` and **negate** the value stored there. If you visit an index and
find the value **already negative**, that means you've seen this value
before — it's a duplicate.

```python
def find_duplicates(arr):
    duplicates = []
    for x in arr:
        index = abs(x) - 1
        if arr[index] < 0:
            duplicates.append(abs(x))
        else:
            arr[index] = -arr[index]
    return duplicates
```

**Trace for `arr = [4, 3, 2, 7, 8, 2, 3, 1]`:**
| x | index=abs(x)-1 | arr[index] before | already negative? | action | arr after |
|---|---|---|---|---|---|
| 4 | 3 | 7 | no | negate | [4,3,2,-7,8,2,3,1] |
| 3 | 2 | 2 | no | negate | [4,3,-2,-7,8,2,3,1] |
| 2 | 1 | 3 | no | negate | [4,-3,-2,-7,8,2,3,1] |
| 7 | 6 | 3 | no | negate | [4,-3,-2,-7,8,2,-3,1] |
| 8 | 7 | 1 | no | negate | [4,-3,-2,-7,8,2,-3,-1] |
| 2 | 1 | -3 | **yes** | duplicate! append 2 | (unchanged) |
| 3 | 2 | -2 | **yes** | duplicate! append 3 | (unchanged) |
| 1 | 0 | 4 | no | negate | [-4,-3,-2,-7,8,2,-3,-1] |

Result: `duplicates = [2, 3]`. Correct — `2` and `3` are the values that
appear twice in the original array.

**Complexity:** **O(n) time** (single pass; each index is visited a bounded
number of times). **O(1) auxiliary space** (beyond the output list) — this
is the key achievement, since the "obvious" approach (a hash set tracking
seen values) would cost O(n) space. **Caveat:** this technique **mutates the
input array** (temporarily, via sign flips) and only works because of the
guarantee that all values lie in `[1, n]` — it's a specialized trick for
this specific constraint, not a general-purpose duplicate-finder. If you
need to preserve the original array, restore the signs afterward (a final
pass taking the absolute value of every element), or use a hash set instead
if O(n) space is acceptable.

---

## Worked Examples — Trace These Yourself First

**Example A:** Why does the Next Permutation algorithm search for the pivot
`i` from the **right**, rather than the left?
<details><summary>Answer</summary>
We want the **smallest possible change** that still produces a strictly
greater permutation — and a change made further to the right affects the
value of the overall number/arrangement less than a change made further
left (like how increasing the units digit changes a number less than
increasing the tens digit). Searching from the right finds the *rightmost*
position where an increase is even possible, guaranteeing we make the
smallest-magnitude change available.
</details>

**Example B:** In `find_leaders`, why does scanning from the **right**
(rather than the left) let you compute "is this element greater than
everything to its right" in a single pass, when scanning from the left
would require nested loops?
<details><summary>Answer</summary>
"Everything to the right of position `i`" is exactly the set of elements
already visited if you scan right-to-left starting from the end. So a single
running maximum (`max_from_right`), updated as you go, always holds
"the max of everything already scanned" = "the max of everything to the
right of the current position" — no re-scanning needed. Scanning left to
right would require, for each position, a fresh scan of everything after
it (since that maximum isn't known yet), forcing nested loops and O(n²).
</details>

**Example C:** In `find_duplicates`, why must the code check `arr[index] < 0`
using the value *at* `index`, rather than checking the original `x` itself
for negativity?
<details><summary>Answer</summary>
`x` (the current element being iterated) might itself already be negative
from an *earlier* negation applied when some other element pointed to its
index — so checking `x < 0` directly would be checking "was some other
value, earlier, marked as pointing to me," not "have I, this specific value,
been seen before." We need `abs(x)` to recover the *original* value (undoing
any earlier negation done *to* this slot), and then check whether *that
value's own designated slot* (`arr[abs(x)-1]`) has already been marked — that
tells us if this value specifically has occurred before.
</details>

---

## Practice Questions

### Question 1 — Next Permutation
**Question:** Given an array of numbers, rearrange it in-place into the next
lexicographically greater permutation, wrapping around to the smallest if
it's already the largest.
**Input:** `arr = [1, 2, 3]`
**Output:** `[1, 3, 2]`
**Input 2:** `arr = [3, 2, 1]`
**Output 2:** `[1, 2, 3]`
**Solution:**
```python
def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr

print(next_permutation([1, 2, 3]))   # [1, 3, 2]
print(next_permutation([3, 2, 1]))   # [1, 2, 3]
```
Find the rightmost ascending pair (the pivot), swap it with the smallest
larger value to its right, then reverse the now-descending suffix to make it
ascending (the smallest possible tail). Complexity: `O(n)` time, `O(1)`
space (section 1).

### Question 2 — Leaders in an Array
**Question:** Given an array, return all elements that are strictly greater
than every element to their right, in original left-to-right order.
**Input:** `arr = [16, 17, 4, 3, 5, 2]`
**Output:** `[17, 5, 2]`
**Solution:**
```python
def find_leaders(arr):
    leaders = []
    max_from_right = float('-inf')
    for x in reversed(arr):
        if x > max_from_right:
            leaders.append(x)
            max_from_right = x
    leaders.reverse()
    return leaders

print(find_leaders([16, 17, 4, 3, 5, 2]))   # [17, 5, 2]
```
Scan right-to-left, tracking a running maximum; any element exceeding that
running max is a leader (the last element is always a leader). Complexity:
`O(n)` time, `O(k)` output space (section 2).

### Question 3 — Find All Duplicates in an Array (Without Extra Space)
**Question:** Given an array of `n` integers where each value is in
`[1, n]` and some values appear exactly twice, find all values that appear
twice, using O(1) auxiliary space.
**Input:** `arr = [4, 3, 2, 7, 8, 2, 3, 1]`
**Output:** `[2, 3]`
**Solution:**
```python
def find_duplicates(arr):
    duplicates = []
    for x in arr:
        index = abs(x) - 1
        if arr[index] < 0:
            duplicates.append(abs(x))
        else:
            arr[index] = -arr[index]
    return duplicates

print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))   # [2, 3]
```
Use each value as an index into the array itself, marking "visited" by
negating the value stored there — a second visit to an already-negated slot
reveals a duplicate. Complexity: `O(n)` time, `O(1)` auxiliary space
(section 3) — mutates the input array (recoverable by taking absolute values
afterward if the original array must be preserved).

## Revision

- Quick recall (5 min): re-solve Best Time to Buy and Sell Stock from Day 10
  cold.

## Key Takeaways

- **Next Permutation** works by finding the rightmost position where an
  increase is possible (the pivot), making the smallest possible increase
  there (swap with the smallest larger value to its right), then arranging
  everything after it in the smallest possible order (ascending) — all in
  `O(n)` time, `O(1)` space.
- **Leaders in an Array** are found efficiently by scanning **from the
  right** and tracking a running maximum — recognizing which scan direction
  gives you "free" access to the information you need (everything to one
  side already processed) avoids an O(n²) nested-loop trap.
- The **sign-marking trick** (using array values as indices, and negating
  to mark "visited") solves duplicate-finding in `O(1)` auxiliary space when
  the problem guarantees values fall within `[1, n]` — a specialized
  technique, not a general hash-map replacement.
- Across today's three problems: **the direction you scan from, and what
  you choose to track as a running value (min, max, or a marked visitation
  state), is usually the entire trick** — the loops themselves are simple
  once that choice is made correctly.

---

## Additional Topics — Filling Gaps in Day 11's Scope

Day 11 covered permutations (next permutation) and a hard duplicate-finding
trick. Two natural companions were missing: a **simpler** missing-number
warm-up (before Day 14's harder repeating+missing version), and generating
the **Kth permutation directly** without listing all permutations.

### 4. Missing Number (Simple Version — No Duplicate)

**The problem:** an array of size `n` contains `n` distinct numbers taken
from the range `[0, n]` (so exactly **one** number in that range is
missing, and there are no duplicates) — find the missing number. This is a
simpler cousin of Day 14's "Find the Repeating and Missing Number" (which
has both a duplicate *and* a missing number); here there's only a missing
number, nothing repeated.

**Example:** `arr = [3, 0, 1]` (`n=3`, range `[0,3]`) → `2` is missing.

**Idea 1 — sum difference:** the expected sum of `0..n` is `n(n+1)/2`; the
missing number is that expected sum minus the array's actual sum.

```python
def missing_number(arr):
    n = len(arr)
    expected = n * (n + 1) // 2
    return expected - sum(arr)

print(missing_number([3, 0, 1]))   # 2
```

**Trace for `arr = [3, 0, 1]`:** `n=3`, `expected = 3*4//2 = 6`,
`sum(arr) = 3+0+1 = 4`, `missing = 6 - 4 = 2`. Matches.

**Idea 2 — XOR (avoids any risk of integer overflow in other languages,
though not a practical concern in Python):** XOR every array value together
with every number from `0` to `n` — every value that appears in both
cancels to `0` (via `a^a=0`), leaving only the number that appears **once**
(the missing one, present only in the `0..n` range, not in the array).

```python
def missing_number_xor(arr):
    n = len(arr)
    result = n                      # start with n, since it's not covered by the loop below
    for i in range(n):
        result ^= i ^ arr[i]
    return result

print(missing_number_xor([3, 0, 1]))   # 2
```

**Complexity (both versions):** **O(n) time**, **O(1) space** — this is the
direct, simpler ancestor of Day 14's sum/sum-of-squares approach (section
1), which needed a *second* equation only because it had *two* unknowns
(repeating **and** missing); with just one unknown, one equation suffices.

### 5. Kth Permutation Sequence

**The problem:** given `n` and `k`, return the `k`-th permutation (in
lexicographic order, 1-indexed) of the numbers `1` to `n`, **without**
generating and sorting all `n!` permutations.

**Key insight — factorial number system:** with `n` numbers remaining to
place, there are exactly `(n-1)!` permutations starting with **each**
possible choice for the first position. So `k // (n-1)!` (0-indexed `k`)
tells you exactly **which** of the remaining numbers goes first; the
remainder tells you which permutation-among-those-starting-with-that-choice
you need next, recursively, one position at a time.

```python
import math

def get_permutation(n, k):
    nums = list(range(1, n + 1))
    k -= 1                                   # convert to 0-indexed
    result = []
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)         # permutations per choice of next digit
        idx = k // fact                       # which of the remaining numbers to place next
        result.append(str(nums.pop(idx)))
        k %= fact                              # remaining rank within that choice
    return ''.join(result)

print(get_permutation(3, 3))   # "213"
print(get_permutation(4, 9))   # "2314"
```

**Trace for `n=3, k=3`** (`nums=[1,2,3]`, `k→2` after 0-indexing):
- `i=3`: `fact=2! =2`. `idx = 2//2=1` → pop `nums[1]=2` → `result=['2']`,
  `nums=[1,3]`. `k = 2%2=0`.
- `i=2`: `fact=1! =1`. `idx=0//1=0` → pop `nums[0]=1` → `result=['2','1']`,
  `nums=[3]`. `k=0%1=0`.
- `i=1`: `fact=0! =1`. `idx=0//1=0` → pop `nums[0]=3` →
  `result=['2','1','3']`.

Result: `"213"`. Verify by listing all permutations of `[1,2,3]` in order:
`123, 132, 213, 231, 312, 321` — the 3rd one is indeed `213`. Matches.

**Why does dividing by `(i-1)!` correctly identify which remaining number
comes next, without ever generating a full permutation list?** With `i`
numbers still unplaced, fixing any one of them as "next" leaves `(i-1)!`
ways to arrange the rest — so the numbers `0` through `(i-1)!-1` (in
0-indexed rank) all correspond to permutations starting with the
**smallest** remaining number, the next `(i-1)!` ranks correspond to the
**second-smallest**, and so on. Integer division by `(i-1)!` directly
computes which "block" the target rank `k` falls into — precisely which
remaining number to place — without ever materializing the other
permutations in that block.

**Complexity:** **O(n²) time** in this implementation (the `list.pop(idx)`
operation is `O(n)`, done `n` times) — this can be improved to `O(n log n)`
with a more advanced data structure (e.g. a Fenwick tree) if needed, but
`O(n²)` is standard and sufficient for typical interview constraints.
**O(n) space** for `nums` and `result`. Dramatically better than the naive
"generate all `n!` permutations, sort, index in" approach, which is
**O(n! · n log n)** or worse.

## Additional Key Takeaways (Day 11 Supplement)

- **Missing Number (simple)** is the single-unknown ancestor of Day 14's
  repeating+missing problem — one equation (sum difference, or XOR
  cancellation) suffices when there's only one unknown to solve for.
- **Kth Permutation Sequence** uses the **factorial number system** to
  jump directly to the answer, position by position, without ever
  generating other permutations — division by `(remaining-1)!` at each step
  tells you exactly which value to place next.
- Both problems reinforce a recurring theme from Day 11: **converting a
  seemingly combinatorial/brute-force problem into direct arithmetic**
  (sum differences, factorial-block division) avoids exponential blowup.
