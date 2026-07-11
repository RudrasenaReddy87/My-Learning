

## Day 3 — Arrays: Basic Operations

### What is an Array?

An **array** is a collection of elements of the same type, stored in **contiguous (back-to-back) memory locations**, and accessed using an **index**.

Think of it like a row of numbered lockers in a hallway — locker `0`, locker `1`, locker `2`, etc. Because the lockers are side-by-side with no gaps and the same size, if you know the locker number, you can walk directly to it without checking every locker before it.

```
Index:    0     1     2     3     4
Array:  [ 10 ]  20   30    40    50
Memory: 1000  1004  1008  1012  1016   (assuming each int takes 4 bytes)
```

### How Arrays Are Stored in Memory

- All elements sit in **one continuous block** of memory.
- The array variable really just stores the **base address** (address of index 0).
- To find any element, the computer calculates its address using a simple formula:

```
address(index i) = base_address + (i × size_of_each_element)
```

For the array above (base address 1000, each int = 4 bytes), to find index `3`:
```
address(3) = 1000 + (3 × 4) = 1012   ✅ matches the diagram
```

Because this is just **one multiplication and one addition** — a fixed amount of work no matter how big the array is — **accessing any element by index is O(1)** (constant time). This is the single most important property of arrays.

### Why not O(1) for everything?
Access is O(1) because of the direct-address-calculation trick above. But **insertion** and **deletion** are a different story — because contiguous memory means there are no "gaps" to insert into; shifting is required. Let's go through each operation.

### Static Arrays vs Dynamic Arrays

This is a distinction almost every DSA course skips early on, but it matters a lot once you start reasoning about complexity properly.

**Static array** — a fixed size decided at creation time. In languages like C/C++/Java, you must declare the size upfront (`int arr[5]`), and it can never grow or shrink. If it's full, you cannot add a 6th element — period.

**Dynamic array** — resizes itself automatically as elements are added. Python's built-in `list`, Java's `ArrayList`, and C++'s `std::vector` are all dynamic arrays.

**How does a dynamic array "grow" if arrays need contiguous memory?**
It doesn't actually grow the existing block — it can't, because the memory right after it might already be used by something else. Instead, under the hood, when it runs out of room:
1. A **new, bigger block** of memory is allocated (typically **double** the old size).
2. Every existing element is **copied** into the new block — `O(n)` work.
3. The old block is freed, and the new one is used going forward.

```python
import sys
arr = []
for i in range(10):
    print(f"length={len(arr)}, size in bytes={sys.getsizeof(arr)}")
    arr.append(i)
```
Running this shows the allocated size jumps in chunks, not one-by-one — proof that Python is over-allocating space ahead of time rather than resizing on every single append.

**Why is `.append()` still called O(1) if resizing is O(n)?**
Because resizing only happens occasionally (when the buffer is full), not on every append. If you average the cost over many appends, the occasional expensive `O(n)` resize gets "spread out" across all the cheap `O(1)` appends before it. This averaging is called **amortized time complexity**, and the amortized cost of `.append()` works out to **O(1)**.

| | Static Array | Dynamic Array |
|---|---|---|
| Size | Fixed at creation | Grows/shrinks automatically |
| Examples | C arrays, Java arrays (`int[]`) | Python `list`, Java `ArrayList`, C++ `vector` |
| Append at end | O(1), but fails if full | O(1) amortized (may trigger O(n) resize occasionally) |
| Memory usage | Exactly what's needed | Slightly more (over-allocated for future growth) |

### A Note on Indexing

- Valid indices for an array of length `n` are `0` to `n-1`. Accessing `arr[n]` or beyond raises an **`IndexError`** (out of bounds) — a very common bug source.
- Python allows **negative indexing**: `arr[-1]` is the last element, `arr[-2]` the second-last, and so on. This is a Python convenience, not a general array concept — most languages (C, Java) don't support it.
```python
arr = [10, 20, 30, 40, 50]
print(arr[-1])     # 50 (last element)
print(arr[-2])       # 40 (second-last element)
print(arr[5])          # IndexError: list index out of range
```

---

### 1. Traversal — Visiting Every Element

**Definition:** Going through each element of the array one by one, usually to read, print, or process it.

```python
arr = [10, 20, 30, 40, 50]

# Traverse using index
for i in range(len(arr)):
    print(arr[i])

# Traverse using direct iteration (Pythonic way)
for value in arr:
    print(value)
```

**Time Complexity:** `O(n)` — you must visit all `n` elements at least once.
**Space Complexity:** `O(1)` — no extra space used (besides the loop variable).

---

### 2. Insertion — Adding an Element

There are two cases: inserting **at the end**, and inserting **at a specific index**.

