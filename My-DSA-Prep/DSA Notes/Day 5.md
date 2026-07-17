# Day 5 — Sorting Algorithms I (Basic)

**Language: Python**

---

## 1. What Is Sorting, and Why Learn Multiple Algorithms?

**Sorting** means rearranging elements of a collection into a specific order
(usually ascending or descending). It sounds trivial — Python even gives you
`arr.sort()` for free — but sorting algorithms are one of the richest
teaching grounds in DSA because different algorithms make different
trade-offs, and recognizing those trade-offs is a skill that transfers to
almost every other topic in this plan.

Two properties you'll evaluate every sorting algorithm on:

- **Time complexity** — how the number of comparisons/swaps grows with input
  size `n`, in the best, worst, and average case.
- **In-place vs. not** — does it rearrange the existing array using O(1) extra
  space, or does it need to allocate a new array (O(n) extra space)?
- **Stability** — covered in depth in section 5, but the short version: does
  it preserve the relative order of elements that are considered "equal"?

Today covers the three simplest sorting algorithms — Selection, Bubble, and
Insertion Sort. All three are **O(n²)** in the worst case, which makes them
impractical for large inputs, but they are the essential warm-up for
understanding Day 6's `O(n log n)` algorithms (Merge Sort, Quick Sort), and
the *patterns* they use (scanning for a minimum, swapping adjacent
out-of-order pairs, inserting into an already-sorted prefix) reappear
throughout the rest of this plan.

---

## 2. Selection Sort

**Idea:** for each position in the array (starting from the front), find the
**minimum** element in the remaining unsorted portion, and swap it into that
position. Repeat for every position.

Think of it as: "find the smallest thing, put it first. Find the next
smallest, put it second. Repeat."

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):        # scan the unsorted remainder
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]   # swap into place
    return arr
```

**Trace for `arr = [5, 2, 8, 1, 9]`:**
| i | unsorted portion scanned | min found at index | arr after swap |
|---|---|---|---|
| 0 | [5,2,8,1,9] | 3 (value 1) | [1,2,8,5,9] |
| 1 | [2,8,5,9] | 1 (value 2) | [1,2,8,5,9] (already in place, "swap" with itself) |
| 2 | [8,5,9] | 3 (value 5) | [1,2,5,8,9] |
| 3 | [8,9] | 3 (value 8) | [1,2,5,8,9] (already in place) |

Result: `[1, 2, 5, 8, 9]`. Sorted correctly.

**Time complexity derivation:** the outer loop runs `n` times. For each
outer iteration `i`, the inner loop scans `n - i - 1` remaining elements
looking for the minimum. Total comparisons:
`(n-1) + (n-2) + ... + 1 + 0 = n(n-1)/2`, which is **O(n²)**.

**Crucially, this happens no matter what the input looks like** — even if
the array is already sorted, Selection Sort still scans the entire remaining
portion every single time to *confirm* the minimum, because it has no way to
know in advance that it's already sorted. This means:
- **Best case: O(n²)**
- **Worst case: O(n²)**
- **Average case: O(n²)**

Selection Sort is the rare algorithm where all three cases are identical —
its performance is completely input-independent.

**Space:** O(1) — sorts in place, only a few scalar variables used.

**Stability:** **Not stable** (in this straightforward swap-based
implementation) — swapping a found minimum into place can jump it past equal
elements, changing their relative order. See section 5 for a concrete example.

**Number of swaps:** exactly `n` swaps (at most one per outer iteration) —
notably fewer than Bubble Sort, which matters in scenarios where writes are
expensive (e.g., flash memory).

---

## 3. Bubble Sort

**Idea:** repeatedly scan through the array, comparing each pair of
**adjacent** elements, and swap them if they're out of order. Each full pass
"bubbles" the largest remaining unsorted element up to its correct position
at the end — hence the name.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):       # unsorted portion shrinks each pass
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:                      # no swaps means it's already sorted
            break
    return arr
```

**Trace for `arr = [5, 2, 8, 1]` (showing full inner passes):**

