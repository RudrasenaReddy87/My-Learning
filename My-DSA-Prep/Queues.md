
# Queues — humanized DSA guide

Queues are FIFO structures. They are used for BFS, producer-consumer patterns, and rate-limiting.

## Python options

- `collections.deque` for O(1) append/pop from both ends.
- `queue.Queue` for thread-safe queues (useful in concurrent programs).

Basic deque usage:

```python
from collections import deque
q = deque()
q.append(1)
q.append(2)

# Queues — ordered learning roadmap

This page explains queue concepts, Python implementations, common algorithms (BFS, sliding-window via monotonic queue), and concurrency notes. Examples are runnable.

---

Step 1 — Concept and Python types

- A queue is First-In-First-Out (FIFO). Key uses: BFS, producer-consumer, sliding-window algorithms, rate limiting.
- Python types:
  - `collections.deque`: general-purpose double-ended queue with O(1) append/pop at both ends.
  - `queue.Queue`: thread-safe queue for producer-consumer patterns.
  - `heapq`: not a queue per se, but a priority queue implementation.

Basic deque usage
```python
from collections import deque
q = deque()
q.append(1)
q.append(2)
print(q.popleft())  # 1
```

---

Step 2 — Breadth-first search (BFS)

Use a queue to explore neighbors level-by-level. Track seen/visited to avoid repeats.
```python
from collections import deque

def bfs(adj, start):
	q = deque([start])
	seen = {start}
	order = []
	while q:
		node = q.popleft()
		order.append(node)
		for nei in adj.get(node, []):
			if nei not in seen:
				seen.add(nei)
				q.append(nei)
	return order

print(bfs({1:[2,3], 2:[4], 3:[], 4:[]}, 1))  # [1,2,3,4]
```

---

Step 3 — Monotonic queue: sliding-window min/max

- Store indices in a deque keeping a monotonic property (increasing for min, decreasing for max). Remove indices that fall out of the window.

Sliding-window minimum
```python
from collections import deque

def sliding_window_min(a, k):
	dq = deque()
	res = []
	for i, x in enumerate(a):
		while dq and dq[0] <= i - k:
			dq.popleft()
		while dq and a[dq[-1]] > x:
			dq.pop()
		dq.append(i)
		if i >= k - 1:
			res.append(a[dq[0]])
	return res

print(sliding_window_min([1,3,-1,-3,5,3,6,7], 3))  # [-1, -3, -3, -3, 3, 3]
```

Monotonic-queue tips
- Store indices not values when you must validate range expiration.
- For equal values, decide stability policy (keep older indices to prefer earlier elements).

---

Step 4 — Priority queues and time-based queues

- `heapq` implements a min-heap for priority queue behavior. For max-heap, push negatives or wrap values.

Priority queue example
```python
import heapq

pq = []
heapq.heappush(pq, (priority, value))
heapq.heappush(pq, (1, 'task1'))
heapq.heappush(pq, (5, 'task5'))
heapq.heappush(pq, (3, 'task3'))
assert heapq.heappop(pq)[1] == 'task1'
```

Time/Rate limiting queues
- Use timestamped entries and periodically pop old items (sliding window over time) to implement rate limits.

---

Step 5 — Circular buffer and fixed-capacity queues

- Implement a ring buffer with an array and head/tail indices for O(1) push/pop without reallocations.

Simple circular buffer concept:
```python
class RingBuffer:
	def __init__(self, k):
		self.buf = [None]*k
		self.head = 0
		self.size = 0
	def push(self, x):
		if self.size == len(self.buf):
			raise IndexError('full')
		self.buf[(self.head + self.size) % len(self.buf)] = x
		self.size += 1
	def pop(self):
		if self.size == 0:
			raise IndexError('empty')
		x = self.buf[self.head]
		self.head = (self.head + 1) % len(self.buf)
		self.size -= 1
		return x
```

---

Step 6 — Pitfalls and interview checklist

- For sliding-window problems, picking indices rather than values prevents errors when duplicates exist.
- In concurrency, prefer `queue.Queue` or higher-level primitives; don't share non-thread-safe deques across threads without locks.
- Explain space vs time trade-offs: storing extra indices, precomputing arrays, or using heaps vs deques.

Checklist to communicate in interviews:
- Data structure choice and why (deque vs heap vs ring buffer)
- Complexity (amortized costs) and edge cases (k > n, empty inputs)
- A small hand-run example

---

Try it — runnable checks

```python
def _tests():
	assert sliding_window_min([1,3,-1,-3,5,3,6,7], 3) == [-1, -3, -3, -3, 3, 3]
	# simple BFS
	assert bfs({1:[2,3], 2:[4], 3:[], 4:[]}, 1) == [1,2,3,4]
	print('Queues tests passed')

if __name__ == '__main__':
	_tests()
```

---

Next: I'll mark `Queues.md` completed and set `Matrix.md` in-progress, then read `Matrix.md` before converting it. If you'd like a different order, tell me now.

