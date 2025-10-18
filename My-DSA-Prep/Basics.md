# Programming Basics: The Foundation of Coding

Hey coder! Before diving into complex data structures, let's solidify the basics. This covers variables, data types, operators, typecasting, input/output, comments, and more – the building blocks. Why important? Without these, you can't write a single line of code. Use cases: Every program starts here. In CP, understanding types prevents bugs. Let's make this intuitive with examples, tips, and personal insights from my early coding days.

## Introduction

Programming basics are the syntax and concepts every language shares. Variables store data, types define what data, operators manipulate, typecasting converts. Importance: Enables logic building. Use cases: Calculations, decisions, storage. In Python, basics are straightforward, but mastering them avoids silly errors.

Personal note: I once spent hours debugging because I forgot Python is case-sensitive; basics matter!

## Variables

Containers for data. Store values that can change.
```python
x = 5
name = "Alice"
```
Rules: Start with letter/underscore, no keywords. Case-sensitive.

Example: Assign and print.
```python
age = 25
print(age)  # 25
```

Multiple assignment.
```python
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3
```

Constants: Use uppercase, but Python doesn't enforce.
```python
PI = 3.14159
```

## Data Types

### int
Whole numbers. No decimal.
Range: Unlimited in Python (unlike C++).

Example: 42
Operations: +, -, *, //

### float
Decimals. Floating-point.
Precision: Double (64-bit).

Example: 3.14
Pitfall: Floating-point errors, e.g., 0.1 + 0.2 != 0.3

### str
Strings. Sequence of characters.
Immutable.

Example: "text"
Concat: "hello" + "world" = "helloworld"

### bool
True/False. From comparisons.

Example: True
Values: True (1), False (0)

### None
Represents absence of value.

Example: result = None

### Complex
For math: real + imag j

Example: 3 + 4j

## Operators

### Arithmetic
+, -, *, / (float div), // (floor div), % (mod), ** (power)

Example: 5 + 3 = 8
5 // 2 = 2
5 % 2 = 1
2 ** 3 = 8

### Comparison
==, !=, <, >, <=, >=
Return bool.

Example: 5 > 3  # True
"abc" == "abc"  # True

### Logical
and, or, not
Short-circuit: and stops on False, or on True.

Example: True and False  # False
not True  # False

### Bitwise
&, |, ^, ~, <<, >>

Example: 5 & 3 = 1 (binary)

### Membership
in, not in

Example: 'a' in "apple"  # True

### Identity
is, is not

Example: x is None

### Assignment
=, +=, -=, *=, /=, //=, %=, **=

Example: x += 1  # x = x + 1

## Typecasting

Convert types explicitly.
int(x), float(x), str(x), bool(x)

Example: int("123")  # 123
float("3.14")  # 3.14
str(42)  # "42"
bool(0)  # False

Implicit: Python does some, but better explicit.

Pitfall: int("abc") raises ValueError.

## Input and Output

### Input
input() reads string from user.
```python
name = input("Enter name: ")
print("Hello", name)
```

For numbers: int(input())

### Output
print() displays.
```python
print("Hello", "world", sep=" ", end="\n")
```

Formatted: f-strings.
```python
age = 25
print(f"I am {age} years old")
```

## Comments

Single: #
Multi: """ """

Example:
```python
# This is a comment
"""
Multi-line
comment
"""
```

## Control Flow Basics

### if
```python
if condition:
    # code
```

### if-else
```python
if condition:
    # code
else:
    # code
```

### if-elif-else
```python
if cond1:
    # code
elif cond2:
    # code
else:
    # code
```

## Loops Basics

### for
```python
for i in range(5):
    print(i)
```

### while
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## Functions Basics

Define with def.
```python
def greet(name):
    return f"Hello {name}"

print(greet("Alice"))
```

## Modules and Imports

Import libraries.
```python
import math
print(math.sqrt(16))
```

From import.
```python
from math import pi
print(pi)
```

## Exceptions Basics