Pass 1 (`i=0`, `j` from 0 to 2):
- `j=0`: `5 > 2`? yes, swap → `[2,5,8,1]`
- `j=1`: `5 > 8`? no
- `j=2`: `8 > 1`? yes, swap → `[2,5,1,8]`
- `swapped=True`, continue

Pass 2 (`i=1`, `j` from 0 to 1):
- `j=0`: `2 > 5`? no
- `j=1`: `5 > 1`? yes, swap → `[2,1,5,8]`
- `swapped=True`, continue

Pass 3 (`i=2`, `j` from 0 to 0):
- `j=0`: `2 > 1`? yes, swap → `[1,2,5,8]`
- `swapped=True`, continue

Pass 4 (`i=3`, `j` range is empty): no comparisons, `swapped` stays `False`
→ loop breaks early.

Result: `[1, 2, 5, 8]`. Sorted correctly. Notice `8`, the largest element,
reached its final position after just the first pass — that's the "bubbling
up" behavior.

**Time complexity derivation:**
- **Worst case (reverse-sorted input): O(n²).** Every pass makes the maximum
  number of swaps, and you need roughly `n` passes each doing up to `n`
  comparisons — `n(n-1)/2` comparisons total, same shape as Selection Sort.
- **Best case (already-sorted input): O(n)**, *because of the `swapped`
  flag optimization*. On an already-sorted array, the very first pass makes
  zero swaps, so `swapped` stays `False`, and the loop breaks immediately
  after just one O(n) pass. **This early-exit optimization is what
  distinguishes a "good" Bubble Sort implementation from a naive one** — the
  naive version (without the `swapped` check) is always O(n²) regardless of
  input.
- **Average case: O(n²)** — a randomly ordered array won't trigger the
  early exit until many passes have run.

**Space:** O(1) — sorts in place.

**Stability:** **Stable.** Bubble Sort only swaps *adjacent* elements, and
only when the left one is strictly greater than the right one (`>`, not
`>=`). Two equal elements are never swapped past each other, so their
original relative order is always preserved.

---

## 4. Insertion Sort

**Idea:** the same way you might sort a hand of playing cards — go through
the array one element at a time, and insert each new element into its
correct position within the already-sorted portion built so far (to its
left).

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]              # the element we're inserting
        j = i - 1
        while j >= 0 and arr[j] > key:   # shift larger elements right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key            # insert key into its correct spot
    return arr
