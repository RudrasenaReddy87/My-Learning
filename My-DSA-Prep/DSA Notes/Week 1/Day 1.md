## Date : 10.07.2026

# Day 1 — Complexity Analysis


## 1. What Is an Algorithm?

An **algorithm** is just a step-by-step approach for solving a problem. It's not code — code is just one way of *writing down* an algorithm in a language a computer understands.

**In simple words**
> To find the largest number in a list: look at each number one by one, and keep track of the biggest one you've seen so far.

That's an algorithm. You could write it in Python, Java, or even explain it to a 10-year-old — the *idea* stays the same.

### Why We Compare Algorithms by Growth Rate, Not Raw Speed

Imagine two people solving the same problem:
- Person A uses a slow old laptop but a smart algorithm.
- Person B uses a super-fast gaming PC but a dumb algorithm.

If the input is small, Person B might win just because their machine is faster. But as the input grows bigger (say, from 100 items to 100 million items), the *algorithm* matters far more than the *hardware*.

This is why we don't measure algorithms in seconds or milliseconds — because that depends on:
- The speed of the computer
- The programming language
- Background processes running on the machine
- Compiler/interpreter optimizations

Instead, we measure **how the number of operations grows as the input size (n) grows**. This is called **growth rate**, and it's a property of the algorithm itself — independent of hardware.

**Example:**
- Algorithm A does `n` operations for input size `n`.
- Algorithm B does `n²` operations for input size `n`.

For `n = 10`: A does 10 steps, B does 100 steps — B seems only "a bit" slower.
For `n = 1,000,000`: A does 1,000,000 steps, B does 1,000,000,000,000 steps — B is now catastrophically slower.

This is the whole point of complexity analysis: **predicting how an algorithm behaves at scale**, before you even run it.

---

## 2. Big-O, Big-Theta, Big-Omega

These are three different "lenses" for describing how an algorithm's running time grows with input size `n`. Think of them as answering three different questions.

### Big-O (O) — Upper Bound ("Worst Case" / "At Most")
> "This algorithm will **never be slower than** this rate of growth."

Big-O describes the **worst-case** scenario — the maximum number of operations the algorithm could possibly take.

**Example:** Searching for a value in an unsorted list of `n` items using linear search.
- Best case: the value is the first item → 1 check.
- Worst case: the value is the last item, or not present at all → `n` checks.
- We say this algorithm is **O(n)** because in the worst case, it takes time proportional to `n`.

### Big-Omega (Ω) — Lower Bound ("Best Case" / "At Least")
> "This algorithm will **never be faster than** this rate of growth."

**Example:** For linear search, the best case is Ω(1) — the item you're looking for happens to be the very first one checked.

### Big-Theta (Θ) — Tight Bound ("Exactly This Rate")
> "This algorithm **always** grows at exactly this rate, both in the best and worst case."

**Example:** If an algorithm always loops through all `n` elements no matter what (like finding the sum of a list), it's Θ(n) — there's no lucky shortcut, and there's no unlucky slowdown either. Best case = worst case = average case.

### Why Interviews Focus on Big-O (Worst Case)

In real-world systems (and interviews), we care most about **guarantees**. You want to know: *"How bad can this possibly get?"* — not *"How lucky could I get?"*

- A payment system that's fast 99% of the time but occasionally takes 10 minutes is a serious problem.
- Big-O tells you the worst-case ceiling, so you can design systems that won't fall over under bad inputs.

**Rule of thumb for interviews:** Unless explicitly asked for best case or average case, always analyze and report the **worst-case time complexity using Big-O notation**.

---

## 3. Time Complexity of Loops

This is the most practical skill you'll use daily. The core idea: **count how many times the innermost line of code runs, in terms of `n`.**

### Single Loop — O(n)

```python
for i in range(n):
    print(i)
```
This loop runs exactly `n` times. Each iteration does a constant amount of work (printing one number). So total work = `n × O(1)` = **O(n)**.

### Loop with a Step/Skip — Still Often O(n) or O(n/2) → simplified to O(n)

```python
for i in range(0, n, 2):   # jumps by 2 each time
    print(i)
```
This runs `n/2` times. But in Big-O, we **drop constants** (more on this below), so O(n/2) simplifies to **O(n)**.

### Nested Loop (Independent) — O(n²)

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
For every single value of `i` (n values), the inner loop runs `n` times. Total = `n × n` = **O(n²)**.

**Real-world example:** Comparing every pair of items in a list of `n` items (like checking all pairs of students to see if any two have the same birthday) is a classic O(n²) pattern.

### Nested Loop (Dependent) — Still O(n²), but let's see why

