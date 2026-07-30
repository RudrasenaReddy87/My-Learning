# Day 9 — Kadane's Algorithm & Subarray Problems

**Week 2: Arrays Part 1–2** | [Week overview](README.md)

**Language: Python**

---

## 1. Maximum Subarray Sum — The Problem

**The problem:** given an array of integers (which may include negatives),
find the **contiguous subarray** (elements next to each other, not just any
subset) with the largest possible sum, and return that sum.

**Example:** `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` → the maximum sum comes from
the subarray `[4, -1, 2, 1]`, summing to `6`.

### Brute force approaches (know these, but don't stop here)

- **Check every subarray individually:** for every pair `(i, j)`, sum
  `arr[i..j]` and track the max. That's `O(n²)` pairs, each costing `O(n)`
  to sum, giving **O(n³)** total — very slow.
- **Precompute prefix sums to get each subarray sum in O(1):** still `O(n²)`
  pairs to check, giving **O(n²)** total — better, but still not good enough
  for large `n`.

We want **O(n)** — a single pass. That's what Kadane's Algorithm gives us.

---

## 2. Deriving Kadane's Algorithm

**The key insight:** as you scan left to right, maintain a running sum
(`current_sum`) of "the best subarray sum ending exactly at the current
position." At each new element, you face a choice:

- **Extend** the existing running subarray by adding the current element to it, OR
- **Start fresh** — throw away everything accumulated so far and start a new
  subarray at just the current element.

**When should you start fresh?** Precisely when the running sum so far
(`current_sum`) is **negative** — because adding a negative running sum to
the current element can only make things worse than starting over.
Formally: `current_sum = max(arr[i], current_sum + arr[i])`. Then track the
best `current_sum` ever seen, across the whole scan, in a separate variable
(`best_sum`) — because the maximum sum might end anywhere in the array, not
necessarily at the last position.

```python
def kadane_max_subarray_sum(arr):
    current_sum = arr[0]
    best_sum = arr[0]
    for x in arr[1:]:
        current_sum = max(x, current_sum + x)   # extend or restart
        best_sum = max(best_sum, current_sum)     # track the best seen so far
    return best_sum
```

**Trace for `arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`:**
| x | current_sum + x | max(x, current_sum+x) | current_sum | best_sum |
|---|---|---|---|---|
| start | — | — | -2 | -2 |
| 1 | -2+1=-1 | max(1,-1)=1 | 1 | 1 |
| -3 | 1-3=-2 | max(-3,-2)=-2 | -2 | 1 |
| 4 | -2+4=2 | max(4,2)=4 | 4 | 4 |
| -1 | 4-1=3 | max(-1,3)=3 | 3 | 4 |
| 2 | 3+2=5 | max(2,5)=5 | 5 | 5 |
| 1 | 5+1=6 | max(1,6)=6 | 6 | **6** |
| -5 | 6-5=1 | max(-5,1)=1 | 1 | 6 |
| 4 | 1+4=5 | max(4,5)=5 | 5 | 6 |

Result: `best_sum = 6`, matching the expected answer from section 1. Notice
`current_sum` "restarted" at `4` when `x=4` was reached (because the running
sum `-2` at that point was negative — extending would have given `-2+4=2`,
worse than just starting fresh at `4`), and from there it built up to `6`
without ever needing to restart again.

**Complexity: O(n) time** (single pass), **O(1) space** — a dramatic
improvement over both brute-force approaches. This exact "running best,
reset when it goes negative" pattern is one of the most famous and most
reused patterns in all of DSA — you already saw a preview of the general
"running best" idea back on Day 3 (finding the largest element), and
Kadane's is really that same idea, applied to a running *sum* instead of a
running *max*, with an added "reset" rule.

**Edge case worth knowing:** this version assumes the array is non-empty and
correctly handles an array of **all negative numbers** — e.g. for
`[-3, -1, -2]`, it would correctly return `-1` (the single least-negative
element), because `current_sum` never has a reason to "restart" at 0 (there's
no 0 baseline in this version — `current_sum` always starts genuinely at
`arr[0]` and only ever compares against extending vs. the current element
itself). This matters: some naive Kadane's implementations incorrectly
initialize `current_sum = 0` and end up allowing an "empty subarray" with sum
0 to beat every genuinely negative option, which is wrong unless the problem
explicitly allows empty subarrays.

