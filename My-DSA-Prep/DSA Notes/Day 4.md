# Day 4 — Basic Recursion

**Language: Python**

---

## 1. What Is Recursion?

**Recursion** is when a function calls **itself** to solve a smaller version
of the same problem, until it reaches a version so small it can answer
directly without calling itself again.

Every correct recursive function needs exactly two parts:

1. **Base case** — the smallest, simplest version of the problem, answered
   directly, with no further recursive calls. This is what *stops* the
   recursion.
2. **Recursive case** — breaks the current problem into a smaller version of
   the same problem, calls itself on that smaller version, and combines the
   result into the answer for the current problem.

**A concrete analogy:** imagine a line of people, and you want to know how
many people are in front of you. You could count them all yourself — or you
could ask the person directly in front of you, "how many people are in front
of *you*?", add 1, and that's your answer. That person does the exact same
thing — asks the person in front of *them*. This continues until someone at
the very front (no one ahead of them) answers "0" directly, without asking
anyone else. That's the base case. Once that "0" is known, each person adds
1 and passes the answer back, until it reaches you.

**Every recursive function you write should follow this shape:**

```python
def recursive_function(problem):
    if is_base_case(problem):
        return direct_answer
    else:
        smaller_result = recursive_function(smaller_version_of(problem))
        return combine(smaller_result, problem)
```

**If you forget the base case, or the recursive case never actually shrinks
the problem toward it, the function calls itself forever** — in practice,
Python will raise a `RecursionError` ("maximum recursion depth exceeded")
once you hit its default recursion limit (1000 calls deep). This is the
recursive equivalent of an infinite loop, and it's the single most common
recursion bug — always check that your base case is reachable.

---

## 2. The Call Stack — What's Actually Happening in Memory

When function `A` calls function `B`, the computer doesn't forget about `A` —
it **pauses** `A` exactly where it is, remembers everything `A` needs to
resume later (its local variables, and the exact line to come back to), and
puts that paused state onto a structure called the **call stack**. Then it
runs `B`. When `B` finishes and returns a value, the computer pops `B`'s
frame off the stack and resumes `A` exactly where it left off, plugging in
`B`'s return value.

A **stack** (you'll formally meet this data structure in Week 6) works like a
stack of plates: the last plate you put on is the first one you take off
("Last In, First Out" — LIFO). Function calls behave the same way: the most
recently called function is the first one to finish and return.

Recursion is just this exact same mechanism, except `A` and `B` happen to be
the *same function*, called with different arguments. Each recursive call
gets its **own separate frame** on the call stack, with its own separate copy
of the local variables (including the parameter values) — they don't
interfere with each other.

**Visualizing `factorial(4)`:**

```
factorial(4) calls factorial(3), and PAUSES, waiting for the result
    factorial(3) calls factorial(2), and PAUSES, waiting for the result
        factorial(2) calls factorial(1), and PAUSES, waiting for the result
            factorial(1) calls factorial(0), and PAUSES, waiting for the result
                factorial(0) is the BASE CASE — returns 1 immediately, no further calls
            factorial(1) resumes: returns 1 * 1 = 1
        factorial(2) resumes: returns 2 * 1 = 2
    factorial(3) resumes: returns 3 * 2 = 6
factorial(4) resumes: returns 4 * 6 = 24
```

Notice the two distinct phases: calls go **down** (deeper into recursion,
building up paused frames on the stack) until the base case is hit, then
results come back **up** (unwinding the stack, one return value at a time)
until the very first call finally returns. This "down then up" shape is
present in *every* recursive function — internalizing it is the single
biggest unlock for reading and writing recursive code.

**This is also exactly why recursion has a space cost:** every paused frame
sits in memory until it's popped. A recursion that goes `n` levels deep uses
**O(n) auxiliary space** on the call stack — even if the function itself
doesn't allocate a single array (you saw this mentioned already on Day 1,
section 5, with the `factorial` example — now you know precisely why).

---

## 3. Print Numbers 1 to N (and N to 1) Using Recursion

**Print 1 to N** — the trick is to recurse *first*, then print:

```python
def print_1_to_n(n):
    if n == 0:              # base case: nothing left to print
        return
    print_1_to_n(n - 1)      # recurse on the smaller problem FIRST
    print(n)                 # THEN print, on the way back up
```

