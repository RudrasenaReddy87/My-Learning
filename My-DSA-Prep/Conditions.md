# Conditions — roadmap, patterns, and examples

This document is an ordered roadmap to learn and apply conditional logic in Python for algorithms and interview problems. Follow the steps below: each step explains concepts, shows short examples, and suggests exercises to practice.

Note: structural pattern matching (`match` / `case`) requires Python 3.10+. Other examples run on Python 3.8+.

---

Step 1 — Basic syntax and flow

- Goal: understand `if`, `elif`, and `else` and how a simple decision is written.
- Concept: conditions are expressions that are evaluated for truthiness; the first matching branch executes.

Example:
```python
x = 7
if x % 2 == 0:
    print('even')
elif x % 3 == 0:
    print('divisible by 3')
else:
    print('odd and not divisible by 3')
```

Exercises:
- Write a function that classifies numbers as negative/zero/positive.
- Convert nested `if` blocks into `elif` chains where appropriate.

---

Step 2 — Compact condition forms

- Goal: know when to use one-line `if` and ternary expressions without sacrificing readability.

Examples:
```python
if cond: do_something()
status = 'ok' if 200 <= code < 300 else 'error'
```

Guideline: prefer ternary for simple expressions; use full `if` blocks for clarity when logic grows.

Exercises:
- Rewrite a simple `if/else` that assigns a value into a ternary expression where appropriate.

---

Step 3 — Truthiness and short-circuit semantics

- Goal: understand which values are truthy/falsy in Python and how `and`/`or` short-circuit evaluation works.

Key points:
- Falsy values: `False`, `None`, numeric zeros, and empty containers (`'', (), [], {}`), and objects with `__bool__`/`__len__` returning falsy.
- Short-circuiting: `A and B` evaluates `B` only if `A` is truthy; `A or B` evaluates `B` only if `A` is falsy.

Example:
```python
def expensive():
    print('running expensive')
    return True

if False and expensive():
    pass  # expensive() is not called

if True or expensive():
    pass  # expensive() is not called

print(0 or 'fallback')  # 'fallback'
print('a' and 'b')      # 'b'

# Guarding unsafe operations
if s and s[0] == 'a':
    print('starts with a')
```

Exercises:
- Implement guarded indexing for a string and test with empty input.

---

Step 4 — Assignment expressions (walrus operator)

- Goal: learn the `:=` operator to assign inside expressions where it improves clarity and avoids recomputation.

Example:
```python
if (n := len(items)) > 0:
    print(f'{n} items')
```

Guideline: use sparingly; prefer explicit assignment when it improves readability.

Exercises:
- Refactor a conditional that computes the same expression twice to use the walrus operator.

---

Step 5 — Structural pattern matching (Python 3.10+)

- Goal: use `match` / `case` when you need readable destructuring of structured data.

Example:
```python
def handle(x):
    match x:
        case 0:
            return 'zero'
        case [a, b]:
            return f'pair {a},{b}'
        case {'key': v}:
            return f'got key={v}'
        case _:
            return 'default'
```

Exercise:
- Parse simple expressions encoded as nested tuples using `match`.

---

Step 6 — Condition-driven algorithm patterns

- Goal: understand how conditional branches affect algorithm correctness and invariants.

Topics and short templates:

- Binary search templates (closed and half-open intervals). Choose based on whether you need exact matches or insertion points.

Closed-interval binary search (find exact match):
```python
def binary_search_closed(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

Half-open binary search (lower_bound / insertion point):
```python
def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

- Partitioning for quickselect/quicksort: ensure pivot comparisons and swaps are consistent.

Partition template:
```python
def partition(a, lo, hi):
    pivot = a[hi]
    i = lo
    for j in range(lo, hi):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[hi] = a[hi], a[i]
    return i
```

- Greedy algorithms: make clear accept/reject condition (e.g., `if s >= last_end` for interval scheduling).

- Dynamic programming: use condition checks when updating states (e.g., `if dp[s-x]: dp[s]=True`).

Exercises:
- Implement `first_true` (monotone predicate) and test on small arrays.
- Implement partition and use it in a quickselect-like helper.

---

Step 7 — Advanced tips, pitfalls, and best practices

- Prefer `if not x` for falsy checks and explicit comparisons when checking identity (`is None`) or boolean identity (`is True` / `is False`).
- Avoid heavy work within a conditional expression if it obscures intent; assign to a local variable instead.
- Chained comparisons (`a < b < c`) are both concise and efficient.
- Use `assert` during development to state and check invariants; remember `assert` can be disabled with optimization flags.

Examples:
```python
if 0 < x < 10:
    print('x in (0,10)')

assert n >= 0, 'n must be non-negative'
```

---

Step 8 — Practice problems and suggested order

Follow this practice roadmap:
1. Basic condition exercises (classify numbers, guarded indexing).
2. Compact forms and small refactorings (ternary, walrus).
3. Binary search templates and off-by-one exercises.
4. Partitioning and quickselect practice.
5. Greedy decision problems (interval scheduling, coin change heuristics).
6. Advanced: implement a simple boolean-expression evaluator and small `match`-based parser.

---

Try it — runnable examples

Example 1 — `first_true` template (find first index where predicate is true):
```python
def first_true(lo, hi, pred):
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo if pred(lo) else None

a = [0,0,0,1,1,1]
print('first_true =>', first_true(0, len(a)-1, lambda i: a[i] == 1))  # 3
```

Example 2 — guarded indexing and short-circuit:
```python
s = ''
if s and s[0] == 'a':
    print('starts with a')
else:
    print('empty or does not start with a')
```

Example 3 — walrus refactor:
```python
items = [1,2,3]
if (n := len(items)) > 0:
    print(f'len = {n}')
```

---

What next

- Implement the exercises in a small script and run them to validate your understanding.
- If you want translated snippets (C++/Java) for interview preparation, specify which sections to convert.


