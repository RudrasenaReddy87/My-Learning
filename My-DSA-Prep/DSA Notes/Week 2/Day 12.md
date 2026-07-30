# Day 12 — 2D Array Basics: Matrix Problems

**Week 2: Arrays Part 1–2** | [Week overview](README.md)

**Language: Python**

---

## 1. Working With 2D Arrays (Matrices) in Python

A **matrix** is just a 2D array — in Python, a list of lists:
`matrix = [[1,2,3],[4,5,6],[7,8,9]]` represents a 3×3 grid, where
`matrix[i][j]` accesses the element at **row `i`, column `j`** (0-indexed).
`matrix[i]` alone gives you the whole `i`-th row as a list.

**Dimensions:** `rows = len(matrix)`, `cols = len(matrix[0])` (assuming a
non-ragged/rectangular matrix, which all problems today assume).

Everything from Day 3 (arrays) still applies — the only new wrinkle is
**two** indices instead of one, and a few classic manipulation patterns
(transposing, rotating, spiraling) that only make sense in 2D.

---

## 2. Set Matrix Zeroes

**The problem:** given an `m x n` matrix, if an element is `0`, set its
**entire row and entire column** to `0` — do this **in-place**, ideally
using `O(1)` extra space (beyond the output, which is the mutated input
itself).

**Example:**
```
Input:            Output:
1 1 1              1 0 1
1 0 1      →       0 0 0
1 1 1              1 0 1
```
(the middle `0` zeroes out its entire row and column)

### Why the naive approach breaks

You might think: "just scan the matrix, and the moment you see a `0`,
immediately zero out its row and column." **This is wrong** — if you zero
things out *while* scanning, you'll create new `0`s that get misinterpreted
as "original" zeroes later in the same scan, cascading incorrectly and
zeroing out far more than intended.

### A correct-but-not-optimal approach: extra marker sets

First pass: **record** (without modifying anything yet) which rows and
columns contain at least one original `0`, using two sets. Second pass: zero
out every cell whose row or column is marked.

```python
def set_zeroes_extra_space(matrix):
    rows_to_zero = set()
    cols_to_zero = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows_to_zero or j in cols_to_zero:
                matrix[i][j] = 0
    return matrix
```
This is correct (separating "detection" from "mutation" avoids the cascade
problem above) but uses **O(m + n)** extra space for the two sets.

### The optimal O(1) space trick: use the first row/column as markers

**Idea:** instead of separate sets, use the matrix's own **first row** and
**first column** as the "marker" storage — if `matrix[i][j] == 0`, instead
of adding to a separate set, just set `matrix[i][0] = 0` and
`matrix[0][j] = 0` directly in the matrix. The only complication: the first
row and first column would then be "contaminated" both as data and as
markers, so we need one extra boolean to separately track whether the first
row/column *themselves* originally contained a zero (since that fact would
otherwise get lost/conflated with marker usage).

```python
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

    # Use row 0 and column 0 themselves as marker storage.
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out cells based on the markers (skip row 0 / col 0 themselves for now).
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Finally, handle row 0 and column 0 using the separately saved flags.
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix
```

**Trace for `matrix = [[1,1,1],[1,0,1],[1,1,1]]`:**
- `first_row_has_zero = False` (row 0 is `[1,1,1]`).
- `first_col_has_zero = False` (col 0 is `[1,1,1]`).
- Scan interior (`i,j` from 1): `matrix[1][1]=0` → set `matrix[1][0]=0` and
  `matrix[0][1]=0`. Matrix is now `[[1,0,1],[0,0,1],[1,1,1]]`.
- Zero based on markers: `matrix[1][1]`: `matrix[1][0]=0` → zero (already
  0). `matrix[1][2]`: `matrix[1][0]=0` → zero → `matrix[1][2]=0`.
  `matrix[2][1]`: `matrix[0][1]=0` → zero → `matrix[2][1]=0`. `matrix[2][2]`:
  neither marker set → unchanged.