Try-except.
```python
try:
    x = int("abc")
except ValueError:
    print("Invalid")
```

## File I/O Basics

Read file.
```python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
```

Write.
```python
with open("file.txt", "w") as f:
    f.write("Hello")
```

## Common Mistakes

- Uninitialized variables: NameError.
- Type mismatches: TypeError.
- Indentation errors: Python-specific.
- Off-by-one in loops.

Tips: Use descriptive names, check types with type(), debug with print().

## Examples

Calculate area.
```python
length = float(input("Length: "))
width = float(input("Width: "))
area = length * width
print(f"Area: {area}")
```

FizzBuzz.
```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

## Advanced Basics

### List Comprehensions
```python
squares = [x**2 for x in range(10)]
print(squares)  # [0,1,4,9,...]
```

### Dictionaries
Key-value pairs.
```python
d = {"a": 1, "b": 2}
print(d["a"])
```

### Sets
Unique elements.
```python
s = {1,2,3}
s.add(4)
```

### Tuples
Immutable lists.
```python
t = (1,2,3)
```

### Lambda Functions
Anonymous.
```python
add = lambda x, y: x + y
print(add(2,3))  # 5
```

### Generators
Yield values.
```python
def gen():
    for i in range(3):
        yield i

for x in gen():
    print(x)
```

## Tips for CP

- Use sys.stdin for fast input.
- Avoid global variables.
- Know operator precedence.
- Practice with HackerRank basics.

Personal tip: Start with small programs, build up.

## Operator Precedence

Operators have precedence; higher precedence evaluated first. Use parentheses for clarity.

Order (high to low): **, ~, +, -, *, @, /, //, %, +, -, &, ^, |, <=, <, >, >=, ==, !=, =, %=, /=, //=, -=, +=, *=, **=, &=, ^=, |=, <<=, >>=, :=, is, is not, in, not in, not, or, and, if-else.

Example: 2 + 3 * 4 = 14 (not 20).

Personal note: I once forgot precedence and got wrong results in a math problem.

## Bitwise Tricks

Useful in CP for efficiency.

- Check even: x & 1 == 0
- Toggle bit: x ^ (1 << pos)
- Count bits: bin(x).count('1')

Example: Is power of 2? x & (x-1) == 0

## String Formatting Variations

Beyond f-strings.

- % formatting: "Hello %s" % name
- str.format(): "Hello {}".format(name)
- Template: from string import Template; Template("Hello $name").substitute(name=name)

Example: Align: "{:>10}".format("hi")  # '        hi'

## Error Handling Details

Exceptions: BaseException, Exception, ValueError, etc.

Multiple except: except (ValueError, TypeError):

Finally: Always runs.

Raise: raise ValueError("msg")

Example:
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("Done")
```

## File Modes

Modes: 'r' read, 'w' write (overwrite), 'a' append, 'x' exclusive create, 'b' binary, 't' text.

Example: 'rb' read binary.

With open: Automatically closes.

## Decorators Basics

Modify functions.

```python
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hi():
    print("Hi")

say_hi()  # Before Hi After
```

## Context Managers

With statement for resources.

```python
class MyContext:
    def __enter__(self):
        print("Enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit")

with MyContext():
    print("Inside")
```

Built-in: with open() as f:

## More Examples

### Factorial Recursive
```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
```

### Palindrome Check
```python
def is_pal(s):
    return s == s[::-1]
```

### Sum of List
```python
nums = [1,2,3]
total = sum(nums)
```

### Dictionary Operations
```python
d = {'a':1}
d['b'] = 2
print(d.get('c', 0))  # 0
```

### Set Operations
```python
s1 = {1,2}
s2 = {2,3}
print(s1 | s2)  # {1,2,3}
```

## Edge Cases

- Division by zero: ZeroDivisionError
- Index out of range: IndexError
- Key not found: KeyError
- Empty inputs: Handle with defaults

## Interview Questions

- What is None?
- Difference between is and ==?
- How to swap two variables? a, b = b, a

