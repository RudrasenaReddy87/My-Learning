
# Linked Lists — humanized DSA guide

Linked lists are linear collections where each element (node) points to the next. They trade O(1) insert/delete at known positions for O(n) random access. Use them when insertion/deletion inside a sequence is frequent and random access is less critical.

## How nodes are stored

- Each node typically stores `value` and `next` pointer. In languages like C, nodes are allocated separately on the heap; in Python, node objects are referenced by pointers in lists or other structures.

```python
class Node:
	def __init__(self, val=0, nxt=None):
		self.val = val
		self.next = nxt

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, val):
		if not self.head:
			self.head = Node(val)
			return
		cur = self.head
		while cur.next:
			cur = cur.next
		cur.next = Node(val)

	def to_list(self):
		res = []
		cur = self.head
		while cur:
			res.append(cur.val)
			cur = cur.next
		return res

ll = LinkedList()
for x in [1,2,3]:
	ll.append(x)
print(ll.to_list())  # [1,2,3]
```

## Variants

- Singly linked list: each node points to next.
- Doubly linked list: nodes have `prev` and `next` pointers (easy deletion, more memory).
- Circular linked list: last node points to head.
# Linked Lists — ordered learning roadmap

This page is a step-by-step roadmap for learning and practicing linked lists. Work through the steps in order: core concept → variants and costs → common techniques → algorithms with implementations → advanced patterns → practice problems and runnable checks.

---

Step 1 — Core concept and memory model

- Goal: understand how nodes and pointers represent a sequence and why linked lists trade random access for cheap insert/delete at known positions.
- Node structure (singly): value + next pointer. In Python, Node objects are heap-allocated and referenced by variables; the list is formed by linking Node.next references.

Basic Node and small helpers
```python
class Node:
	def __init__(self, val=0, nxt=None):
		self.val = val
		self.next = nxt

def build_list(vals):
	dummy = Node(0)
	cur = dummy
	for v in vals:
		cur.next = Node(v)
		cur = cur.next
	return dummy.next

def to_list(head):
	res = []
	cur = head
	while cur:
		res.append(cur.val)
		cur = cur.next
	return res

# quick smoke
lst = build_list([1,2,3])
print(to_list(lst))  # [1,2,3]
```

---

Step 2 — Variants and operation costs

- Singly linked list: O(1) insert at head; O(n) search; O(1) delete if you have previous node or O(n) otherwise.
- Doubly linked list: nodes have prev/next — O(1) deletion given node, slightly more memory.
- Circular lists: tail.next -> head, useful for round-robin or rotations.

Common costs:
- Insert at head: O(1)
- Insert at tail: O(1) if tail pointer available, else O(n)
- Delete at arbitrary index: O(n) (need prev)

Tip: in interviews mention whether you're maintaining a tail pointer or a size field — they affect complexity for operations like append and indexing.

---

Step 3 — Small invariants and idioms

- Use a dummy (sentinel) node to simplify head changes in insertion/deletion.
- For two-pointer techniques, use slow/fast pointers for middle or cycle detection.
- When manipulating groups, identify group boundaries (kth node) carefully and reuse pointers rather than allocating new lists when possible.

Dummy pattern example
```python
def remove_nth_from_end(head, n):
	dummy = Node(0)
	dummy.next = head
	fast = slow = dummy
	for _ in range(n + 1):
		fast = fast.next
	while fast:
		fast = fast.next
		slow = slow.next
	slow.next = slow.next.next
	return dummy.next
```

---

Step 4 — Core algorithms and implementations

Implement these and be ready to walk through invariants and edge cases.

1) Reverse a linked list (iterative)
```python
def reverse_list(head):
	prev = None
	cur = head
	while cur:
		nxt = cur.next
		cur.next = prev
		prev = cur
		cur = nxt
	return prev
```

