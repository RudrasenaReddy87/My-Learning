## Date : 10.07.2026

# Day 2 — Math for DSA

## 1. Count Digits, Reverse a Number, Check Palindrome Number

These three problems all rely on the same basic trick: **peeling off digits one at a time using `% 10` (modulo) and `// 10` (integer division).**

### Why This Works
- `number % 10` gives you the **last digit** of the number.
- `number // 10` **removes** the last digit (integer division drops the remainder).

**Example:** `1234 % 10 = 4` (last digit), `1234 // 10 = 123` (number without last digit).

If you repeat this in a loop until the number becomes `0`, you visit every digit — from the last to the first.

### Count Digits

```python
def count_digits(n):
    count = 0
    if n == 0:
        return 1          # special case: 0 has 1 digit
    n = abs(n)             # handle negative numbers
    while n > 0:
        n = n // 10
        count += 1
    return count

print(count_digits(12345))   # Output: 5
```
**How it works:** Each time we do `n // 10`, we chop off one digit. We count how many times we can do that before `n` becomes 0.

**Time Complexity:** O(log₁₀ n) — because the number of digits in `n` is roughly `log₁₀(n) + 1`.
**Space Complexity:** O(1).

### Reverse a Number

```python
def reverse_number(n):
    reversed_num = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n > 0:
        last_digit = n % 10        # extract last digit
        reversed_num = reversed_num * 10 + last_digit   # build reversed number
        n = n // 10                 # remove last digit
    return sign * reversed_num

print(reverse_number(1234))   # Output: 4321
print(reverse_number(-120))   # Output: -21
```
**How it works:** Each loop, we pull off the last digit of `n` and "push" it into `reversed_num` by shifting existing digits left (`× 10`) and adding the new digit.

**Walkthrough for n = 123:**
| Step | n | last_digit | reversed_num |
|---|---|---|---|
| Start | 123 | - | 0 |
| 1 | 12 | 3 | 0×10+3 = 3 |
| 2 | 1 | 2 | 3×10+2 = 32 |
| 3 | 0 | 1 | 32×10+1 = 321 |

**Time Complexity:** O(log n). **Space Complexity:** O(1).

> **Note:** In real interviews, watch out for integer overflow in languages like Java/C++ (a reversed number might not fit in a 32-bit integer). Python doesn't have this issue since integers can grow arbitrarily large.

### Check Palindrome Number

A **palindrome number** reads the same forwards and backwards (like `121` or `1221`).

```python
def is_palindrome(n):
    if n < 0:
        return False          # negative numbers are never palindromes
    original = n
    reversed_num = reverse_number(n)
    return original == reversed_num

print(is_palindrome(121))   # True
print(is_palindrome(123))   # False
```
**How it works:** Simply reverse the number and check if it equals the original. If they match, it's a palindrome.

**Time Complexity:** O(log n). **Space Complexity:** O(1).

---

## 2. GCD/HCF (Euclidean Algorithm) and LCM

### What Is GCD/HCF?
**GCD (Greatest Common Divisor)**, also called **HCF (Highest Common Factor)**, is the largest number that divides two numbers exactly, with no remainder.

**Example:** GCD of 12 and 18 → both are divisible by 1, 2, 3, 6 → the greatest is **6**.

### The Naive Way (Slow)
You could check every number from `min(a, b)` down to `1` and find the first one that divides both. But this is O(min(a, b)) — slow for large numbers.

### The Euclidean Algorithm (Fast and Elegant)

**Key insight:** `GCD(a, b) = GCD(b, a % b)`, and we keep repeating this until `b` becomes `0`. At that point, `a` is the answer.

**Why does this work?** Any number that divides both `a` and `b` also divides `a % b` (the remainder when `a` is divided by `b`). So the GCD doesn't change if we replace `a` with `b`, and `b` with `a % b` — we're just shrinking the numbers while preserving the GCD, much faster than counting down one by one.

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))   # Output: 6
```

**Walkthrough for gcd(48, 18):**
| a | b | a % b |
|---|---|---|
| 48 | 18 | 12 |
| 18 | 12 | 6 |
| 12 | 6 | 0 |
| 6 | 0 | stop → answer is 6 |

**Time Complexity:** O(log(min(a, b))) — dramatically faster than the naive approach, because each step roughly cuts the numbers down by a large factor (related to Fibonacci-like shrinkage in the worst case).
**Space Complexity:** O(1) for the iterative version (or O(log(min(a,b))) if written recursively, due to call stack).

**Recursive version (common in interviews):**
```python
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
```

### LCM (Least Common Multiple)

The **LCM** of two numbers is the smallest number that both numbers divide into evenly.

**Key formula:** 
```
LCM(a, b) = (a × b) / GCD(a, b)
```

**Why this works:** There's a neat mathematical relationship: the product of two numbers always equals the product of their GCD and LCM. So once you know the GCD (which is fast to compute), you can derive the LCM instantly instead of searching for it.

```python
def lcm(a, b):
    return (a * b) // gcd(a, b)