#### a) Insertion at the end (if there's space)
```python
arr = [10, 20, 30, 40, 50]
arr.append(60)     # arr is now [10, 20, 30, 40, 50, 60]
```
**Time Complexity:** `O(1)` on average (Python lists over-allocate space, so most appends don't need to resize). In a *fixed-size* array (like in C), this is also `O(1)` **if space already exists** at the end.

#### b) Insertion at a specific index (the important one)
To insert a value at index `i`, every element from index `i` onward must be **shifted one position to the right** first, to make room.

```python
def insert_at_index(arr, index, value):
    arr.append(None)                       # make room for one more element
    for i in range(len(arr) - 1, index, -1):  # shift elements right, from the end backward
        arr[i] = arr[i - 1]
    arr[index] = value                       # place the new value
    return arr

arr = [10, 20, 30, 40, 50]
print(insert_at_index(arr, 2, 99))   # [10, 20, 99, 30, 40, 50]
```

**Why shift from the END backward, not the front forward?**
If you shift from the front, you'd overwrite values before copying them. Shifting from the back preserves each value before it gets overwritten.

**Time Complexity:**
- Best case (insert at the end): `O(1)`
- Worst case (insert at the beginning, index 0): `O(n)` — every single element must shift
- Average case: `O(n)`

**Space Complexity:** `O(1)` extra space (shifting happens in-place; Python's `.append` may internally reallocate, but conceptually it's in-place).

---

### 3. Deletion — Removing an Element

Similarly, deleting from a specific index requires shifting all elements **after** it one position to the **left**, to close the gap.

```python
def delete_at_index(arr, index):
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]      # shift elements left
    arr.pop()                       # remove the last (now duplicate) element
    return arr

arr = [10, 20, 30, 40, 50]
print(delete_at_index(arr, 1))   # [10, 30, 40, 50]
```

**Time Complexity:**
- Best case (delete the last element): `O(1)`
- Worst case (delete the first element, index 0): `O(n)` — everything shifts left
- Average case: `O(n)`

**Space Complexity:** `O(1)` extra space.

### Quick Recap Table

| Operation | Best Case | Worst Case | Why |
|---|---|---|---|
| Access by index | O(1) | O(1) | Direct address calculation |
| Traversal | O(n) | O(n) | Must visit every element |
| Insert at end | O(1) | O(1)* | No shifting needed |
| Insert at beginning/middle | O(n) | O(n) | Must shift elements right |
| Delete at end | O(1) | O(1) | No shifting needed |
| Delete at beginning/middle | O(n) | O(n) | Must shift elements left |

*In a dynamic array like Python's list, occasional resizing can make a single append O(n), but this happens rarely enough that the **amortized** cost is still O(1).

---

### Searching for an Element (Linear Search)

**Definition:** Check each element one by one until you find the target (or reach the end).

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i          # found it — return the index
    return -1                    # not found

arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print(linear_search(arr, 41))    # 3
print(linear_search(arr, 100))     # -1 (not present)
```

**Time Complexity:**
- Best case (target is the first element): `O(1)`
- Worst case (target is the last element, or not present at all): `O(n)` — must check every element

**Space Complexity:** `O(1)`.

> **Why not binary search here?** Binary search (`O(log n)`) only works on a **sorted** array. Since a general array has no guaranteed order, linear search is the only option unless you sort first (which itself costs `O(n log n)`) or already know it's sorted. Binary search is its own topic for a later day.

---

### 4. Find the Largest and Smallest Element

**Definition:** Scan through the array once, keeping track of the biggest/smallest value seen so far.

```python
def find_largest(arr):
    largest = arr[0]                # assume first element is the largest to start
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]         # update whenever we find something bigger
    return largest

def find_smallest(arr):
    smallest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print(find_largest(arr))    # 45
print(find_smallest(arr))    # 2
```

**Time Complexity:** `O(n)` — one full pass through the array, comparing each element once.
**Space Complexity:** `O(1)` — only one extra variable used.

> Python also has built-in `max(arr)` and `min(arr)` which do exactly this internally — but understanding the manual version is important for interviews.

---

### 5. Find the Second Largest and Second Smallest Element

**Naive approach:** Sort the array, then pick the second-from-last / second element. This works but costs `O(n log n)` because of the sort — we can do better.

**Optimal approach — single pass, O(n):** Track the largest AND second largest at the same time as you scan.

```python
def second_largest(arr):
    first = second = float('-inf')     # start with negative infinity
    for num in arr:
        if num > first:
            second = first               # old largest becomes second largest
            first = num                    # new largest found
        elif num > second and num != first:
            second = num                     # found a new second largest
    return second