```

**Trace for `arr = [5, 2, 8, 1]`:**

`i=1`, `key=2`: compare to `arr[0]=5`. `5 > 2`, shift `5` right →
`[5,5,8,1]`, `j=-1`, loop stops (out of bounds). Insert `key=2` at `j+1=0`
→ `[2,5,8,1]`.

`i=2`, `key=8`: compare to `arr[1]=5`. `5 > 8`? No. Loop doesn't run. Insert
`key=8` at `j+1=2` (no shift needed) → `[2,5,8,1]`.

`i=3`, `key=1`: compare to `arr[2]=8`. `8 > 1`, shift → `[2,5,8,8]`. Compare
to `arr[1]=5`. `5 > 1`, shift → `[2,5,5,8]`. Compare to `arr[0]=2`. `2 > 1`,
shift → `[2,2,5,8]`. `j=-1`, loop stops. Insert `key=1` at `j+1=0` →
`[1,2,5,8]`.

Result: `[1, 2, 5, 8]`. Sorted correctly.

**Time complexity derivation:**
- **Worst case (reverse-sorted input): O(n²).** Every new element must be
  compared against, and shifted past, *every* element already in the sorted
  portion — same `n(n-1)/2` shape as before.
- **Best case (already-sorted input): O(n).** For each `i`, the `while`
  condition `arr[j] > key` is `False` on the very first check (since
  everything to the left is already ≤ `key`), so the inner loop never runs.
  Just `n-1` cheap checks total.
- **Average case: O(n²).**

**Space:** O(1) — sorts in place.

**Stability:** **Stable.** The `while` condition uses strict `>`, so an
element equal to `key` is never shifted past it — `key` is inserted
immediately after any equal elements already placed, preserving original
relative order.

**Why Insertion Sort matters beyond today:** it's the algorithm real-world
systems often fall back to for **small subarrays** even inside more advanced
sort implementations (e.g., some hybrid sorts switch to insertion sort once
a partition shrinks below ~10-20 elements), because its low overhead makes
it genuinely faster than "smarter" algorithms at small scale, despite the
worse Big-O. Big-O describes *growth rate*, not "always faster" — a useful
reminder for interviews.

---

## 5. Stability — What It Means and Why It Matters

A sorting algorithm is **stable** if, whenever two elements are considered
"equal" by the sort key, their **original relative order is preserved** in
the output.

This matters whenever you're sorting by one key but the elements have other
data attached. Classic example: sort a list of students by grade, but you
also want students with the same grade to stay in their original
(e.g., alphabetical, or enrollment) order.

**Concrete illustration:**
```python
students = [("Alice", 90), ("Bob", 85), ("Carol", 90), ("Dave", 85)]
# Sort by grade (the second element).
```
If the sort is **stable**, sorting by grade gives:
`[("Bob", 85), ("Dave", 85), ("Alice", 90), ("Carol", 90)]`
— notice `Bob` still comes before `Dave` (their original relative order,
both having grade 85, is preserved), and `Alice` still comes before `Carol`.

If the sort is **unstable**, you might instead get:
`[("Dave", 85), ("Bob", 85), ("Carol", 90), ("Alice", 90)]`
— same grades grouped correctly, but their *internal* order among themselves
is no longer guaranteed to match the input.

**Why does Selection Sort lose stability?** Its swap can jump an element far
across the array, past other elements — including ones equal to it — without
regard for their relative order. Concrete counterexample: take
`[4a, 4b, 1]`, where `4a` and `4b` are two equal-valued elements (subscripts
just track their original identity so we can watch what happens to their
order).
- `i=0`: scan `[4a, 4b, 1]` for the minimum → `1` at index 2. Swap indices 0
  and 2 → `[1, 4b, 4a]`.
- `i=1`: scan `[4b, 4a]` for the minimum → both equal, and since the scan
  uses strict `<`, the first one found (`4b` at index 1) stays as
  `min_index`. Swap index 1 with itself (no change) → `[1, 4b, 4a]`.

Final result: `[1, 4b, 4a]`. But in the original array, `4a` appeared
**before** `4b` — after sorting, their relative order has **flipped** to
`4b` before `4a`. That single swap in the first pass (jumping `1` from index
2 all the way to index 0) dragged `4a` along with it, past `4b`. This is a
concrete violation of stability, which is why Selection Sort is classified
as **not stable**.

**Practical takeaway:** if you ever need to preserve secondary ordering,
either use a stable sort (Bubble, Insertion, and — spoiler for tomorrow —
Merge Sort are all stable) or explicitly sort by a composite key (e.g.,
`(grade, original_index)`) so ties are broken deterministically regardless
of the underlying algorithm's stability.

---

## 6. Optimized Bubble Sort — Shrinking the Range With Last-Swap Tracking

The `swapped` flag (section 3) only tells you *whether* to stop entirely.
A further optimization tells you *how far* the unsorted portion still
extends, so later passes can skip comparisons that are already guaranteed
sorted.

**Idea:** every element **after** the last swap made in a pass is already in
its final position (nothing after it moved, so nothing after it is
out of order). Track the index of the last swap, and next pass only scan up
to there.

```python
def bubble_sort_optimized(arr):
    n = len(arr)
    right = n - 1               # everything beyond `right` is confirmed sorted
    while right > 0:
        last_swap_index = 0
        for j in range(right):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last_swap_index = j       # remember where the last swap happened
        right = last_swap_index           # next pass only needs to go this far
    return arr
```

**Trace for `arr = [2, 1, 3, 4, 9, 8]`:**
```
Pass 1 (right=5): swaps at j=0 (2>1) and j=4 (9>8)
  → [1, 2, 3, 4, 8, 9], last_swap_index = 4
  right becomes 4