```python
for i in range(n):
    for j in range(i, n):     # inner loop depends on i
        print(i, j)
```
Here, the inner loop doesn't always run `n` times:
- When `i = 0`, inner loop runs `n` times.
- When `i = 1`, inner loop runs `n-1` times.
- When `i = 2`, inner loop runs `n-2` times.
- ...
- When `i = n-1`, inner loop runs 1 time.

Total operations = `n + (n-1) + (n-2) + ... + 1` = `n(n+1)/2`

If you expand this, it's `(n² + n) / 2`. In Big-O, we drop constants and lower-order terms (the `+n` and `/2`), leaving us with **O(n²)**.

> **Key takeaway:** Even though the dependent loop technically does *less* work than a fully independent double loop, it still grows at the same *rate* — quadratically. That's why both are O(n²).

### Three Nested Loops — O(n³)

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```
Each additional independent nested loop multiplies by another `n`. So this is **O(n³)**.

### Loops That Don't Multiply — Sequential Loops Add, Not Multiply

```python
for i in range(n):        # O(n)
    print(i)

for j in range(n):        # O(n)
    print(j)
```
These two loops run one after another (not nested), so total work = `O(n) + O(n)` = `O(2n)` → simplified to **O(n)**.

> **Rule:** Nested loops → multiply their complexities. Sequential (back-to-back) loops → add their complexities, then simplify.

```
For constrains in Problem statement

1 <= arr.size() <= 10^5      -> O(nlogn) or O(n^2)

-10^4 <= arr[i] <= 10^4      -> O(n)

-10^9 <= K <= 10^9

So here

<= 20    --> O(2^n), O(n!)
<= 100   --> O(n^3)
<= 1000  --> O(n^2)
<= 10^5  --> O(nlogn) or O(n)
<= 10^6  --> O(n)
```
---

## 4. Space Complexity: Auxiliary Space vs Input Space

**Space complexity** measures how much extra memory an algorithm needs as the input size grows — just like time complexity measures operations.

### Input Space
This is the memory needed just to **store the input** you were given. We usually don't count this against the algorithm, because you need it regardless of which algorithm you use.

### Auxiliary Space
This is the **extra memory** the algorithm uses *beyond* the input — temporary variables, extra arrays, recursion call stacks, hash maps, etc. **This is what we usually mean when we say "space complexity" in interviews.**

**Example 1 — O(1) auxiliary space:**
```python
def find_max(arr):
    max_val = arr[0]          # one extra variable
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
```
We use just one extra variable (`max_val`) no matter how big `arr` is. This is **O(1) auxiliary space** — constant, doesn't grow with input.

**Example 2 — O(n) auxiliary space:**
```python
def double_all(arr):
    result = []                # new array, grows with input
    for num in arr:
        result.append(num * 2)
    return result
```
Here we create a brand-new list `result` that grows as big as the input. This is **O(n) auxiliary space**.

**Example 3 — Recursion and space:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```
Every recursive call adds a new frame to the "call stack" (like a stack of plates — each function call waits on top of the previous one). For `factorial(n)`, there will be `n` stacked calls before any return happens. This means recursion here uses **O(n) auxiliary space**, even though there's no visible array!

> **Interview tip:** Always mention *both* time and space complexity, and be ready to explain if recursion is involved (since it silently uses stack space).

---

## 5. Common Complexity Classes — Ranked from Best to Worst

Here they are, ordered from fastest-growing-slowest (best) to fastest-growing-fastest (worst):

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

| Complexity | Name | Simple Meaning | Real Example |
|---|---|---|---|
| **O(1)** | Constant | Same amount of work no matter how big the input is | Accessing `arr[5]` directly; checking if a number is even |
| **O(log n)** | Logarithmic | Work reduces by half (or some fraction) each step | Binary search in a sorted list |
| **O(n)** | Linear | Work grows directly in proportion to input size | Looping through a list once; linear search |
| **O(n log n)** | Linearithmic | A bit worse than linear, common in efficient sorting | Merge sort, Quick sort (average case), Heap sort |
| **O(n²)** | Quadratic | Work grows by the square of input size | Bubble sort, comparing every pair in nested loops |
| **O(2ⁿ)** | Exponential | Work doubles with every additional input item | Naive recursive Fibonacci; generating all subsets of a set |
| **O(n!)** | Factorial | Work grows by every possible ordering | Generating all permutations of a list (Traveling Salesman brute force) |

### Visualizing the Difference (for n = 10 vs n = 20)

| n | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|---|---|---|---|---|
| 10 | ~3 | 10 | ~33 | 100 | 1,024 |
| 20 | ~4 | 20 | ~86 | 400 | 1,048,576 |

Notice: doubling `n` barely changes O(log n), but it makes O(2ⁿ) explode. This is why exponential algorithms are usually unusable for anything beyond small inputs (roughly n > 25–30 becomes painfully slow).

### Why We Drop Constants and Lower-Order Terms

