
# Loops in Python — for, while, and loop patterns for DSA

Loops are the workhorse of algorithms. Learn the idioms (for over indices vs for over values, while loops for two-pointer patterns) and the complexity consequences.

## Types of loops

- `for` loops iterate over iterables (Pythonic and preferred when possible).
- `while` loops for conditions that change inside the loop (two-pointers, sliding windows).

Examples:

# Loops in Python — ordered learning roadmap

This roadmap covers loop types and common loop patterns used in algorithm problems (two-pointers, sliding window, fast-slow, nested loops with pruning), plus invariants and debugging tips.

---

Step 1 — Loop types and Python idioms

- `for` loops: iterate over iterables — Pythonic and concise.
- `while` loops: use when the stopping condition isn't a simple index (two-pointer, sliding-window loops).
- `enumerate()` for index+value, `zip()` for parallel iteration, and `reversed()` for backwards.

Examples
```python
for i, val in enumerate([10,20,30]):
	print(i, val)

arr = [1,2,3,4]
left, right = 0, len(arr)-1
while left < right:
	# two-pointer pattern
	left += 1
```

---

Step 2 — Two-pointer patterns

- Use on sorted arrays or when scanning from both ends to satisfy a condition.
- Common templates: find pair with sum, remove duplicates in-place, partitioning.

Pair sum in sorted array
```python
def pair_with_sum(a, target):
	l, r = 0, len(a)-1
	while l < r:
		s = a[l] + a[r]
		if s == target:
			return (l, r)
		elif s < target:
			l += 1
		else:
			r -= 1
	return None

print(pair_with_sum([1,2,3,4,6], 6))  # (1,3)
```

Tips:
- Always document whether pointers are inclusive/exclusive.
- Use while loops for variable-length shrinking/expanding windows.

---

Step 3 — Sliding window

- Fixed-length windows: maintain running sum or deque of candidates.
- Variable-length windows: expand/contract using two pointers and maintain invariants (e.g., window sum <= k).

Fixed-length example (max sum of k)
```python
def max_subarray_fixed_k(a, k):
	if len(a) < k: return None
	cur = sum(a[:k])
	best = cur
	for i in range(k, len(a)):
		cur += a[i] - a[i-k]
		best = max(best, cur)
	return best

print(max_subarray_fixed_k([1,4,2,10,23,3,1,0,20], 4))
```

Variable-length example (min-length subarray with sum >= s)
```python
def min_subarray_len(a, s):
	n = len(a)
	l = 0
	cur = 0
	best = n+1
	for r in range(n):
		cur += a[r]
		while cur >= s:
			best = min(best, r-l+1)
			cur -= a[l]
			l += 1
	return best if best <= n else 0
```

---

Step 4 — Fast-slow pointers (cycle detection, middle element)

- Use two pointers with different speeds to detect cycles or find middle of a linked list or runner problems.

Template
```python
slow = fast = start
while fast and fast.next:
	slow = slow.next
	fast = fast.next.next
# slow is at middle or cycle detection
```

---

Step 5 — Nested loops, pruning, and invariants

- Before using nested loops, check if a trick exists (prefix sums, hash map, sorting + two-pointer).
- Always identify a loop invariant and test it on small cases.

Example: nested loops with pruning
```python
def three_sum_closest(a, target):
	a.sort()
	best = float('inf')
	for i in range(len(a)-2):
		l, r = i+1, len(a)-1
		while l < r:
			s = a[i] + a[l] + a[r]
			if abs(s-target) < abs(best-target):
				best = s
			if s < target:
				l += 1
			else:
				r -= 1
	return best
```

---

Step 6 — Iterators, generators, and avoiding mutation pitfalls

- Use generators for memory-efficient streaming and `itertools` for common patterns.
- Avoid mutating a list you're iterating over with `for`. If needed, iterate over a copy or build a new list.

Example: safe filtering
```python
lst = [1,2,3,4]
lst = [x for x in lst if x%2==0]
```

---

Step 7 — Loop invariants and interview checklist

- State the invariant (what's true at loop entry/exit).
- Declare whether indices are inclusive/exclusive.
- Mention complexity clearly and any amortized claims.

---

Try it — runnable checks

```python
def _tests():
	assert pair_with_sum([1,2,3,4,6], 6) == (1,3)
	assert max_subarray_fixed_k([1,4,2,10,23,3,1,0,20], 4) == 39
	assert min_subarray_len([2,3,1,2,4,3], 7) == 2
	print('Loops tests passed')

if __name__ == '__main__':
	_tests()
```

---

Next: I'll mark `Loops.md` completed and set `Basics.md` in-progress, then read `Basics.md` before converting. If you'd like me to add `itertools` or generator examples, say which ones.