Pass 2 (right=4): compare j=0..3 → [1,2,3,4] already in order, no swaps
  last_swap_index stays 0 → right becomes 0 → loop ends
```
Compare this to the plain `swapped`-flag version, which would still run a
*second full pass* over indices 0–3 before confirming nothing changed. The
optimized version shrinks the scan range every pass instead of only
detecting "fully done." Worst-case complexity is unchanged (**O(n²)**), but
on partially-sorted input — especially input that's sorted at the *front*
with disorder concentrated near the end — this variant does meaningfully
fewer comparisons in practice.

---

## 7. Binary Insertion Sort — Fewer Comparisons, Same Shifts

Plain Insertion Sort (section 4) finds where `key` belongs by **scanning
linearly** backward through the sorted prefix (`while j >= 0 and arr[j] >
key`). But the sorted prefix is, by definition, already sorted — so you can
find the correct insertion point with **binary search** instead, cutting the
number of *comparisons* from O(n) down to O(log n) per element.

```python
def binary_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        # Binary search for the correct insertion index within arr[0..i-1]
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        insert_at = left                # binary search converges here

        # Still need to physically shift elements right to make room
        for j in range(i - 1, insert_at - 1, -1):
            arr[j + 1] = arr[j]
        arr[insert_at] = key
    return arr

print(binary_insertion_sort([5, 2, 8, 1]))   # [1, 2, 5, 8]
```

**Important subtlety:** this reduces *comparisons* to **O(n log n)** total,
but the **shifting** of elements to make room still has to touch every
element it passes, so **shifts remain O(n²)** in the worst case — meaning
**overall time complexity is still O(n²)**, just with a smaller constant
from cheaper comparisons. This is a common trap: optimizing one part of an
algorithm (comparisons) doesn't automatically change its Big-O if a
different part (shifting/array-writes) is still the bottleneck. Binary
Insertion Sort is still **stable**, provided the binary search uses `>`
(not `>=`) exactly like plain Insertion Sort, for the same reason as
section 4.

---

## 8. Sorting With Custom Keys — Descending Order and Non-Numeric Data

Every algorithm today compares elements with `>`. In real code you rarely
sort raw numbers — you sort **objects by some property**, or you want
**descending** instead of ascending order. Both are the same underlying
algorithm with one line changed.

**Descending order** — flip the comparison direction:
```python
def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:      # flipped: < instead of >
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort_desc([5, 2, 8, 1]))   # [8, 5, 2, 1]
```

**Sorting by a key function** — compare a derived value instead of the
element itself, e.g. sorting `(name, score)` tuples by `score`:
```python
def insertion_sort_by_key(arr, key_func):
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        key_value = key_func(key_item)
        j = i - 1
        while j >= 0 and key_func(arr[j]) > key_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