Big-O cares about **growth trend**, not exact operation counts.

**Example:**
An algorithm that does `3n² + 5n + 100` operations is still written as **O(n²)**, because:
- As `n` gets huge, the `n²` term dominates completely — the `5n` and `100` become insignificant in comparison.
- The constant `3` doesn't change the *shape* of growth, just scales it slightly.

**Example:**
`O(2n)` simplifies to `O(n)`. `O(n + log n)` simplifies to `O(n)` (since `n` dominates `log n` for large inputs).

---

## 6. How to Read Code and State Its Complexity (Practice Method)

Here's a step-by-step method you can use on **any** code snippet:

1. **Find the loops (or recursive calls).** These are where repeated work happens.
2. **Ask: "How many times does this loop run, relative to `n`?"**
3. **Are loops nested or sequential?** Nested → multiply. Sequential → add.
4. **Check what's happening inside the innermost part.** Is it O(1) work (like a comparison), or does it call another function with its own complexity?
5. **Simplify:** drop constants, drop lower-order terms, keep only the dominant term.
6. **Say it out loud** — literally practice narrating: *"This has a single loop that runs n times, and inside it we do constant work, so the time complexity is O(n)."*

### Worked Examples — Practice Reading These Out Loud

**Snippet A:**
```python
def print_pairs(arr):
    for i in arr:
        for j in arr:
            print(i, j)
```
*"There are two nested loops, both running `n` times independently. Multiply: n × n = O(n²)."*

**Snippet B:**
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
*"Each iteration cuts the search space in half. Starting from n, after k halvings we reach 1 when n / 2^k = 1, so k = log₂(n). Time complexity is O(log n)."*

**Snippet C:**
```python
def has_duplicates(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
```
*"Single loop of n iterations. Checking membership in a set and adding to a set are both O(1) on average. Total time: O(n). Space: O(n) because the set can grow up to the size of the input."*

**Snippet D:**
```python
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total
```
*"This loop doesn't depend on array size `n` — it depends on the number of digits in `n`, which is roughly log₁₀(n). So the time complexity is O(log n)."*

**Snippet E:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```
*"Each call branches into two more calls, and this keeps happening until we hit the base case. This creates a tree of calls that roughly doubles at each level, giving O(2ⁿ) time complexity — very slow for large n. Space complexity, however, is only O(n), because at any given moment the call stack only holds one path down the tree."*

---

## 7. Bonus Topics (Good to Know, Often Missed by Beginners)

### Best Case, Worst Case, and Average Case
- **Best case:** the most favorable input (e.g., element found immediately).
- **Worst case:** the least favorable input (e.g., element not found, or at the very end).
- **Average case:** the expected performance over all possible inputs, assuming a typical/random distribution.

In interviews, when someone just says "what's the complexity?", they usually mean **worst-case Big-O**, unless stated otherwise.

### Amortized Complexity
Some operations are usually cheap but occasionally expensive, and it "averages out" over many operations.

**Example:** Appending to a dynamic array (like Python's `list.append()`) is usually O(1), but occasionally the array needs to resize (copy all elements to a bigger array), which is O(n) for that one operation. Averaged over many appends, it still comes out to **O(1) amortized**.

### Why We Care About the Dominant Term Only
When an algorithm has multiple parts, like `O(n) + O(n²)`, we simplify to just **O(n²)**, because it dominates for large `n`. Always report the single worst-growing term as your final answer.

### Common Mistakes Beginners Make
- **Confusing "number of lines of code" with complexity.** A single line calling a library sort function is still O(n log n) internally — complexity is about *operations*, not lines written.
- **Forgetting hidden loops.** Built-in functions like `.sort()`, `in` checks on lists, or string concatenation in a loop can hide extra complexity.
- **Ignoring recursion's stack space.** Recursive solutions often silently use O(n) or more space, even if there's no explicit array.
- **Not simplifying.** Writing O(2n + 5) instead of simplifying to O(n).

---

## 8. Quick Recap / Cheat Sheet

- **Algorithm** = a recipe for solving a problem, independent of any programming language.
- We compare algorithms by **growth rate**, not raw seconds, because growth rate predicts behavior at scale regardless of hardware.
- **Big-O** = worst case (most commonly used in interviews). **Big-Omega** = best case. **Big-Theta** = tight bound (best = worst).
- **Loops:** single loop → O(n). Nested independent loops → multiply (O(n²), O(n³)...). Sequential loops → add, then simplify.
- **Space complexity:** input space (don't count) vs auxiliary space (extra memory used — this is what we report). Recursion uses stack space too.
- **Complexity ranking (best to worst):**
  `O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)`
- Always **simplify**: drop constants and lower-order terms, keep only the dominant term.
- Practice **narrating complexity out loud** for every piece of code you read — this builds the instinct needed for interviews.

---