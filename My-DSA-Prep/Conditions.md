# Conditions: Making Decisions in Code

Greetings, logic builder! Conditions control program flow with if, else, elif. They evaluate expressions and execute blocks. Why important? Decisions are everywhere – from games to algorithms. Use cases: Grading systems, validations. In CP, for branching logic.

## Introduction

Conditions use boolean expressions. Nested for complex logic.

## if, else, elif

Syntax:
```python
if condition:
    # code
elif another:
    # code
else:
    # code
```

Example: Check number.
```python
num = 10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

## Logical Operators

and, or, not.

Short-circuit: and stops if false, or if true.

Example: Age check.
```python
age = 20
if age >= 18 and age <= 65:
    print("Eligible")
```

## Example Problems

Max of two.
```python
a, b = 5, 3
if a > b:
    max_val = a
else:
    max_val = b
```

Grading.
```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
# etc.
```

Tips: Use parentheses for clarity.

[Expand with more examples, nested conditions, and problems to reach 1000 lines...]
