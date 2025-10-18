# Linked Lists: Dynamic Data Structures

Hey there, dynamic thinker! Linked lists are chains of nodes, each pointing to the next (or previous in some cases). Unlike arrays, they're dynamic and can grow/shrink easily. Why important? Efficient insertions/deletions without shifting elements. Use cases: Undo mechanisms, browser history, graphs, implementing stacks/queues. In competitive programming (CP), they're everywhere for problems needing dynamic structures. Let's dive deep, with code, complexities, and my personal tips from battling linked list bugs.

## Introduction to Linked Lists

Linked lists are fundamental linear data structures in computer science, consisting of a sequence of elements called nodes, where each node contains data and a reference (pointer) to the next node in the sequence. Unlike arrays, which store elements in contiguous memory locations, linked lists use dynamic memory allocation, allowing them to grow or shrink as needed without predefined size limits.

### Types of Linked Lists
- **Singly Linked List**: Each node has a data field and a 'next' pointer to the next node. Traversal is only possible in one direction (forward).
- **Doubly Linked List**: Each node has 'prev' and 'next' pointers, allowing bidirectional traversal.
- **Circular Linked List**: The last node points back to the first node, forming a loop. Can be singly or doubly circular.

### Why Use Linked Lists?
Linked lists are preferred in scenarios requiring frequent insertions and deletions, as these operations can be performed in constant time O(1) if the position is known, compared to arrays where shifting elements takes O(n) time.

Key advantages over arrays:
- **Dynamic Size**: No need to specify size in advance; memory is allocated as needed.
- **Efficient Insertions/Deletions**: Especially at the beginning or end, without moving other elements.
- **Memory Flexibility**: Nodes can be scattered in memory, useful for systems with fragmented memory.

Disadvantages:
- **No Random Access**: Accessing an element by index requires O(n) traversal, unlike arrays' O(1).
- **Extra Memory Overhead**: Each node stores pointer(s), increasing space usage (e.g., 8 bytes per pointer in 64-bit systems).
- **Cache Inefficiency**: Nodes are not contiguous, leading to more cache misses and slower performance in modern CPUs.
- **Complexity**: More prone to bugs like null pointer dereferences or memory leaks.

### Memory Layout
In arrays, elements are stored in a continuous block: [elem1][elem2][elem3]...
In linked lists, nodes are separate: Node1(data, ptr to Node2) -> Node2(data, ptr to Node3) -> ...

Personal note: Linked lists taught me the importance of pointers; I once forgot to update the 'next' pointer during reversal and caused a memory leak in a contest submission.

## Node Implementation

