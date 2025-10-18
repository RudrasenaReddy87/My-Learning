
# Basics of Programming & Data Structures (Humanized)

This file gives a compact but complete review of the core building blocks you need before diving into algorithms: types, memory model, complexity notation, and common primitives in Python. It's written in a humanized way—like a short mentor session.

## Why basics matter

Algorithms are built from small steps. If you understand how values are stored, how operations cost, and how primitives behave (mutability, references), you will reason correctly about algorithms and bugs.
# Basics — ordered learning roadmap

This file collects small but essential programming principles you should know before tackling algorithms: types, mutability, complexity, Python idioms, common pitfalls, and quick examples.

---

Step 1 — Why basics matter

- Small details (mutability, cost of operations, reference semantics) change algorithm correctness and performance. Start every solution by clarifying input shapes and constraints.

Step 2 — Primitive types and mutability

- Numbers (`int`, `float`): immutable. Python integers are arbitrary-precision.
- Strings: immutable sequences of characters (operations usually return new strings).
- Lists: mutable dynamic arrays (store references to objects).
- Tuples: immutable ordered collections (hashable when contents are hashable).
- Dicts: hash tables (amortized O(1) lookup/insert).
- Set: unordered collection of unique elements (hash-based).

Example — mutation vs immutability
```python
lst = [1, 2]
def append_three(x):
	x.append(3)

append_three(lst)
print(lst)  # [1, 2, 3]

s = 'ab'
try:
	s[0] = 'x'
except TypeError:
	print('strings are immutable')
```

---

Step 3 — References, copying, and aliasing

- Assignment copies a reference, not the object. Use `.copy()`, `list()` or the `copy` module for shallow/deep copies when needed.

```python
a = [1,2]
b = a
b.append(3)
print(a)  # [1,2,3]

c = a.copy()
c.append(4)
print(a)  # [1,2,3]
print(c)  # [1,2,3,4]
```

Pitfall — mutable default arguments
```python
def append_to(x, items=None):
	if items is None:
		items = []
	items.append(x)
	return items

print(append_to(1))
print(append_to(2))
```

---

Step 4 — Time & space complexity quick rules

- O(1): simple arithmetic, index access
- O(log n): binary search on sorted data
- O(n): single pass over data
- O(n log n): efficient sorts
- O(n^2): typical nested loops

Always count auxiliary space (temporary arrays, recursion stack).

---

Step 5 — Quick Python toolbox & idioms

- `enumerate(iterable)`: index+value
- `zip(a,b)`: parallel iteration
- List/dict/set comprehensions for concise construction
- `sorted()` and `.sort()`; `bisect` for binary-search insertion points
- `itertools` for combinatorics and streaming patterns

Examples
```python
pairs = [(i,x) for i,x in enumerate(['a','b','c'])]
z = list(zip([1,2],[3,4]))  # [(1,3),(2,4)]
```

---

Step 6 — Small tricks and bitwise tips

- Swap in Python: `a, b = b, a` (clear and idiomatic).
- Power-of-two check: `x > 0 and (x & (x-1)) == 0`.
- Count bits: `bin(x).count('1')` (or use builtins/popcount when available).

---

Step 7 — Common pitfalls and testing ritual

- Avoid mutating an iterable while iterating over it — iterate over a copy or use indices.
- Use `is` for singletons (`None`) and `==` for equality checks.
- For float comparisons, use a small tolerance: `abs(a-b) < 1e-9`.

Interview testing ritual:
1. Restate the problem and constraints.
2. Describe brute force and then the optimized approach with complexity.
3. Walk through a small example and note edge cases (empty, single-element, duplicates).

---

Practice examples (copy into files or REPL)

1) First duplicate index
```python
def first_duplicate(a):
	seen = set()
	for i, x in enumerate(a):
		if x in seen:
			return i
		seen.add(x)
	return -1

print(first_duplicate([2,5,1,2,3]))  # 3
```

2) Power-of-two test
```python
def is_power_of_two(x):
	return x > 0 and (x & (x-1)) == 0

assert is_power_of_two(1)
assert is_power_of_two(2)
assert not is_power_of_two(3)
```

---

Try it — runnable smoke tests

```python
def _tests():
	assert first_duplicate([2,5,1,2,3]) == 3
	assert is_power_of_two(8)
	assert not is_power_of_two(7)
	print('Basics tests passed')

if __name__ == '__main__':
	_tests()
```

---

Next: I'll finalize the `strings_cheatsheet.md` file into a concise one-page roadmap (I'll mark it in-progress next). If you'd like more examples (generators, `itertools` recipes), tell me and I'll include them.

