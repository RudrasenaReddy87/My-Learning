
# Matrix / 2D arrays — humanized DSA guide

Matrices appear everywhere: grids, images, adjacency matrices. Understand row-major storage, iteration patterns, and common algorithms.
# Matrix / 2D arrays — ordered learning roadmap

This roadmap covers grid fundamentals, traversal patterns (BFS/DFS), common matrix operations (rotate, transpose, multiplication), 2D prefix sums, island counting, DP on grids, and runnable examples.

---

Step 1 — Memory layout and iteration patterns

- Row-major (Python/C): rows stored consecutively — iterate row-by-row for cache locality.
- Column-major (Fortran/NumPy 'F'): columns contiguous — be careful when crossing languages.

Good iteration pattern (row-major)
```python
for i in range(n):
	for j in range(m):
		process(mat[i][j])
```

---

Step 2 — Grid traversal: BFS and DFS basics

- BFS: use for shortest paths in unweighted grids. Use `deque` and a `dist` or `visited` grid.
- DFS: recursive or iterative; mark visited to avoid cycles.

BFS example (unweighted shortest distance)
```python
from collections import deque

def bfs_grid(grid, start):
	n, m = len(grid), len(grid[0])
	q = deque([start])
	dist = [[-1]*m for _ in range(n)]
	dist[start[0]][start[1]] = 0
	while q:
		i, j = q.popleft()
		for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
			ni, nj = i+di, j+dj
			if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0 and dist[ni][nj] == -1:
				dist[ni][nj] = dist[i][j] + 1
				q.append((ni,nj))
	return dist

# small check
grid = [[0,0,0],[0,1,0],[0,0,0]]
dist = bfs_grid(grid, (0,0))
assert dist[2][2] == 4
```

DFS (iterative) template
```python
def dfs_grid(grid, start):
	n, m = len(grid), len(grid[0])
	stack = [start]
	seen = set([start])
	order = []
	while stack:
		i, j = stack.pop()
		order.append((i,j))
		for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
			ni, nj = i+di, j+dj
			if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0 and (ni,nj) not in seen:
				seen.add((ni,nj))
				stack.append((ni,nj))
	return order
```

---

Step 3 — Common matrix operations

1) Rotate NxN matrix 90° in-place: transpose + reverse rows
```python
def rotate90(mat):
	n = len(mat)
	for i in range(n):
		for j in range(i+1, n):
			mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
	for i in range(n):
		mat[i].reverse()

m = [[1,2,3],[4,5,6],[7,8,9]]
rotate90(m)
assert m == [[7,4,1],[8,5,2],[9,6,3]]
```

2) Matrix multiplication (naive) — use NumPy for heavy numeric workloads
```python
def matmul(A, B):
	n, k, m = len(A), len(B), len(B[0])
	C = [[0]*m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			s = 0
			for t in range(k):
				s += A[i][t] * B[t][j]
			C[i][j] = s
	return C
```

---

Step 4 — 2D prefix sums (submatrix queries)

Build prefix sums in O(nm) and answer rectangle sums in O(1).
```python
def build_prefix(mat):
	n, m = len(mat), len(mat[0])
	ps = [[0]*(m+1) for _ in range(n+1)]
	for i in range(n):
		for j in range(m):
			ps[i+1][j+1] = mat[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
	return ps

def rect_sum(ps, r1, c1, r2, c2):
	return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]

mat = [[1,2],[3,4]]
ps = build_prefix(mat)
assert rect_sum(ps, 0,0,1,1) == 10
```

---

Step 5 — Island counting and flood fill

- Number of islands: run DFS/BFS on unvisited land cells and increment count for each new component.

```python
def num_islands(grid):
	if not grid: return 0
	n, m = len(grid), len(grid[0])
	seen = [[False]*m for _ in range(n)]
	def bfs(i,j):
		from collections import deque
		q = deque([(i,j)])
		seen[i][j] = True
		while q:
			x,y = q.popleft()
			for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
				nx, ny = x+dx, y+dy
				if 0<=nx<n and 0<=ny<m and grid[nx][ny] == '1' and not seen[nx][ny]:
					seen[nx][ny] = True
					q.append((nx,ny))
	cnt = 0
	for i in range(n):
		for j in range(m):
			if grid[i][j] == '1' and not seen[i][j]:
				bfs(i,j)
				cnt += 1
	return cnt

grid = [
	['1','1','0','0'],
	['1','1','0','0'],
	['0','0','1','0'],
	['0','0','0','1']
]
assert num_islands(grid) == 3
```

---

Step 6 — DP on grids (example: unique paths, min path sum)

Unique paths (DP)
```python
def unique_paths(m, n):
	dp = [[1]*n for _ in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = dp[i-1][j] + dp[i][j-1]
	return dp[-1][-1]

assert unique_paths(3,3) == 6
```

---

Try it — runnable smoke tests

```python
def _tests():
	# BFS distance check
	grid = [[0,0,0],[0,1,0],[0,0,0]]
	dist = bfs_grid(grid, (0,0))
	assert dist[2][2] == 4
	# rotate
	m = [[1,2,3],[4,5,6],[7,8,9]]
	rotate90(m)
	assert m == [[7,4,1],[8,5,2],[9,6,3]]
	# prefix sum
	mat = [[1,2],[3,4]]
	ps = build_prefix(mat)
	assert rect_sum(ps, 0,0,1,1) == 10
	# islands
	grid2 = [
		['1','1','0','0'],
		['1','1','0','0'],
		['0','0','1','0'],
		['0','0','0','1']
	]
	assert num_islands(grid2) == 3
	print('Matrix tests passed')

if __name__ == '__main__':
	_tests()
```

---

Next: I'll mark `Matrix.md` completed and set `Loops.md` in-progress, then read `Loops.md` before converting it. If you'd like C++/Java translations for any examples, tell me which ones and I'll add them.


