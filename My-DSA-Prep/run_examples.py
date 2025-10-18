# Run Examples: Interactive Snippets from All Topics

import sys
import os

def run_array_examples():
    print("Array Examples")
    arr = [1,2,3,4,5]
    print("Original:", arr)
    arr.append(6)
    print("After append:", arr)
    arr.sort()
    print("Sorted:", arr)
    # More examples...

def run_string_examples():
    print("String Examples")
    s = "hello world"
    print("Split:", s.split())
    print("Upper:", s.upper())
    # More...

def run_basics_examples():
    print("Basics Examples")
    x = 5
    y = 3.14
    print("Int:", x, "Float:", y)
    # More...

def run_conditions_examples():
    print("Conditions Examples")
    num = 10
    if num > 0:
        print("Positive")
    # More...

def run_loops_examples():
    print("Loops Examples")
    for i in range(5):
        print(i)
    # More...

def run_linkedlist_examples():
    print("Linked List Examples")
    # Node class and examples...
    # Since it's code, implement simple LL

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print("Traversal:")
traverse(head)

def run_matrix_examples():
    print("Matrix Examples")
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print("Matrix:")
    for row in matrix:
        print(row)
    # More...

def run_queues_examples():
    print("Queues Examples")
    from collections import deque
    q = deque([1,2,3])
    q.append(4)
    print("Queue:", list(q))
    front = q.popleft()
    print("Dequeued:", front)
    # More...

def run_stacks_examples():
    print("Stacks Examples")
    stack = [1,2,3]
    stack.append(4)
    print("Stack:", stack)
    top = stack.pop()
    print("Popped:", top)
    # More...

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_examples.py <topic>")
        print("Topics: arrays, strings, basics, conditions, loops, linkedlist, matrix, queues, stacks")
        return

    topic = sys.argv[1].lower()
    if topic == "arrays":
        run_array_examples()
    elif topic == "strings":
        run_string_examples()
    elif topic == "basics":
        run_basics_examples()
    elif topic == "conditions":
        run_conditions_examples()
    elif topic == "loops":
        run_loops_examples()
    elif topic == "linkedlist":
        run_linkedlist_examples()
    elif topic == "matrix":
        run_matrix_examples()
    elif topic == "queues":
        run_queues_examples()
    elif topic == "stacks":
        run_stacks_examples()
    else:
        print("Invalid topic")

if __name__ == "__main__":
    main()

# Expand with more detailed examples, outputs, and CLI enhancements to reach 1000 lines...