arr = [12, 45, 2, 41, 31, 10, 8, 6, 4]
print(second_largest(arr))    # 41
```

**Logic walkthrough:**
- We keep two trackers: `first` (largest so far) and `second` (second largest so far).
- For every number: if it beats `first`, the OLD `first` gets demoted to `second`, and the new number becomes `first`.
- Else if it beats `second` (but isn't equal to `first`, to avoid counting duplicates), it becomes the new `second`.

Second smallest works the same way, just flip the comparisons:
```python
def second_smallest(arr):
    first = second = float('inf')
    for num in arr:
        if num < first:
            second = first
            first = num
        elif num < second and num != first:
            second = num
    return second

print(second_smallest(arr))    # 4
```

**Time Complexity:** `O(n)` — single pass, much better than sorting's `O(n log n)`.
**Space Complexity:** `O(1)`.

---

### 6. Check if an Array is Sorted

**Definition:** Verify whether every element is `≤` (or `≥`) the one after it, in one pass.

```python
def is_sorted_ascending(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:      # if any element is bigger than the next one, not sorted
            return False
    return True

print(is_sorted_ascending([1, 2, 3, 4, 5]))   # True
print(is_sorted_ascending([1, 3, 2, 4, 5]))    # False
```

**Time Complexity:** `O(n)` — checks each adjacent pair once. **Best case can short-circuit early** (returns False the moment it finds a violation), but worst case (already sorted) still checks all `n-1` pairs.
**Space Complexity:** `O(1)`.

---

### 7. Reverse an Array In-Place

**Definition:** Flip the order of elements WITHOUT using a second array — using only `O(1)` extra space.

**Two-pointer technique:** Use one pointer starting at the beginning (`left`) and one at the end (`right`). Swap them, then move both pointers toward the middle, until they meet.

```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]    # swap
        left += 1
        right -= 1
    return arr

arr = [10, 20, 30, 40, 50]
print(reverse_array(arr))    # [50, 40, 30, 20, 10]
```

**Visual walkthrough:**
```
[10, 20, 30, 40, 50]
  L               R      → swap 10,50 → [50, 20, 30, 40, 10]
      L       R          → swap 20,40 → [50, 40, 30, 20, 10]
          LR             → left meets right, stop
```

**Time Complexity:** `O(n)` — technically `O(n/2)` swaps, but constants are dropped, so it's `O(n)`.
**Space Complexity:** `O(1)` — swapping happens in the same array, no extra array created.

---

### 8. Left Rotate an Array by One Position

**Definition:** Shift every element one step to the left; the first element wraps around to become the last.

```
Before: [10, 20, 30, 40, 50]
After:  [20, 30, 40, 50, 10]
```

```python
def left_rotate_by_one(arr):
    first = arr[0]                      # save the first element
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]               # shift every element one step left
    arr[-1] = first                         # place the saved first element at the end
    return arr

arr = [10, 20, 30, 40, 50]
print(left_rotate_by_one(arr))    # [20, 30, 40, 50, 10]
```

**Time Complexity:** `O(n)` — every element is shifted once.
**Space Complexity:** `O(1)` — only one extra variable (`first`) used.

---

### 9. Left Rotate an Array by D Places

Now we need to rotate left by `D` positions instead of just 1.

```
Before (D=2): [10, 20, 30, 40, 50]
After:        [30, 40, 50, 10, 20]
```

#### Brute Force Approach — repeat "rotate by 1", D times
```python
def left_rotate_brute(arr, d):
    n = len(arr)
    d = d % n                        # handle d larger than array length
    for _ in range(d):
        left_rotate_by_one(arr)        # reuse the rotate-by-1 function, D times
    return arr

arr = [10, 20, 30, 40, 50]
print(left_rotate_brute(arr, 2))    # [30, 40, 50, 10, 20]
```
**Time Complexity:** `O(n × d)` — because we do a full `O(n)` shift, `d` times. If `d` is close to `n`, this becomes `O(n²)` — too slow for large arrays.
**Space Complexity:** `O(1)`.

#### Optimal Approach — The Reversal Trick (O(n), single pass style)

**Key insight:** Rotating an array left by `D` places is the same as:
1. Reverse the first `D` elements.
2. Reverse the remaining `n - D` elements.
3. Reverse the WHOLE array.

```python
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate_optimal(arr, d):
    n = len(arr)
    d = d % n                    # handle d larger than array length
    reverse(arr, 0, d - 1)         # step 1: reverse first d elements
    reverse(arr, d, n - 1)           # step 2: reverse remaining elements
    reverse(arr, 0, n - 1)              # step 3: reverse the whole array
    return arr