**Trace for `print_1_to_n(3)`:**
```
print_1_to_n(3) calls print_1_to_n(2), pauses
    print_1_to_n(2) calls print_1_to_n(1), pauses
        print_1_to_n(1) calls print_1_to_n(0), pauses
            print_1_to_n(0) is base case, returns immediately
        print_1_to_n(1) resumes: prints 1
    print_1_to_n(2) resumes: prints 2
print_1_to_n(3) resumes: prints 3
```
Output, in order printed: `1`, `2`, `3`. Because the `print(n)` happens
**after** the recursive call (on the way back "up" the stack, from the
smallest problem toward the largest), the smallest values print first.

**Print N to 1** — flip the order: print *before* recursing.

```python
def print_n_to_1(n):
    if n == 0:
        return
    print(n)                  # print FIRST (on the way down)
    print_n_to_1(n - 1)         # THEN recurse
```

Trace for `print_n_to_1(3)`: prints `3`, then calls `print_n_to_1(2)` which
prints `2`, then calls `print_n_to_1(1)` which prints `1`, then calls
`print_n_to_1(0)` which is the base case (prints nothing). Output: `3, 2, 1`.

**The general principle:** whether you act **before** or **after** the
recursive call determines whether you process values on the way **down**
(largest-to-smallest order) or on the way **up** (smallest-to-largest order).
This one choice — "before or after the recursive call" — is something you
will consciously decide for every recursive function you ever write.

**Complexity for both:** O(n) time (n calls made), **O(n) space** (n frames
deep on the call stack at the peak).

---

## 4. Factorial

`n!` (n factorial) = `n * (n-1) * (n-2) * ... * 1`, and by definition `0! = 1`.

```python
def factorial(n):
    if n == 0:                     # base case
        return 1
    return n * factorial(n - 1)     # recursive case
```

This matches the general template exactly: base case `n == 0` returns
directly; recursive case reduces the problem (`n` → `n-1`) and combines the
result (`n *` the smaller factorial). See the full call-stack trace in
section 2 above — `factorial(4)` correctly unwinds to `24`.

**Complexity:** O(n) time (n recursive calls), O(n) space (call stack depth).

---

## 5. Sum of First N Natural Numbers

```python
def sum_n(n):
    if n == 0:              # base case: sum of nothing is 0
        return 0
    return n + sum_n(n - 1)  # recursive case
```

**Trace for `sum_n(4)`:**
```
sum_n(4) = 4 + sum_n(3)
sum_n(3) = 3 + sum_n(2)
sum_n(2) = 2 + sum_n(1)
sum_n(1) = 1 + sum_n(0)
sum_n(0) = 0                     ← base case
```
Unwinding: `sum_n(1) = 1+0 = 1`, `sum_n(2) = 2+1 = 3`, `sum_n(3) = 3+3 = 6`,
`sum_n(4) = 4+6 = 10`. Result: `10` (matches `1+2+3+4=10`). Complexity: O(n)
time, O(n) space — identical shape to `factorial`, just `+` instead of `*`.

---

## 6. Sum of Digits of a Number (Recursive)

Combines Day 2's digit-extraction trick (`% 10` and `// 10`) with recursion.

```python
def sum_of_digits(n):
    if n == 0:                          # base case: no digits left
        return 0
    return (n % 10) + sum_of_digits(n // 10)   # last digit + recurse on the rest
```

**Trace for `sum_of_digits(1234)`:**
```
sum_of_digits(1234) = 4 + sum_of_digits(123)
sum_of_digits(123)  = 3 + sum_of_digits(12)
sum_of_digits(12)   = 2 + sum_of_digits(1)
sum_of_digits(1)    = 1 + sum_of_digits(0)
sum_of_digits(0)    = 0                        ← base case
```
Unwinding: `1+0=1`, `2+1=3`, `3+3=6`, `4+6=10`. Result: `10` (matches
`1+2+3+4=10`). Complexity: O(d) time and space, where `d` is the number of
digits (recall from Day 2: `d ≈ log₁₀ n`).

---

## 7. Check if an Array Is Sorted (Recursively)