- Result before row0/col0 fixup: `[[1,0,1],[0,0,0],[1,0,1]]`.
- `first_row_has_zero` and `first_col_has_zero` are both `False`, so no
  further changes.

Final result: `[[1,0,1],[0,0,0],[1,0,1]]`. Matches the expected output.

**Complexity:** **O(m × n) time** (a constant number of full passes over the
matrix), **O(1) extra space** (just two boolean flags — the matrix itself is
reused as marker storage, which is the key trick).

---

## 3. Rotate Matrix by 90 Degrees (In-Place)

**The problem:** given an `n x n` square matrix, rotate it 90 degrees
clockwise, in-place.

**Example:**
```
1 2 3         7 4 1
4 5 6    →    8 5 2
7 8 9         9 6 3
```

**The trick — decompose the rotation into two simpler, well-known steps:**
1. **Transpose** the matrix (flip across the main diagonal: `matrix[i][j]`
   and `matrix[j][i]` swap).
2. **Reverse each row.**

**Why does transpose + reverse-each-row equal a 90° clockwise rotation?**
Transposing turns rows into columns (the first *row* becomes the first
*column*). Reversing each row then flips that new column's order — turning
"first row becomes first column, top-to-bottom" into "first row becomes
**last** column, top-to-bottom," which is exactly what a clockwise rotation
does (the top-left corner moves to the top-right corner).

```python
def rotate_90_clockwise(matrix):
    n = len(matrix)
    # Step 1: transpose (swap matrix[i][j] with matrix[j][i], for i < j)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: reverse each row
    for row in matrix:
        row.reverse()
    return matrix
```

**Trace for `matrix = [[1,2,3],[4,5,6],[7,8,9]]`:**

Transpose (swap `(0,1)↔(1,0)`, `(0,2)↔(2,0)`, `(1,2)↔(2,1)`; diagonal
elements `(0,0),(1,1),(2,2)` stay put):
```
1 4 7
2 5 8
3 6 9
```
Reverse each row:
```
7 4 1
8 5 2
9 6 3
```
Matches the expected output.

**Why only iterate `j` from `i+1` (not from `0`) in the transpose step?**
Swapping `matrix[i][j]` with `matrix[j][i]` for **every** `(i,j)` pair would
swap each off-diagonal pair **twice** — once as `(i,j)` and again later as
`(j,i)` — which would undo the first swap and leave the matrix unchanged.
Restricting to `j > i` ensures each pair is swapped exactly once.

**Complexity:** **O(n²) time** (touching every cell a constant number of
times), **O(1) extra space** — both steps operate entirely in-place on the
existing matrix, no new matrix allocated.

**Counter-clockwise rotation, for reference:** reverse each row **first**,
then transpose (or equivalently: transpose, then reverse each **column**
instead of each row) — the mirrored order of operations flips the rotation
direction.

---

## 4. Print Matrix in Spiral Order

**The problem:** given an `m x n` matrix, return all its elements in
**spiral order** — starting at the top-left, going right across the top row,
then down the right column, then left across the bottom row, then up the
left column, and spiraling further inward, repeating.

**Example:**
```
1  2  3
4  5  6
7  8  9
```
→ spiral order: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`

**Idea:** maintain four boundaries — `top`, `bottom`, `left`, `right` —
representing the current "unprocessed" rectangle. Repeatedly walk the four
edges of that rectangle (right along the top, down the right side, left
along the bottom, up the left side), then shrink each boundary inward after
processing it, and repeat until the boundaries cross.

```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):        # walk right along the top row
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):          # walk down along the right column
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:                            # guard: a row might remain
            for col in range(right, left - 1, -1):    # walk left along the bottom row
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:                             # guard: a column might remain
            for row in range(bottom, top - 1, -1):     # walk up along the left column
                result.append(matrix[row][left])
            left += 1

    return result
