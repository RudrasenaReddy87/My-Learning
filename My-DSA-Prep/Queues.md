# Queues: First-In-First-Out Structures

Queue enthusiast! Queues follow FIFO (First-In-First-Out) principle: add to rear, remove from front. Why important? Preserve order of operations. Use cases: Print jobs, task scheduling, BFS traversal. In competitive programming (CP), essential for level-order tree traversal, graph exploration, and sliding window problems.

## Introduction to Queues

Queues are abstract data types that maintain the order of elements based on arrival time. The first element added is the first to be removed.

### What Are Queues?
- **FIFO Principle**: Elements are added at the rear and removed from the front.
- **Operations**: Enqueue (add), Dequeue (remove), Peek (view front), IsEmpty, Size.
- **Real-World Uses**: Printer queues, CPU task scheduling, call centers, breadth-first search.

### Types of Queues
- **Simple Queue**: Basic FIFO.
- **Circular Queue**: Fixed size, wraps around to reuse space.
- **Priority Queue**: Elements dequeued based on priority, not order.
- **Deque (Double-Ended Queue)**: Add/remove from both ends.
- **Blocking Queue**: Waits if full/empty (multithreading).

### Why Queues in CP?
- **BFS**: Explore levels in graphs/trees.
- **Sliding Windows**: Maintain window of elements.
- **Task Scheduling**: Process in order.

## Basic Operations

All operations with time complexities.

### Enqueue
Add element to rear.

```python
# Using deque
q.append(item)  # O(1)
```

### Dequeue
Remove and return front element.

```python
front = q.popleft()  # O(1) with deque
```

### Peek
View front without removing.

```python
front = q[0]  # O(1)
```

### IsEmpty
Check if queue is empty.

```python
empty = len(q) == 0  # O(1)
```

### Size
Get number of elements.

```python
size = len(q)  # O(1)
```

## Implementations

### Array-Based Queue (List)
Simple but inefficient for dequeue.

```python
class QueueList:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)  # O(n)

    def peek(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Deque-Based Queue
Efficient for both ends.

```python
from collections import deque

class QueueDeque:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)  # O(1)

    def dequeue(self):
        return self.items.popleft() if self.items else None  # O(1)

    def peek(self):
        return self.items[0] if self.items else None  # O(1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Circular Queue
Fixed size, efficient space usage.

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        if self.front == -1:
            self.front = self.rear
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        return self.queue[self.front] if not self.is_empty() else None

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
```

### Linked List Queue
Dynamic size.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class QueueLinked:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return item

    def peek(self):
        return self.front.val if self.front else None

    def is_empty(self):
        return self.size == 0
```

## Advanced Types

### Deque (Double-Ended Queue)
Add/remove from both ends.

```python
from collections import deque
dq = deque()
dq.append(1)      # Add right
dq.appendleft(2)  # Add left
dq.pop()          # Remove right
dq.popleft()      # Remove left
```

### Priority Queue
Dequeue highest priority (use heap).

```python
import heapq
pq = []
heapq.heappush(pq, (priority, item))  # Min-heap
item = heapq.heappop(pq)[1]
```

### Blocking Queue
For multithreading (Python: queue.Queue).

```python
import queue
bq = queue.Queue(maxsize=10)
bq.put(item)  # Blocks if full
item = bq.get()  # Blocks if empty
```

## Algorithms and Applications

### BFS (Breadth-First Search)
Explore graph level by level.

```python
from collections import deque
def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
```

### Sliding Window Maximum
Use deque to maintain max in window.

```python
from collections import deque
def sliding_window_max(nums, k):
    if not nums: return []
    dq = deque()
    result = []
    for i in range(len(nums)):
        # Remove out of window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### Task Scheduling
Process tasks with cooldown.

```python
from collections import deque
def task_scheduler(tasks, n):
    count = [0] * 26
    for task in tasks:
        count[ord(task) - ord('A')] += 1
    max_count = max(count)
    max_tasks = count.count(max_count)
    return max((max_count - 1) * (n + 1) + max_tasks, len(tasks))
```

### LRU Cache (Using Deque)
Approximate LRU with deque.

```python
from collections import deque
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            oldest = self.order.popleft()
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)
```

### Tree Traversals Using Queues (Level Order)

Queues are used for level-order tree traversals.

#### Level Order Traversal (BFS)
Visit nodes level by level.

```python
from collections import deque
def level_order(root):
    if not root: return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result
```

Example: For tree [1,2,3,4,5], result: [[1],[2,3],[4,5]]

#### Preorder Traversal (Iterative with Queue)
Visit root, left, right using queue.

```python
from collections import deque
def preorder_iterative_queue(root):
    if not root: return []
    result = []
    q = deque([root])
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.right: q.appendleft(node.right)  # Right first for preorder
        if node.left: q.appendleft(node.left)
    return result