**Idea:** an array is sorted if its first two elements are in order **and**
the rest of the array (everything from index 1 onward) is also sorted. This
is a direct recursive restatement of the iterative version from Day 3.

```python
def is_sorted_recursive(arr, index=0):
    if index >= len(arr) - 1:      # base case: 0 or 1 elements left — trivially sorted
        return True
    if arr[index] > arr[index + 1]:   # found a violation
        return False
    return is_sorted_recursive(arr, index + 1)   # check the rest
```

**Trace for `is_sorted_recursive([1, 2, 4, 3])`:**
```
index=0: arr[0]=1 <= arr[1]=2, OK → recurse with index=1
index=1: arr[1]=2 <= arr[2]=4, OK → recurse with index=2
index=2: arr[2]=4 > arr[3]=3, VIOLATION → return False immediately
```
Result: `False`. Notice this is functionally identical to the Day 3 loop
version — same early-exit behavior, just expressed as recursive calls
instead of a `for` loop. **Complexity:** O(n) time, **O(n) space** — this is
an important contrast with Day 3's iterative version, which was O(1) space.
Recursion trades some space (the call stack) for a different way of
expressing the same logic — worth noticing every time you have both an
iterative and recursive option for a problem.

---

## 8. Fibonacci Number (Plain Recursion) — and Why It's Exponential

The Fibonacci sequence: `0, 1, 1, 2, 3, 5, 8, 13, ...` — each number is the
sum of the two before it. Formally: `F(0)=0`, `F(1)=1`,
`F(n) = F(n-1) + F(n-2)` for `n ≥ 2`.

```python
def fibonacci(n):
    if n <= 1:                     # base case: F(0)=0, F(1)=1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive case
```

This looks innocent, but unlike every function above (which made exactly
**one** recursive call per invocation), this one makes **two**. That changes
everything about its complexity.

**Draw the recursion tree for `fibonacci(4)`:**
```
                    fib(4)
                   /      \
              fib(3)        fib(2)
             /     \        /    \
        fib(2)   fib(1)  fib(1)  fib(0)
        /    \
    fib(1)  fib(0)
```
Look closely: `fib(2)` is computed **twice** (once as part of `fib(3)`'s
subtree, once directly under `fib(4)`), and `fib(1)` is computed **three**
times. Nothing is cached or reused — every branch redoes work that a sibling
branch already did. As `n` grows, the number of redundant calls **doubles**
roughly every time `n` increases by 1, because each call spawns 2 more calls.

**Complexity:** roughly **O(2ⁿ)** time (technically closer to `O(φⁿ)` where
`φ ≈ 1.618` is the golden ratio, but "exponential" is the takeaway — the
exact base doesn't matter for intuition). This is dramatically worse than
every other function in today's lesson, purely because of the *branching*
recursion (two calls instead of one) combined with *overlapping
subproblems* (the same smaller inputs get recomputed repeatedly).

**Why this matters for what's coming:** this exact inefficiency —
recomputing the same subproblem many times — is precisely the problem that
**memoization** and **Dynamic Programming** (Week 9, and the full DP track
after Day 60) are designed to fix, by *caching* results of subproblems the
first time they're computed instead of redoing the work. You don't need DP
today — just internalize *why* naive Fibonacci is slow, because recognizing
"this recursion recomputes overlapping subproblems" is the trigger that
should make you think "this needs memoization" later on.

**Space complexity:** O(n) — even though there are exponentially many total
calls, the call stack's *depth* at any given moment is bounded by `n` (the
tree in the diagram above is `n` levels tall; the exponential blowup is in
the total number of nodes, i.e. calls made in total, not the stack depth at
any single point in time).

---

## 9. Recursive Search on Arrays — Linear Search and Maximum

Recursion doesn't just apply to numbers — it applies to any problem that can
be broken into "the first element, plus the same problem on the rest of the
array." Two classic examples: **linear search** and **finding the maximum**.

**Recursive Linear Search:**

```python
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):              # base case: fell off the end
        return -1
    if arr[index] == target:           # base case: found it
        return index
    return linear_search_recursive(arr, target, index + 1)   # recurse on the rest
```

Notice this has **two base cases**, not one — "not found" and "found."
Whenever a problem has more than one way to stop, write each as its own
`if`, checked in order.

