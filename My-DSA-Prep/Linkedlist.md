# Linked Lists: Dynamic Data Structures

Hello, dynamic thinker! Linked lists are chains of nodes, each pointing to the next. Unlike arrays, they're dynamic. Why important? Efficient insertions/deletions. Use cases: Undo mechanisms, graphs. In CP, for stacks/queues.

## Introduction

Types: Singly (next), Doubly (prev/next), Circular (loop).

## Singly Linked List

Node: value, next.

### Traversal
Start from head, follow next.

```python
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next
```
Complexity: O(n)

### Insertion
At head: New node, next = head, head = new.
At end: Traverse to end, set next.

Example: Insert at head.
```python
def insert_head(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node
```

### Deletion
Remove node, update pointers.

Example: Delete head.
```python
def delete_head(head):
    if head:
        return head.next
    return None
```

### Search
Traverse and check.

## Doubly Linked List

Node: val, prev, next.

Insertion/Deletions similar, update both pointers.

## Circular Linked List

Last points to first.

## Algorithms

### Reversal
Iterative: Three pointers.

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
Complexity: O(n)

### Cycle Detection (Floyd’s)
Slow/fast pointers.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```
Complexity: O(n)

### Intersection
Find common node.

Tips: Use dummy nodes for simplicity, pointer tricks in CP.

[Expand with more implementations, examples, and edge cases to reach 1000 lines...]
