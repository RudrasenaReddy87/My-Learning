# Stacks: Last-In-First-Out Structures

Hey there, stack enthusiast! Stacks are a fundamental linear data structure that follows the principle of Last-In-First-Out (LIFO), also known as First-In-Last-Out (FILO). Imagine a stack of plates: you add to the top and remove from the top. Why are stacks important? They're crucial for managing function calls, undo operations, and parsing expressions. In competitive programming (CP), stacks shine in problems like balancing parentheses, evaluating postfix expressions, and finding next greater elements. Use cases abound: browser back buttons, text editors' undo, recursion simulation. Let's dive deep into stacks, with implementations, algorithms, examples, complexities, and my personal tips from countless debugging sessions.

## Introduction to Stacks

A stack is an abstract data type (ADT) with operations: push (add to top), pop (remove from top), peek (view top without removing), is_empty, and sometimes is_full. In Python, we can implement stacks using lists or deques for efficiency. Stacks are simple yet powerful, forming the backbone of many algorithms.

Key properties:
- LIFO order.
- Operations are O(1) with proper implementation.
- Can be bounded (fixed size) or unbounded.

### What Are Stacks?
- **LIFO Principle**: Last in, first out.
- **Operations**: Push, pop, peek, is_empty, size.
- **Real-World Uses**: Function call stack, undo in editors, backtracking.
- **Types**: Simple stack, bounded stack, min/max stack.

### Why Stacks in CP?
- **Parsing**: Expressions, parentheses.
- **Monotonic**: Next greater, sliding windows.
- **Recursion**: Simulate calls iteratively.
- **Backtracking**: DFS paths.

Personal note: I once struggled with stack overflows in recursion; understanding stacks saved me!

## Basic Operations

All operations with time complexities.

### Push
Add element to top.

```python
# Using list
stack.append(item)  # O(1)
```

### Pop
Remove and return top element.

```python
top = stack.pop()  # O(1)
```

### Peek
View top without removing.

```python
top = stack[-1]  # O(1)
```

### IsEmpty
Check if stack is empty.

```python
empty = len(stack) == 0  # O(1)
```

### Size
Get number of elements.

```python
size = len(stack)  # O(1)
```

## Implementations

### List-Based Stack
Simple but amortized O(1).

```python
class StackList:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Deque-Based Stack
Efficient for large stacks.

```python
from collections import deque

class StackDeque:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Linked List Stack
Dynamic, no resize issues.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class StackLinked:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        item = self.top.val
        self.top = self.top.next
        self.size -= 1
        return item

    def peek(self):
        return self.top.val if self.top else None

    def is_empty(self):
        return self.size == 0
```

### Bounded Stack
Fixed size.

```python
class BoundedStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
        self.size = 0

    def push(self, item):
        if self.size < self.capacity:
            self.items.append(item)
            self.size += 1
            return True
        return False  # Overflow

    def pop(self):
        if not self.is_empty():
            self.size -= 1
            return self.items.pop()
        return None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
```

## Advanced Types

### Min Stack
Track minimum element.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val
        return None

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
```

### Max Stack
Similar, track maximum.

```python
class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.max_stack[-1]:
                self.max_stack.pop()
            return val
        return None

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMax(self):
        return self.max_stack[-1] if self.max_stack else None
```

### Monotonic Stack
Maintain increasing/decreasing order.

```python
# Increasing monotonic stack
def monotonic_increasing(nums):
    stack = []
    for num in nums:
        while stack and stack[-1] > num:
            stack.pop()
        stack.append(num)
    return stack
```

## Algorithms and Applications

### Parentheses Matching
Check balanced parentheses.

```python
def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack
```

### Expression Evaluation (Postfix)
Evaluate postfix.

```python
def evaluate_postfix(expr):
    stack = []
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
    return stack[0]
```

### Infix to Postfix Conversion
Convert infix to postfix.

```python
def infix_to_postfix(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    result = []
    for char in expr:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(char, 0):
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return ''.join(result)
```

### Infix to Prefix Conversion
Convert infix to prefix.

```python
def infix_to_prefix(expr):
    # Reverse the expression and swap parentheses
    expr = expr[::-1]
    expr = expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    postfix = infix_to_postfix(expr)
    return postfix[::-1]
```

### Prefix Evaluation
Evaluate prefix expression.

```python
def evaluate_prefix(expr):
    stack = []
    for char in reversed(expr.split()):
        if char.isdigit():
            stack.append(int(char))
        else:
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
    return stack[0]
```

Example: Evaluate "+ * 3 4 2" (prefix for (3*4)+2 = 14)

### Postfix to Infix Conversion
Convert postfix to infix.

```python
def postfix_to_infix(expr):
    stack = []
    for char in expr.split():
        if char.isalnum():
            stack.append(char)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a}{char}{b})")
    return stack[0]
```

Example: "3 4 * 2 +" -> "((3*4)+2)"