```

**Trace for `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
(`top=0,bottom=2,left=0,right=2`):**
- Walk right along top row (`row=0`, `col` 0→2): append `1,2,3`. `top→1`.
- Walk down right column (`col=2`, `row` 1→2): append `6,9`. `right→1`.
- Check `top(1) <= bottom(2)`: yes. Walk left along bottom row (`row=2`,
  `col` 1→0): append `8,7`. `bottom→1`.
- Check `left(0) <= right(1)`: yes. Walk up left column (`col=0`, `row`
  1→1): append `4`. `left→1`.
- Loop check: `top(1) <= bottom(1)` and `left(1) <= right(1)`: yes, continue.
- Walk right along top row (`row=1`, `col` 1→1): append `5`. `top→2`.
- Walk down right column (`col=1`, `row` 2→1): range is empty (2 to 1 doesn't
  execute forward), nothing appended. `right→0`.
- Check `top(2) <= bottom(1)`: **False**, skip bottom-row walk.
- Check `left(1) <= right(0)`: **False**, skip left-column walk.
- Loop check: `top(2) <= bottom(1)`: **False** → loop ends.

Result: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`. Matches the expected spiral order.

**Why the two `if` guards before the bottom-row and left-column walks?**
Once a matrix has been mostly consumed (e.g., only a single row or single
column remains), walking "right along the top" and then unconditionally
"left along the bottom" would **re-walk the same row twice** if `top` and
`bottom` have crossed (or already point at the same, now-fully-consumed
row). The guards ensure we only walk the bottom row / left column if there's
genuinely still unprocessed space there.

**Complexity:** **O(m × n) time** (every cell is visited and appended
exactly once), **O(m × n) space** for the output list (unavoidable, since
that's the required result) — auxiliary space beyond the output is O(1).

---

## 5. Search a 2D Matrix (Row/Column Sorted)

**The problem:** given a matrix where **each row is sorted left to right**,
and **the first element of each row is greater than the last element of the
previous row** (meaning the entire matrix, read row by row, is one big
sorted sequence), determine whether a target value exists.

**Example:**
```
1  3  5  7
10 11 16 20
23 30 34 60
```
Reading row by row: `1,3,5,7,10,11,16,20,23,30,34,60` — genuinely sorted as
one long sequence. This is the key property that unlocks binary search.

**Idea:** since the matrix behaves like one big sorted 1D array of length
`rows × cols`, run a standard **Binary Search** (Week 1, Day 7) over the
*virtual* index range `[0, rows*cols - 1]`, converting each virtual index
back to real `(row, col)` coordinates with division and modulo.

```python
def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = low + (high - low) // 2
        row, col = divmod(mid, cols)        # convert virtual index -> real coordinates
        value = matrix[row][col]
        if value == target:
            return True
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
```

**Why does `divmod(mid, cols)` give the correct `(row, col)`?** If you laid
the matrix out row by row into one flat list, the element at flat index
`mid` would be at row `mid // cols` (how many full rows of length `cols` fit
before it) and column `mid % cols` (the remainder — its position within that
row). `divmod(mid, cols)` returns exactly `(mid // cols, mid % cols)` in one
call.

**Trace for `matrix` above, `target = 16`** (`rows=3, cols=4`,
`low=0, high=11`):
| low | high | mid | (row,col) | value | comparison | action |
|---|---|---|---|---|---|---|
| 0 | 11 | 5 | (1,1) | 11 | 11 < 16 | low=6 |
| 6 | 11 | 8 | (2,0) | 23 | 23 > 16 | high=7 |
| 6 | 7 | 6 | (1,2) | 16 | equal | **return True** |

Found in 3 comparisons. Complexity: **O(log(m × n)) time** (standard binary
search over `m*n` virtual elements), **O(1) space** — this is the exact same
halving-search pattern from Week 1, Day 7, just with an index-translation
step added.

---

## Worked Examples — Trace These Yourself First