## Common Patterns

- Ternary: x if cond else y
- List slicing: arr[::2] even indices
- Unpacking: *args, **kwargs

## Performance Tips

- Use list for dynamic, tuple for immutable.
- Avoid global vars in functions.
- Profile with time module.

## Debugging

- Use pdb: import pdb; pdb.set_trace()
- Print statements.
- Assertions: assert condition, "msg"

## Libraries Basics

- random: random.randint(1,10)
- datetime: datetime.now()
- json: json.dumps(dict)

Example: Random choice.
```python
import random
print(random.choice([1,2,3]))
```

## CP Specific Tips

- Fast input: sys.stdin.read().split()
- Output buffering: Use print with flush=False
- Memory: Use generators for large data

Personal anecdote: In a contest, slow input cost me time; switched to sys.stdin and won.

## More Advanced Topics

### Recursion Basics

Function calls itself.

Example: Fibonacci.
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

Pitfall: Stack overflow for large n.

### OOP Basics

Classes: Blueprint for objects.

```python
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hi {self.name}"

p = Person("Alice")
print(p.greet())
```

Inheritance: class Student(Person): pass

## Final Tips

- Read PEP 8 for style.
- Practice daily.
- Understand underlying concepts.

This should give a solid foundation. Keep coding!

## More on Data Structures Basics

### Lists in Depth

Lists are mutable sequences.

Methods: append, insert, remove, pop, index, count, sort, reverse, clear, copy.

Example: Insert at index.
```python
lst = [1,2,3]
lst.insert(1, 99)  # [1,99,2,3]
```

Slicing: lst[1:3] = [99,2]

List comprehension with condition.
```python
evens = [x for x in range(10) if x % 2 == 0]
```

Nested lists: matrix = [[1,2], [3,4]]

### Dictionaries in Depth

Keys must be hashable.

Methods: keys(), values(), items(), get(), pop(), update(), clear().

Example: Update.
```python
d = {'a':1}
d.update({'b':2})  # {'a':1, 'b':2}
```

Dict comprehension.
```python
squares = {x: x**2 for x in range(5)}
```

### Sets in Depth

Unordered, unique.

Methods: add, remove, discard, pop, clear, union, intersection, difference, symmetric_difference.

Example: Union.
```python
s1 = {1,2}
s2 = {2,3}
print(s1.union(s2))  # {1,2,3}
```

Frozen set: Immutable set.

### Tuples in Depth

Immutable lists.

Methods: count, index.

Packing/unpacking.
```python
t = 1,2,3
a, b, c = t
```

## Functions Advanced

### Parameters

Positional, keyword, default, *args, **kwargs.

Example:
```python
def func(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)

func(1, 2, 3, 4, c=5)  # 1 2 (3,4) {'c':5}
```

### Scope

Local, global, nonlocal.

Global keyword to modify global var.

### Recursion with Memoization

Use lru_cache for efficiency.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

## Modules and Packages

Packages: Directories with __init__.py

Import from package: from package.module import func

Standard library: os, sys, re, etc.

## More Examples

### Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Prime Check
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
```

### File Read Lines
```python
with open("file.txt") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

### JSON Handling
```python
import json
data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json') as f:
    loaded = json.load(f)
```

## More Advanced Topics

### Iterators and Iterables

Iterables: Can be looped over.

Iterators: Have __next__().

Example: iter(list)

### Comprehensions Advanced

Nested: [x+y for x in range(3) for y in range(3)]

Dict: {k: v for k, v in zip(keys, values)}

Set: {x**2 for x in range(10)}

### Closures

Function inside function, inner accesses outer vars.

```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add5 = outer(5)
print(add5(3))  # 8
```

### Map, Filter, Reduce

Map: apply function to each.
```python
list(map(lambda x: x**2, [1,2,3]))  # [1,4,9]
```

Filter: select based on condition.
```python
list(filter(lambda x: x > 2, [1,2,3,4]))  # [3,4]
```