students = [("Alice", 85), ("Bob", 92), ("Carol", 85)]
print(insertion_sort_by_key(students, key_func=lambda s: s[1]))
# [('Alice', 85), ('Carol', 85), ('Bob', 92)]
```
Notice `("Alice", 85)` stays before `("Carol", 85)` — because the `while`
condition still uses strict `>`, this preserves **stability** even when
sorting by a derived key rather than the raw value, exactly as discussed in
section 5. This pattern — comparing `key_func(x)` instead of `x` directly —
is how you'll sort custom objects for the rest of this course, and it's
worth internalizing now rather than re-deriving it each time.

---

## 9. Choosing Between Selection, Bubble, and Insertion Sort

All three share the same worst-case Big-O, so "which is fastest" depends
entirely on context:

| Situation | Best choice | Why |
|---|---|---|
| Writes/swaps are expensive (e.g. flash memory, large records) | **Selection Sort** | Guarantees only `O(n)` swaps total — far fewer than Bubble or Insertion |
| Data is already mostly sorted | **Insertion Sort** or **Bubble Sort** | Both hit `O(n)` best case; Insertion is generally preferred in practice (see below) |
| Small array (roughly n < 20) | **Insertion Sort** | Low constant-factor overhead beats "smarter" `O(n log n)` algorithms at small scale — real hybrid sorts (Day 6 preview) fall back to it for exactly this reason |
| You need stability and don't know input order | **Insertion Sort** or **Bubble Sort** | Both stable; Selection Sort is not |
| Teaching / simplest to reason about | **Selection Sort** | Fewest moving parts, input-independent behavior is easy to predict |
| Large, unpredictable, real-world data | **None of these** | All three degrade to `O(n²)` — this is exactly the motivation for Day 6's `O(n log n)` Merge Sort and Quick Sort |

**Why Insertion Sort usually wins among these three in practice:** it
combines Bubble Sort's adaptiveness (fast on nearly-sorted data) with fewer
total operations on average, since each element only shifts as far as it
needs to — it doesn't require a full extra pass just to confirm "no swaps
happened" the way Bubble Sort's `swapped` flag does. This is also why it's
the one real hybrid sorting algorithms (like Timsort, which Python's
`sort()` uses internally) fall back to for small subarrays.

---

## Comparison Table — Build This From Memory by End of Day

| Algorithm | Best | Worst | Average | Space | Stable? |
|---|---|---|---|---|---|
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Bubble Sort | O(n) (with early-exit) | O(n²) | O(n²) | O(1) | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |

**One-line intuition for each, to help you recall the mechanism instantly:**
- **Selection Sort:** repeatedly find the min, swap it into place.
- **Bubble Sort:** repeatedly swap adjacent out-of-order neighbors.
- **Insertion Sort:** repeatedly insert the next element into its correct
  spot in the sorted prefix.

---

## Worked Examples — Trace These Yourself First

**Example A:** Why is Selection Sort's best case still O(n²), while Bubble
Sort and Insertion Sort both achieve O(n) on an already-sorted array?
<details><summary>Answer</summary>
Bubble Sort and Insertion Sort can both **detect** that no more work is
needed and stop early — Bubble Sort via the `swapped` flag (no swaps in a
full pass means done), Insertion Sort via the `while` loop condition failing
immediately (nothing to its left is greater, so no shifting happens).
Selection Sort has no such detection mechanism: its inner loop unconditionally
scans the *entire* remaining unsorted portion every single time to find the
minimum, regardless of whether the array is already sorted — it has no way
to "notice" and stop early.
</details>

**Example B:** Why does Insertion Sort's inner `while` loop use `arr[j] > key`
(strict greater-than) rather than `arr[j] >= key`? What would break if you
used `>=` instead?
<details><summary>Answer</summary>
Using strict `>` means an element *equal* to `key` is never shifted past it
— the loop stops as soon as it finds an element ≤ `key`, so `key` is inserted
right after any equal elements, preserving their original relative order
(this is exactly what makes Insertion Sort stable). Using `>=` instead would
shift equal elements out of the way too, meaning `key` could end up inserted
*before* an equal element that appeared earlier in the original array —
breaking stability, even though the final sorted values would still be
numerically correct.
</details>

**Example C:** For an array of `n = 1000` elements that's already sorted,
roughly how many comparisons will Bubble Sort perform (with the `swapped`
optimization), and how many will Selection Sort perform?
<details><summary>Answer</summary>
Bubble Sort: one full pass of `n-1 = 999` comparisons, all resulting in no
swaps, so `swapped` stays `False` and it exits after that single pass — about
999 comparisons total, i.e. O(n). Selection Sort: it always does the full
`n(n-1)/2 = 1000*999/2 = 499,500` comparisons regardless of input order — the
sorted-ness of the input is completely invisible to it. This ~500x
difference in comparison count on this specific input is a vivid illustration
of "same Big-O worst case, very different real-world behavior on easy
inputs."
</details>

**Example D:** In Binary Insertion Sort (section 7), why is the overall time
complexity still O(n²) even though comparisons are reduced to O(n log n)?
<details><summary>Answer</summary>
Binary search only speeds up the process of *finding* where `key` belongs —
it doesn't speed up the physical work of *shifting* every element between
the old and new positions to make room. In the worst case (e.g.
reverse-sorted input), each insertion still shifts up to `i` elements, and
summed over all `i` that's still `n(n-1)/2` shifts — `O(n²)`. The overall
complexity is dominated by whichever operation is more expensive, and since
shifting didn't improve, the Big-O doesn't improve either — only the
constant factor on comparisons does.
</details>

**Example E:** You need to sort a list of `(username, last_login_days_ago)`
tuples so that the most recently active users come first, and users with
the exact same `last_login_days_ago` should keep their original relative
order. Which algorithm(s) from today are safe to use, and what would you
sort by?
<details><summary>Answer</summary>
Bubble Sort or Insertion Sort — both stable — using a key function
`key_func=lambda u: u[1]` (ascending, since fewer days ago means more
recent) as shown in section 8. Selection Sort must be avoided here because
it isn't stable: two users with the same `last_login_days_ago` could have
their original order swapped, which would silently corrupt whatever
tie-breaking order they started in (e.g. alphabetical or signup order).
</details>

---

## Practice Questions

### Question 1 — Implement Selection Sort
**Question:** Given an array, sort it in ascending order using Selection Sort.
**Input:** `arr = [5, 2, 8, 1, 9]`
**Output:** `[1, 2, 5, 8, 9]`
**Solution:**
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([5, 2, 8, 1, 9]))   # [1, 2, 5, 8, 9]
```
For each position, scan the remaining unsorted portion for the minimum and
swap it into place. Complexity: `O(n²)` time in all cases (best, worst,
average), `O(1)` space, **not stable** (section 2).

