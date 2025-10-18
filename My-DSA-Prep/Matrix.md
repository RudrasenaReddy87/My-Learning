# Matrices: 2D Arrays and Operations

Hey matrix master! Matrices are 2D arrays, grids of data representing spatial relationships. Essential for images, graphs, math computations. Why important? Handle spatial data efficiently. Use cases: Image processing, game boards, adjacency graphs. In competitive programming (CP), matrices solve grid-based problems like pathfinding, islands, and puzzles.

## Introduction to Matrices

Matrices are rectangular arrays of numbers, symbols, or expressions arranged in rows and columns. In programming, they're 2D lists or arrays.

### What Are Matrices?
- **Definition**: A matrix is a 2D array with m rows and n columns, denoted as m x n.
- **Elements**: Accessed by matrix[i][j], where i is row, j is column (0-based).
- **Dimensions**: Rows x Columns, e.g., 3x3 for square matrix.

### Types of Matrices
- **Square Matrix**: m = n, e.g., 3x3.
- **Rectangular Matrix**: m ≠ n.
- **Identity Matrix**: Diagonal 1s, rest 0s.
- **Sparse Matrix**: Mostly zeros, efficient storage needed.
- **Jagged Array**: Rows of different lengths (not true matrix).

### Representations
- **2D List in Python**: matrix = [[1,2,3], [4,5,6]]
- **Numpy Array**: import numpy as np; matrix = np.array([[1,2],[3,4]])
- **Flattened**: 1D array with row-major order.

### Use Cases
- **Math**: Linear algebra, transformations.
- **Images**: Pixels as matrix.
- **Graphs**: Adjacency matrix.
- **CP**: Grids for mazes, boards, dynamic programming tables.

## Initialization and Representation

### Using List Comprehension
```python
# 3x3 matrix of zeros
matrix = [[0 for _ in range(3)] for _ in range(3)]

# Identity matrix
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]

# Random matrix
import random
matrix = [[random.randint(0,9) for _ in range(4)] for _ in range(3)]
```

### Using Numpy (Python)
```python
import numpy as np

# Create matrix
matrix = np.array([[1,2,3], [4,5,6]])

# Zeros, ones, identity
zeros = np.zeros((3,3))
ones = np.ones((2,4))
identity = np.eye(3)

# Reshape
arr = np.arange(12).reshape(3,4)
```

### Jagged Arrays
```python
jagged = [[1,2], [3,4,5], [6]]
# Row 0: 2 elements, Row 1: 3, Row 2: 1
```

## Traversal Techniques

Traversal visits each element. Time: O(rows * cols)

### Row-wise Traversal
```python
def traverse_row(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()
```

### Column-wise Traversal
```python
def traverse_col(matrix):
    if not matrix: return
    cols = len(matrix[0])
    rows = len(matrix)
    for j in range(cols):
        for i in range(rows):
            print(matrix[i][j], end=" ")
        print()
```

### Diagonal Traversal
- **Main Diagonal**: i == j
- **Anti-Diagonal**: i + j == cols - 1

```python
def sum_diagonals(matrix):
    n = len(matrix)
    main_sum = anti_sum = 0
    for i in range(n):
        main_sum += matrix[i][i]
        anti_sum += matrix[i][n-1-i]
    return main_sum, anti_sum
```

### Zigzag Traversal
Alternate directions per row.

```python
def zigzag(matrix):
    result = []
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1])
    return result
```

### Spiral Traversal
Clockwise from top-left.

```python
def spiral(matrix):
    if not matrix: return []
    result = []
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1
    while top <= bottom and left <= right:
        # Top row
        for j in range(left, right+1):
            result.append(matrix[top][j])
        top += 1
        # Right column
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1
        # Bottom row (if needed)
        if top <= bottom:
            for j in range(right, left-1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        # Left column (if needed)
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
```

## Basic Operations

### Sum and Product
```python
def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)

def matrix_product(matrix):
    prod = 1
    for row in matrix:
        for val in row:
            prod *= val
    return prod
```

### Min/Max in Matrix
```python
def find_min_max(matrix):
    if not matrix: return None, None
    min_val = max_val = matrix[0][0]
    for row in matrix:
        for val in row:
            if val < min_val: min_val = val
            if val > max_val: max_val = val
    return min_val, max_val
```

### Search
Linear search:
```python
def search(matrix, target):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == target:
                return i, j
    return -1, -1
```

Binary search (if row/column sorted):
```python
def search_sorted(matrix, target):
    if not matrix: return False
    rows, cols = len(matrix), len(matrix[0])
    i, j = 0, cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False
```

### Sorting Rows/Columns
Sort each row:
```python
for row in matrix:
    row.sort()
```

Sort each column:
```python
for j in range(cols):
    col = [matrix[i][j] for i in range(rows)]
    col.sort()
    for i in range(rows):
        matrix[i][j] = col[i]
```

## Advanced Algorithms