print(lcm(4, 6))   # Output: 12
```

**Time Complexity:** O(log(min(a, b))) — dominated by the GCD calculation.
**Space Complexity:** O(1).

> **Tip:** Compute GCD first, then divide *before* multiplying if numbers are huge, to avoid overflow: `(a // gcd(a,b)) * b` instead of `(a * b) // gcd(a,b)`.

---

## 3. Check Prime (O(√n) Trial Division) and Sieve of Eratosthenes

### What Is a Prime Number?
A number greater than 1 that has **no divisors other than 1 and itself**. Examples: 2, 3, 5, 7, 11, 13...

### Naive Prime Check (Slow — O(n))
Check every number from `2` to `n-1` and see if any divides `n` evenly. This works but is wasteful.

### The O(√n) Trick

**Key insight:** If `n` has a divisor larger than `√n`, it must also have a corresponding divisor *smaller* than `√n`. 

**Why?** Divisors come in pairs that multiply to `n`. For example, for `n = 36`, the divisor pairs are (1,36), (2,18), (3,12), (4,9), (6,6). Notice that once you pass `√36 = 6`, the pairs just repeat in reverse (9,4 is the same info as 4,9). So you only ever need to check divisors up to `√n` — if none of them divide `n`, none of the larger ones will either.

```python
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):   # only check odd numbers
        if n % i == 0:
            return False
    return True

print(is_prime(29))   # True
print(is_prime(30))   # False
```
**How it works:** We check divisibility only up to `√n`, and we skip even numbers after checking 2 (since no even number besides 2 is prime).

**Time Complexity:** O(√n). **Space Complexity:** O(1).

### Sieve of Eratosthenes — Finding All Primes up to N

If you need **all primes up to N** (not just checking one number), checking each number individually with O(√n) is wasteful (that would be O(n√n) total). Instead, use the **Sieve of Eratosthenes**.

**Core idea:** Start by assuming every number is prime. Then, starting from the smallest prime (2), cross out all of its multiples (since they can't be prime). Move to the next number that's still marked prime, and repeat.

```python
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False   # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # mark all multiples of i as not prime, starting from i*i
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes

print(sieve_of_eratosthenes(30))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**Why start crossing out from `i * i` instead of `2 * i`?**
Because all smaller multiples of `i` (like `2×i`, `3×i`, ...) have already been crossed out by smaller primes earlier in the process. For example, when `i = 5`, numbers like `10` and `15` were already marked by `2` and `3`. So we can safely start at `i × i = 25`.

**Why stop the outer loop at `√n`?**
Same reasoning as before — if `i` is bigger than `√n`, then `i × i` would already exceed `n`, so there's nothing left to mark.

**Time Complexity:** O(n log log n) — this is very close to O(n), and is one of the most efficient known ways to generate all primes up to N.
**Space Complexity:** O(n) — for the boolean array tracking which numbers are prime.

**When to use which:**
| Situation | Use |
|---|---|
| Check if a *single* number is prime | O(√n) trial division |
| Need *all* primes up to N (or many prime checks) | Sieve of Eratosthenes |

---

## 4. Power(x, n) Using Fast Exponentiation (Binary Exponentiation)

### The Naive Way (Slow — O(n))
```python
def power_naive(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result
```
This multiplies `x` by itself `n` times — O(n) time. For large `n` (like a billion), this is far too slow.

### The Fast Way — Binary Exponentiation (O(log n))

**Key insight:** You can compute `x^n` by repeatedly **squaring**, cutting the exponent in half each time, instead of multiplying one at a time.

**The core trick:**
- If `n` is even: `x^n = (x^(n/2))²`
- If `n` is odd: `x^n = x × x^(n-1)`, and now `n-1` is even, so apply the rule above.

**Example — computing 3^13:**
Binary of 13 is `1101`. Instead of multiplying 3 by itself 13 times, we build up powers by squaring:
- `3^1 = 3`
- `3^2 = 9` (square of 3^1)
- `3^4 = 81` (square of 3^2)
- `3^8 = 6561` (square of 3^4)

Since `13 = 8 + 4 + 1`, we combine: `3^13 = 3^8 × 3^4 × 3^1 = 6561 × 81 × 3 = 1,594,323`

Instead of 13 multiplications, we did it in about `log₂(13) ≈ 4` squaring steps plus a few multiplications.

```python
def power_fast(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:              # if current bit is 1 (n is odd)
            result *= x
        x *= x                      # square x
        n //= 2                     # move to the next bit
    return result

print(power_fast(3, 13))   # Output: 1594323
```

**Walkthrough for power_fast(3, 13):**
| n | n odd? | result | x (before squaring) |
|---|---|---|---|
| 13 | yes | 1×3 = 3 | 3 → 9 |
| 6 | no | 3 | 9 → 81 |
| 3 | yes | 3×81 = 243 | 81 → 6561 |
| 1 | yes | 243×6561 = 1594323 | 6561 → ... |
| 0 | stop | **1594323** | |

**Time Complexity:** O(log n) — because we're halving `n` every step, just like binary search.
**Space Complexity:** O(1) for the iterative version.

**Recursive version:**
```python
def power_recursive(x, n):
    if n == 0:
        return 1
    half = power_recursive(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
```

> **Why "binary" exponentiation?** Because we're essentially processing the binary representation of `n`, bit by bit — squaring `x` at each bit position, and multiplying into the result whenever we hit a `1` bit.

---

## 5. Basics of Modular Arithmetic (Why `% (10^9 + 7)` Shows Up Everywhere)

### The Problem: Numbers Get Too Big

In many DSA and competitive programming problems, you're asked to count something — like the number of ways to arrange items, or the result of `2^1000000`. These answers can become **astronomically large** — far bigger than what a computer can store efficiently (or even bigger than what fits in standard integer types in languages like C++/Java).

**Modular arithmetic** solves this: instead of computing the exact huge number, we compute the answer **modulo** some fixed number (usually a large prime), which keeps numbers small while preserving the correctness of arithmetic operations like addition, subtraction, and multiplication.

### What Does `%` (mod) Actually Mean?

`a % m` gives you the **remainder** when `a` is divided by `m`. The result is always between `0` and `m-1`.

**Example:** `17 % 5 = 2`, because `17 = 3×5 + 2`.

Think of it like a clock: if `m = 12` (like a 12-hour clock), then no matter how large a number gets, the result always "wraps around" back into the range `0` to `11`.

### Why Specifically `10^9 + 7`?

`10^9 + 7 = 1,000,000,007` is a **prime number**, and it's just under the maximum value that fits comfortably in a 32-bit signed integer (~2.1 billion), which means:
- It's large enough that answers "modulo this number" still feel meaningfully large and avoid too many collisions.
- Being **prime** matters a lot for advanced operations like modular division (using modular inverses) — many mathematical properties (like Fermat's Little Theorem) only work cleanly with a prime modulus.
- It's become a de-facto industry/competitive-programming standard, so most online judges and interviewers expect this exact number.

### Key Rules of Modular Arithmetic

Given `MOD = 10^9 + 7`:

**Addition:**
```
(a + b) % MOD = ((a % MOD) + (b % MOD)) % MOD
```

**Subtraction (careful — can go negative!):**
```
(a - b) % MOD = ((a % MOD) - (b % MOD) + MOD) % MOD
```
We add `MOD` before taking the final `%` to avoid negative results (since in math, remainders should stay non-negative).

**Multiplication:**
```
(a * b) % MOD = ((a % MOD) * (b % MOD)) % MOD
```

**Division is trickier** — you can't just do `(a / b) % MOD` directly. Instead, you multiply by the **modular inverse** of `b` (a number that behaves like `1/b` under this modulus), often computed using Fermat's Little Theorem:
```
b^(-1) mod MOD = b^(MOD - 2) mod MOD      (only works when MOD is prime)
```
This is computed using the fast exponentiation technique from Section 4!

### Practical Example

```python
MOD = 10**9 + 7

def factorial_mod(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD    # take mod at every step, not just at the end
    return result

print(factorial_mod(20))
```

**Why take `% MOD` at every step, instead of computing the full factorial and modding at the end?**
Because the full factorial of large `n` (like `n = 10000`) would be a number with thousands of digits — extremely slow to compute and store. By applying `% MOD` after every multiplication, we keep the numbers small throughout, making each operation fast, while still arriving at the mathematically correct final answer.

### Where You'll See This
- "Return the answer modulo 10^9 + 7" — extremely common in counting problems (number of paths, number of ways to climb stairs, number of subsequences, etc.)
- Any problem involving factorials, combinatorics (`nCr`, `nPr`), or large power calculations.
- Hashing algorithms (like rolling hash / Rabin-Karp string matching).

---

## 6. Quick Recap / Cheat Sheet

| Topic | Key Trick | Time Complexity |
|---|---|---|
| Count digits / Reverse number | Use `% 10` and `// 10` to peel off digits | O(log n) |
| Palindrome check | Reverse the number and compare | O(log n) |
| GCD (Euclidean algorithm) | `GCD(a,b) = GCD(b, a % b)` until b = 0 | O(log(min(a,b))) |
| LCM | `LCM(a,b) = (a × b) / GCD(a,b)` | O(log(min(a,b))) |
| Prime check | Only test divisors up to √n | O(√n) |
| All primes up to N | Sieve of Eratosthenes — cross out multiples | O(n log log n) |
| Power(x, n) | Binary exponentiation — square and halve exponent | O(log n) |
| Modular arithmetic | Apply `% MOD` after every operation to keep numbers small | — |

**Golden rules to remember:**
- Whenever you see digit-by-digit processing → think `% 10` and `// 10`.
- Whenever you see "greatest common divisor" → think Euclidean algorithm, not brute force.
- Whenever you need **many** primes → think Sieve, not repeated O(√n) checks.
- Whenever exponents are large → think binary exponentiation, not a simple loop.
- Whenever a problem says "modulo 10^9+7" → apply mod after every arithmetic step, not just at the end, to avoid huge/overflowing numbers.

---