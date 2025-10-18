# Queues: First-In-First-Out Structures

Queue enthusiast! Queues follow FIFO. Add to rear, remove from front. Why important? Order preservation. Use cases: Print jobs, BFS. In CP, for level-order traversal.

## Introduction

Abstract data type. Implement with lists or deque.

## Basics

Operations: enqueue (add), dequeue (remove), peek, is_empty.

## Deque Implementation

```python
from collections import deque
q = deque()
q.append(1)  # enqueue
front = q.popleft()  # dequeue
```

## Implementations

### List
enqueue: append, dequeue: pop(0) – O(n)

### Deque
O(1) for both ends.

### Circular Queue
Fixed size, wrap around.

## Algorithms

### BFS
Use queue for levels.

```python
from collections import deque
def bfs(graph, start):
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
```

### Sliding Window Maximum
Use deque for monotonic.

Tips: Deque for efficiency, avoid lists for large queues.

[Expand with more examples, problems, and implementations to reach 1000 lines...]