Reduce: cumulative.
```python
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3,4])  # 10
```

### Regular Expressions

import re

Search: re.search(pattern, string)

Find all: re.findall(pattern, string)

Example: emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)

## Performance and Optimization

- Time complexity: O(1), O(log n), O(n), etc.

- Space: In-place vs extra space.

- Profiling: import cProfile; cProfile.run('func()')

## Best Practices

- DRY: Don't repeat yourself.

- KISS: Keep it simple.

- Use meaningful names.

- Comment complex logic.

- Test edge cases.

## Common Pitfalls in CP

- Integer overflow: Use long in other langs.

- Floating point precision.

- Time limits: Optimize algorithms.

- Memory limits: Use efficient data structures.

## Resources

- Official Python docs.

- LeetCode, HackerRank for practice.

- Books: "Automate the Boring Stuff", "Python Crash Course".

This comprehensive guide should cover basics thoroughly. Happy coding!

## Advanced String Operations

Strings are immutable, so operations return new strings.

### String Methods Deep Dive

- capitalize(): First char upper, rest lower.
- casefold(): Aggressive lower for case-insensitive compare.
- center(width, fillchar): Center in width.
- count(sub, start, end): Count occurrences.
- encode(encoding, errors): To bytes.
- endswith(suffix, start, end): Check end.
- expandtabs(tabsize): Expand tabs to spaces.
- find(sub, start, end): Index or -1.
- format(*args, **kwargs): Format string.
- format_map(mapping): Format with mapping.
- index(sub, start, end): Like find, but error.
- isalnum(): Alpha and numeric.
- isalpha(): Alphabetic.
- isascii(): ASCII chars.
- isdecimal(): Decimal digits.
- isdigit(): Digits.
- isidentifier(): Valid identifier.
- islower(): Lowercase.
- isnumeric(): Numeric chars.
- isprintable(): Printable.
- isspace(): Whitespace.
- istitle(): Title case.
- isupper(): Uppercase.
- join(iterable): Join with separator.
- ljust(width, fillchar): Left justify.
- lower(): Lowercase.
- lstrip(chars): Left strip.
- maketrans(x, y, z): Translation table.
- partition(sep): Split at first sep.
- replace(old, new, count): Replace.
- rfind(sub, start, end): Right find.
- rindex(sub, start, end): Right index.
- rjust(width, fillchar): Right justify.
- rpartition(sep): Right partition.
- rsplit(sep, maxsplit): Right split.
- rstrip(chars): Right strip.
- split(sep, maxsplit): Split.
- splitlines(keepends): Split lines.
- startswith(prefix, start, end): Check start.
- strip(chars): Strip both.
- swapcase(): Swap case.
- title(): Title case.
- translate(table): Translate chars.
- upper(): Uppercase.
- zfill(width): Zero fill.

Example: Check if string is title case.
```python
"hello world".istitle()  # False
"Hello World".istitle()  # True
```

## More on Numbers

### Int Operations

- Bit length: x.bit_length()
- To bytes: x.to_bytes(length, byteorder)
- From bytes: int.from_bytes(bytes, byteorder)

### Float Operations

- As integer ratio: x.as_integer_ratio()
- Is integer: x.is_integer()
- Hex: x.hex()

### Complex Operations

- Conjugate: z.conjugate()
- Real, imag: z.real, z.imag

## Collections Module

Useful for advanced data structures.

- Counter: Count elements.
```python
from collections import Counter
c = Counter([1,2,2,3])  # {2:2, 1:1, 3:1}
```

- defaultdict: Default values.
```python
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1  # 1
```

- deque: Double-ended queue.
```python
from collections import deque
dq = deque([1,2,3])
dq.appendleft(0)  # [0,1,2,3]
```