arr = [10, 20, 30, 40, 50]
print(left_rotate_optimal(arr, 2))    # [30, 40, 50, 10, 20]
```

**Visual walkthrough for D=2:**
```
Original:                [10, 20, 30, 40, 50]
Step 1 (reverse [0..1]):  [20, 10, 30, 40, 50]
Step 2 (reverse [2..4]):  [20, 10, 50, 40, 30]
Step 3 (reverse [0..4]):  [30, 40, 50, 10, 20]   ✅ matches expected output
```

**Why does this work?** Reversing the two chunks separately, then reversing the whole thing, effectively swaps the positions of the two chunks while keeping each chunk's *internal* order correct — exactly what a left rotation needs.

**Time Complexity:** `O(n)` — three reversal passes, each proportional to array size, but they don't multiply — they add: `O(d) + O(n-d) + O(n)` = `O(2n)` = `O(n)`.
**Space Complexity:** `O(1)` — everything happens in-place, no extra array.

### 10. Right Rotate an Array by One Position

**Definition:** The mirror image of left rotation — shift every element one step to the **right**; the last element wraps around to become the first.

```
Before: [10, 20, 30, 40, 50]
After:  [50, 10, 20, 30, 40]
```

```python
def right_rotate_by_one(arr):
    last = arr[-1]                        # save the last element
    for i in range(len(arr) - 1, 0, -1):    # shift every element one step right (from the back)
        arr[i] = arr[i - 1]
    arr[0] = last                              # place the saved last element at the front
    return arr

arr = [10, 20, 30, 40, 50]
print(right_rotate_by_one(arr))    # [50, 10, 20, 30, 40]
```

**Why shift from the back this time (not the front)?** Same reasoning as insertion: to avoid overwriting a value before it's copied. Since everything is moving rightward, we must copy the rightmost values first.

**Time Complexity:** `O(n)`. **Space Complexity:** `O(1)`.

---

### 11. Right Rotate an Array by D Places

```
Before (D=2): [10, 20, 30, 40, 50]
After:        [40, 50, 10, 20, 30]
```

#### Brute Force — repeat "rotate right by 1", D times
```python
def right_rotate_brute(arr, d):
    n = len(arr)
    d = d % n
    for _ in range(d):
        right_rotate_by_one(arr)
    return arr
```
**Time Complexity:** `O(n × d)` — same weakness as the brute-force left rotation.

#### Optimal — The Reversal Trick (mirrored)

Right rotation by `D` is the same as **left rotation by `(n - D)`**, so you can reuse the exact same reversal-trick function from left rotation with an adjusted `d`:

```python
def right_rotate_optimal(arr, d):
    n = len(arr)
    d = d % n
    left_rotate_optimal(arr, n - d)    # right rotate by d == left rotate by (n - d)
    return arr

arr = [10, 20, 30, 40, 50]
print(right_rotate_optimal(arr, 2))    # [40, 50, 10, 20, 30]
```

Or, done directly with its own three reversal steps (without relying on the left-rotate function):
```python
def right_rotate_direct(arr, d):
    n = len(arr)
    d = d % n
    reverse(arr, 0, n - d - 1)     # step 1: reverse the first (n-d) elements
    reverse(arr, n - d, n - 1)       # step 2: reverse the last d elements
    reverse(arr, 0, n - 1)              # step 3: reverse the whole array
    return arr
```

**Time Complexity:** `O(n)`. **Space Complexity:** `O(1)`.

> 💡 **Key relationship to remember:** `right_rotate(arr, d)` is always equivalent to `left_rotate(arr, n - d)`. Interviewers love asking you to derive this on the spot.

---

### Rotation Approaches Compared

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Brute force (rotate by 1, D times) | O(n × d) | O(1) | Simple but slow for large d |
| Extra array (copy shifted positions) | O(n) | O(n) | Fast but uses extra memory |
| Reversal trick | O(n) | O(1) | **Best of both worlds** — optimal time AND space |

---

### 🧠 Day 3 Key Takeaways

- Arrays give **O(1) access** because of contiguous memory and direct address math — this is their superpower.
- Arrays give **O(n) insertion/deletion** (except at the very end) because shifting is required — this is their weakness.
- **Static arrays** have a fixed size; **dynamic arrays** (like Python's `list`) resize by allocating double the space and copying everything over — but because that only happens occasionally, `.append()` is still **O(1) amortized**.
- Watch for **`IndexError`** on out-of-bounds access, and remember negative indexing (`arr[-1]`) is a Python-specific convenience, not a universal array feature.
- **Linear search** is `O(n)` and works on any array; **binary search** (`O(log n)`) needs a sorted array — don't reach for binary search unless you know the data is sorted.
- Many "find X" problems (largest, second largest) can be solved in a **single O(n) pass** by tracking the right variables as you go — avoid sorting (`O(n log n)`) when a single pass will do.
- The **two-pointer technique** (used in reversing an array) is a pattern you'll see again and again in array problems.
- The **reversal trick** for rotation is a classic example of turning an `O(n×d)` brute-force solution into an optimal `O(n)` one by finding a clever mathematical relationship — a common theme in DSA.
- **Right rotation by D is the same as left rotation by (n - D)** — a relationship worth memorizing so you never have to derive rotation logic twice.

