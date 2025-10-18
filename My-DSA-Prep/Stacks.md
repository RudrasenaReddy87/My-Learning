
# Stacks — humanized DSA guide

Stacks are LIFO structures used for DFS, expression evaluation, backtracking, and maintaining state.

## Python usage

- Use `list` as a stack with `append()` and `pop()` methods (O(1) amortized).

```python
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())  # 2
```

## Applications and examples

### 1. Evaluate Reverse Polish Notation (RPN)

```python
def eval_rpn(tokens):
	stack = []
	ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
	for t in tokens:
		if t in ops:
			# Stacks — ordered learning roadmap

			This roadmap covers core stack concepts, Python idioms, common algorithms, monotonic stacks, and practical interview patterns. Examples are runnable; copy them into a file and run when practicing.

			---

			Step 1 — Concept and Python idioms

			- A stack is a Last-In-First-Out (LIFO) structure. Common uses: DFS, backtracking, expression evaluation, and maintaining call frames.
			- Python: use `list` for a stack (`append`/`pop`) or `collections.deque` if you need O(1) appends/pops on both ends.

			Simple usage
			```python
			stack = []
			stack.append(1)
			stack.append(2)
			print(stack.pop())  # 2
			```

			Tip: `stack[-1]` peeks without popping.

			---

			Step 2 — Classic stack problems and implementations

			1) Evaluate Reverse Polish Notation (RPN)
			```python
			def eval_rpn(tokens):
				stack = []
				ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b, '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
				for t in tokens:
					if t in ops:
						b = stack.pop(); a = stack.pop()
						stack.append(ops[t](a,b))
					else:
						stack.append(int(t))
				return stack[-1]

			print(eval_rpn(['2','1','+','3','*']))  # 9
			```

			2) Valid parentheses (matching pairs)
			```python
			def is_valid_paren(s):
				stack = []
				pairs = {')':'(', ']':'[', '}':'{'}
				for ch in s:
					if ch in pairs.values():
						stack.append(ch)
					elif ch in pairs:
						if not stack or stack.pop() != pairs[ch]:
							return False
				return not stack

			print(is_valid_paren('()[]{}'))  # True
			```

			3) Convert recursion to iterative DFS (explicit stack)
			```python
			def dfs_iterative(adj, start):
				seen = set()
				stack = [start]
				order = []
				while stack:
					node = stack.pop()
					if node in seen:
						continue
					seen.add(node)
					order.append(node)
					for nei in adj.get(node, []):
						if nei not in seen:
							stack.append(nei)
				return order
			```

			---

			Step 3 — Monotonic stacks and next-greater patterns

			- Monotonic stacks store elements (or indices) in increasing or decreasing order. Useful for nearest-greater/smaller queries, histogram max area, and sliding window problems.

			1) Next Greater Element (right)
			```python
			def next_greater(a):
				res = [-1]*len(a)
				stack = []  # indices of a in decreasing order
				for i, x in enumerate(a):
					while stack and a[stack[-1]] < x:
						res[stack.pop()] = x
					stack.append(i)
				return res

			print(next_greater([2,1,2,4,3]))  # [4,2,4,-1,-1]
			```

			2) Largest Rectangle in Histogram (stack-based O(n))
			```python
			def largest_rectangle(heights):
				stack = []  # will store indices of increasing bar heights
				max_area = 0
				for i, h in enumerate(heights + [0]):
					while stack and heights[stack[-1]] > h:
						H = heights[stack.pop()]
						L = stack[-1] + 1 if stack else 0
						max_area = max(max_area, H * (i - L))
					stack.append(i)
				return max_area

			print(largest_rectangle([2,1,5,6,2,3]))  # 10
			```

			---

			Step 4 — Expression parsing (infix evaluation with two stacks)

			- Use two stacks (operators and operands) to evaluate infix expressions with precedence, or convert to postfix then evaluate.

			Simple infix evaluator (supports +,-,*,/ and parentheses)
			```python
			def precedence(op):
				return {'+':1, '-':1, '*':2, '/':2}.get(op, 0)

			def apply_op(ops, vals):
				op = ops.pop()
				b = vals.pop(); a = vals.pop()
				if op == '+': vals.append(a+b)
				elif op == '-': vals.append(a-b)
				elif op == '*': vals.append(a*b)
				elif op == '/': vals.append(int(a/b))

			def eval_infix(expr):
				vals, ops = [], []
				i = 0
				while i < len(expr):
					ch = expr[i]
					if ch.isdigit():
						j = i
						while j < len(expr) and expr[j].isdigit(): j += 1
						vals.append(int(expr[i:j])); i = j; continue
					if ch == '(':
						ops.append(ch)
					elif ch == ')':
						while ops and ops[-1] != '(':
							apply_op(ops, vals)
						ops.pop()
					elif ch in '+-*/':
						while ops and precedence(ops[-1]) >= precedence(ch):
							apply_op(ops, vals)
						ops.append(ch)
					i += 1
				while ops:
					apply_op(ops, vals)
				return vals[-1]

			print(eval_infix('2+(1+3)*2'))  # 10
			```

			---

			Step 5 — Pitfalls and interview checklist

			- Be careful with integer division semantics when implementing `/` in expression evaluators (use int(a/b) for trunc toward zero behavior similar to many languages).
			- When using stacks for indices, store indices rather than values when you need to compute widths/distances.
			- For monotonic stacks, think about sentinel values (append 0) to flush remaining items.

			Checklist to explain during an interview:
			- State the stack invariants (what it stores, order maintained)
			- Explain amortized costs for push/pop
			- Walk a small example with pointer/state transitions

			---

			Try it — runnable checks

			```python
			def _tests():
				assert eval_rpn(['2','1','+','3','*']) == 9
				assert is_valid_paren('()[]{}') is True
				assert next_greater([2,1,2,4,3]) == [4,2,4,-1,-1]
				assert largest_rectangle([2,1,5,6,2,3]) == 10
				assert eval_infix('2+(1+3)*2') == 10
				print('Stacks tests passed')

			if __name__ == '__main__':
				_tests()
			```

			---

			Next: I'll convert `Queues.md` into the roadmap style (I'll mark it in-progress and read the file before editing). If you'd rather change order or add language translations (C++/Java), say so now.


