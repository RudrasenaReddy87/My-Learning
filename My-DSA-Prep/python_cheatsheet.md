# Python Cheatsheet: Core Concepts Quick Reference

Comprehensive guide to Python fundamentals. Covers all core concepts with small notes, tricks, and tips. Python is interpreted, high-level, dynamically typed. Tip: Use Python 3.8+ for modern features like walrus operator.

## Basics

- **Hello World**: `print("Hello, World!")` (Tip: Use `print(end='')` to suppress newline; `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)` for full control)
- **Comments**: `# single line`, `"""multi-line"""` (docstrings; accessible via `obj.__doc__`; PEP 257 for conventions)
- **Indentation**: 4 spaces (mandatory, no braces). Tip: Use spaces, not tabs; mix causes IndentationError. Trick: Configure editor for auto-indent.
- **Variables**: `x = 5` (no declaration, dynamic typing). Tip: Variables are references; `x = y` shares object if mutable. Trick: `del x` deletes reference; `x is None` for None checks.
- **Constants**: Convention: `PI = 3.14` (not enforced). Tip: Use uppercase for constants; `from typing import Final; PI: Final = 3.14` for type hints.
- **Keywords**: 35 reserved words (e.g., if, for, class). Check with `import keyword; keyword.kwlist`. Tip: Avoid using as var names; `and`, `or`, `not`, `is`, `in` are logical.
- **Shebang**: `#!/usr/bin/env python3` (for scripts). Tip: Makes script executable on Unix; `chmod +x script.py`.
- **Encoding**: Default UTF-8. Tip: Specify `# -*- coding: utf-8 -*-` if needed; `sys.getdefaultencoding()` to check.
- **Script Execution**: `python script.py` or `./script.py` (if executable). Tip: Use `if __name__ == '__main__':` for main block; `sys.argv` for args.
- **Execution Model**: Interpreted, bytecode compiled to `.pyc`. Tip: `python -m py_compile script.py` to compile; `import dis; dis.dis(func)` to disassemble.
- **Namespaces**: Global, local, enclosing, built-in. Tip: `globals()`, `locals()` to access; `dir()` for attributes.
- **Scopes**: LEGB rule (Local, Enclosing, Global, Built-in). Tip: `global var` to modify global; `nonlocal var` for enclosing.
- **Modules**: Files as modules. Tip: `import sys; sys.path` for search paths; `__name__` for module name.
- **Packages**: Directories with `__init__.py`. Tip: Relative imports with `.`; absolute with package name.
- **Import System**: `importlib` for dynamic imports. Tip: `importlib.import_module('module')`; `from importlib import reload; reload(module)`.
- **Built-in Types**: Immutable: int, float, complex, str, bytes, tuple, frozenset. Mutable: list, dict, set, bytearray. Tip: `type(obj)`, `isinstance(obj, type)`.
- **Literals**: Numeric: `42`, `3.14`, `1+2j`. String: `'str'`, `"str"`, `'''multi'''`, `r"raw"`, `f"{var}"`. Collections: `[1,2]`, `(1,2)`, `{1,2}`, `{'k': 'v'}`.
- **Expressions vs Statements**: Expressions evaluate to values; statements perform actions. Tip: `x = 5` is assignment statement; `x + 5` is expression.
- **Evaluation Order**: Left-to-right, except assignments right-to-left. Tip: `a = b = c = 5` assigns right to left.
- **Short-Circuiting**: `and`, `or` stop early. Tip: `x or default` for defaults; `x and y` for conditional.
- **Truthiness**: Falsy: `None`, `False`, `0`, `0.0`, `0j`, `''`, `[]`, `{}`, `set()`, `frozenset()`. Tip: `bool(obj)` to check.
- **Identity vs Equality**: `is` checks identity (same object); `==` checks value. Tip: `is None` preferred; interned strings share identity.
- **Copying**: Shallow: `copy.copy(obj)`; Deep: `import copy; copy.deepcopy(obj)`. Tip: Mutable containers need deep copy.
- **Memory Management**: Reference counting + cyclic GC. Tip: `gc.collect()` to force GC; `sys.getrefcount(obj)` for refs.
- **Performance Tips**: Use built-ins; avoid globals; list comps over loops; `join()` for strings; `collections` for efficiency.

## Data Types