### Question 2 — Implement Bubble Sort
**Question:** Given an array, sort it in ascending order using Bubble Sort,
with an early-exit optimization for already-sorted input.
**Input:** `arr = [5, 2, 8, 1]`
**Output:** `[1, 2, 5, 8]`
**Solution:**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort([5, 2, 8, 1]))   # [1, 2, 5, 8]
```
Repeatedly swap adjacent out-of-order pairs; each pass pushes the current
largest remaining element to its final position. Complexity: `O(n)` best
case (already sorted, thanks to the `swapped` flag), `O(n²)` worst/average,
`O(1)` space, **stable** (section 3).

### Question 3 — Implement Insertion Sort
**Question:** Given an array, sort it in ascending order using Insertion Sort.
**Input:** `arr = [5, 2, 8, 1]`
**Output:** `[1, 2, 5, 8]`
**Solution:**
```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([5, 2, 8, 1]))   # [1, 2, 5, 8]
```
Build up a sorted prefix one element at a time, shifting larger elements
right to make room for each newly inserted value. Complexity: `O(n)` best
case (already sorted), `O(n²)` worst/average, `O(1)` space, **stable**
(section 4).

### Question 4 — State Complexity and Stability From Memory
**Question:** Without looking anything up, state the best/worst/average time
complexity, space complexity, and stability for Selection Sort, Bubble Sort,
and Insertion Sort.
**Input:** N/A (recall exercise).
**Output:** The comparison table from the "Comparison Table" section above.
**Solution:** See the table above — the key facts to internalize: Selection
Sort is O(n²) in *every* case with no way to detect an easy input and is not
stable; Bubble Sort and Insertion Sort both achieve O(n) best case via
early-exit mechanisms and are both stable; all three are O(1) space (sort
in-place) and O(n²) in the worst/average case.

### Question 5 — Optimized Bubble Sort With Range Shrinking
**Question:** Implement Bubble Sort so that each pass only scans up to the
index of the last swap made in the previous pass (not just an early-exit
flag).
**Input:** `arr = [2, 1, 3, 4, 9, 8]`
**Output:** `[1, 2, 3, 4, 8, 9]`
**Solution:**
```python
def bubble_sort_optimized(arr):
    n = len(arr)
    right = n - 1
    while right > 0:
        last_swap_index = 0
        for j in range(right):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last_swap_index = j
        right = last_swap_index
    return arr