2) Detect cycle (Floyd's tortoise and hare)
```python
def has_cycle(head):
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			return True
	return False
```

3) Merge two sorted lists (helper used in merge-sort)
```python
def merge_two_lists(l1, l2):
	dummy = Node(0)
	cur = dummy
	while l1 and l2:
		if l1.val <= l2.val:
			cur.next = l1
			l1 = l1.next
		else:
			cur.next = l2
			l2 = l2.next
		cur = cur.next
	cur.next = l1 or l2
	return dummy.next
```

4) Merge sort on a linked list (O(n log n) time, O(log n) recursion)
```python
def merge_sort_list(head):
	if not head or not head.next:
		return head
	# split list
	slow = fast = head
	prev = None
	while fast and fast.next:
		prev = slow
		slow = slow.next
		fast = fast.next.next
	prev.next = None
	left = merge_sort_list(head)
	right = merge_sort_list(slow)
	return merge_two_lists(left, right)
```

5) Reverse nodes in k-group
```python
def reverse_k_group(head, k):
	if k <= 1 or not head:
		return head
	dummy = Node(0)
	dummy.next = head
	group_prev = dummy
	while True:
		kth = group_prev
		for _ in range(k):
			kth = kth.next
			if not kth:
				return dummy.next
		group_next = kth.next
		# reverse group
		prev, cur = group_next, group_prev.next
		while cur is not group_next:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
		tmp = group_prev.next
		group_prev.next = kth
		group_prev = tmp

	# unreachable

```

6) Copy a list with a random pointer (O(n) time, O(1) extra space)
```python
class RandNode:
	def __init__(self, val=0, nxt=None, rand=None):
		self.val = val
		self.next = nxt
		self.rand = rand

def copy_random_list(head):
	if not head:
		return None
	# Step 1: weave copies
	cur = head
	while cur:
		nxt = cur.next
		cur.next = RandNode(cur.val, nxt)
		cur = nxt
	# Step 2: assign random pointers
	cur = head
	while cur:
		if cur.rand:
			cur.next.rand = cur.rand.next
		cur = cur.next.next
	# Step 3: unweave
	cur = head
	copy_head = head.next
	while cur:
		copy = cur.next
		cur.next = copy.next
		cur = cur.next
		if copy.next:
			copy.next = copy.next.next
	return copy_head
```

---

Step 5 — Edge cases, invariants, and interview tips

- Always consider empty list and single-node list.
- When using k-group functions, if k > length, return the original head.
- Use dummy nodes to simplify head changes.
- When asked about space/time, mention whether you modify nodes in place and whether recursion depth matters.

Quick checklist to explain in interviews:
- Input shape and constraints
- Chosen invariants (e.g., slow/fast movement or group boundaries)
- Time and space complexity
- Example walk-through on a small input

---

Try it — runnable checks

Use these quick tests to verify implementations. Copy into `run_examples.py` or run in a REPL.

```python
def _tests():
	# build helpers
	lst = build_list([1,2,3,4,5])
	rev = reverse_list(lst)
	assert to_list(rev) == [5,4,3,2,1]

	lst2 = build_list([1,2,3,4])
	rot = reverse_k_group(lst2, 2)
	assert to_list(rot) == [2,1,4,3]

	# merge-sort
	a = build_list([4,2,1,3])
	sorted_head = merge_sort_list(a)
	assert to_list(sorted_head) == [1,2,3,4]

	# cycle detection
	cyc = build_list([1,2,3])
	tail = cyc
	while tail.next:
		tail = tail.next
	tail.next = cyc.next  # create a cycle
	assert has_cycle(cyc) is True

	print('Linkedlist tests passed')

if __name__ == '__main__':
	_tests()
```

---

Related practice problems and next steps

- Merge k sorted lists, reorder list (L0→Ln→L1→Ln-1...), detect and remove cycle, check palindrome (reverse half + compare), add two numbers represented as linked lists (digit-wise), flatten multilevel lists.
- Next: convert `Stacks.md` to the same roadmap format (I'll start that next unless you prefer a different order).