**Example A:** In `set_zeroes`, why must `first_row_has_zero` and
`first_col_has_zero` be computed and saved **before** the main marking pass
begins?
<details><summary>Answer</summary>
The main marking pass uses row 0 and column 0 themselves as marker storage —
so by the time that pass finishes, row 0 and column 0 may contain zeroes
that were placed there purely as *markers* for other rows/columns, not
because those cells were originally zero. If you checked "did row 0
originally have a zero" *after* the marking pass, you couldn't distinguish
an original zero from a marker zero — you must capture that fact before any
markers are written.
</details>

**Example B:** Why does `rotate_90_clockwise` reverse each **row** after
transposing, rather than reversing each **column**?
<details><summary>Answer</summary>
After transposing, the matrix's rows are the original matrix's columns.
Reversing each row of the transposed matrix means reversing what were
originally top-to-bottom columns, turning them left-to-right — which,
combined with the transpose, produces the 90° clockwise effect described in
section 3. Reversing columns instead (after transposing) would produce a
counter-clockwise rotation instead — the direction is entirely determined by
this choice.
</details>

**Example C:** In `search_2d_matrix`, what's the time complexity difference
between this approach and one that runs a separate binary search on each
row (checking `rows` separate binary searches over `cols` elements)? Which
approach is actually better and why?
<details><summary>Answer</summary>
Running binary search on each row separately would cost `O(rows × log(cols))`
in the worst case (a full binary search attempted on every row). The
virtual-single-array approach costs `O(log(rows × cols))`. Using logarithm
properties, `log(rows × cols) = log(rows) + log(cols)`, which is
significantly smaller than `rows × log(cols)` for any reasonably sized
matrix — the virtual-array approach is genuinely better because it exploits
the *full* sorted structure (across rows too), not just within-row sortedness.
</details>

---

## Practice Questions

### Question 1 — Set Matrix Zeroes
**Question:** Given a matrix, if an element is `0`, set its entire row and
column to `0`, in-place, using O(1) extra space.
**Input:** `matrix = [[1,1,1],[1,0,1],[1,1,1]]`
**Output:** `[[1,0,1],[0,0,0],[1,0,1]]`
**Solution:**
```python
def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0
    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0
    return matrix

print(set_zeroes([[1,1,1],[1,0,1],[1,1,1]]))
# [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
```
Use the first row/column as marker storage (saving their original zero-state
first), then zero out cells based on those markers. Complexity: `O(m*n)`
time, `O(1)` extra space (section 2).

### Question 2 — Rotate Matrix by 90 Degrees
**Question:** Given a square matrix, rotate it 90 degrees clockwise, in-place.
**Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:** `[[7,4,1],[8,5,2],[9,6,3]]`
**Solution:**
```python
def rotate_90_clockwise(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

print(rotate_90_clockwise([[1,2,3],[4,5,6],[7,8,9]]))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```
Transpose (swap across the main diagonal), then reverse each row.
Complexity: `O(n²)` time, `O(1)` extra space (section 3).