print(bubble_sort_optimized([2, 1, 3, 4, 9, 8]))   # [1, 2, 3, 4, 8, 9]
```
Everything after the last swap in a pass is already correctly placed, so
the next pass never needs to re-scan it. Worst case is still `O(n²)`, but
this does noticeably fewer comparisons than the plain `swapped`-flag version
on inputs sorted at the front (section 6).

### Question 6 — Sort Tuples by a Key, Descending, Preserving Stability
**Question:** Given a list of `(name, score)` tuples, sort by `score` in
**descending** order, keeping equal-score entries in their original
relative order.
**Input:** `arr = [("Alice", 85), ("Bob", 92), ("Carol", 85)]`
**Output:** `[("Bob", 92), ("Alice", 85), ("Carol", 85)]`
**Solution:**
```python
def insertion_sort_by_key_desc(arr, key_func):
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        key_value = key_func(key_item)
        j = i - 1
        while j >= 0 and key_func(arr[j]) < key_value:   # flipped for descending
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

students = [("Alice", 85), ("Bob", 92), ("Carol", 85)]
print(insertion_sort_by_key_desc(students, key_func=lambda s: s[1]))
# [('Bob', 92), ('Alice', 85), ('Carol', 85)]
```
Combines section 8's key-function pattern with the flipped comparison for
descending order; `Alice` still precedes `Carol` because the `while`
condition remains strict (`<`, not `<=`), preserving stability.

### Question 7 — Pick the Right Algorithm
**Question:** For each scenario, name which of today's three sorts (or
"none, wait for Day 6") is the best fit, and give a one-sentence reason.
1. Sorting 15 log entries that arrive nearly in chronological order already.
2. Sorting 2 million random records where every swap writes to slow storage.
3. Sorting 100,000 completely random integers.
**Input:** N/A (reasoning exercise).
**Solution:**
1. **Insertion Sort** — small, nearly-sorted input is exactly its best
   case, `O(n)`, with minimal overhead (section 9).
2. **Selection Sort** — its `O(n)` guaranteed swap count minimizes
   expensive writes, even though comparisons stay `O(n²)` (section 2, 9).
3. **None of today's three** — at this scale `O(n²)` is impractical; use
   Day 6's `O(n log n)` Merge Sort or Quick Sort instead (section 9).

## Revision

- Quick recall (5 min): re-solve one recursion problem from Day 4 (e.g.
  Factorial or Sum of Digits) cold, without looking at your notes.

## Key Takeaways

- **Selection Sort** always scans the full remaining unsorted portion to
  find the minimum — its O(n²) behavior is **input-independent**, and it is
  **not stable**. Its saving grace is a guaranteed **O(n) swap count**,
  useful when writes are expensive (section 2, 9).
- **Bubble Sort** repeatedly swaps adjacent out-of-order pairs; a `swapped`
  flag lets it detect an already-sorted array and exit early in O(n). It is
  **stable**. A further optimization tracks the **last swap index** to
  shrink the scan range every pass, doing less work on partially-sorted
  input without changing the worst-case Big-O (section 6).
- **Insertion Sort** builds up a sorted prefix, inserting each new element
  into its correct spot; it also achieves O(n) on already-sorted input, and
  is **stable**. Using **binary search** to locate the insertion point
  (Binary Insertion Sort) cuts comparisons to O(n log n), but the overall
  complexity stays O(n²) because shifting elements is still the bottleneck
  (section 7) — a reminder that optimizing one part of an algorithm doesn't
  always change its Big-O.
- All three are **O(1) space** (in-place) and degrade to **O(n²)** in the
  worst and average case — they don't scale well, which motivates Day 6's
  O(n log n) algorithms.
- **Stability** matters whenever "equal" elements carry other data you want
  to preserve the relative order of — Bubble and Insertion Sort guarantee
  it via their use of **strict** comparisons (`>`, never `>=`); Selection
  Sort's swap-based relocation does not guarantee it. The same
  strict-comparison rule extends naturally to sorting by a **key
  function** or in **descending order** (section 8).
- **Choosing an algorithm is context-dependent**, not just about Big-O:
  expensive writes favor Selection Sort, nearly-sorted or small input favors
  Insertion Sort, and large unpredictable input favors neither — that's
  exactly what motivates Day 6 (section 9).
