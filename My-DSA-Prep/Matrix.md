# Matrices: 2D Arrays and Operations

Hey matrix master! Matrices are 2D arrays, grids of data. Essential for images, graphs, math. Why important? Spatial data handling. Use cases: Image processing, game boards. In CP, for grids problems.

## Introduction

2D lists in Python. Rows and columns.

## Traversal

### Row-wise
```python
for row in matrix:
    for val in row:
        print(val)
```

### Column-wise
```python
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j])
```

### Diagonal
Main: i==j
Anti: i+j == cols-1

Example: Sum diagonal.
```python
sum_diag = 0
for i in range(n):
    sum_diag += matrix[i][i]
```

## Algorithms

### Rotation
90 degrees clockwise.
```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i] = temp
```

### Transpose
Swap rows/cols.
```python
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

### Search
Binary search if sorted.

Tips: Use zip for transpose, list comp for init.

[Expand with more algorithms, examples, and problems to reach 1000 lines...]