**Trace for `linear_search_recursive([4, 7, 2, 9], 2)`:**
```
index=0: arr[0]=4 != 2 → recurse index=1
index=1: arr[1]=7 != 2 → recurse index=2
index=2: arr[2]=2 == 2 → return 2   ← found, base case hit
```
Result: `2`. Complexity: **O(n) time** worst case (target absent, or at the
last index), **O(n) space** (call stack depth) — contrast with the iterative
version's O(1) space, the same trade-off you saw with `is_sorted_recursive`
in section 7.

**Recursive Maximum:**

```python
def find_max_recursive(arr, index=0):
    if index == len(arr) - 1:                 # base case: one element left
        return arr[index]
    max_of_rest = find_max_recursive(arr, index + 1)   # recurse first
    return arr[index] if arr[index] > max_of_rest else max_of_rest  # combine
```

**Trace for `find_max_recursive([3, 7, 2, 9, 4])`:**
```
find_max(0) needs find_max(1)
  find_max(1) needs find_max(2)
    find_max(2) needs find_max(3)
      find_max(3) needs find_max(4)
        find_max(4) is base case → returns 4
      find_max(3) = max(9, 4) = 9
    find_max(2) = max(2, 9) = 9
  find_max(1) = max(7, 9) = 9
find_max(0) = max(3, 9) = 9
```
Result: `9`. This is the same "compare current element to the answer for
the rest" shape as `sum_n`, just with `max()` instead of `+` as the
combining step — a good reminder that many recursive functions differ only
in *what* they combine, not *how* they recurse.

**Complexity for both:** O(n) time, O(n) space.

---

## 10. Recursion vs. Iteration — Choosing Between Them

Every recursive function in this lesson (except Fibonacci) has a direct
iterative equivalent, and Day 3 already showed you several of these problems
solved with loops. It's worth being explicit about the trade-off:

| | Recursion | Iteration |
|---|---|---|
| **Space** | O(depth) — one stack frame per call | O(1) typically — just a few variables |
| **Readability** | Often shorter, mirrors the problem's own recursive definition (e.g. factorial, tree traversal) | Can be more verbose for naturally recursive problems |
| **Risk** | `RecursionError` if depth exceeds Python's limit (~1000) | No depth limit — just runs until the loop condition is false |
| **Best fit** | Problems that are naturally defined in terms of themselves (factorial, tree/graph traversal, divide-and-conquer) | Problems that are naturally a simple repeated counter or accumulator (summing a list, searching linearly) |

**Rule of thumb:** if you can just as easily write it with a `for` or
`while` loop, and there's no natural "smaller version of the same problem"
structure, prefer iteration — it's cheaper on memory and has no depth limit.
Reach for recursion when the problem itself is defined recursively (you'll
see this constantly with trees and graphs later in the course), or when the
recursive version is meaningfully clearer to read.

**Example — converting `sum_n` from recursive to iterative:**
```python
# Recursive (O(n) space)
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

# Iterative (O(1) space) — same result, no call stack growth
def sum_n_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```
Both are O(n) time. The only difference is space — this is *exactly* the
same contrast Day 3 vs. Day 4 has been building toward all along.

---

## 11. Tail Recursion

A recursive call is a **tail call** if it's the very last thing the function
does — nothing happens after it returns (no `* n`, no `+`, no further work).

```python
# NOT tail recursive — the multiplication happens AFTER the recursive
# call returns, so the current frame must stay on the stack waiting
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)     # work happens after the call returns

# Tail recursive — the recursive call is the LAST operation; nothing
# is left to do once it returns, so in principle nothing needs to be
# kept "waiting" on the stack
def factorial_tail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)   # last operation, no work after
```

The trick is an **accumulator parameter** that carries the running result
*into* the recursive call, instead of combining results on the way back up.

**Why it matters:** in languages that support "tail call optimization"
(TCO), a tail-recursive function can run in O(1) space, because the
compiler/interpreter reuses the same stack frame instead of stacking a new
one for every call. **Python deliberately does not implement TCO** — every
call, tail or not, still gets its own stack frame in Python, so
`factorial_tail` still uses O(n) space here. It's worth knowing the concept
because you'll meet it again in other languages (and in interviews), even
though rewriting Python code to be tail-recursive doesn't save you memory
the way it would in, say, Scheme or a well-optimized functional language.