### Prefix to Infix Conversion
Convert prefix to infix.

```python
def prefix_to_infix(expr):
    stack = []
    for char in reversed(expr.split()):
        if char.isalnum():
            stack.append(char)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(f"({a}{char}{b})")
    return stack[0]
```

Example: "+ * 3 4 2" -> "((3*4)+2)"

### Next Greater Element
Find next greater.

```python
def next_greater(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        stack.append(i)
    return result
```

### Previous Smaller Element
Find previous smaller.

```python
def prev_smaller(nums):
    stack = []
    result = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[stack[-1]] >= nums[i]:
            stack.pop()
        if stack:
            result[i] = nums[stack[-1]]
        stack.append(i)
    return result
```

### Stock Span Problem
Days span where price is higher.

```python
def stock_span(prices):
    stack = []
    result = []
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()
        span = i - stack[-1] if stack else i + 1
        result.append(span)
        stack.append(i)
    return result
```

### Largest Rectangle in Histogram
Find largest rectangle.

```python
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
```

### Trapping Rain Water
Calculate trapped water.

```python
def trap(height):
    stack = []
    water = 0
    for i in range(len(height)):
        while stack and height[stack[-1]] < height[i]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            water += distance * bounded_height
        stack.append(i)
    return water
```

### Stack for Recursion Simulation
Factorial iteratively.

```python
def factorial_iterative(n):
    stack = []
    result = 1
    while n > 1 or stack:
        if n > 1:
            stack.append(n)
            n -= 1
        else:
            n = stack.pop()
            result *= n
            n -= 1
    return result
```

### Simplify Path
Simplify Unix path.

```python
def simplify_path(path):
    stack = []
    for part in path.split('/'):
        if part == '..':
            if stack:
                stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)
```

### Tree Traversals Using Stacks (Iterative)

Stacks are used for iterative tree traversals to simulate recursion.

#### Preorder Traversal (Root, Left, Right)
Visit root, then left subtree, then right subtree.

```python
def preorder_iterative(root):
    if not root: return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return result
```

Example: For tree [1,2,3,4,5], result: [1,2,4,5,3]

#### Inorder Traversal (Left, Root, Right)
Visit left subtree, root, then right subtree.

```python
def inorder_iterative(root):
    stack = []
    result = []
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

#### Postorder Traversal (Left, Right, Root)
Visit left subtree, right subtree, then root.

```python
def postorder_iterative(root):
    if not root: return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return result[::-1]
```

Example: For tree [1,2,3,4,5], result: [4,5,2,3,1]

## CP Problems and Solutions

### Valid Parentheses (LeetCode 20)
Check valid parentheses.

(Already covered above)

### Min Stack (LeetCode 155)
Design min stack.

(Already covered)

### Evaluate Reverse Polish Notation (LeetCode 150)
Evaluate RPN.

```python
def eval_rpn(tokens):
    stack = []
    for token in tokens:
        if token not in '+-*/':
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))
    return stack[0]
```

### Daily Temperatures (LeetCode 739)
Next warmer day.

```python
def daily_temperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result
```

### Remove K Digits (LeetCode 402)
Remove k digits to make smallest number.

```python
def remove_kdigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    return ''.join(stack).lstrip('0') or '0'
```

### Asteroid Collision (LeetCode 735)
Simulate asteroid collisions.

```python
def asteroid_collision(asteroids):
    stack = []
    for ast in asteroids:
        while stack and stack[-1] > 0 and ast < 0:
            if stack[-1] < -ast:
                stack.pop()
                continue
            elif stack[-1] == -ast:
                stack.pop()
            break
        else:
            stack.append(ast)
    return stack
```

### Decode String (LeetCode 394)
Decode encoded string.

```python
def decode_string(s):
    stack = []
    current_string = ''
    current_num = 0
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ''
            current_num = 0
        elif char == ']':
            last_string, num = stack.pop()
            current_string = last_string + num * current_string
        else:
            current_string += char
    return current_string
```

## Optimizations

### Choosing Implementation
- **Small Stacks**: List is fine.
- **Large Stacks**: Deque for O(1).
- **Min/Max**: Auxiliary stack.
- **Bounded**: Array with size check.

### Space Efficiency
- Deque avoids list resize overhead.
- Monotonic stacks reduce comparisons.

## Pitfalls and Common Mistakes

### Underflow
Pop from empty stack.

```python
# Bad
top = stack.pop()  # Crash if empty

# Good
top = stack.pop() if stack else None
```

### Overflow
Push to full bounded stack without check.

### Forgetting to Check Empty
Peek without is_empty.

### Wrong Order
Pushing/popping in wrong sequence.

### Thread-Safety
Stacks not thread-safe; use locks.

## Multi-Language Examples

### C++ Stack
```cpp
#include <stack>
using namespace std;