### Primitive
- **int**: `x = 42` (arbitrary precision). Tip: No overflow; use for big numbers. Trick: `int('101', 2)` for binary conversion.
- **float**: `y = 3.14` (double precision). Tip: `float('inf')`, `float('-inf')`, `float('nan')`. Trick: Use `decimal.Decimal` for precision.
- **complex**: `z = 1 + 2j` (real + imag). Tip: `z.real`, `z.imag`, `z.conjugate()`.
- **bool**: `True`, `False` (subclass of int: True=1, False=0). Tip: Any non-zero/non-empty is True.
- **str**: `'hello'`, `"world"`, `"""multi"""` (immutable, Unicode). Tip: Raw strings `r"\\n"` for regex. Trick: F-strings `f"{var}"` (Python 3.6+).
- **bytes**: `b'hello'` (immutable binary). Tip: Encode/decode with `str.encode()`, `bytes.decode()`.
- **bytearray**: `bytearray(b'hello')` (mutable binary). Tip: Modify in-place.
- **None**: Singleton for no value. Tip: Check with `is None`.

### Collections
- **list**: `[1, 2, 3]` (mutable, ordered). Tip: Append with `append()`, extend with `extend()`. Trick: `list.pop()` removes last.
- **tuple**: `(1, 2, 3)` (immutable, ordered). Tip: Single element: `(1,)`. Trick: Unpack with `a, b = (1, 2)`.
- **dict**: `{'a': 1, 'b': 2}` (mutable, unordered, keys hashable). Tip: `dict.get(key, default)`. Trick: Dict comprehension `{k: v for k, v in zip(keys, values)}`.
- **set**: `{1, 2, 3}` (mutable, unordered, unique). Tip: Operations: `&`, `|`, `-`, `^`. Trick: `set.add()`, `set.discard()`.
- **frozenset**: `frozenset([1, 2])` (immutable set). Tip: Hashable, can be dict key.
- **range**: `range(5)` (lazy sequence). Tip: `list(range(5))` to materialize. Trick: `range(start, stop, step)`.
- **deque**: `from collections import deque; d = deque([1,2,3])` (double-ended queue). Tip: `d.appendleft()`, `d.popleft()` for efficient ops.

### Type Checking and Conversion
- `type(obj)`: Get type. Tip: `type(42) == int`.
- `isinstance(obj, cls)`: Check instance. Tip: `isinstance(42, (int, float))` for multiple.
- `id(obj)`: Memory address. Tip: `id(a) == id(b)` checks same object.
- **Casting**: `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`, `dict()`. Tip: `bool(0)` → False, `bool(1)` → True.
- **Mutable vs Immutable**: Lists/dicts/sets are mutable; tuples/strings are immutable. Tip: Use `copy()` or `deepcopy()` for copies.

## Operators

### Arithmetic
- `+`, `-`, `*`, `/` (float div), `//` (floor div), `%`, `**` (power). Tip: `//` floors towards negative infinity. Trick: `%` for cyclic indices.

### Comparison
- `==`, `!=`, `<`, `>`, `<=`, `>=`. Tip: Chained: `1 < x < 10`. Trick: `==` for value, `is` for identity.

### Logical
- `and`, `or`, `not`. Tip: Short-circuit: `and` stops at first False, `or` at first True. Trick: `x or default` for defaults.

### Bitwise
- `&` (and), `|` (or), `^` (xor), `~` (not), `<<` (left shift), `>>` (right shift). Tip: Use for flags, masks. Trick: `1 << n` for powers of 2.

### Assignment
- `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`. Tip: Augmented assignments are efficient.

### Membership
- `in`, `not in`. Tip: O(1) for dict/set, O(n) for list. Trick: `if x in [a,b,c]` but use set for large.

### Identity
- `is`, `is not` (checks id). Tip: `is None` preferred over `== None`. Trick: Interned strings: `'hello' is 'hello'`.

### Ternary (Walrus Operator Python 3.8+)
- `x if condition else y`. Tip: `:=` for assignment in expr: `if (n := len(data)) > 0:`. Trick: Reduces lines.

## Control Structures

### Conditional
```python
if condition:
    # code
elif another:
    # code
else:
    # code
```
Tip: Use `elif` for multiple branches. Trick: `if x := get_val():` with walrus for assignment.