```

Example: For tree [1,2,3,4,5], result: [1,2,4,5,3]

#### Inorder Traversal (Iterative with Queue)
Visit left, root, right using queue.

```python
from collections import deque
def inorder_iterative_queue(root):
    result = []
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result
```

Example: For tree [1,2,3,4,5], result: [4,2,5,1,3]

#### Postorder Traversal (Iterative with Queue)
Visit left, right, root using queue.

```python
from collections import deque
def postorder_iterative_queue(root):
    if not root: return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return result[::-1]
```

Example: For tree [1,2,3,4,5], result: [4,5,2,3,1]

## CP Problems and Solutions

### Level Order Traversal (LeetCode 102)
BFS on tree.

```python
from collections import deque
def level_order(root):
    if not root: return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        result.append(level)
    return result
```

### Rotten Oranges (LeetCode 994)
Multi-source BFS.

```python
from collections import deque
def oranges_rotting(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    if fresh == 0: return 0
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        i, j, time = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh -= 1
                q.append((ni, nj, time + 1))
    return -1 if fresh else time
```

### First Unique Character (LeetCode 387)
Use queue to track order.

```python
from collections import deque, Counter
def first_uniq_char(s):
    count = Counter(s)
    q = deque()
    for i, char in enumerate(s):
        if count[char] == 1:
            q.append(i)
    return q[0] if q else -1
```

### Task Scheduler (LeetCode 621)
Priority queue for frequencies.

```python
import heapq
from collections import Counter, deque
def least_interval(tasks, n):
    count = Counter(tasks)
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)
    q = deque()
    time = 0
    while max_heap or q:
        time += 1
        if max_heap:
            freq = heapq.heappop(max_heap) + 1
            if freq:
                q.append((freq, time + n))
        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
    return time
```

### Walls and Gates (LeetCode 286)
Multi-source BFS for shortest path.

```python
from collections import deque
def walls_and_gates(rooms):
    if not rooms: return
    rows, cols = len(rooms), len(rooms[0])
    q = deque()
    for i in range(rows):
        for j in range(cols):
            if rooms[i][j] == 0:
                q.append((i, j))
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and rooms[ni][nj] == 2147483647:
                rooms[ni][nj] = rooms[i][j] + 1
                q.append((ni, nj))
```

### Open the Lock (LeetCode 752)
BFS for shortest path in lock combinations.

```python
from collections import deque
def open_lock(deadends, target):
    dead = set(deadends)
    if "0000" in dead: return -1
    q = deque([("0000", 0)])
    visited = set(["0000"])
    while q:
        lock, turns = q.popleft()
        if lock == target: return turns
        for i in range(4):
            for d in [-1, 1]:
                new_digit = (int(lock[i]) + d) % 10
                new_lock = lock[:i] + str(new_digit) + lock[i+1:]
                if new_lock not in visited and new_lock not in dead:
                    visited.add(new_lock)
                    q.append((new_lock, turns + 1))
    return -1
```

### Zigzag Level Order (LeetCode 103)
Alternate directions per level.

```python
from collections import deque
def zigzag_level_order(root):
    if not root: return []
    result = []
    q = deque([root])
    left_to_right = True
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        if not left_to_right:
            level.reverse()
        result.append(level)
        left_to_right = not left_to_right
    return result
```

## Optimizations

### Choosing Implementation
- **Small Queues**: List is fine.
- **Large Queues**: Deque for O(1) ops.
- **Fixed Size**: Circular queue.
- **Priority**: Heap-based.

### Space Efficiency
- Deque uses less memory than list for frequent dequeues.
- Circular avoids wasted space.

## Pitfalls and Common Mistakes

### Underflow
Dequeue from empty queue.

```python
# Bad
if not q: front = q.popleft()  # Crash

# Good
front = q.popleft() if q else None
```

### Overflow
Enqueue to full circular queue without check.

### Inefficient List Use
Using list.pop(0) in loops – O(n) per op.

### Thread-Safety
Queues not thread-safe by default; use locks or blocking queues.

### Forgetting to Check Empty
Peek without is_empty.

## Multi-Language Examples

### C++ Queue
```cpp
#include <queue>
using namespace std;

queue<int> q;
q.push(1);  // enqueue
int front = q.front();  // peek
q.pop();  // dequeue
bool empty = q.empty();
```

### Java Queue
```java
import java.util.LinkedList;
import java.util.Queue;

Queue<Integer> q = new LinkedList<>();
q.add(1);  // enqueue
int front = q.peek();  // peek
q.poll();  // dequeue
boolean empty = q.isEmpty();
```

### C++ Deque
```cpp
#include <deque>
using namespace std;

