# Loops: Repeating Actions Efficiently

Hey there, iterative thinker! Loops are the backbone of programming, allowing us to execute code repeatedly until a condition is met. They're essential for processing data, simulations, and algorithms. In competitive programming (CP), loops handle iterations within time limits, making efficiency crucial. Let's master loops with examples, optimizations, and pitfalls.

## Introduction to Loops

Loops control the flow of execution by repeating a block of code. There are several types: for loops for known iterations, while loops for condition-based repetition, and nested loops for multi-dimensional operations.

### Why Loops Matter
- **Iteration Over Data**: Process arrays, lists, strings, or files.
- **Simulations**: Model real-world processes like games or physics.
- **Algorithms**: Implement sorting, searching, and dynamic programming.
- **CP Importance**: Handle large inputs (e.g., 10^5 elements) within time limits (1-2 seconds).

### Types of Loops
- **For Loop**: Best for fixed iterations.
- **While Loop**: Best for unknown iterations based on conditions.
- **Nested Loops**: Loops inside loops for grids or matrices.
- **Infinite Loops**: Loops that run forever (intentional or by mistake).

### Loop Invariants
A property that holds before and after each iteration. Useful for proving correctness.

## For Loops in Detail

For loops iterate over iterables like lists, ranges, or strings.

### Basic Syntax
```python
for variable in iterable:
    # code block
```

### Using range()
Generates a sequence of numbers.

```python
for i in range(5):  # 0 to 4
    print(i)
```

With start, stop, step:
```python
for i in range(1, 10, 2):  # 1, 3, 5, 7, 9
    print(i)
```

### enumerate()
Adds index to iteration.

```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### zip()
Iterate over multiple iterables simultaneously.

```python
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
```

### Iterating Over Data Structures
- **Lists**: for item in my_list:
- **Strings**: for char in my_string:
- **Dictionaries**: for key, value in my_dict.items():
- **Sets**: for item in my_set:

Example: Sum of list
```python
nums = [1, 2, 3, 4, 5]
total = 0
for num in nums:
    total += num
print(total)  # 15
```

## While Loops in Detail

While loops repeat as long as a condition is true.

### Basic Syntax
```python
while condition:
    # code block
```

### Examples
Countdown:
```python
n = 5
while n > 0:
    print(n)
    n -= 1
print("Blast off!")
```

### Infinite Loops
Run forever unless broken.

```python
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

### Sentinel-Controlled Loops
Use a sentinel value to stop.

```python
total = 0
while True:
    num = int(input("Enter number (0 to stop): "))
    if num == 0:
        break
    total += num
print(f"Total: {total}")
```

### Do-While Equivalent
Python doesn't have do-while, but simulate it:

```python
while True:
    # code
    if not condition:
        break
```

## Nested Loops

Loops inside loops, common for 2D data.

### Basic Nested For
```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
```

Output:
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)

### Matrix Operations
Transpose a matrix:
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[0]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        transpose[j][i] = matrix[i][j]
print(transpose)
```

### Time Complexity
Nested loops: O(n^2) for n x n, O(n*m) for n x m. Optimize by reducing nesting or using early exits.

## Loop Control Statements

### break
Exit the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0-4
```

### continue
Skip to next iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # Prints 0,1,3,4
```

### pass
Placeholder, does nothing.

```python
for i in range(5):
    if i % 2 == 0:
        pass  # Even, do nothing
    else:
        print(i)  # Odd
```

## Optimizations and Best Practices

### Loop Unrolling
Manually expand loop to reduce overhead (rarely needed in Python).

### Reducing Nested Loops
Use single loops where possible, e.g., flatten 2D to 1D.

### Early Termination
Break when condition met to save time.

### Avoid Modifying Loop Variables
Can cause infinite loops or skipped iterations.

### Use Built-ins
Prefer sum(), max() over manual loops for simplicity.

Example: Sum with built-in
```python
nums = [1, 2, 3, 4, 5]
print(sum(nums))  # 15
```

## Common Algorithms Using Loops

### Factorial
```python
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(5))  # 120
```

### Fibonacci
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)
```

### Prime Checking
```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(17))  # True
```

### Linear Search
```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

### Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

### Pattern Printing
Triangle:
```python
for i in range(5):
    print('*' * (i+1))
```

Pyramid:
```python
for i in range(5):
    print(' ' * (4-i) + '*' * (2*i+1))