---

## 3. Printing the Actual Subarray, Not Just the Sum

Knowing the *sum* is often not enough — many problems want the subarray
itself (or at least its start/end indices). **Idea:** track the start index
whenever you "restart," and update the recorded best start/end whenever
`best_sum` improves.

```python
def kadane_with_subarray(arr):
    current_sum = arr[0]
    best_sum = arr[0]
    current_start = 0
    best_start = best_end = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:   # restarting beats extending
            current_sum = arr[i]
            current_start = i                 # new subarray starts here
        else:
            current_sum += arr[i]              # extend the existing subarray

        if current_sum > best_sum:
            best_sum = current_sum
            best_start, best_end = current_start, i

    return best_sum, arr[best_start:best_end + 1]
```

**Trace for `arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`** (focusing on the
start-tracking, building on section 2's trace): when `i=3` (`x=4`), the
restart condition triggers (`4 > -2+4=2`), so `current_start` moves to `3`.
From there, `current_sum` grows to `6` by `i=6`, at which point
`best_start=3, best_end=6` are recorded. Final result:
`(6, arr[3:7]) = (6, [4, -1, 2, 1])` — matching the expected subarray from
section 1.

**Complexity:** still O(n) time, O(1) extra space (a few more scalar
trackers, not proportional to input size).

---

## 4. Maximum Product Subarray

**The problem:** same idea as Maximum Subarray Sum, but with **product**
instead of sum. This is meaningfully harder, for one specific reason:
**multiplying by a negative number flips the sign** — so the best product
ending at a position might come from extending the *smallest* (most
negative) running product just as easily as the *largest* one, if the
current element is negative.

**The fix:** track **both** a running maximum product AND a running minimum
product ending at each position. When you encounter a negative number, the
running min and max **swap roles** (the min, multiplied by a negative,
becomes a candidate for the new max, and vice versa).

```python
def max_product_subarray(arr):
    current_max = current_min = best = arr[0]
    for x in arr[1:]:
        if x < 0:
            current_max, current_min = current_min, current_max   # swap before combining
        current_max = max(x, current_max * x)
        current_min = min(x, current_min * x)
        best = max(best, current_max)
    return best
```

**Trace for `arr = [2, 3, -2, 4]`:**
| x | swap? | current_max candidate | current_min candidate | current_max | current_min | best |
|---|---|---|---|---|---|---|
| start | — | — | — | 2 | 2 | 2 |
| 3 | no | max(3,2*3=6)=6 | min(3,2*3=6)=3 | 6 | 3 | 6 |
| -2 | **yes**, swap(6,3)→(3,6) | max(-2,3*-2=-6)=-2 | min(-2,6*-2=-12)=-12 | -2 | -12 | 6 |
| 4 | no | max(4,-2*4=-8)=4 | min(4,-12*4=-48)=-48 | 4 | -48 | 6 |

Result: `best = 6` — matching `[2,3]` which has product `6` (the full array
`[2,3,-2,4]` has product `-48`, and other subarrays don't beat `6`). Notice
at `x=-2`, the swap is what allows `current_min` (which was tracking the
*most negative* product, `-12` after combining) to become relevant — without
the swap-before-multiply step, a subsequent positive number couldn't
"rescue" a large negative product back into a large positive one correctly.

**Complexity:** O(n) time (single pass), O(1) space. Same overall shape as
Kadane's Algorithm, but doubled state (max **and** min tracked) to handle
sign flips correctly.

---

## 5. Majority Element (> n/2 Times) — Full Moore's Voting Implementation

You met the "cancellation" intuition for this on Day 8, section 4. Here's
the complete algorithm, including the **verification pass** that makes it
robust even when a majority element isn't guaranteed to exist.

```python
def majority_element(arr):
    candidate = None
    count = 0
    for x in arr:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1

    # Verification pass: confirm `candidate` actually appears > n/2 times.
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None    # no true majority element exists
```

**Trace for `arr = [2, 2, 1, 1, 1]`** (majority is `1`, appearing 3/5 times
— matches the informal trace from Day 8):
| x | count==0? | action | candidate | count |
|---|---|---|---|---|
| 2 | yes | candidate=2, count=1 | 2 | 1 |
| 2 | no, x==candidate | count=2 | 2 | 2 |
| 1 | no, x!=candidate | count=1 | 2 | 1 |
| 1 | no, x!=candidate | count=0 | 2 | 0 |
| 1 | **yes** (count hit 0) | candidate=1, count=1 | 1 | 1 |

First phase ends with `candidate=1`. Verification: `arr.count(1) = 3`,
`len(arr)//2 = 2`, and `3 > 2` → confirmed, return `1`. Correct.

**Complexity:** the voting phase is O(n) time, O(1) space. The verification
pass (`arr.count(candidate)`) is another O(n) pass. Total: still **O(n)
time, O(1) space** — the verification pass doesn't change the complexity
class, it just adds a second linear scan. This two-phase structure (find a
*candidate* cheaply, then *verify* it) is a pattern you'll see again in other
"find the element with property X" problems.

---

## Worked Examples — Trace These Yourself First

**Example A:** In Kadane's Algorithm, why is `current_sum = max(x, current_sum + x)` correct — specifically, why is comparing against just `x` (not `0`, and not `current_sum` alone) the right thing to do?
<details><summary>Answer</summary>
`x` alone represents "start a brand new subarray right here, discarding
everything before." `current_sum + x` represents "extend the existing
running subarray by one more element." Comparing against `0` would
incorrectly allow an *empty* subarray as an option, which is wrong when
you need at least one element (and breaks all-negative-array cases, as
discussed in section 2's edge case). Comparing against `current_sum` alone
(without adding `x`) wouldn't make sense — `x` must be included in the sum
either way, since we're deciding the sum of a subarray ending exactly at
the current position.
</details>

**Example B:** In Maximum Product Subarray, why must the swap
(`current_max, current_min = current_min, current_max`) happen **before**
computing the new `current_max`/`current_min`, not after?
<details><summary>Answer</summary>
The new `current_max` is computed as `max(x, current_max * x)` — but if `x`
is negative, multiplying the *old* `current_max` (a large positive number)
by a negative `x` produces a very negative result, while multiplying the
*old* `current_min` (a very negative number) by negative `x` produces a
large positive result — the actual best candidate for the new max. Swapping
first ensures that when you then compute `current_max * x`, you're using
what *was* `current_min`, giving the correct candidate. Doing the swap after
would use the wrong (already-updated) values.
</details>

**Example C:** Why does `majority_element` need a **verification pass** at
all — couldn't you just trust the candidate returned by the voting phase?
<details><summary>Answer</summary>
The voting phase's cancellation logic only *guarantees* a correct result
when a true majority element (appearing more than n/2 times) actually
exists. If no such element exists (e.g. `[1, 2, 3, 4]`), the voting phase
still produces *some* candidate — but it's meaningless. The verification
pass (`arr.count(candidate) > len(arr) // 2`) is what distinguishes "genuine
majority found" from "no majority exists," and is only skippable if the
problem statement explicitly guarantees a majority element is present.
</details>

---

## Practice Questions

### Question 1 — Maximum Subarray Sum (Kadane's Algorithm)
**Question:** Given an array of integers, return the sum of the maximum-sum
contiguous subarray.
**Input:** `arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
**Output:** `6`
**Solution:**
```python
def kadane_max_subarray_sum(arr):
    current_sum = arr[0]
    best_sum = arr[0]
    for x in arr[1:]:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

print(kadane_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
```
At each position, either extend the running subarray or restart from the
current element, keeping whichever running sum is larger; track the best
seen throughout. Complexity: `O(n)` time, `O(1)` space (section 2).

### Question 2 — Maximum Subarray Sum, With the Subarray Itself
**Question:** Same as Question 1, but also return the actual subarray that
achieves the maximum sum.
**Input:** `arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
**Output:** `(6, [4, -1, 2, 1])`
**Solution:**
```python
def kadane_with_subarray(arr):
    current_sum = arr[0]
    best_sum = arr[0]
    current_start = 0
    best_start = best_end = 0

    for i in range(1, len(arr)):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            current_start = i
        else:
            current_sum += arr[i]

        if current_sum > best_sum:
            best_sum = current_sum
            best_start, best_end = current_start, i

    return best_sum, arr[best_start:best_end + 1]

print(kadane_with_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# (6, [4, -1, 2, 1])
```
Track the start index of the current running subarray, and snapshot the
start/end whenever `best_sum` improves. Complexity: `O(n)` time, `O(1)`
extra space (section 3).

### Question 3 — Maximum Product Subarray
**Question:** Given an array of integers, return the largest product
achievable by a contiguous subarray.
**Input:** `arr = [2, 3, -2, 4]`
**Output:** `6`
**Solution:**
```python
def max_product_subarray(arr):
    current_max = current_min = best = arr[0]
    for x in arr[1:]:
        if x < 0:
            current_max, current_min = current_min, current_max
        current_max = max(x, current_max * x)
        current_min = min(x, current_min * x)
        best = max(best, current_max)
    return best

print(max_product_subarray([2, 3, -2, 4]))   # 6
```
Track both a running max and running min product ending at each position,
swapping them before combining whenever the current element is negative (a
negative number can turn the smallest running product into the largest).
Complexity: `O(n)` time, `O(1)` space (section 4).

### Question 4 — Majority Element (Moore's Voting Algorithm)
**Question:** Given an array, return the element that appears more than
`n/2` times, or `None` if no such element exists.
**Input:** `arr = [2, 2, 1, 1, 1]`
**Output:** `1`
**Input 2:** `arr = [1, 2, 3, 4]`
**Output 2:** `None`
**Solution:**
```python
def majority_element(arr):
    candidate = None
    count = 0
    for x in arr:
        if count == 0:
            candidate = x
            count = 1
        elif x == candidate:
            count += 1
        else:
            count -= 1

    if arr.count(candidate) > len(arr) // 2:
        return candidate
    return None

print(majority_element([2, 2, 1, 1, 1]))   # 1
print(majority_element([1, 2, 3, 4]))       # None
```
A "cancellation" pass finds a candidate in O(n)/O(1); a verification pass
(`arr.count`) confirms it's genuinely a majority before returning it.
Complexity: `O(n)` time (two linear passes), `O(1)` space (section 5).

## Revision

- Quick recall (5 min): re-solve "Move all negative numbers to one side"
  from Day 8 cold.

## Key Takeaways

- **Kadane's Algorithm** maintains a running sum that either **extends** the
  current subarray or **restarts** at the current element, whichever is
  larger — `O(n)` time, `O(1)` space, and the same "running best" family of
  patterns you first saw on Day 3.
- Recovering the **actual subarray** (not just the sum) only requires
  tracking a start index alongside the running sum, with no change to time
  complexity.
- **Maximum Product Subarray** needs both a running **max and min**, because
  multiplying by a negative number can turn the smallest running product
  into the largest — a direct consequence of sign flips that sum-based
  Kadane's never has to worry about.
- **Moore's Voting Algorithm** finds a majority-element candidate via
  cancellation in `O(n)`/`O(1)`, but always needs a **verification pass**
  unless the problem guarantees a majority element exists.

---

## Additional Topics — Filling Gaps in Day 9's Scope

Kadane's Algorithm has one extremely common variant missing from today's
coverage: what happens when the array is **circular** (the subarray is
allowed to wrap around from the end back to the start)?

### 6. Maximum Sum Circular Subarray

**The problem:** given a **circular** array (the end connects back to the
start), find the maximum possible sum of a **non-empty** contiguous
subarray — where "contiguous" now also allows wrapping around the end.

**Example:** `arr = [5, -3, 5]` → the best *non-wrapping* subarray is `[5]`
or `[5,-3,5]` (sum `7`), but the best *wrapping* subarray is `[5, 5]`
(wrapping around, skipping the `-3`), summing to `10` — the wrap-around
option wins here.

**Key insight — split into two cases:**
1. **The optimal subarray does NOT wrap around.** This is exactly what
   ordinary Kadane's (section 2) already finds — call this `max_normal`.
2. **The optimal subarray DOES wrap around.** A wrapping subarray is
   equivalent to: **total array sum minus the *minimum* contiguous
   subarray sum** (the wrapped part is everything **except** some
   contiguous "gap" in the middle — and to maximize what's kept, you want
   to **minimize** what's excluded). Finding the minimum subarray sum is
   just Kadane's Algorithm run with `min`/`max` swapped throughout.

```python
def max_subarray_circular(arr):
    def kadane_max(a):
        cur = best = a[0]
        for x in a[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best

    def kadane_min(a):
        cur = best = a[0]
        for x in a[1:]:
            cur = min(x, cur + x)
            best = min(best, cur)
        return best

    total = sum(arr)
    max_normal = kadane_max(arr)
    min_sub = kadane_min(arr)
    max_wrap = total - min_sub

    # Edge case: if every element is negative, max_wrap would incorrectly
    # equal 0 (an empty "kept" region) — in that case, the non-wrapping
    # answer (the single least-negative element) is correct, and wrapping
    # must not be considered at all.
    if max_normal < 0:
        return max_normal
    return max(max_normal, max_wrap)

print(max_subarray_circular([1, -2, 3, -2]))   # 3  (no wrap needed)
print(max_subarray_circular([5, -3, 5]))        # 10 (wrap: 5 + 5, skipping -3)
print(max_subarray_circular([-3, -2, -3]))      # -2 (all negative — no wrap)
```

**Trace for `arr = [5, -3, 5]`:**
- `total = 5 + (-3) + 5 = 7`.
- `kadane_max`: `cur=5,best=5` → `x=-3`: `cur=max(-3,5-3=2)=2,best=5` →
  `x=5`: `cur=max(5,2+5=7)=7,best=7`. So `max_normal = 7`.
- `kadane_min`: `cur=5,best=5` → `x=-3`: `cur=min(-3,5-3=2)=-3,best=-3` →
  `x=5`: `cur=min(5,-3+5=2)=2,best=-3`. So `min_sub = -3`.
- `max_wrap = total - min_sub = 7 - (-3) = 10`.
- `max_normal(7) >= 0`, so return `max(7, 10) = 10`.

Result: `10`. Matches — the wrapping subarray `[5 (last), 5 (first)]` beats
any non-wrapping option.

**Why does `total - min_sub` correctly compute the best wrap-around sum?**
A wrap-around subarray keeps a "prefix" and a "suffix" of the array while
skipping some contiguous middle chunk. The sum of what's **kept** equals
`total - (sum of what's skipped)`. To maximize the kept sum, you want to
**minimize** the skipped sum — and the skipped middle chunk is itself just
some contiguous subarray, so its minimum possible sum is exactly what
`kadane_min` computes.

**Why is the `max_normal < 0` check necessary?** If every element is
negative, `min_sub` would equal `total` itself (the minimum subarray is the
*entire* array), making `max_wrap = total - min_sub = 0` — but a sum of `0`
would represent skipping the *entire* array and keeping *nothing*, which
isn't a valid non-empty subarray. In this case, the wrap-around case must be
discarded entirely, falling back to `max_normal` (the least-negative single
element), which ordinary Kadane's already handles correctly (Day 9, section
2's edge case).

**Complexity:** **O(n) time** (two Kadane's passes plus one sum, all
linear), **O(1) space** — same complexity class as ordinary Kadane's, just
combining two runs of the same underlying algorithm with one extra
arithmetic identity (`total - min_sub`).

## Additional Key Takeaways (Day 9 Supplement)

- **Maximum Sum Circular Subarray** splits into "does the optimal subarray
  wrap around or not" — the non-wrapping case is ordinary Kadane's, and the
  wrapping case reduces to `total sum - minimum subarray sum` (found via a
  min-tracking variant of Kadane's).
- The **all-negative edge case** needs special handling here too, just like
  ordinary Kadane's (Day 9, section 2) — a reminder that "run Kadane's
  twice and combine" doesn't automatically inherit correctness without
  re-checking edge cases at the combination step.