deque<int> dq;
dq.push_back(1);   // enqueue
dq.push_front(2);  // add front
dq.pop_front();    // dequeue
```

### Java Priority Queue
```java
import java.util.PriorityQueue;

PriorityQueue<Integer> pq = new PriorityQueue<>();  // Min-heap
pq.add(3);
pq.add(1);
int min = pq.poll();  // 1
```

## Practice Section

### Solved Examples

1. **Reverse Queue**
   ```python
   from collections import deque
   def reverse_queue(q):
       stack = []
       while q: stack.append(q.popleft())
       while stack: q.append(stack.pop())
       return q
   ```

2. **Generate Binary Numbers**
   ```python
   from collections import deque
   def generate_binary(n):
       q = deque(['1'])
       result = []
       for _ in range(n):
           num = q.popleft()
           result.append(num)
           q.append(num + '0')
           q.append(num + '1')
       return result
   ```

3. **Queue Using Stacks**
   ```python
   class QueueWithStacks:
       def __init__(self):
           self.s1 = []
           self.s2 = []

       def enqueue(self, x):
           self.s1.append(x)

       def dequeue(self):
           if not self.s2:
               while self.s1:
                   self.s2.append(self.s1.pop())
           return self.s2.pop() if self.s2 else None
   ```

4. **Interleave First Half with Second Half**
   ```python
   from collections import deque
   def interleave(q):
       if not q: return
       n = len(q)
       half = n // 2
       first_half = deque()
       for _ in range(half):
           first_half.append(q.popleft())
       while first_half:
           q.append(first_half.popleft())
           q.append(q.popleft())
   ```

5. **Find Maximum in Sliding Window**
   (Already covered above)

### Walkthrough: Sliding Window Maximum
For [1,3,-1,-3,5,3,6,7], k=3:
- Window 1,3,-1: max=3
- 3,-1,-3: max=3
- -1,-3,5: max=5
- -3,5,3: max=5
- 5,3,6: max=6
- 3,6,7: max=7

### LeetCode-Style Problems
1. Implement Queue using Stacks.
2. Moving Average from Data Stream.
3. Design Circular Queue.
4. Kth Largest Element in a Stream (priority queue).
5. Number of Recent Calls (using queue for timestamps).
6. Reveal Cards In Increasing Order (using queue and sort).
7. Design Hit Counter (using queue for hits).

## Interview Questions

- Implement queue using stacks.
- Find the first unique character in a string.
- Rotten oranges problem.
- Task scheduler with cooldown.
- Sliding window maximum.
- Level order traversal of binary tree.
- Walls and gates (shortest path in grid).
- Open the lock (BFS on combinations).

## Edge Cases

- Empty queue: Dequeue/peek should handle gracefully.
- Single element: Enqueue/dequeue works.
- Full circular queue: Enqueue should fail or overwrite.
- Large inputs: Use efficient implementations.
- Negative numbers: In priority queues, handle correctly.

## Time Complexities in Detail

- Enqueue (list): O(1)
- Dequeue (list): O(n)
- Enqueue/Dequeue (deque): O(1)
- Peek/Size: O(1)
- Sliding Window Max: O(n)
- BFS: O(V + E)

## Personal Stories

- In a contest, I used list for queue and got TLE on large test cases; switched to deque and passed.
- Forgot to check is_empty before peek, got index error.
- Used queue for LRU but order was wrong; needed to remove and re-add on access.

## Code Variations

- Recursive BFS (not recommended, stack overflow).
- Iterative BFS with levels.
- Priority queue with custom comparator.
- Thread-safe queue with locks.

## Examples to Practice

1. Reverse first k elements of queue.
2. Sort a queue using another queue.
3. Find sum of minimum and maximum in sliding window.
4. Implement stack using queues.
5. Josephus problem (circular queue simulation).

## Comparisons

### Queue vs Stack
- Queue: FIFO, add rear remove front.
- Stack: LIFO, add/remove top.

### Deque vs Queue
- Deque: Both ends.
- Queue: Only rear add, front remove.

### BFS vs DFS
- BFS: Queue, level order.
- DFS: Stack/recursion, depth first.

## Appendices

### Glossary
- **Queue**: FIFO data structure.
- **Enqueue**: Add to rear.
- **Dequeue**: Remove from front.
- **Circular Queue**: Wrap-around fixed size.

### Time Complexities
- Enqueue/Dequeue (deque): O(1)
- Enqueue/Dequeue (list): O(1)/O(n)
- Peek/Size: O(1)

### References
- Python collections.deque docs
- LeetCode queue problems
- CLRS for data structures

Personal note: Queues are simple but crucial; I once used list.pop(0) in a contest and got TLE.
