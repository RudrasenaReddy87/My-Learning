# Conditions: Making Decisions in Code

Greetings, logic builder! Conditions control program flow with if, else, elif. They evaluate expressions and execute blocks. Why important? Decisions are everywhere – from games to algorithms. Use cases: Grading systems, validations. In CP, for branching logic.

## Introduction

Conditions use boolean expressions. Nested for complex logic. In Python, indentation defines blocks. Conditions return True or False.

Key properties:
- Evaluated left to right.
- Short-circuiting with and/or.
- Can be chained with elif.

Personal note: Conditions are the heart of logic; I once forgot else and debugged for hours.

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
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(grade)
```

## Nested Conditions

If inside if for complex logic.

Explanation: Nested conditions allow for multi-level decision making. The inner if is only executed if the outer condition is true. This can create a tree-like structure for logic.

Example: Nested if for number classification.
```python
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Non-positive")
```

Indentation matters; use 4 spaces. Avoid too deep nesting (max 3-4 levels) for readability; refactor into functions if needed.

Complexity: O(1) for simple conditions, but logical depth affects readability.

Tip: In CP, nested conditions are common for multi-criteria checks, like in graph problems for node types.

## Ternary Operator

One-liner conditional: value_if_true if condition else value_if_false

Explanation: The ternary operator (also called conditional expression) provides a concise way to write simple if-else statements. It's useful for assigning values based on a condition without multiple lines.

Example: Max of two using ternary.
```python
a, b = 5, 3
max_val = a if a > b else b
print(max_val)  # Output: 5
```

Nested ternary (use sparingly):
```python
status = "adult" if age >= 18 else ("teen" if age >= 13 else "child")
```

Pros: Concise, readable for simple cases.
Cons: Hard to read if nested deeply.
When to use: In lambda functions, list comprehensions, or simple assignments.

## Truthy and Falsy Values

Non-booleans: 0, empty lists, None are falsy; others truthy.

Explanation: In Python, conditions don't require explicit booleans. Any value can be evaluated as True or False. Falsy values include: False, None, 0, 0.0, '', [], {}, set(), range(0). All others are truthy.

Example: Check if list is empty.
```python
lst = []
if lst:  # Equivalent to if len(lst) > 0
    print("Not empty")
else:
    print("Empty")  # Output: Empty
```

Example: Check string.
```python
s = ""
if s:
    print("Non-empty string")
else:
    print("Empty string")  # Output: Empty string
```

Tip: Use this for quick checks, but be aware of edge cases like [0] which is truthy despite containing falsy.

## Short-Circuit Evaluation

and/or stop early.

Explanation: Logical operators evaluate from left to right and short-circuit. For 'and', if the first operand is falsy, the second isn't evaluated. For 'or', if the first is truthy, the second isn't evaluated. This can prevent errors, like division by zero.

Example: Safe division.
```python
denom = 0
if denom != 0 and 10 / denom > 1:
    print("Greater than 1")  # Second part not evaluated, no ZeroDivisionError
else:
    print("Invalid denominator")
```

Example: Default value.
```python
name = None
full_name = name or "Anonymous"
print(full_name)  # Output: Anonymous
```

In CP: Use to avoid unnecessary computations, e.g., if n > 1 and arr[0] > arr[1].

## Switch Statements

Python uses if/elif chains. In C++/Java, switch for exact matches.

Explanation: Switch statements are for multi-way branching on a single value. Python 3.10+ has match-case, but traditionally uses if-elif. In C++, switch on integers/chars, with fall-through unless break.

Python (if-elif equivalent):
```python
day = 1
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
# etc.
```

Python 3.10+ match-case:
```python
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid")
```

C++ example:
```cpp
int day = 1;
switch (day) {
    case 1:
        cout << "Monday";
        break;
    case 2:
        cout << "Tuesday";
        break;
    default:
        cout << "Invalid";
}
```

Pros: Cleaner for many cases.
Cons: Limited to equality checks in traditional switch.

## Advanced Examples

Complex conditions with multiple operators.

Example: Determine triangle type.
```python
a, b, c = 3, 4, 5
if a + b > c and a + c > b and b + c > a:  # Valid triangle
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")
```

Example: BMI calculator.
```python
height, weight = 1.75, 70
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI: {bmi:.2f}, Category: {category}")
```

## Competitive Programming Problems

Conditions are crucial for problem-solving logic.

### Leap Year Check
Explanation: A year is leap if divisible by 4, but not 100 unless 400.

```python
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

### Grading System (Expanded)
Explanation: Assign grades based on score ranges.

```python
score = 85
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid'
print(f"Grade: {grade}")
```

### Number Classification (Armstrong, Prime, etc.)
Explanation: Classify based on properties.

```python
num = 153
if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
    # Prime check
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Composite")
                break
        else:
            print("Prime")
    # Armstrong
    digits = len(str(num))
    arm = sum(int(d)**digits for d in str(num))
    if arm == num:
        print("Armstrong")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

### Age Category with Discounts
Explanation: Categories for eligibility.

```python
age = 25
income = 50000
if age < 13:
    category = "Child"
    discount = 50
elif 13 <= age < 20:
    category = "Teen"
    discount = 20
elif 20 <= age < 65:
    category = "Adult"
    discount = 10 if income < 60000 else 0