stack<int> s;
s.push(1);  // push
int top = s.top();  // peek
s.pop();  // pop
bool empty = s.empty();
```

### Java Stack
```java
import java.util.Stack;

Stack<Integer> s = new Stack<>();
s.push(1);  // push
int top = s.peek();  // peek
s.pop();  // pop
boolean empty = s.isEmpty();
```

### C++ Min Stack
```cpp
#include <stack>
using namespace std;

class MinStack {
    stack<int> s, min_s;
public:
    void push(int x) {
        s.push(x);
        if (min_s.empty() || x <= min_s.top()) min_s.push(x);
    }
    void pop() {
        if (s.top() == min_s.top()) min_s.pop();
        s.pop();
    }
    int top() { return s.top(); }
    int getMin() { return min_s.top(); }
};
```

### Java Min Stack
```java
import java.util.Stack;

class MinStack {
    Stack<Integer> s = new Stack<>();
    Stack<Integer> min = new Stack<>();
    public void push(int x) {
        s.push(x);
        if (min.isEmpty() || x <= min.peek()) min.push(x);
    }
    public void pop() {
        if (s.peek().equals(min.peek())) min.pop();
        s.pop();
    }
    public int top() { return s.peek(); }
    public int getMin() { return min.peek(); }
}
```

## Practice Section

### Solved Examples

1. **Reverse Stack**
   ```python
   def reverse_stack(stack):
       if not stack: return
       temp = stack.pop()
       reverse_stack(stack)
       insert_at_bottom(stack, temp)

   def insert_at_bottom(stack, item):
       if not stack:
           stack.append(item)
           return
       temp = stack.pop()
       insert_at_bottom(stack, temp)
       stack.append(item)
   ```

2. **Sort Stack**
   ```python
   def sort_stack(stack):
       if not stack: return
       temp = stack.pop()
       sort_stack(stack)
       sorted_insert(stack, temp)

   def sorted_insert(stack, item):
       if not stack or stack[-1] <= item:
           stack.append(item)
           return
       temp = stack.pop()
       sorted_insert(stack, temp)
       stack.append(item)
   ```

3. **Stack Permutations**
   Check if one sequence is stack permutation of another.

   ```python
   def is_stack_permutation(input, output):
       stack = []
       j = 0
       for num in input:
           stack.append(num)
           while stack and stack[-1] == output[j]:
               stack.pop()
               j += 1
       return not stack
   ```

### Walkthrough: Next Greater Element
For [4,5,2,10,8]:
- i=0: stack=[0]
- i=1: 5 > 4, result[0]=5, stack=[1]
- i=2: 2 < 5, stack=[1,2]
- i=3: 10 > 2, result[2]=10; 10 > 5, result[1]=10; stack=[3]
- i=4: 8 < 10, stack=[3,4]
- Result: [5,10,10,-1,-1]

### LeetCode-Style Problems
1. Implement Stack using Queues.
2. Basic Calculator II.
3. Longest Valid Parentheses.
4. Exclusive Time of Functions.
5. Validate Stack Sequences.
6. Car Fleet.

## Interview Questions

- Implement stack using queues.
- Evaluate expression.
- Find next greater element.
- Largest rectangle in histogram.
- Simplify path.
- Decode string.

## Edge Cases

- Empty stack: Pop/peek should handle.
- Single element: Works.
- All increasing: No pops in monotonic.
- All same: Handle duplicates.
- Negative numbers: In expressions.

## Time Complexities in Detail

- Push/Pop/Peek: O(1)
- Next Greater: O(n)
- Histogram: O(n)
- Sort Stack: O(n^2)

## Personal Stories

- In a contest, I used list.pop(0) thinking it was stack; got TLE.
- Forgot sentinel in histogram; got wrong answers.
- Used stack for DFS; avoided recursion limits.

## Code Variations

- Recursive stack reversal.
- Iterative vs recursive implementations.
- Stack with iterators.

## Examples to Practice

1. Implement two stacks in one array.
2. Check if stack can sort array.
3. Find maximum in sliding window (deque).
4. Tower of Hanoi simulation.
5. Expression tree from postfix.

## Comparisons

### Stack vs Queue
- Stack: LIFO, push/pop top.
- Queue: FIFO, enqueue/dequeue front.

### Array vs Linked List Stack
- Array: Fast access, resize overhead.
- Linked: Dynamic, extra space for pointers.

### Monotonic Increasing vs Decreasing
- Increasing: Pop larger.
- Decreasing: Pop smaller.

## Appendices

### Glossary
- **Stack**: LIFO data structure.
- **Push**: Add to top.
- **Pop**: Remove from top.
- **Monotonic Stack**: Maintain order.

### Time Complexities
- Push/Pop: O(1)
- Amortized: O(1) for list.

### References
- Python docs for deque.
- LeetCode stack problems.
- CLRS for stacks.

Personal note: Stacks are simple but powerful; master them for interviews!