### Rotation
90 degrees clockwise (in-place):
```python
def rotate_90_clockwise(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
```

180 degrees:
```python
def rotate_180(matrix):
    matrix.reverse()
    for row in matrix:
        row.reverse()
```

270 degrees (or 90 counterclockwise):
```python
def rotate_270_clockwise(matrix):
    rotate_90_clockwise(matrix)
    rotate_90_clockwise(matrix)
    rotate_90_clockwise(matrix)
```

### Transpose
```python
def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

# In-place for square
def transpose_square(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### Matrix Multiplication
```python
def multiply(A, B):
    m, k = len(A), len(A[0])
    k2, n = len(B), len(B[0])
    if k != k2: return None
    result = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for p in range(k):
                result[i][j] += A[i][p] * B[p][j]
    return result
```

### Determinant (for 2x2/3x3)
```python
def det_2x2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def det_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
```

### Inversion (Simplified for 2x2)
```python
def invert_2x2(matrix):
    det = det_2x2(matrix)
    if det == 0: return None
    return [[matrix[1][1]/det, -matrix[0][1]/det],
            [-matrix[1][0]/det, matrix[0][0]/det]]
```

## Graph Representations

### Adjacency Matrix
```python
# For graph with n nodes
adj_matrix = [[0]*n for _ in range(n)]
# Add edge: adj_matrix[u][v] = 1 (undirected) or weight
```

### DFS on Grid
```python
def dfs_grid(matrix, i, j, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or visited[i][j] or matrix[i][j] == 0:
        return
    visited[i][j] = True
    # Process
    dfs_grid(matrix, i+1, j, visited)
    dfs_grid(matrix, i-1, j, visited)
    dfs_grid(matrix, i, j+1, visited)
    dfs_grid(matrix, i, j-1, visited)
```

### BFS on Grid
```python
from collections import deque
def bfs_grid(matrix, start_i, start_j):
    if not matrix: return
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False]*cols for _ in range(rows)]
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True
    while queue:
        i, j = queue.popleft()
        # Process
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj] and matrix[ni][nj] == 1:
                visited[ni][nj] = True
                queue.append((ni, nj))
```

## Image Processing Basics

### Convolution (Simple 3x3 Kernel)
```python
def convolve(matrix, kernel):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0]*cols for _ in range(rows)]
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            sum_val = 0
            for ki in range(3):
                for kj in range(3):
                    sum_val += matrix[i-1+ki][j-1+kj] * kernel[ki][kj]
            result[i][j] = sum_val
    return result
```

### Edge Detection Kernel
```python
sobel_x = [[-1,0,1], [-2,0,2], [-1,0,1]]
# Apply convolve(matrix, sobel_x)
```

## CP Problems and Solutions

### Number of Islands (LeetCode 200)
```python
def num_islands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '0'  # Mark visited
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
```

### Word Search (LeetCode 79)
```python
def exist(board, word):
    if not board: return False
    rows, cols = len(board), len(board[0])
    for i in range(rows):
        for j in range(cols):
            if dfs_word(board, i, j, word, 0):
                return True
    return False

def dfs_word(board, i, j, word, index):
    if index == len(word): return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
        return False
    temp = board[i][j]
    board[i][j] = '#'  # Mark visited
    found = dfs_word(board, i+1, j, word, index+1) or \
            dfs_word(board, i-1, j, word, index+1) or \
            dfs_word(board, i, j+1, word, index+1) or \
            dfs_word(board, i, j-1, word, index+1)
    board[i][j] = temp
    return found
```

### Shortest Path in Grid (BFS)
```python
def shortest_path(grid, start, end):
    from collections import deque
    if not grid: return -1
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # i, j, dist
    visited = set([(start[0], start[1])])
    while queue:
        i, j, dist = queue.popleft()
        if (i, j) == end: return dist
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 0 and (ni,nj) not in visited:
                visited.add((ni,nj))
                queue.append((ni, nj, dist+1))
    return -1
```

### Sudoku Solver (Backtracking)
```python
def solve_sudoku(board):
    def is_valid(num, pos):
        row, col = pos
        # Check row
        for j in range(9):
            if board[row][j] == str(num) and j != col:
                return False
        # Check col
        for i in range(9):
            if board[i][col] == str(num) and i != row:
                return False
        # Check box
        box_i = row // 3
        box_j = col // 3
        for i in range(box_i*3, box_i*3+3):
            for j in range(box_j*3, box_j*3+3):
                if board[i][j] == str(num) and (i,j) != pos:
                    return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in range(1,10):
                        if is_valid(num, (i,j)):
                            board[i][j] = str(num)
                            if solve():
                                return True
                            board[i][j] = '.'
                    return False
        return True
    solve()