---

## 12. Common Recursion Bugs — and How to Spot Them

Three mistakes account for the vast majority of broken recursive functions.
Learning to recognize them on sight will save you significant debugging
time.

**Bug 1 — Missing base case.**
```python
def broken(n):
    return n + broken(n - 1)   # no base case at all → RecursionError
```
Every recursive function needs at least one `if` that returns *without*
calling itself.

**Bug 2 — Base case exists but is unreachable.**
```python
def broken(n):
    if n == 0:
        return 0
    return n + broken(n - 2)   # skips over 0 whenever n starts odd!
```
`broken(5)` goes `5 → 3 → 1 → -1 → -3 → ...` and never hits exactly `0`.
Always double-check that the recursive case's step size actually lands on
the base case for *every* valid input, not just some of them.

**Bug 3 — Forgetting to `return` the recursive call.**
```python
def broken_sum(arr, index=0):
    if index >= len(arr):
        return 0
    arr[index] + broken_sum(arr, index + 1)   # missing `return`!
```
This computes the correct value and then **discards it** — the function
falls off the end and implicitly returns `None`. This is an easy typo to
make and an easy one to miss, because Python raises no error; the function
just silently returns the wrong thing. If a recursive function is returning
`None` unexpectedly, check first that every branch has an explicit `return`.

**How to debug a broken recursive function:** add a `print` at the top of
the function showing the current argument, so you can watch the sequence of
calls as they happen:
```python
def sum_n(n, depth=0):
    print("  " * depth + f"sum_n({n})")
    if n == 0:
        return 0
    return n + sum_n(n - 1, depth + 1)
```
The indentation visually reproduces the "down then up" shape from section 2
— if the calls never stop going down, you have Bug 1 or Bug 2; if the
printed calls look right but the final answer is wrong, you likely have
Bug 3.

---

## Worked Examples — Trace These Yourself First

**Example A:** What happens if you call `factorial(-1)`? Why, and how would
you guard against it?
<details><summary>Answer</summary>
It never terminates normally: `factorial(-1)` calls `factorial(-2)`, which
calls `factorial(-3)`, and so on — `n` moves further from the base case
(`n == 0`) instead of toward it, since decrementing a negative number never
reaches exactly 0. In Python, this eventually raises `RecursionError:
maximum recursion depth exceeded`. Guard against it with an explicit check,
e.g. `if n < 0: raise ValueError("n must be non-negative")` before the
recursive logic — a reminder that the base case must actually be *reachable*
from every valid recursive step, not just defined.
</details>

**Example B:** In `print_1_to_n`, what would happen to the output order if
you moved the `print(n)` line to *before* the recursive call instead of
after?
<details><summary>Answer</summary>
It would print `n, n-1, ..., 1` instead of `1, 2, ..., n` — i.e. it would
behave exactly like `print_n_to_1`. This confirms the rule from section 3:
printing before the recursive call processes values on the way down
(largest first), printing after processes them on the way up (smallest
first).
</details>