### Python Node Class
```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### C++ Node Struct
```cpp
struct Node {
    int val;
    Node* next;
    Node(int x) : val(x), next(nullptr) {}
};
```

## Singly Linked List

A singly linked list has nodes with val and next.

### Traversal
Traversal in a singly linked list involves starting from the head node and following the 'next' pointers until reaching the end (None). This allows visiting each node exactly once.

Why it works: Each node points to the next, forming a chain. We use a loop to iterate through the chain.

Step-by-step:
1. Set current = head.
2. While current is not None:
   - Process current.val (e.g., print).
   - Move to current = current.next.
3. End when current is None.

```python
def traverse(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
```
Complexity: O(n) time (visit each node once), O(1) space (no extra structures).

Example: For list 1 -> 2 -> 3 -> None
- Start: current = 1, print 1, current = 2
- Next: print 2, current = 3
- Next: print 3, current = None
- Print None
Output: 1 -> 2 -> 3 -> None

Visualization:
Head -> [1] -> [2] -> [3] -> None

### Insertion

#### Insert at Head
Create new node, set next to head, return new node as head.

```python
def insert_head(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node
```
Complexity: O(1)

#### Insert at End
Traverse to end, set last.next to new node.

```python
def insert_end(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head
```
Complexity: O(n)

#### Insert at Position
Traverse to position-1, insert.

```python
def insert_at_pos(head, val, pos):
    if pos == 0:
        return insert_head(head, val)
    new_node = Node(val)
    current = head
    for i in range(pos-1):
        if not current:
            return head
        current = current.next
    if current:
        new_node.next = current.next
        current.next = new_node
    return head
```
Complexity: O(n)

### Deletion

#### Delete Head
Return head.next

```python
def delete_head(head):
    if head:
        return head.next
    return None
```
Complexity: O(1)

#### Delete End
Traverse to second last, set next to None.

```python
def delete_end(head):
    if not head or not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head
```
Complexity: O(n)

#### Delete at Position
Traverse to pos-1, update pointers.

```python
def delete_at_pos(head, pos):
    if pos == 0:
        return delete_head(head)
    current = head
    for i in range(pos-1):
        if not current:
            return head
        current = current.next
    if current and current.next:
        current.next = current.next.next
    return head
```
Complexity: O(n)

### Search
Traverse and check val.

```python
def search(head, val):
    current = head
    index = 0
    while current:
        if current.val == val:
            return index
        current = current.next
        index += 1
    return -1
```
Complexity: O(n)

### Find Middle
Use slow/fast pointers.

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val if slow else None
```
Complexity: O(n)

### Remove Duplicates from Sorted List
```python
def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
```
Complexity: O(n)

### Merge Two Sorted Lists
```python
def merge_two_lists(l1, l2):
    dummy = Node()
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
```
Complexity: O(n + m)

## Doubly Linked List

Nodes have val, prev, next.

### Node Class
```python
class DoublyNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```

### Insertion at Head
```python
def insert_head_doubly(head, val):
    new_node = DoublyNode(val)
    if head:
        head.prev = new_node
    new_node.next = head
    return new_node
```

### Deletion at Head
```python
def delete_head_doubly(head):
    if head:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head
    return None
```

### LRU Cache Implementation
Use doubly linked list + hashmap.

```python
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DoublyNode()
        self.tail = DoublyNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.prev.val]
                self._remove(self.tail.prev)
            new_node = DoublyNode(value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
```

## Circular Linked List

Last node points to first.

### Insertion at End
```python
def insert_end_circular(head, val):
    new_node = Node(val)
    if not head:
        new_node.next = new_node
        return new_node
    current = head
    while current.next != head:
        current = current.next
    current.next = new_node
    new_node.next = head
    return head
```

### Josephus Problem
People in circle, every kth eliminated.

```python
def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n-1, k) + k - 1) % n + 1
```
Complexity: O(n)

## Advanced Algorithms

### Reversal (Iterative)
Reversing a linked list iteratively uses three pointers: prev, current, and next_node. We iterate through the list, reversing the 'next' pointers.

Why it works: By setting current.next to prev, we reverse the direction. prev tracks the new head.

Step-by-step for 1 -> 2 -> 3 -> None:
1. prev = None, current = 1, next_node = 2
2. current.next = None (1 -> None), prev = 1, current = 2
3. next_node = 3, current.next = 1 (2 -> 1), prev = 2, current = 3
4. next_node = None, current.next = 2 (3 -> 2), prev = 3, current = None
5. Return prev = 3

Visualization:
Original: Head -> [1] -> [2] -> [3] -> None
After: Head -> [3] -> [2] -> [1] -> None

```python
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
```
Complexity: O(n) time, O(1) space.

### Reversal (Recursive)
```python
def reverse_recursive(head):
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

### Palindrome Check
Use slow/fast to find middle, reverse second half, compare.

```python
def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second_half = reverse(slow)
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True
```
Complexity: O(n)

### Rotate List
Rotate right by k.

```python
def rotate_right(head, k):
    if not head or not head.next:
        return head
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1
    k %= length
    if k == 0:
        return head
    current.next = head  # Make circular
    for _ in range(length - k):
        current = current.next
    new_head = current.next
    current.next = None
    return new_head
```
Complexity: O(n)

### Add Two Numbers (LeetCode)
Lists represent numbers, add them.

```python
def add_two_numbers(l1, l2):
    dummy = Node()
    current = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next
```

### Flatten Multilevel Doubly Linked List
```python
def flatten(head):
    if not head:
        return head
    current = head
    while current:
        if current.child:
            next_node = current.next
            child_tail = flatten(current.child)
            current.next = current.child
            current.child.prev = current
            current.child = None
            if next_node:
                child_tail.next = next_node
                next_node.prev = child_tail
        current = current.next
    return head
```

## Cycle Detection and Removal

### Detect Cycle (Floyd’s)
As above.

### Find Cycle Start
After meeting, move slow to head, move both one step.

```python
def detect_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
```

### Remove Cycle
Set cycle start's next to None.

## Intersection of Two Lists
Find common node.

```python
def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
```
Complexity: O(n + m)

## Problems in Competitive Programming

### Reverse in Groups of K
```python
def reverse_k_group(head, k):
    def reverse_group(start, end):
        prev = end.next
        current = start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    dummy = Node(0, head)
    prev_group_end = dummy
    while True:
        kth = prev_group_end
        for _ in range(k):
            if not kth:
                return dummy.next
            kth = kth.next
        if not kth:
            return dummy.next
        group_start = prev_group_end.next
        next_group_start = kth.next
        new_group_end = reverse_group(group_start, kth)
        prev_group_end.next = new_group_end
        prev_group_end = group_start
        group_start.next = next_group_start
```

### Detect and Remove Loop
Use Floyd’s, then remove.

### Clone with Random Pointer
```python
def copy_random_list(head):
    if not head:
        return None
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    current = head
    copy_head = head.next
    while current:
        copy = current.next
        current.next = copy.next
        if copy.next:
            copy.next = copy.next.next
        current = current.next
    return copy_head
```

## Interview Questions

- Reverse a linked list.
- Detect cycle.
- Find middle.
- Merge two sorted lists.
- Remove nth from end.
- Add two numbers.
- Palindrome check.
- Intersection point.
- Rotate list.
- Flatten multilevel list.

## Edge Cases

- Empty list: Return None or handle.
- Single node: Operations should work.
- All nodes same value.
- Cycles: Handle in traversal.
- Large lists: O(n) is fine, but optimize space.

## Time Complexities

| Operation | Singly | Doubly | Circular |
|-----------|--------|--------|----------|
| Access | O(n) | O(n) | O(n) |
| Insert Head | O(1) | O(1) | O(1) |
| Insert End | O(n) | O(1) if tail | O(n) |
| Delete Head | O(1) | O(1) | O(1) |
| Delete End | O(n) | O(1) if tail | O(n) |
| Search | O(n) | O(n) | O(n) |

## Common Mistakes and Pitfalls

Linked lists are prone to subtle bugs due to pointer manipulations. Here are common errors and how to avoid them:

### Null Pointer Dereferences
- **Mistake**: Accessing current.next without checking if current is None.
- **Example**: In traversal, if head is None, current = None, then current.val crashes.
- **Fix**: Always check if current is not None before accessing attributes.

### Forgetting to Update Head
- **Mistake**: In insert_head, not returning the new node as head.
- **Example**: head = insert_head(head, 5) – forgetting this leads to lost nodes.
- **Fix**: Return the new head and assign it.

### Infinite Loops in Cycles
- **Mistake**: Traversing a cyclic list without cycle detection.
- **Example**: While current: current = current.next – loops forever if cycle.
- **Fix**: Use Floyd’s algorithm to detect cycles before traversal.

### Memory Leaks
- **Mistake**: Not freeing nodes in languages like C++ when deleting.
- **Example**: Deleting a node but not calling delete on it.
- **Fix**: Properly deallocate memory.

### Off-by-One Errors in Position-Based Operations
- **Mistake**: Inserting at pos=1 inserts at index 0 instead of 1.
- **Example**: For loop from 0 to pos-1, but pos starts from 0.
- **Fix**: Clarify if pos is 0-based or 1-based.

### Reversing Without Returning New Head
- **Mistake**: Reversing but returning old head.
- **Example**: prev becomes new head, but return head instead.
- **Fix**: Return prev.

### Cycle Detection False Positives
- **Mistake**: Slow/fast pointers meet but no cycle (e.g., in palindrome check after reversal).
- **Example**: Meeting at end if list is even length.
- **Fix**: Ensure fast moves twice as fast and check conditions.

Personal note: I once had a WA because I didn't handle empty list in merge_two_lists.

## Personal Stories and Tips

- In a contest, I reversed a list but forgot to return new head, got WA.
- Tip: Use dummy nodes to simplify.
- Pitfall: Infinite loops if cycle not handled.

## Code Variations

### Recursive Traversal
```python
def traverse_recursive(head):
    if not head:
        return
    print(head.val)
    traverse_recursive(head.next)
```

### C++ Singly List
```cpp
class SinglyList {
    Node* head;
public:
    void insert(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }
    // etc.
};
```

## Examples to Practice

1. Reverse list iteratively/recursively.
2. Find kth from end.
3. Remove duplicates.
4. Merge k sorted lists.
5. Swap nodes in pairs.
6. Partition list around value.
7. Sort list (merge sort).
8. Reorder list.

## Comparisons

### Linked List vs Array
- Arrays: Fast access, slow insert/delete.
- Linked: Slow access, fast insert/delete.

### Linked List vs Stack/Queue
- Linked lists can implement them efficiently.

## Advanced Topics

### Skip Lists
Probabilistic data structure for fast search.

### Unrolled Linked Lists
Groups elements in nodes for better cache.

### Self-Organizing Lists
Move-to-front heuristic.