```

## Optimizations

### Space-Time Trade-offs
- **In-place operations**: Modify matrix directly to save space.
- **Sparse matrices**: Use dictionaries for zeros-heavy matrices.
- **Caching**: Store computed values.

### In-Place Rotation
As above, O(1) space.

### Boundary Checks
Always check i >=0, i < rows, etc., to avoid index errors.

## Pitfalls and Common Mistakes

### Index Errors
- **Mistake**: Accessing matrix[i][j] without bounds.
- **Fix**: Check 0 <= i < rows and 0 <= j < cols.

### Modifying During Traversal
- **Mistake**: Changing values while iterating, affecting logic.
- **Fix**: Use copies or mark visited properly.

### Memory Usage
- **Mistake**: Creating large matrices in memory-constrained environments.
- **Fix**: Process row-by-row or use generators.

### Off-by-One in Loops
- **Mistake**: range(rows) vs range(rows-1).
- **Fix**: Double-check loop bounds.

### Assuming Square Matrix
- **Mistake**: len(matrix) == len(matrix[0]).
- **Fix**: Handle rectangular matrices.

## Multi-Language Examples

### C++ Matrix Initialization
```cpp
#include <vector>
using namespace std;

vector<vector<int>> matrix(3, vector<int>(3, 0));  // 3x3 zeros
```

### Java Transpose
```java
public int[][] transpose(int[][] matrix) {
    int m = matrix.length, n = matrix[0].length;
    int[][] transposed = new int[n][m];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            transposed[j][i] = matrix[i][j];
        }
    }
    return transposed;
}
```

### C++ Spiral Traversal
```cpp
#include <vector>
using namespace std;

vector<int> spiralOrder(vector<vector<int>>& matrix) {
    vector<int> result;
    if (matrix.empty()) return result;
    int top = 0, bottom = matrix.size() - 1;
    int left = 0, right = matrix[0].size() - 1;
    while (top <= bottom && left <= right) {
        for (int j = left; j <= right; j++) result.push_back(matrix[top][j]);
        top++;
        for (int i = top; i <= bottom; i++) result.push_back(matrix[i][right]);
        right--;
        if (top <= bottom) {
            for (int j = right; j >= left; j--) result.push_back(matrix[bottom][j]);
            bottom--;
        }
        if (left <= right) {
            for (int i = bottom; i >= top; i--) result.push_back(matrix[i][left]);
            left++;
        }
    }
    return result;
}
```

### Java DFS for Islands
```java
public int numIslands(char[][] grid) {
    if (grid == null || grid.length == 0) return 0;
    int count = 0;
    for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[0].length; j++) {
            if (grid[i][j] == '1') {
                dfs(grid, i, j);
                count++;
            }
        }
    }
    return count;
}

private void dfs(char[][] grid, int i, int j) {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != '1') return;
    grid[i][j] = '0';
    dfs(grid, i + 1, j);
    dfs(grid, i - 1, j);
    dfs(grid, i, j + 1);
    dfs(grid, i, j - 1);
}
```

## Practice Section

### Solved Examples

1. **Matrix Sum**
   ```python
   matrix = [[1,2,3], [4,5,6]]
   total = sum(sum(row) for row in matrix)
   print(total)  # 21
   ```

2. **Find Max in Each Row**
   ```python
   matrix = [[1,2,3], [4,5,6]]
   for row in matrix:
       print(max(row))
   # 3
   # 6
   ```

3. **Check Symmetric Matrix**
   ```python
   def is_symmetric(matrix):
       n = len(matrix)
       for i in range(n):
           for j in range(n):
               if matrix[i][j] != matrix[j][i]:
                   return False
       return True
   ```

### Walkthrough: Spiral Traversal
For [[1,2,3],[4,5,6],[7,8,9]]:
- Top row: 1,2,3
- Right: 6,9
- Bottom: 8,7
- Left: 4
- Result: [1,2,3,6,9,8,7,4]

### LeetCode-Style Problems
1. Rotate Image: In-place 90 degree rotation.
2. Set Matrix Zeroes: If element is 0, set row and column to 0.
3. Valid Sudoku: Check if board is valid.
4. Surrounded Regions: Capture regions surrounded by 'X'.

## Comparisons

### Matrix vs Array
- Arrays: 1D, simple access.
- Matrices: 2D, spatial ops, higher complexity.

### DFS vs BFS on Grids
- DFS: Recursion, stack overflow risk, good for exploration.
- BFS: Queue, finds shortest path, uses more space.

## Appendices

### Glossary
- **Matrix**: 2D array.
- **Transpose**: Swap rows and columns.
- **Adjacency Matrix**: Graph representation.
- **Convolution**: Sliding window operation.

### Time Complexities
- Traversal: O(m*n)
- Rotation: O(n^2)
- Multiplication: O(m*n*p)
- Search: O(m*n) linear, O(m+n) sorted

### References
- LeetCode Matrix problems
- CLRS for algorithms
- Numpy docs for advanced ops

Personal note: Matrices are powerful but error-prone; always visualize the grid before coding.