**Example C:** How many total calls does `fibonacci(5)` make (including the
initial call and all base-case calls)? Draw the tree and count the nodes.
<details><summary>Answer</summary>
Drawing it out: `fib(5)` branches into `fib(4)` and `fib(3)`; `fib(4)`
branches into `fib(3)` and `fib(2)`; and so on down to the base cases
`fib(1)` and `fib(0)`. Counting every node in the full tree gives **15 total
calls** for `fibonacci(5)` — notice `fib(3)` alone is computed twice (once
under `fib(5)`'s left branch, once under `fib(4)`), and this duplication
compounds rapidly as `n` grows, which is exactly the O(2ⁿ) blowup described
in section 8.
</details>

**Example D:** Is `find_max_recursive` (section 9) tail recursive? Why or
why not?
<details><summary>Answer</summary>
No. After `find_max_recursive(arr, index + 1)` returns, the function still
has to compare `arr[index]` against `max_of_rest` and pick the larger one —
that comparison is work done *after* the recursive call, which by
definition disqualifies it from being a tail call (section 11). To make it
tail recursive, you'd need to pass the running maximum *into* the call as an
accumulator, the same way `factorial_tail` passes in a running product.
</details>

**Example E:** A function `mystery(n)` is defined with base case `n == 0`
and recursive case `return mystery(n - 3)`. For which starting values of `n`
does this terminate normally, and for which does it crash?
<details><summary>Answer</summary>
It terminates only when `n` is a non-negative multiple of 3 (`0, 3, 6, 9,
...`), since each call subtracts exactly 3 and the only base case is exactly
`n == 0`. For any other non-negative `n` (e.g. `n = 7`: `7 → 4 → 1 → -2 →
...`), the value steps past `0` without ever landing on it exactly, and the
function recurses forever, eventually raising `RecursionError` — this is
Bug 2 from section 12, an unreachable base case.
</details>

---

## Practice Questions

### Question 1 — Print Numbers 1 to N and N to 1 (Recursive)
**Question:** Write two recursive functions: one that prints `1` up to `N`
in increasing order, and one that prints `N` down to `1` in decreasing order.
**Input:** `n = 5`
**Output:** `1 2 3 4 5` (from the first function) and `5 4 3 2 1` (from the second)
**Solution:**
```python
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=' ')

def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=' ')
    print_n_to_1(n - 1)

print_1_to_n(5)   # 1 2 3 4 5
print()
print_n_to_1(5)   # 5 4 3 2 1
```
The only difference between the two is whether `print` happens before or
after the recursive call — see section 3 for the full trace and the general
"before vs. after" principle. Complexity: `O(n)` time, `O(n)` space (call
stack depth) for both.

### Question 2 — Factorial (Recursive)
**Question:** Given a non-negative integer `n`, compute `n!` recursively.
**Input:** `n = 5`
**Output:** `120`
**Solution:**
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```
Base case `factorial(0) = 1`; recursive case multiplies `n` by the factorial
of everything smaller. Complexity: `O(n)` time, `O(n)` space (section 4).

### Question 3 — Sum of First N Natural Numbers (Recursive)
**Question:** Given a non-negative integer `n`, compute `1 + 2 + ... + n`
recursively.
**Input:** `n = 4`
**Output:** `10`
**Solution:**
```python
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(4))   # 10
```
Base case `sum_n(0) = 0`; recursive case adds `n` to the sum of everything
smaller. Complexity: `O(n)` time, `O(n)` space (section 5). (As a sanity
check, this should match the closed-form `n*(n+1)/2 = 4*5/2 = 10`.)

### Question 4 — Sum of Digits (Recursive)
**Question:** Given an integer `n`, compute the sum of its digits recursively.
**Input:** `n = 1234`
**Output:** `10`
**Solution:**
```python
def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print(sum_of_digits(1234))   # 10
```
Peel off the last digit with `% 10`, recurse on the rest with `// 10`, sum
as the calls unwind. Complexity: `O(d)` time and space, `d` = digit count
(section 6).

### Question 5 — Fibonacci Number (Recursive)
**Question:** Given `n`, compute the `n`-th Fibonacci number (`F(0)=0,
F(1)=1`) using plain recursion.
**Input:** `n = 6`
**Output:** `8`
**Solution:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))   # 8
```
Sequence check: `0,1,1,2,3,5,8` — `F(6)=8`. Complexity: **O(2ⁿ)** time (two
branching calls per invocation, with massive overlapping-subproblem
recomputation — see the recursion tree in section 8), `O(n)` space (call
stack depth only, despite the exponential total call count). Try calling
`fibonacci(35)` and notice it visibly lags — that lag *is* the O(2ⁿ) growth
made tangible.

### Question 6 — Check if an Array Is Sorted (Recursive)
**Question:** Given an array, determine recursively whether it's sorted in
non-decreasing order.
**Input:** `arr = [1, 2, 4, 3]`
**Output:** `False`
**Input 2:** `arr = [1, 2, 2, 5]`
**Output 2:** `True`
**Solution:**
```python
def is_sorted_recursive(arr, index=0):
    if index >= len(arr) - 1:
        return True
    if arr[index] > arr[index + 1]:
        return False
    return is_sorted_recursive(arr, index + 1)