### Question 3 — Spiral Matrix Traversal
**Question:** Given a matrix, return all its elements in spiral order.
**Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:** `[1, 2, 3, 6, 9, 8, 7, 4, 5]`
**Solution:**
```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
Shrink four boundaries (top/bottom/left/right) inward after walking each
edge, with guards to avoid re-walking a row/column that's already fully
consumed. Complexity: `O(m*n)` time, `O(m*n)` output space (section 4).

### Question 4 — Search a 2D Matrix
**Question:** Given a matrix where each row is sorted and each row's first
element exceeds the previous row's last element, determine whether a target
exists.
**Input:** `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 16`
**Output:** `True`
**Solution:**
```python
def search_2d_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = low + (high - low) // 2
        row, col = divmod(mid, cols)
        value = matrix[row][col]
        if value == target:
            return True
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_2d_matrix(matrix, 16))   # True
```
Treat the matrix as one big virtual sorted array and binary search over it,
translating the virtual index to `(row, col)` with `divmod`. Complexity:
`O(log(m*n))` time, `O(1)` space (section 5).

## Revision

- Quick recall (5 min): re-solve Next Permutation from Day 11 cold.

## Key Takeaways

- **Set Matrix Zeroes** achieves `O(1)` extra space by reusing the matrix's
  **own first row and column** as marker storage — the only subtlety is
  saving whether the first row/column originally had a zero *before* they
  get overwritten as markers.
- **Rotating a matrix 90°** decomposes into **transpose + reverse rows** (for
  clockwise) — a two-step composition that's far simpler to implement
  correctly than trying to compute rotated positions directly.
- **Spiral traversal** is a boundary-shrinking walk (`top`/`bottom`/`left`/
  `right`), with guard checks needed once the matrix is mostly consumed to
  avoid re-visiting cells.
- **Searching a row/column-sorted matrix** reduces to a **single binary
  search** over a virtual flattened array, using `divmod` to translate
  between the virtual index and real `(row, col)` coordinates — `O(log(m*n))`,
  better than running a separate search per row.

---

## Additional Topics — Filling Gaps in Day 12's Scope

Two more matrix problems belong alongside today's set — both classic
"exploit the sorted structure with a corner-starting pointer walk" problems
that are distinct from (but related to) today's Search 2D Matrix (section
5).

### 6. Row With Maximum Ones (Sorted Binary Matrix)

**The problem:** given a binary matrix (only `0`s and `1`s) where **each
row is individually sorted** (all `0`s before all `1`s), find the index of
the row containing the **most** `1`s. (If multiple rows tie, return any of
them — this version returns the last one found, but the specific tie-break
choice doesn't affect the core technique.)

**Brute force:** count ones in every row — `O(rows × cols)`.

**Optimal — start at the top-right corner, walk down-left:** since each row
is sorted, the row with the most ones is the row whose "first `1`" appears
**earliest** (furthest left). Start a pointer at the top-right corner; if
the current cell is `1`, move **left** (there might be more `1`s in this
row) and record this row as the best-so-far; if the current cell is `0`,
move **down** (this row has no more ones to find further left, so we're
done searching it).

```python
def row_with_max_ones(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_row = -1
    col = cols - 1
    for row in range(rows):
        while col >= 0 and matrix[row][col] == 1:
            col -= 1
            max_row = row
    return max_row

print(row_with_max_ones([[0,0,0],[0,1,1],[1,1,1]]))   # 2
```

**Trace for `matrix = [[0,0,0],[0,1,1],[1,1,1]]`** (`col` starts at `2`):
- `row=0`: `matrix[0][2]=0` → inner `while` doesn't execute (condition
  fails immediately).
- `row=1`: `matrix[1][2]=1` → `col→1, max_row=1`. `matrix[1][1]=1` →
  `col→0, max_row=1`. `matrix[1][0]=0` → stop.
- `row=2`: `matrix[2][0]=1` → `col→-1, max_row=2`. Loop condition `col>=0`
  now fails for all further rows.

Result: `max_row = 2` (row `2`, `[1,1,1]`, has the most ones — `3`, versus
row `1`'s `2`). Matches.

**Why does `col` never need to reset or move rightward across rows?** Once
`col` has moved left past a certain point, no **later** row could possibly
have its first `1` any further right than where we already know a `1`
exists — if it did, that row would have *fewer* ones than the current best,
not more (since a *later* first-`1` position, further right, always means
strictly fewer trailing ones in a sorted-row binary matrix). This
monotonic, one-directional pointer movement (across the *entire* matrix,
not resetting per row) is what keeps this `O(rows + cols)` instead of
`O(rows × cols)`.

**Complexity:** **O(rows + cols) time** (the `col` pointer moves left at
most `cols` times total, across all rows combined, and `row` advances at
most `rows` times), **O(1) space** — substantially better than the
`O(rows × cols)` brute force.

### 7. Search a 2D Matrix II (Staircase Search)

**Important distinction from Day 12's Question 4:** that problem assumed
the *entire* matrix, read row by row, forms **one single sorted sequence**
(each row's first element exceeds the previous row's last element) — which
allowed a single binary search. **This** problem has a **weaker**
guarantee: only that **each row is sorted left-to-right** AND **each column
is sorted top-to-bottom** — rows are *not* globally ordered relative to
each other (e.g. row 2 might start smaller than row 1 ends). This weaker
structure needs a different technique.

**Example:**
```
1   4   7  11  15
2   5   8  12  19
3   6   9  16  22
10  13  14  17  24
18  21  23  26  30
```
Notice row 2 (`3,6,9,...`) starts *smaller* than row 1 ends (`...,19`) —
this would violate Day 12 Question 4's assumption, so binary search over a
flattened virtual array doesn't apply here.

**Idea — start at the top-right corner (or bottom-left) and walk:** at the
top-right corner, every value **below** is larger (column sorted), and
every value **to the left** is smaller (row sorted). So comparing the
current cell to the target tells you an unambiguous direction to move:
if the current value is **too large**, move **left** (eliminate this
column — everything below in this column is even larger, so it's all too
large too); if **too small**, move **down** (eliminate this row —
everything to the left in this row is even smaller).

```python
def search_matrix_ii(matrix, target):
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1        # start at top-right corner
    while row < len(matrix) and col >= 0:
        val = matrix[row][col]
        if val == target:
            return True
        elif val > target:
            col -= 1                          # too big — eliminate this column
        else:
            row += 1                          # too small — eliminate this row
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],
          [10,13,14,17,24],[18,21,23,26,30]]