### Loops
- **for**: `for i in iterable:`. Tip: `for i, v in enumerate(iterable):` for index. Trick: `for a, b in zip(list1, list2):`.
- **while**: `while condition:`. Tip: `while True:` for infinite loops. Trick: `while (line := f.readline()):`.
- **break**: Exit loop. Tip: Breaks innermost loop.
- **continue**: Next iteration. Tip: Skips rest of loop body.
- **else**: Executes if no break. Tip: Useful for search loops. Trick: `for item in items: if found: break else: not_found()`.

### Comprehensions
- List: `[x for x in iterable if condition]`. Tip: Nested: `[x for sub in lists for x in sub]`. Trick: Flatten lists.
- Dict: `{k: v for k, v in iterable}`. Tip: `{k: v for k, v in d.items() if v > 0}`. Trick: Filter dicts.
- Set: `{x for x in iterable}`. Tip: Unique values. Trick: `{f(x) for x in iterable}`.
- Generator: `(x for x in iterable)` (lazy). Tip: Memory efficient for large data. Trick: `sum(x for x in range(10))`.

## Functions

### Definition
```python
def func(param, default=val):
    """Docstring"""
    return result
```
Tip: Functions are first-class objects. Trick: `return a, b` returns tuple.

### Parameters
- Positional, keyword, *args (tuple), **kwargs (dict). Tip: *args for variable args, **kwargs for keyword. Trick: `func(*list, **dict)`.
- Default values: Must be immutable. Tip: Defaults evaluated once; use None for mutable defaults. Trick: `def f(x, y=None): y = y or []`.

### Lambda
- `lambda x: x**2` (anonymous, single expression). Tip: Use in `sorted(key=lambda x: x[1])`. Trick: `lambda: None` for no-op.

### Scope
- Local, enclosing, global, built-in (LEGB). Tip: Variables in enclosing scope readable. Trick: Use `nonlocal` to modify enclosing.
- `global var`: Modify global. Tip: Avoid globals; pass as params.
- `nonlocal var`: Modify enclosing. Tip: For nested functions.