print(is_sorted_recursive([1, 2, 4, 3]))   # False
print(is_sorted_recursive([1, 2, 2, 5]))   # True
```
Base case: fewer than 2 elements remain to compare → trivially sorted.
Recursive case: check the current adjacent pair, then recurse on the rest.
Complexity: `O(n)` time, `O(n)` space — note this is worse in space than
Day 3's iterative version (`O(1)` space), a direct illustration of
recursion's call-stack cost (section 7).

### Question 7 — Recursive Linear Search
**Question:** Given an array and a target value, return the index of the
target using recursion, or `-1` if it isn't present.
**Input:** `arr = [4, 7, 2, 9]`, `target = 2`
**Output:** `2`
**Solution:**
```python
def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index + 1)

print(linear_search_recursive([4, 7, 2, 9], 2))    # 2
print(linear_search_recursive([4, 7, 2, 9], 10))   # -1
```
Two base cases — "fell off the end" and "found it" — checked in that order
before the recursive case. Complexity: `O(n)` time, `O(n)` space (section 9).

### Question 8 — Recursive Maximum
**Question:** Given a non-empty array, find its maximum element using
recursion (no built-in `max()` over the whole array).
**Input:** `arr = [3, 7, 2, 9, 4]`
**Output:** `9`
**Solution:**
```python
def find_max_recursive(arr, index=0):
    if index == len(arr) - 1:
        return arr[index]
    max_of_rest = find_max_recursive(arr, index + 1)
    return arr[index] if arr[index] > max_of_rest else max_of_rest

print(find_max_recursive([3, 7, 2, 9, 4]))   # 9
```
Base case: a single remaining element is trivially its own max. Recursive
case: compare the current element against the max of everything after it.
Complexity: `O(n)` time, `O(n)` space (section 9).

### Question 9 — Convert to Tail-Recursive Form
**Question:** Rewrite `sum_n` (Question 3) as a tail-recursive function
using an accumulator parameter, so the recursive call is the last operation
performed.
**Input:** `n = 4`
**Output:** `10`
**Solution:**
```python
def sum_n_tail(n, accumulator=0):
    if n == 0:
        return accumulator
    return sum_n_tail(n - 1, accumulator + n)   # recursive call is the LAST operation

print(sum_n_tail(4))   # 10
```
Compare to the original `sum_n`, which computes `n + sum_n(n - 1)` — the
addition happens *after* the call returns, so that version is not tail
recursive. Here, `accumulator + n` is computed *before* recursing, and
passed in, so nothing is left to do once the call returns (section 11).
Note Python still uses `O(n)` space either way, since it doesn't optimize
tail calls — the benefit is conceptual/portable to languages that do.

## Revision

- Quick recall (5 min): re-solve "Find the largest element in an array" from
  Day 3, this time recursively instead of iteratively (hint: base case is a
  single-element array; recursive case compares the first element to the
  largest of the rest — see section 9 if you get stuck).

## Key Takeaways

- Every recursive function needs a **reachable base case** and a **recursive
  case that shrinks toward it** — skipping either causes infinite recursion
  (a `RecursionError` in Python).
- The **call stack** pauses each call's state while a deeper call runs; this
  gives recursion a natural **O(depth) space cost**, even with no explicit
  data structures.
- Whether you act **before or after** the recursive call determines whether
  you process values on the way down (largest/outermost first) or on the way
  up (smallest/innermost first).
- Recursive functions that make **one** call per invocation (factorial, sum,
  sum-of-digits) tend to be `O(n)` time; functions that make **multiple**
  branching calls with overlapping subproblems (naive Fibonacci) blow up to
  **exponential** time — a red flag that should make you think "memoization"
  once you reach Dynamic Programming.
- The same problem can often be solved both iteratively (Day 3, typically
  `O(1)` space) and recursively (typically `O(n)` space) — recursion isn't
  automatically "better," it's a different tool with its own trade-offs; use
  recursion when the problem is naturally self-similar, iteration when it's
  just a simple repeated counter (section 10).
- A recursive call is **tail recursive** if it's the last operation
  performed (usually via an accumulator parameter) — a useful concept for
  other languages' optimizers, though Python doesn't take advantage of it
  (section 11).
- The three most common recursion bugs are a **missing base case**, a
  **base case the recursive step skips past**, and **forgetting to `return`
  the recursive call's result** — recognizing these on sight is the fastest
  path to debugging broken recursive code (section 12).