```

### Sum/Product of Arrays
```python
nums = [1, 2, 3, 4, 5]
total = 0
product = 1
for num in nums:
    total += num
    product *= num
print(f"Sum: {total}, Product: {product}")
```

## Pitfalls and Common Mistakes

### Infinite Loops
- **Cause**: Condition never false.
- **Fix**: Ensure condition changes.

```python
# Bad
i = 0
while i < 5:
    print(i)
    # Forgot i += 1

# Good
i = 0
while i < 5:
    print(i)
    i += 1
```

### Off-by-One Errors
- **Cause**: Loop runs one too many/few times.
- **Fix**: Check bounds carefully.

```python
# Wrong: range(1, n) for 1 to n-1
for i in range(1, n+1):  # Correct
```

### Modifying Loop Variables
- **Cause**: Changing i inside loop.
- **Fix**: Use separate variables.

### Performance Issues
- **Cause**: Nested loops on large data.
- **Fix**: Optimize or use better algorithms.

### Forgetting to Initialize
- **Cause**: Using uninitialized variables.
- **Fix**: Initialize before loop.

## Advanced Topics

### Iterators and Generators
Generators yield values lazily.

```python
def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for num in my_range(5):
    print(num)
```

### Recursion vs Loops
Recursion for trees, loops for linear. Recursion can cause stack overflow.

### Loop Invariants
For binary search:
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# Invariant: target in arr[left..right] if exists
```

### Parallel Processing Basics
Use multiprocessing for CPU-bound tasks, but loops are sequential.

## Multi-Language Examples

### C++ For Loop
```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 5; i++) {
        cout << i << endl;
    }
    return 0;
}
```

### Java While Loop
```java
public class Main {
    public static void main(String[] args) {
        int n = 5;
        while (n > 0) {
            System.out.println(n);
            n--;
        }
    }
}
```

### C++ Factorial
```cpp
#include <iostream>
using namespace std;

long long factorial(int n) {
    long long fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

int main() {
    cout << factorial(5) << endl;
    return 0;
}
```

### Java Fibonacci
```java
public class Main {
    public static void main(String[] args) {
        int n = 10;
        int a = 0, b = 1;
        for (int i = 0; i < n; i++) {
            System.out.print(a + " ");
            int temp = a;
            a = b;
            b = temp + b;
        }
    }
}
```

## Practice Section

### Solved Examples

1. **Sum of Even Numbers**
   ```python
   nums = [1, 2, 3, 4, 5, 6]
   even_sum = 0
   for num in nums:
       if num % 2 == 0:
           even_sum += num
   print(even_sum)  # 12
   ```

2. **Reverse a String**
   ```python
   s = "hello"
   reversed_s = ""
   for char in s:
       reversed_s = char + reversed_s
   print(reversed_s)  # "olleh"
   ```

3. **Count Vowels**
   ```python
   s = "hello world"
   vowels = "aeiou"
   count = 0
   for char in s.lower():
       if char in vowels:
           count += 1
   print(count)  # 3
   ```

### Walkthrough: Bubble Sort
- Start with [5, 3, 8, 1]
- Pass 1: Compare adjacent, swap if needed: [3, 5, 8, 1] -> [3, 5, 1, 8] -> [3, 5, 1, 8]
- Pass 2: [3, 5, 1, 8] -> [3, 1, 5, 8] -> [3, 1, 5, 8]
- Pass 3: [3, 1, 5, 8] -> [1, 3, 5, 8]
- Sorted.

### LeetCode-Style Problems
1. Two Sum: Use nested loops (O(n^2)) or hashmap (O(n)).
2. Maximum Subarray: Kadane's algorithm with loop.
3. Move Zeroes: Loop to move non-zeros.

## Comparisons

### Loops vs Recursion
- Loops: Efficient, no stack overflow risk.
- Recursion: Elegant for trees, but limited depth.

### For vs While
- For: When iterations known.
- While: When condition-based.

## Appendices

### Glossary
- **Iteration**: One execution of loop body.
- **Iterable**: Object that can be looped over.
- **Loop Invariant**: Property true before/after each iteration.

### Time Complexities
- Single loop: O(n)
- Nested: O(n^2)
- Logarithmic: O(log n) (e.g., binary search)

### References
- Python Docs: Loops
- LeetCode: Loop problems
- CLRS Book: Algorithm analysis

Personal note: Loops are simple but powerful; I once forgot to increment in a while loop and got TLE in a contest.