- namedtuple: Tuple with names.
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)  # 1
```

## Itertools Module

For efficient looping.

- product: Cartesian product.
```python
from itertools import product
list(product([1,2], [3,4]))  # [(1,3),(1,4),(2,3),(2,4)]
```

- permutations: Permutations.
```python
from itertools import permutations
list(permutations([1,2,3], 2))  # All pairs
```

- combinations: Combinations.
```python
from itertools import combinations
list(combinations([1,2,3], 2))  # [(1,2),(1,3),(2,3)]
```

- cycle: Infinite cycle.
```python
from itertools import cycle
c = cycle([1,2,3])
next(c)  # 1, then 2,3,1,...
```

## Functools Module

Higher-order functions.

- partial: Partial application.
```python
from functools import partial
add5 = partial(lambda x, y: x + y, 5)
add5(3)  # 8
```

- reduce: As above.

- wraps: For decorators.

## OS and Sys Modules

- os.getcwd(): Current directory.
- os.listdir(path): List files.
- os.path.join: Join paths.
- sys.argv: Command line args.
- sys.exit(): Exit program.

## Time and Datetime

- time.time(): Current time.
- datetime.now(): Current datetime.
- timedelta: Time differences.

Example:
```python
from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(days=1)
```

## Random Module

- random.random(): 0 to 1.
- random.randint(a,b): Int in range.
- random.choice(seq): Random choice.
- random.shuffle(lst): Shuffle list.
- random.seed(x): Set seed.

## Math Module

- math.pi, math.e
- math.sqrt(x)
- math.sin(x), etc.
- math.gcd(a,b)
- math.lcm(a,b)  # Python 3.9+
- math.comb(n,k): Combinations
- math.perm(n,k): Permutations

## Heapq Module

For heaps.

- heapq.heappush(heap, item)
- heapq.heappop(heap)
- heapq.heapify(lst)

Example: Min heap.
```python
import heapq
heap = [3,1,4,1,5]
heapq.heapify(heap)  # [1,1,4,3,5]
heapq.heappush(heap, 2)  # [1,1,2,3,4,5]
```

## Bisect Module

For binary search on lists.

- bisect.bisect_left(a, x): Insert position.
- bisect.insort(a, x): Insert sorted.

## Copy Module

- copy.copy(): Shallow copy.
- copy.deepcopy(): Deep copy.

## Pickle Module

Serialize objects.

- pickle.dump(obj, file)
- pickle.load(file)

## CSV Module

For CSV files.

```python
import csv
with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age'])
```

## Argparse Module

Command line arguments.

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--name')
args = parser.parse_args()
print(args.name)
```

## Logging Module

For logging.

```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is info")
```

## Threading Basics

For concurrency.

```python
import threading
def worker():
    print("Worker")

t = threading.Thread(target=worker)
t.start()
t.join()
```

## Subprocess Module

Run external commands.

```python
import subprocess
result = subprocess.run(['echo', 'hello'], capture_output=True, text=True)
print(result.stdout)
```

## More Algorithms

### Merge Sort
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### Quick Sort
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### DFS and BFS

For graphs (using dict).

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

## Data Structures Implementations

### Stack with List
```python
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
```

### Queue with Deque
```python
from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
    def is_empty(self):
        return len(self.items) == 0
```

### Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
```

## Design Patterns Basics

### Singleton
```python
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Factory
```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

def animal_factory(type):
    if type == 'dog':
        return Dog()
    elif type == 'cat':
        return Cat()
```

## Testing with Unittest

```python
import unittest

class TestBasics(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
```

## Virtual Environments

- python -m venv env
- env\Scripts\activate (Windows)
- pip install package

## Packaging with Setuptools

Create setup.py.

## Web Basics with Flask

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
```

## Database with SQLite

```python
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
conn.commit()
conn.close()
```

## GUI with Tkinter

```python
import tkinter as tk

root = tk.Tk()
label = tk.Label(root, text="Hello")
label.pack()
root.mainloop()
```

## Networking with Sockets

```python
import socket

# Server
s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
conn, addr = s.accept()
conn.send(b'Hello')
conn.close()

# Client
s = socket.socket()
s.connect(('localhost', 12345))
print(s.recv(1024))
s.close()
```