print(search_matrix_ii(matrix, 5))    # True
print(search_matrix_ii(matrix, 20))   # False
```

**Trace for `target = 5`** (`row=0, col=4`):
| row | col | value | comparison | action |
|---|---|---|---|---|
| 0 | 4 | 15 | 15>5 | col→3 |
| 0 | 3 | 11 | 11>5 | col→2 |
| 0 | 2 | 7 | 7>5 | col→1 |
| 0 | 1 | 4 | 4<5 | row→1 |
| 1 | 1 | 5 | equal | **return True** |

Found in 5 steps. Matches.

**Why does eliminating an entire row or column at each step never
accidentally eliminate the target?** When `val > target`, everything in
`val`'s column at or below the current row is `>= val > target` (column
sortedness) — none of it can be the target, so discarding the whole column
(moving left, off it) is safe. Symmetrically for `val < target` and rows.
Every step provably removes at least one row or one column entirely from
consideration without risk.

**Complexity:** **O(rows + cols) time** (the pointer path length is bounded
by the sum of dimensions, since each step eliminates exactly one row or
column, and there are only `rows + cols - 1` such eliminations possible),
**O(1) space** — notice this is **worse** than Day 12 Question 4's
`O(log(rows × cols))` binary search, precisely because this problem's
weaker sortedness guarantee (rows/columns sorted individually, but not
globally chained) doesn't support binary search — a good illustration that
**how strong an ordering guarantee is** directly determines which
technique (and what complexity) is achievable.

## Additional Key Takeaways (Day 12 Supplement)

- **Row With Maximum Ones** and **Search a 2D Matrix II** both use a
  **corner-starting pointer walk** (top-right corner, moving left or down
  based on a comparison) — a distinct technique from Day 12's binary-search
  approach (Question 4), needed specifically because these problems have a
  *weaker* sortedness guarantee (rows/columns individually sorted, not one
  global sorted sequence).
- Comparing Day 12 Question 4 (`O(log(m·n))`, needs full global sortedness)
  against Search 2D Matrix II (`O(m+n)`, only needs row+column sortedness)
  is a clean illustration that **the strength of a sortedness guarantee
  directly bounds the best achievable complexity** — weaker guarantees
  can't unlock binary search, no matter how cleverly you index into the
  matrix.