else:
    category = "Senior"
    discount = 30
print(f"{category}, Discount: {discount}%")
```

### Password Strength Checker
Explanation: Check length, digits, uppercase.

```python
password = "Pass123"
strength = "Strong"
if len(password) < 8:
    strength = "Weak"
elif not any(c.isdigit() for c in password):
    strength = "Medium"
elif not any(c.isupper() for c in password):
    strength = "Medium"
else:
    strength = "Strong"
print(f"Password strength: {strength}")
```

### FizzBuzz
Explanation: Print numbers 1-100, Fizz for multiples of 3, Buzz for 5, FizzBuzz for both.

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

## Edge Cases

- Empty string: "" is falsy, but "0" is truthy.
- Zero: 0 is falsy, but [0] is truthy.
- None: Falsy.
- NaN in floats: Not directly, but math.isnan().
- Large numbers: Python handles arbitrary size, no issue.
- Floating points: Avoid exact == due to precision; use abs(a - b) < epsilon or within range.

Example: Float comparison.
```python
a = 0.1 + 0.2
if abs(a - 0.3) < 1e-9:
    print("Equal")
```

## Tips, Tricks, and Pitfalls

- Use parentheses for clarity: if (a > b) and (c < d)
- Avoid deep nesting; use early returns or functions.
- Pitfall: Assignment = vs comparison == (common bug).
- Trick: Use all() for all true, any() for any true in iterables.
  ```python
  if all(x > 0 for x in lst):
      print("All positive")
  ```
- In CP: Conditions for input validation, e.g., if n < 1 or n > 10**5: handle error.
- Pitfall: Mutable default arguments, but for conditions, watch truthy of lists.
- Trick: Chained comparisons: if 0 < x < 10 (Python-specific).
- Best practice: Write readable conditions; break complex ones.

## More Topics

### Conditional Expressions in Loops
Explanation: Conditions inside loops for filtering.

```python
numbers = [1, 2, 3, 4, 5]
evens = []
for i in numbers:
    if i % 2 == 0:
        evens.append(i)
print(evens)  # [2, 4]
```

List comprehension equivalent:
```python
evens = [i for i in numbers if i % 2 == 0]
```

### Guard Clauses
Explanation: Early returns to reduce nesting.

```python
def divide(a, b):
    if b == 0:
        return None  # Guard
    return a / b
```

### Assertions for Debugging
Explanation: assert checks conditions, raises AssertionError if false.

```python
def factorial(n):
    assert n >= 0, "n must be non-negative"
    if n == 0:
        return 1
    return n * factorial(n-1)
```

In CP: Use sparingly, as assertions may be disabled in release.

### Bitwise vs Logical Operators
Explanation: & | ~ for bits, and or not for logic. Use logical for conditions.

Example: Bitwise and.
```python
if x & 1:  # Odd number
    print("Odd")
```

But prefer x % 2 == 1 for clarity.

## Code Variations

- Chained comparisons: if 0 < x < 10: print("In range")
- Multiple conditions: if a or b or c:  # Any true
- Not: if not condition:  # Negation
- Walrus operator (Python 3.8+): if (n := len(s)) > 10:

Example: Walrus.
```python
if (length := len(data)) > 1000:
    print(f"Large data: {length}")
```

## Examples to Practice

1. FizzBuzz (above).
2. Check if palindrome.
   ```python
   s = "radar"
   if s == s[::-1]:
       print("Palindrome")
   ```
3. Sort three numbers using conditions.
   ```python
   a, b, c = 3, 1, 2
   if a > b:
       a, b = b, a
   if a > c:
       a, c = c, a
   if b > c:
       b, c = c, b
   print(a, b, c)  # 1 2 3
   ```
4. BMI calculator (above).
5. Voting eligibility.
   ```python
   age = 17
   citizen = True
   if age >= 18 and citizen:
       print("Eligible to vote")
   else:
       print("Not eligible")
   ```

## Interview Questions

- Implement max of three using conditions.
- Write a function to check if number is perfect square.
- Handle multiple conditions in a single if.
- Difference between == and is.
- When to use elif vs nested if.

## Common Mistakes and Pitfalls

- Off-by-one in ranges, but for conditions: wrong operator > vs >=.
- Forgetting else: All paths not covered.
- Deep nesting leading to pyramid of doom.
- Using and/or with assignment: if x = 5 and y > 0 (SyntaxError).
- Truthy confusion: if [[]]: True, but empty nested is falsy? No, [[]] truthy.
- Floating point: if 0.1 + 0.2 == 0.3: False.

Personal story: In a contest, I used = instead of == and got wrong answer; always lint code.

## Time Complexities

Conditions are O(1), but in loops: O(n) if inside loop.

## Sorting Algorithm Comparison (Wait, no - this is for conditions, but link to logic in sorts)

Conditions are used in sorting algorithms for comparisons.

## Conditions vs Other Control Flows

- vs Loops: Conditions for decisions, loops for repetition.
- vs Functions: Conditions inside functions for branching.

## Final Tips

- Test all branches with unit tests.
- Use meaningful variable names in conditions.
- In CP, optimize by ordering conditions (most likely first).
- Readability over cleverness.
- Practice on LeetCode problems tagged "conditionals".

This covers conditions thoroughly. Practice implementing logic puzzles. Keep coding!
