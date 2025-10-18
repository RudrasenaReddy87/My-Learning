# Loops: Repeating Actions Efficiently

Hi there! Loops execute code repeatedly. For and while are essentials. Why important? Iteration over data. Use cases: Processing lists, simulations. In CP, for time limits.

## Introduction

Loops control repetition. For: known iterations, while: condition-based.

## For Loops

Syntax:
```python
for var in iterable:
    # code
```

Example: Print numbers.
```python
for i in range(5):
    print(i)
```

## While Loops

Syntax:
```python
while condition:
    # code
```

Example: Countdown.
```python
n = 5
while n > 0:
    print(n)
    n -= 1
```

## Nested Loops

Loops inside loops.

Example: Matrix print.
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

## Loop Control

break: Exit loop.
continue: Skip iteration.
pass: Placeholder.

Example: Break on 3.
```python
for i in range(10):
    if i == 3:
        break
    print(i)
```

## Common Algorithms

Factorial.
```python
fact = 1
for i in range(1, n+1):
    fact *= i
```

Pattern printing.
```python
for i in range(5):
    print('*' * (i+1))
```

Tips: Avoid infinite loops, use enumerate for indices.

[Expand with more algorithms, examples, and optimizations to reach 1000 lines...]