### Built-ins
- `len()`, `max()`, `min()`, `sum()`, `sorted()`, `reversed()`, `enumerate()`, `zip()`, `map()`, `filter()`, `any()`, `all()`. Tip: `sum(iterable, start)`. Trick: `all(x > 0 for x in nums)`.
- `abs()`, `round()`, `pow()`, `divmod()`, `chr()`, `ord()`, `bin()`, `hex()`, `oct()`. Tip: `divmod(a, b)` returns (a//b, a%b).

## Type Hints (Python 3.5+)
- `def func(x: int) -> str:`. Tip: Optional, for readability and tools like mypy.
- `from typing import List, Dict, Optional`. Tip: `List[int]`, `Dict[str, int]`, `Optional[str]`.
- `Union`, `Tuple`, `Callable`. Tip: `Union[int, str]` for multiple types.
- `Any`, `TypeVar`. Tip: `Any` for dynamic types.
- Trick: Use `typing.get_type_hints()` to inspect.

## Async Programming (Python 3.5+)
- `async def func():`. Tip: Define coroutine.
- `await coro`: Wait for coroutine. Tip: Non-blocking.
- `asyncio.run(main())`: Run event loop.
- `import asyncio`. Tip: `asyncio.gather(*coros)` for concurrent.
- Trick: `async for` in async iterators.

## Dataclasses (Python 3.7+)
- `@dataclass`: Auto-generate __init__, __repr__, __eq__. Tip: Reduces boilerplate.
- `from dataclasses import dataclass`. Tip: `field(default=val)` for defaults.
- Trick: `frozen=True` for immutable; `order=True` for comparisons.

## Match Statement (Python 3.10+)
- `match value: case pattern:`. Tip: Structural pattern matching.
- Patterns: Literal, variable, sequence, mapping. Tip: `case [x, y]:` for lists.
- Trick: `case _:` for wildcard; `case x if x > 0:` with guard.

## Data Structure Methods

### List Methods (All)
- `append(x)`: Add x to end. Tip: O(1).
- `clear()`: Remove all items. Tip: O(n).
- `copy()`: Shallow copy. Tip: O(n).
- `count(x)`: Count occurrences of x. Tip: O(n).
- `extend(iterable)`: Add all from iterable. Tip: O(k).
- `index(x, start, end)`: Find index of x. Tip: O(n).
- `insert(i, x)`: Insert x at index i. Tip: O(n).
- `pop(i=-1)`: Remove and return at i. Tip: O(1) for end, O(n) else.
- `remove(x)`: Remove first x. Tip: O(n).
- `reverse()`: Reverse in-place. Tip: O(n).
- `sort(key=None, reverse=False)`: Sort in-place. Tip: Stable, O(n log n).
- Trick: `list[:] = reversed(list)` for copy reverse; `sorted(list)` for new sorted list.

### Dict Methods (All)
- `clear()`: Remove all items. Tip: O(n).
- `copy()`: Shallow copy. Tip: O(n).
- `fromkeys(iterable, value=None)`: New dict from keys. Tip: Class method.
- `get(key, default=None)`: Get value or default. Tip: Safe access.
- `items()`: View of (key, value) pairs. Tip: O(1).
- `keys()`: View of keys. Tip: O(1).
- `pop(key, default)`: Remove and return value. Tip: O(1) avg.
- `popitem()`: Remove and return last (key, value). Tip: LIFO, O(1).
- `setdefault(key, default=None)`: Get or set default. Tip: Useful for counters.
- `update(other)`: Update with other dict. Tip: Overwrites.
- `values()`: View of values. Tip: O(1).
- Trick: `dict(zip(keys, values))` for creation; `dict.get(key, default)` avoids KeyError.

### Set Methods (All)
- `add(x)`: Add x. Tip: O(1).
- `clear()`: Remove all. Tip: O(n).
- `copy()`: Shallow copy. Tip: O(n).
- `difference(*others)`: - operator. Tip: New set.
- `difference_update(*others)`: Remove elements in others. Tip: In-place.
- `discard(x)`: Remove x if present. Tip: Safe, O(1).
- `intersection(*others)`: & operator. Tip: New set.
- `intersection_update(*others)`: Keep only in others. Tip: In-place.
- `isdisjoint(other)`: True if no common elements. Tip: O(min(len)).
- `issubset(other)`: <= operator. Tip: Subset check.
- `issuperset(other)`: >= operator. Tip: Superset check.
- `pop()`: Remove and return arbitrary. Tip: O(1).
- `remove(x)`: Remove x, error if missing. Tip: O(1).
- `symmetric_difference(other)`: ^ operator. Tip: New set.
- `symmetric_difference_update(other)`: Update with symmetric diff. Tip: In-place.
- `union(*others)`: | operator. Tip: New set.
- `update(*others)`: Add from others. Tip: In-place.
- Trick: `set.intersection_update()` modifies in-place; use frozenset for immutable.

### String Methods (All)
- `capitalize()`: Capitalize first char. Tip: Immutable.
- `casefold()`: Casefold for caseless matching. Tip: Stronger than lower().
- `center(width, fillchar=' ')`: Center in width. Tip: Pads with fillchar.
- `count(sub, start=0, end=-1)`: Count non-overlapping sub. Tip: O(n).
- `encode(encoding='utf-8', errors='strict')`: Encode to bytes. Tip: Returns bytes.
- `endswith(suffix, start=0, end=-1)`: True if ends with suffix. Tip: Tuple for multiple.
- `expandtabs(tabsize=8)`: Replace tabs with spaces. Tip: Default 8 spaces.
- `find(sub, start=0, end=-1)`: Index of sub or -1. Tip: O(n).
- `format(*args, **kwargs)`: Format string. Tip: {} placeholders.
- `format_map(mapping)`: Format with mapping. Tip: Like format but dict.
- `index(sub, start=0, end=-1)`: Index of sub, error if not found. Tip: O(n).
- `isalnum()`: True if all alphanumeric. Tip: No spaces.
- `isalpha()`: True if all alphabetic. Tip: No digits/spaces.
- `isascii()`: True if all ASCII. Tip: Python 3.7+.
- `isdecimal()`: True if all decimal digits. Tip: Strict.
- `isdigit()`: True if all digits. Tip: Includes superscripts.
- `isidentifier()`: True if valid identifier. Tip: For variable names.
- `islower()`: True if all lowercase. Tip: Ignores non-letters.
- `isnumeric()`: True if all numeric. Tip: Includes fractions.
- `isprintable()`: True if all printable. Tip: No control chars.
- `isspace()`: True if all whitespace. Tip: Spaces, tabs, etc.
- `istitle()`: True if titlecased. Tip: Each word capitalized.
- `isupper()`: True if all uppercase. Tip: Ignores non-letters.
- `join(iterable)`: Join with string as sep. Tip: Efficient.
- `ljust(width, fillchar=' ')`: Left justify. Tip: Pads right.
- `lower()`: Lowercase. Tip: Immutable.
- `lstrip(chars=None)`: Strip left. Tip: Default whitespace.
- `maketrans(x, y=None, z=None)`: Translation table. Tip: For translate().
- `partition(sep)`: Split at first sep. Tip: Returns (before, sep, after).
- `replace(old, new, count=-1)`: Replace occurrences. Tip: count=-1 for all.
- `rfind(sub, start=0, end=-1)`: Rightmost index or -1. Tip: O(n).
- `rindex(sub, start=0, end=-1)`: Rightmost index, error if not. Tip: O(n).
- `rjust(width, fillchar=' ')`: Right justify. Tip: Pads left.
- `rpartition(sep)`: Split at rightmost sep. Tip: Returns (before, sep, after).
- `rsplit(sep=None, maxsplit=-1)`: Split from right. Tip: maxsplit limits.
- `rstrip(chars=None)`: Strip right. Tip: Default whitespace.
- `split(sep=None, maxsplit=-1)`: Split into list. Tip: sep=None for whitespace.
- `splitlines(keepends=False)`: Split on lines. Tip: Handles \n, \r, etc.
- `startswith(prefix, start=0, end=-1)`: True if starts with prefix. Tip: Tuple for multiple.
- `strip(chars=None)`: Strip both ends. Tip: Default whitespace.
- `swapcase()`: Swap case. Tip: Upper to lower, vice versa.
- `title()`: Title case. Tip: Each word capitalized.
- `translate(table)`: Translate chars. Tip: Use maketrans().
- `upper()`: Uppercase. Tip: Immutable.
- `zfill(width)`: Pad with zeros. Tip: For numbers.
- Trick: `str.maketrans()` for translate; f-strings for formatting.

### Tuple Methods (All)
- `count(x)`: Count occurrences of x. Tip: O(n).
- `index(x, start=0, end=-1)`: Find index of x. Tip: O(n).
- Trick: Immutable, hashable; unpacking: `a, *rest, b = tuple`; single: `(x,)`.

### Range Methods (All)
- No methods, but attributes: `start`, `stop`, `step`. Tip: Lazy, immutable.
- Trick: `list(range(10))` to materialize.

### Frozenset Methods (All)
- Same as set, but immutable: `copy()`, `difference()`, `intersection()`, `isdisjoint()`, `issubset()`, `issuperset()`, `symmetric_difference()`, `union()`. Tip: Hashable, can be dict key.
- Trick: `frozenset(iterable)` for creation.

### Bytes Methods (All)
- `capitalize()`, `center()`, `count()`, `decode()`, `endswith()`, `expandtabs()`, `find()`, `fromhex()`, `hex()`, `index()`, `isalnum()`, `isalpha()`, `isascii()`, `isdecimal()`, `isdigit()`, `isidentifier()`, `islower()`, `isnumeric()`, `isprintable()`, `isspace()`, `istitle()`, `isupper()`, `join()`, `ljust()`, `lower()`, `lstrip()`, `maketrans()`, `partition()`, `replace()`, `rfind()`, `rindex()`, `rjust()`, `rpartition()`, `rsplit()`, `rstrip()`, `split()`, `splitlines()`, `startswith()`, `strip()`, `swapcase()`, `title()`, `translate()`, `upper()`, `zfill()`. Tip: Immutable binary.
- Trick: `bytes.decode()` to str; `str.encode()` to bytes.

### Bytearray Methods (All)
- All bytes methods plus mutable: `append()`, `clear()`, `copy()`, `extend()`, `insert()`, `pop()`, `remove()`, `reverse()`. Tip: Mutable binary.
- Trick: `bytearray(b'hello')` for creation.

## Concurrency
- **Threading**: `import threading`. Tip: `threading.Thread(target=func)`. Trick: GIL limits CPU-bound.
- **Multiprocessing**: `import multiprocessing`. Tip: `multiprocessing.Process(target=func)`. Trick: Bypass GIL.
- **Concurrent.futures**: `ThreadPoolExecutor`, `ProcessPoolExecutor`. Tip: `executor.submit(func)`. Trick: `as_completed()` for results.

## Standard Library Highlights
- **os**: `os.getcwd()`, `os.listdir()`, `os.path.join()`. Tip: Cross-platform paths.
- **sys**: `sys.argv`, `sys.exit()`. Tip: Command-line args.
- **math**: `math.sqrt()`, `math.pi`. Tip: Constants and functions.
- **random**: `random.choice()`, `random.shuffle()`. Tip: `random.seed()` for reproducibility.
- **datetime**: `datetime.now()`, `timedelta`. Tip: `strftime()` for formatting.
- **json**: `json.dumps()`, `json.loads()`. Tip: Serialize/dump.
- **re**: `re.match()`, `re.search()`, `re.findall()`. Tip: Compile patterns: `re.compile()`.
- **collections**: `Counter`, `defaultdict`, `deque`. Tip: Efficient data structures.
- **itertools**: `permutations()`, `combinations()`, `chain()`. Tip: Combinatorics.
- **functools**: `partial()`, `reduce()`, `lru_cache()`. Tip: Function tools.
- **pathlib**: `Path('file.txt')`. Tip: OOP file paths (Python 3.4+).
- **subprocess**: `subprocess.run()`. Tip: Run external commands.
- **logging**: `logging.info()`. Tip: Configurable logging.
- **sqlite3**: `sqlite3.connect()`. Tip: Embedded DB.
- **urllib**: `urllib.request.urlopen()`. Tip: HTTP requests.
- Trick: Use `requests` library for easier HTTP.

## Python 3.8+ Features
- Walrus operator `:=`. Tip: Assignment in expressions.
- Positional-only params: `def f(a, /, b):`. Tip: Enforce positional.
- `math.prod(iterable)`. Tip: Product of elements.

## Python 3.9+ Features
- Dict merge: `d1 | d2`. Tip: New dict.
- `str.removeprefix()`, `str.removesuffix()`. Tip: Remove if present.
- Type hints: `list[int]` instead of `List[int]`. Tip: Built-in generics.

## Python 3.10+ Features
- Match statement. Tip: See above.
- Union types: `int | str`. Tip: Shorter than `Union[int, str]`.

## Python 3.11+ Features
- `ExceptionGroup`. Tip: Group multiple exceptions.
- `NotRequired` in TypedDict. Tip: Optional keys.

## Ecosystem Extensions
- **Data Science**: NumPy (arrays), Pandas (dataframes), Matplotlib (plots), SciPy (scientific computing).
- **Web**: Django (full-stack), Flask (micro), FastAPI (async API), Requests (HTTP client).
- **ML/AI**: TensorFlow (deep learning), PyTorch (neural nets), Scikit-learn (machine learning).
- **Testing**: pytest (framework), unittest (built-in), Selenium (web testing).
- **Dev Tools**: Black (code formatter), Flake8 (linter), mypy (type checker), isort (import sorter).
- **Packaging**: Poetry (dependency management), Pipenv (virtual envs), setuptools (packaging).
- Trick: Use `pip install --upgrade pip` for latest pip.

## All Built-in Functions (with small notes)
- abs(x): Absolute value of x.
- all(iterable): True if all elements are truthy.
- any(iterable): True if any element is truthy.
- ascii(obj): ASCII representation of obj.
- bin(x): Binary string of int x.
- bool(x): Boolean value of x.
- bytearray(source): Mutable byte array.
- bytes(source): Immutable byte sequence.
- callable(obj): True if obj is callable.
- chr(i): Character for Unicode code i.
- classmethod(func): Class method decorator.
- compile(source, filename, mode): Compile source code.
- complex(real, imag): Complex number.
- delattr(obj, name): Delete attribute.
- dict(**kwargs): Create dict.
- dir(obj): List of attributes.
- divmod(a, b): (a//b, a%b).
- enumerate(iterable, start=0): Iterator with index.
- eval(expression): Evaluate expression.
- exec(object): Execute code.
- filter(func, iterable): Filter iterable.
- float(x): Float value.
- format(value, format_spec): Format value.
- frozenset(iterable): Immutable set.
- getattr(obj, name, default): Get attribute.
- globals(): Global symbol table.
- hasattr(obj, name): True if has attribute.
- hash(obj): Hash value.
- help(obj): Help on obj.
- hex(x): Hex string of int x.
- id(obj): Identity of obj.
- input(prompt): Read input.
- int(x, base=10): Integer value.
- isinstance(obj, classinfo): True if instance.
- issubclass(cls, classinfo): True if subclass.
- iter(obj): Iterator.
- len(obj): Length.
- list(iterable): List.
- locals(): Local symbol table.
- map(func, *iterables): Map function.
- max(iterable, *args, key): Maximum.
- memoryview(obj): Memory view.
- min(iterable, *args, key): Minimum.
- next(iterator, default): Next item.
- object(): Base object.
- oct(x): Octal string of int x.
- open(file, mode): Open file.
- ord(c): Unicode code of char c.
- pow(base, exp, mod): Power.
- print(*objects, sep, end, file, flush): Print.
- property(fget, fset, fdel): Property decorator.
- range(start, stop, step): Range object.
- repr(obj): String repr.
- reversed(seq): Reversed iterator.
- round(number, ndigits): Rounded number.
- set(iterable): Set.
- setattr(obj, name, value): Set attribute.
- slice(start, stop, step): Slice object.
- sorted(iterable, key, reverse): Sorted list.
- staticmethod(func): Static method decorator.
- str(obj): String.
- sum(iterable, start): Sum.
- super(type, obj): Super object.
- tuple(iterable): Tuple.
- type(obj): Type of obj.
- vars(obj): __dict__ of obj.
- zip(*iterables): Zip iterators.
- __import__(name): Import module.

## Additional Special Methods (Dunder Methods)
- __add__(self, other): Addition (+).
- __sub__(self, other): Subtraction (-).
- __mul__(self, other): Multiplication (*).
- __truediv__(self, other): Division (/).
- __floordiv__(self, other): Floor division (//).
- __mod__(self, other): Modulo (%).
- __pow__(self, other): Power (**).
- __lt__(self, other): Less than (<).
- __le__(self, other): Less or equal (<=).
- __gt__(self, other): Greater than (>).
- __ge__(self, other): Greater or equal (>=).
- __ne__(self, other): Not equal (!=).
- __hash__(self): Hash value.
- __bool__(self): Boolean value.
- __int__(self): Integer conversion.
- __float__(self): Float conversion.
- __complex__(self): Complex conversion.
- __bytes__(self): Bytes conversion.
- __format__(self, format_spec): Format string.
- __del__(self): Destructor.
- __delattr__(self, name): Delete attribute.
- __setattr__(self, name, value): Set attribute.
- __getattr__(self, name): Get attribute (fallback).
- __getattribute__(self, name): Get attribute.
- __dir__(self): List attributes.
- __slots__: Limit attributes.
- __weakref__: Weak reference support.
- __enter__(self): Context enter.
- __exit__(self, exc_type, exc_val, exc_tb): Context exit.
- __new__(cls, *args): Object creation.
- __init_subclass__(cls, **kwargs): Subclass init.
- __class_getitem__(cls, item): Generic type subscript.

## More Standard Library Modules (with small notes)
- heapq: Heap queue (priority queue).
- bisect: Bisection algorithms (sorted insertion).
- array: Efficient arrays.
- weakref: Weak references.
- copy: Shallow/deep copy.
- pprint: Pretty print.
- textwrap: Text wrapping.
- string: String constants/templates.
- unicodedata: Unicode database.
- locale: Localization.
- calendar: Calendar functions.
- time: Time functions.
- zoneinfo: Time zones (3.9+).
- email: Email handling.
- smtplib: SMTP client.
- imaplib: IMAP client.
- poplib: POP3 client.
- ftplib: FTP client.
- telnetlib: Telnet client.
- xml: XML processing.
- html: HTML parsing.
- csv: CSV files.
- configparser: Config files.
- argparse: Command-line args.
- optparse: Option parsing (deprecated).
- getopt: C-style options.
- readline: GNU readline.
- rlcompleter: Completion.
- sqlite3: SQLite DB.
- zlib: Compression.
- gzip: Gzip files.
- bz2: Bzip2 files.
- lzma: LZMA files.
- tarfile: Tar archives.
- zipfile: Zip archives.
- shutil: High-level file ops.
- tempfile: Temp files.
- linecache: Line caching.
- pickle: Serialization.
- copyreg: Pickle support.
- marshal: Internal serialization.
- dbm: DBM databases.
- shelve: Persistent dict.
- hashlib: Hash functions.
- hmac: HMAC.
- secrets: Cryptographically secure.
- ssl: SSL/TLS.
- socket: Low-level networking.
- mmap: Memory-mapped files.
- contextvars: Context variables.
- concurrent.futures: High-level concurrency.
- multiprocessing: Process-based parallelism.
- threading: Threading.
- _thread: Low-level threading.
- dummy_thread: Dummy threading.
- io: I/O streams.
- codecs: Codecs.
- unicodedata: Unicode data.
- stringprep: String prep.
- re: Regular expressions.
- difflib: Diffs.
- textwrap: Text wrapping.
- string: String utilities.
- struct: Binary data.
- weakref: Weak references.
- gc: Garbage collector.
- inspect: Introspection.
- site: Site-specific config.
- warnings: Warnings.
- contextlib: Context utilities.
- abc: Abstract base classes.
- atexit: Exit handlers.
- traceback: Stack traces.
- __future__: Future statements.
- keyword: Keywords.
- ast: Abstract syntax trees.
- symtable: Symbol tables.
- symbol: Parser symbols.
- token: Parser tokens.
- tokenize: Tokenizer.
- tabnanny: Indentation checker.
- py_compile: Compilation.
- compileall: Compile all.
- dis: Disassembler.
- pickletools: Pickle tools.
- platform: Platform info.
- errno: Error codes.
- ctypes: C types.
- msvcrt: MS VC runtime (Windows).
- posix: POSIX API.
- pwd: Password database.
- spwd: Shadow passwords.
- grp: Group database.
- crypt: Password hashing.
- termios: Terminal control.
- tty: Terminal utilities.
- pty: Pseudo-terminals.
- fcntl: File control.
- pipes: Shell pipelines.
- resource: Resource limits.
- nis: NIS.
- syslog: Syslog.

## Networking and Web
- socket: Low-level sockets.
- ssl: SSL support.
- http: HTTP modules.
- urllib: URL handling.
- ftplib: FTP.
- smtplib: SMTP.
- imaplib: IMAP.
- poplib: POP3.
- telnetlib: Telnet.
- xmlrpc: XML-RPC.
- json: JSON.
- html: HTML.
- cgi: CGI.
- wsgiref: WSGI.

## GUI and Multimedia
- tkinter: GUI toolkit.
- turtle: Turtle graphics.
- curses: Terminal UI.
- wave: WAV files.
- aifc: AIFF files.
- sunau: Sun AU files.
- audioop: Audio ops.
- imageop: Image ops (deprecated).
- rgbimg: RGB images (deprecated).
- imghdr: Image headers.
- colorsys: Color systems.

## Miscellaneous
- doctest: Docstring testing.
- unittest: Unit testing.
- pdb: Debugger.
- profile: Profiling.
- cProfile: C profiling.
- timeit: Timing.
- trace: Trace execution.
- sys: System.
- os: OS interface.
- stat: Stat constants.
- fileinput: File input.
- filecmp: File comparison.
- dircache: Dir caching (deprecated).
- macpath: Mac paths (deprecated).
- ntpath: NT paths.
- posixpath: POSIX paths.
- genericpath: Generic paths.
- fnmatch: Filename matching.
- glob: Pathname expansion.
- linecache: Line caching.
- imp: Import internals (deprecated).
- importlib: Import system.
- pkgutil: Package utilities.
- runpy: Run Python code.
- zipimport: Zip imports.
- modulefinder: Module finder.
- distutils: Distribution (deprecated).
- ensurepip: Ensure pip.
- venv: Virtual environments.
- pip: Package installer (external).

## Python 3.12+ Features (upcoming)
- Per-interpreter GIL (experimental).
- More efficient unions.
- Better error messages.

## Best Practices and Tips
- Use virtual environments.
- Follow PEP 8.
- Write tests.
- Use type hints.
- Avoid mutable defaults.
- Use context managers.
- Prefer EAFP (Easier to Ask for Forgiveness than Permission).
- Use generators for large data.
- Profile before optimizing.
- Keep code DRY (Don't Repeat Yourself).
- Use meaningful names.
- Document with docstrings.
- Handle exceptions properly.
- Use logging over print.
- Secure code: Avoid eval, use secrets for crypto.
- Performance: Use built-ins, list comprehensions, avoid globals.



