# Complete SQL Guide (MySQL) 📘

A complete, example-driven reference for learning SQL from scratch to advanced — window functions, CTEs, indexing, transactions, and real-world query patterns. All examples use **MySQL syntax**.

## 🗂 Sample Schema Used Throughout

Most examples reuse this schema so you can follow along consistently.

```sql
CREATE TABLE departments (
    dept_id     INT PRIMARY KEY AUTO_INCREMENT,
    dept_name   VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    emp_id      INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(50) NOT NULL,
    dept_id     INT,
    salary      DECIMAL(10,2),
    hire_date   DATE,
    manager_id  INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

INSERT INTO departments (dept_name) VALUES ('Engineering'), ('Sales'), ('HR');

INSERT INTO employees (name, dept_id, salary, hire_date, manager_id) VALUES
('Alice', 1, 95000, '2019-03-01', NULL),
('Bob',   1, 85000, '2020-06-15', 1),
('Carol', 1, 78000, '2021-01-10', 1),
('Dave',  2, 60000, '2018-11-20', NULL),
('Eve',   2, 62000, '2022-02-05', 4),
('Frank', 3, 55000, '2020-09-01', NULL);
```

---

## Table of Contents
1. Basics
2. SQL Commands
3. Data Types
4. Table Operations
5. Data Manipulation
6. SELECT Queries
7. DISTINCT
8. Filtering
9. Operators
10. NULL Handling
11. Pattern Matching
12. Range Filtering
13. Set Membership
14. Sorting
15. Limiting Results
16. Aggregate Functions
17. GROUP BY
18. HAVING
19. Joins Basics
20. Joins Advanced
21. Self Join
22. Subqueries
23. Correlated Subqueries
24. Set Operations
25. CASE Statements
26. Window Functions Basics
27. Ranking Functions
28. Aggregate Window Functions
29. Analytical Functions
30. CTE (Common Table Expressions)
31. Views
32. Indexing
33. Index Types
34. Performance Optimization
35. Transactions
36. ACID Properties
37. Constraints
38. Normalization
39. Denormalization
40. String Functions
41. Date Functions
42. Numeric Functions
43. Conditional Queries
44. Data Integrity
45. Temporary Tables
46. Stored Procedures
47. Triggers
48. Security
49. Backup & Recovery
50. Real-world Problem Solving
51. Bonus: GROUP_CONCAT()
52. Bonus: JSON Functions
53. Bonus: Bulk Import/Export (LOAD DATA INFILE)
54. Bonus: User-Defined Functions (UDFs)
55. Bonus: Cursors & Error Handling
56. Bonus: Table Partitioning
57. Bonus: Character Sets & Collations
58. Bonus: AUTO_INCREMENT / Sequences
59. Bonus: Locking & Deadlocks
60. Bonus: Full-Text Search
61. Bonus: Roles

---

## 1. Basics

**Definition:**
SQL (Structured Query Language) is the standard language used to communicate with relational databases — to define, query, and manipulate data. An **RDBMS** (Relational Database Management System) stores data in **tables** made of **rows** (records) and **columns** (fields/attributes), with relationships between tables enforced through keys.

Key concepts:
- **Table** — a collection of related data organized in rows and columns (e.g., `employees`).
- **Row (record/tuple)** — a single entry in a table.
- **Column (field/attribute)** — a named property with a defined data type.
- **Schema** — the structure/blueprint of the database (tables, columns, relationships).
- **Primary Key** — uniquely identifies each row.
- **Foreign Key** — links one table to another.

**Syntax (conceptual):**
```sql
-- A database contains schemas which contain tables
CREATE DATABASE company;
USE company;
```

**Example:**
```sql
CREATE DATABASE company;
USE company;
-- Now create tables inside it (see schema above)
```

**Tips & Tricks:**
- Always design your schema (tables + relationships) on paper/diagram before writing `CREATE TABLE` statements.
- RDBMS examples: MySQL, PostgreSQL, SQL Server, Oracle, SQLite — core SQL is similar, but functions/syntax vary slightly (this guide uses MySQL).
- Table and column names: use `snake_case`, avoid reserved words (`order`, `group`, `select`).

---

## 2. SQL Commands

**Definition:**
SQL commands are grouped into five categories based on purpose:

| Category | Full Form | Purpose | Commands |
|---|---|---|---|
| DDL | Data Definition Language | Define/alter structure | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| DML | Data Manipulation Language | Modify data | `INSERT`, `UPDATE`, `DELETE` |
| DQL | Data Query Language | Read data | `SELECT` |
| TCL | Transaction Control Language | Manage transactions | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |
| DCL | Data Control Language | Manage permissions | `GRANT`, `REVOKE` |

**Syntax & Example:**
```sql
-- DDL
CREATE TABLE test (id INT);
ALTER TABLE test ADD COLUMN name VARCHAR(50);
DROP TABLE test;

-- DML
INSERT INTO employees (name, dept_id, salary) VALUES ('Grace', 1, 70000);
UPDATE employees SET salary = 72000 WHERE name = 'Grace';
DELETE FROM employees WHERE name = 'Grace';

-- DQL
SELECT * FROM employees;

-- TCL
START TRANSACTION;
UPDATE employees SET salary = salary * 1.1;
COMMIT;

-- DCL
GRANT SELECT ON company.* TO 'analyst'@'localhost';
REVOKE SELECT ON company.* FROM 'analyst'@'localhost';
```

**Tips & Tricks:**
- DDL commands **auto-commit** in MySQL — you can't roll them back like DML.
- Remember the order of execution isn't the order you type — but for commands, execution order = statement order.
- `TRUNCATE` is DDL (resets table, faster, no rollback in most engines) vs `DELETE` which is DML (row-by-row, can be rolled back, can use `WHERE`).

---

## 3. Data Types

**Definition:**
Data types define what kind of value a column can store. Choosing the right type saves space and enforces data integrity.

**Common MySQL Data Types:**

| Type | Description | Example |
|---|---|---|
| `INT` | Whole numbers | `age INT` |
| `BIGINT` | Large whole numbers | `population BIGINT` |
| `DECIMAL(p,s)` | Exact fixed-point number | `price DECIMAL(10,2)` |
| `FLOAT` / `DOUBLE` | Approximate floating-point number | `rating FLOAT` |
| `VARCHAR(n)` | Variable-length string, max n chars | `name VARCHAR(100)` |
| `CHAR(n)` | Fixed-length string | `country_code CHAR(2)` |
| `TEXT` | Long text | `description TEXT` |
| `DATE` | Date only (`YYYY-MM-DD`) | `dob DATE` |
| `DATETIME` / `TIMESTAMP` | Date + time | `created_at DATETIME` |
| `BOOLEAN` (alias for `TINYINT(1)`) | True/False (0/1) | `is_active BOOLEAN` |
| `ENUM` | Fixed list of allowed values | `status ENUM('active','inactive')` |

**Syntax:**
```sql
CREATE TABLE products (
    product_id  INT PRIMARY KEY,
    name        VARCHAR(100),
    price       DECIMAL(10,2),
    in_stock    BOOLEAN DEFAULT TRUE,
    added_on    DATE,
    rating      FLOAT
);
```

**Example:**
```sql
INSERT INTO products VALUES (1, 'Laptop', 55999.99, TRUE, '2024-05-01', 4.5);
```

**Tips & Tricks:**
- Use `DECIMAL` (not `FLOAT`) for money — `FLOAT` has rounding errors.
- Prefer `VARCHAR` over `CHAR` unless the length is truly fixed (like a 2-letter country code).
- `BOOLEAN` in MySQL is just `TINYINT(1)` under the hood — values are stored as 0/1.
- Always set a length/precision for `VARCHAR` and `DECIMAL` — don't leave it default.

---

## 4. Table Operations

**Definition:**
Operations to create, modify, and remove table structures.

**Syntax:**
```sql
-- CREATE
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints
);

-- ALTER
ALTER TABLE table_name ADD COLUMN col_name datatype;
ALTER TABLE table_name DROP COLUMN col_name;
ALTER TABLE table_name MODIFY COLUMN col_name new_datatype;
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;
ALTER TABLE table_name RENAME TO new_table_name;

-- DROP
DROP TABLE table_name;
```

**Example:**
```sql
CREATE TABLE interns (
    intern_id INT PRIMARY KEY,
    name VARCHAR(50)
);

ALTER TABLE interns ADD COLUMN stipend DECIMAL(8,2);
ALTER TABLE interns MODIFY COLUMN stipend DECIMAL(10,2);
ALTER TABLE interns RENAME COLUMN stipend TO monthly_stipend;
ALTER TABLE interns DROP COLUMN monthly_stipend;

DROP TABLE interns;
```

**Tips & Tricks:**
- `DROP TABLE` deletes structure + data permanently — always back up first.
- `TRUNCATE TABLE table_name` empties a table fast but keeps the structure (resets `AUTO_INCREMENT` too, unlike `DELETE`).
- Use `CREATE TABLE IF NOT EXISTS` and `DROP TABLE IF EXISTS` to avoid errors in scripts.
- On large production tables, `ALTER TABLE` can lock the table — check for online DDL tools if the table is huge.

---

## 5. Data Manipulation

**Definition:**
DML commands add, change, or remove the actual data (rows) inside tables.

**Syntax:**
```sql
-- INSERT
INSERT INTO table_name (col1, col2) VALUES (val1, val2);
INSERT INTO table_name VALUES (val1, val2, ...);        -- all columns, in order
INSERT INTO table_name (col1, col2) VALUES (v1,v2), (v3,v4); -- multi-row

-- UPDATE
UPDATE table_name SET col1 = val1 WHERE condition;

-- DELETE
DELETE FROM table_name WHERE condition;
```

**Example:**
```sql
INSERT INTO employees (name, dept_id, salary, hire_date)
VALUES ('Henry', 2, 58000, '2023-04-12');

INSERT INTO employees (name, dept_id, salary, hire_date) VALUES
('Ivy', 1, 91000, '2022-07-01'),
('Jack', 3, 53000, '2023-01-15');

UPDATE employees SET salary = salary * 1.05 WHERE dept_id = 1;

DELETE FROM employees WHERE name = 'Jack';
```

**Tips & Tricks:**
- **Always** use `WHERE` with `UPDATE`/`DELETE` unless you intend to affect every row — test with a `SELECT` using the same `WHERE` first.
- Wrap risky `UPDATE`/`DELETE` in a transaction (`START TRANSACTION` ... `ROLLBACK`/`COMMIT`) so mistakes are reversible.
- Multi-row `INSERT` is much faster than multiple single-row inserts.
- Use `INSERT ... ON DUPLICATE KEY UPDATE` in MySQL for upsert behavior.

---

## 6. SELECT Queries

**Definition:**
`SELECT` retrieves data from one or more tables. It's the core of DQL (Data Query Language).

**Syntax:**
```sql
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;          -- all columns
SELECT column1 AS alias FROM table_name;
```

**Example:**
```sql
SELECT name, salary FROM employees;

SELECT * FROM employees;

SELECT name AS employee_name, salary AS monthly_salary FROM employees;

-- Computed column
SELECT name, salary, salary * 12 AS annual_salary FROM employees;
```

**Tips & Tricks:**
- Avoid `SELECT *` in production code — it's slower and breaks if columns change; name columns explicitly.
- Use aliases (`AS`) to make output readable — `AS` is optional (`salary sal` also works) but improves clarity.
- Logical order of a full query: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` (even though you *write* `SELECT` first).

---

## 7. DISTINCT

**Definition:**
`DISTINCT` removes duplicate rows from the result set, based on the selected column(s).

**Syntax:**
```sql
SELECT DISTINCT column1, column2 FROM table_name;
```

**Example:**
```sql
SELECT DISTINCT dept_id FROM employees;

-- Distinct combination of two columns
SELECT DISTINCT dept_id, salary FROM employees;

-- Count distinct values
SELECT COUNT(DISTINCT dept_id) AS total_departments FROM employees;
```

**Tips & Tricks:**
- `DISTINCT` applies to the **combination** of all selected columns, not each column independently.
- `DISTINCT` can be slow on large tables since it typically requires sorting/hashing — use only when needed.
- `COUNT(DISTINCT col)` is a common way to count unique values.

---

## 8. Filtering (WHERE Clause)

**Definition:**
`WHERE` filters rows based on a condition, applied **before** grouping/aggregation.

**Syntax:**
```sql
SELECT column1, column2
FROM table_name
WHERE condition;
```

**Example:**
```sql
SELECT * FROM employees WHERE dept_id = 1;

SELECT * FROM employees WHERE salary > 60000;

SELECT * FROM employees WHERE dept_id = 1 AND salary > 80000;

SELECT * FROM employees WHERE hire_date >= '2020-01-01';
```

**Tips & Tricks:**
- `WHERE` cannot use column aliases defined in the same `SELECT` (use `HAVING` or a subquery/CTE instead).
- `WHERE` cannot filter on aggregate functions (`WHERE COUNT(*) > 5` is invalid) — use `HAVING` for that.
- Index columns that are frequently used in `WHERE` clauses to speed up filtering.

---

## 9. Operators

**Definition:**
Operators are used to build conditions and expressions.

**Comparison operators:** `=`, `!=` / `<>`, `>`, `<`, `>=`, `<=`
**Logical operators:** `AND`, `OR`, `NOT`
**Other:** `+ - * /` (arithmetic), `%` (modulo)

**Syntax & Example:**
```sql
-- Comparison
SELECT * FROM employees WHERE salary >= 60000;
SELECT * FROM employees WHERE dept_id <> 1;

-- Logical AND / OR / NOT
SELECT * FROM employees WHERE dept_id = 1 AND salary > 80000;
SELECT * FROM employees WHERE dept_id = 1 OR dept_id = 3;
SELECT * FROM employees WHERE NOT dept_id = 1;

-- Combining with parentheses (important!)
SELECT * FROM employees
WHERE dept_id = 1 AND (salary > 90000 OR hire_date < '2020-01-01');
```

**Tips & Tricks:**
- `AND` has higher precedence than `OR` — always use parentheses to make intent explicit and avoid logic bugs.
- Use `<>` or `!=` interchangeably in MySQL; `<>` is the ANSI standard.
- `NOT` can be combined with `IN`, `LIKE`, `BETWEEN`: `NOT IN`, `NOT LIKE`, `NOT BETWEEN`.

---

## 10. NULL Handling

**Definition:**
`NULL` represents missing/unknown data. It is not equal to anything, including itself — so `= NULL` never matches. Use `IS NULL` / `IS NOT NULL`.

**Syntax:**
```sql
SELECT * FROM table_name WHERE column IS NULL;
SELECT * FROM table_name WHERE column IS NOT NULL;
```

**Example:**
```sql
SELECT * FROM employees WHERE manager_id IS NULL;   -- top-level employees

SELECT * FROM employees WHERE manager_id IS NOT NULL;

-- Replace NULL with a default value
SELECT name, IFNULL(manager_id, 0) AS manager_id FROM employees;
SELECT name, COALESCE(manager_id, 0) AS manager_id FROM employees;
```

**Tips & Tricks:**
- `WHERE column = NULL` always returns **zero rows** — this is a very common beginner bug. Always use `IS NULL`.
- `COALESCE(a, b, c, ...)` returns the first non-NULL value — works across all databases (more portable than `IFNULL`, which is MySQL-specific).
- Aggregate functions (except `COUNT(*)`) ignore `NULL` values.
- `NULL` in arithmetic/string concatenation makes the whole result `NULL` (e.g., `5 + NULL = NULL`).

---

## 11. Pattern Matching (LIKE)

**Definition:**
`LIKE` matches string patterns using wildcards: `%` (any number of characters, including zero) and `_` (exactly one character).

**Syntax:**
```sql
SELECT * FROM table_name WHERE column LIKE 'pattern';
```

**Example:**
```sql
SELECT * FROM employees WHERE name LIKE 'A%';      -- starts with A
SELECT * FROM employees WHERE name LIKE '%e';       -- ends with e
SELECT * FROM employees WHERE name LIKE '%ar%';     -- contains 'ar'
SELECT * FROM employees WHERE name LIKE '_ob';      -- 3 letters, ends in 'ob' -> Bob
SELECT * FROM employees WHERE name NOT LIKE 'A%';   -- doesn't start with A

-- Case-insensitive by default in MySQL for most collations
SELECT * FROM employees WHERE name LIKE 'alice';    -- matches 'Alice'
```

**Tips & Tricks:**
- `LIKE` with a leading `%` (e.g., `'%son'`) can't use a standard index efficiently — full table scan. For heavy text search, use `FULLTEXT` indexes.
- Use `REGEXP` (MySQL) for more powerful pattern matching: `WHERE name REGEXP '^A'`.
- Escape literal `%` or `_` using `ESCAPE`: `WHERE code LIKE '50\%' ESCAPE '\'`.

---

## 12. Range Filtering (BETWEEN)

**Definition:**
`BETWEEN` filters values within an inclusive range.

**Syntax:**
```sql
SELECT * FROM table_name WHERE column BETWEEN value1 AND value2;
```

**Example:**
```sql
SELECT * FROM employees WHERE salary BETWEEN 60000 AND 90000;

SELECT * FROM employees WHERE hire_date BETWEEN '2019-01-01' AND '2021-12-31';

SELECT * FROM employees WHERE salary NOT BETWEEN 60000 AND 90000;
```

**Tips & Tricks:**
- `BETWEEN` is **inclusive** on both ends (`x >= value1 AND x <= value2`).
- Works with numbers, dates, and even strings (alphabetical range).
- For dates with time components, `BETWEEN '2021-01-01' AND '2021-12-31'` may miss timestamps late on the last day — prefer `>= '2021-01-01' AND < '2022-01-01'` for `DATETIME` columns.

---

## 13. Set Membership (IN / NOT IN)

**Definition:**
`IN` checks whether a value matches any value in a given list or subquery result.

**Syntax:**
```sql
SELECT * FROM table_name WHERE column IN (value1, value2, ...);
SELECT * FROM table_name WHERE column NOT IN (value1, value2, ...);
```

**Example:**
```sql
SELECT * FROM employees WHERE dept_id IN (1, 3);

SELECT * FROM employees WHERE dept_id NOT IN (2);

-- With a subquery
SELECT * FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE dept_name = 'Engineering');
```

**Tips & Tricks:**
- `IN (...)` is cleaner than multiple `OR` conditions: `dept_id = 1 OR dept_id = 3` → `dept_id IN (1, 3)`.
- **Danger:** `NOT IN` with a subquery that can return `NULL` values will return **zero rows** unexpectedly (because `x <> NULL` is unknown). Prefer `NOT EXISTS` when the subquery might contain NULLs.
- `IN` is optimized well by MySQL when the list is small/moderate; for huge lists consider a joined temp table.

---

## 14. Sorting (ORDER BY)

**Definition:**
`ORDER BY` sorts the result set by one or more columns, ascending (`ASC`, default) or descending (`DESC`).

**Syntax:**
```sql
SELECT columns FROM table_name ORDER BY column1 [ASC|DESC], column2 [ASC|DESC];
```

**Example:**
```sql
SELECT name, salary FROM employees ORDER BY salary DESC;

SELECT name, dept_id, salary FROM employees ORDER BY dept_id ASC, salary DESC;

-- Order by column position (works, but not recommended for readability)
SELECT name, salary FROM employees ORDER BY 2 DESC;

-- Order by an expression
SELECT name, salary FROM employees ORDER BY salary * 12 DESC;
```

**Tips & Tricks:**
- `ORDER BY` runs **after** `WHERE`/`GROUP BY`/`HAVING`, so it can reference column aliases from `SELECT`.
- Multiple columns: sorting happens left to right — the first column is the primary sort key.
- `NULL`s sort first in `ASC` order in MySQL (opposite of some other databases like PostgreSQL).
- Combine with `LIMIT` for "Top-N" queries (see Topic 50).

---

## 15. Limiting Results (LIMIT, OFFSET)

**Definition:**
`LIMIT` restricts the number of rows returned. `OFFSET` skips a number of rows before starting to return results (used for pagination). MySQL uses `LIMIT`/`OFFSET` (no `TOP` — that's SQL Server syntax).

**Syntax:**
```sql
SELECT columns FROM table_name LIMIT n;
SELECT columns FROM table_name LIMIT n OFFSET m;
SELECT columns FROM table_name LIMIT m, n;   -- MySQL shorthand: skip m, take n
```

**Example:**
```sql
SELECT * FROM employees ORDER BY salary DESC LIMIT 3;          -- top 3 earners

SELECT * FROM employees ORDER BY salary DESC LIMIT 3 OFFSET 3; -- next 3 (pagination page 2)

SELECT * FROM employees ORDER BY salary DESC LIMIT 3, 3;       -- same as above
```

**Tips & Tricks:**
- Always pair `LIMIT` with `ORDER BY` — without sorting, "top N" rows are undefined/arbitrary.
- SQL Server equivalent: `SELECT TOP 3 * FROM employees ORDER BY salary DESC;`
- For large-offset pagination (e.g., `OFFSET 1000000`), performance degrades — use "keyset pagination" (`WHERE id > last_seen_id LIMIT n`) instead.

---

## 16. Aggregate Functions

**Definition:**
Aggregate functions compute a single summary value across multiple rows.

| Function | Purpose |
|---|---|
| `COUNT()` | Number of rows |
| `SUM()` | Total of numeric column |
| `AVG()` | Average |
| `MIN()` | Smallest value |
| `MAX()` | Largest value |

**Syntax:**
```sql
SELECT COUNT(*), SUM(column), AVG(column), MIN(column), MAX(column) FROM table_name;
```

**Example:**
```sql
SELECT COUNT(*) AS total_employees FROM employees;
SELECT SUM(salary) AS total_payroll FROM employees;
SELECT AVG(salary) AS avg_salary FROM employees;
SELECT MIN(salary) AS lowest_salary, MAX(salary) AS highest_salary FROM employees;

-- Combine with WHERE (filters rows BEFORE aggregation)
SELECT COUNT(*) FROM employees WHERE dept_id = 1;
```

**Tips & Tricks:**
- `COUNT(*)` counts all rows (including NULLs); `COUNT(column)` counts only non-NULL values in that column.
- Aggregate functions ignore `NULL`s (except `COUNT(*)`).
- You generally can't mix aggregate and non-aggregate columns in `SELECT` without `GROUP BY` — MySQL may allow it silently (non-standard mode) but the result is unpredictable; avoid it.

---

## 17. GROUP BY

**Definition:**
`GROUP BY` groups rows sharing the same value(s) in specified column(s) so aggregate functions can be applied **per group**.

**Syntax:**
```sql
SELECT column, AGG_FUNC(column2)
FROM table_name
GROUP BY column;
```

**Example:**
```sql
SELECT dept_id, COUNT(*) AS num_employees
FROM employees
GROUP BY dept_id;

SELECT dept_id, AVG(salary) AS avg_salary, MAX(salary) AS max_salary
FROM employees
GROUP BY dept_id;

-- Group by multiple columns
SELECT dept_id, YEAR(hire_date) AS hire_year, COUNT(*)
FROM employees
GROUP BY dept_id, YEAR(hire_date);
```

**Tips & Tricks:**
- Every non-aggregated column in `SELECT` **must** appear in `GROUP BY` (strict SQL mode in MySQL enforces this — `ONLY_FULL_GROUP_BY`).
- `GROUP BY` runs after `WHERE` but before `HAVING`/`ORDER BY`/`LIMIT`.
- Use `WITH ROLLUP` to add subtotal/grand-total rows: `GROUP BY dept_id WITH ROLLUP`.

---

## 18. HAVING

**Definition:**
`HAVING` filters **grouped/aggregated** results — the equivalent of `WHERE`, but applied after `GROUP BY`.

**Syntax:**
```sql
SELECT column, AGG_FUNC(column2)
FROM table_name
GROUP BY column
HAVING condition;
```

**Example:**
```sql
SELECT dept_id, COUNT(*) AS num_employees
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 2;

SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 70000;

-- WHERE + HAVING together
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= '2019-01-01'
GROUP BY dept_id
HAVING AVG(salary) > 60000;
```

**Tips & Tricks:**
- `WHERE` filters rows **before** grouping; `HAVING` filters groups **after** aggregation — use `WHERE` whenever possible since it's more efficient (filters earlier).
- `HAVING` can reference `SELECT` aliases in MySQL (not standard in all databases).
- You can use `HAVING` without `GROUP BY` to filter on an aggregate over the entire table, but it's rare/unusual style.

---

## 19. Joins Basics (INNER JOIN, LEFT JOIN)

**Definition:**
Joins combine rows from two or more tables based on a related column.
- **INNER JOIN** — returns rows that have matching values in both tables.
- **LEFT JOIN (LEFT OUTER JOIN)** — returns all rows from the left table, plus matched rows from the right (NULLs if no match).

**Syntax:**
```sql
SELECT columns
FROM table1
INNER JOIN table2 ON table1.col = table2.col;

SELECT columns
FROM table1
LEFT JOIN table2 ON table1.col = table2.col;
```

**Example:**
```sql
-- INNER JOIN: employees with a valid department
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN: all employees, even if dept_id is NULL/unmatched
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- Find employees with NO matching department (anti-join pattern)
SELECT e.name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;
```

**Tips & Tricks:**
- Always use table aliases (`e`, `d`) for readability, especially with multiple joins.
- `INNER JOIN` = intersection; `LEFT JOIN` = everything from left + matches.
- The `LEFT JOIN ... WHERE right.col IS NULL` pattern is the standard way to find "rows in A with no match in B".
- Put join conditions in `ON`, not `WHERE` — mixing them (especially with outer joins) can silently turn a LEFT JOIN into an INNER JOIN.

---

## 20. Joins Advanced (RIGHT JOIN, FULL JOIN, CROSS JOIN)

**Definition:**
- **RIGHT JOIN** — all rows from the right table, plus matches from the left.
- **FULL JOIN (FULL OUTER JOIN)** — all rows from both tables, matched where possible (MySQL has **no native `FULL JOIN`** — simulate with `UNION`).
- **CROSS JOIN** — Cartesian product: every row of table1 combined with every row of table2.

**Syntax:**
```sql
SELECT columns FROM table1 RIGHT JOIN table2 ON table1.col = table2.col;

-- FULL JOIN simulation in MySQL
SELECT columns FROM table1
LEFT JOIN table2 ON table1.col = table2.col
UNION
SELECT columns FROM table1
RIGHT JOIN table2 ON table1.col = table2.col;

SELECT columns FROM table1 CROSS JOIN table2;
```

**Example:**
```sql
-- RIGHT JOIN: all departments, even empty ones
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- FULL OUTER JOIN simulation
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
UNION
SELECT e.name, d.dept_name
FROM employees e
RIGHT JOIN departments d ON e.dept_id = d.dept_id;

-- CROSS JOIN: every employee paired with every department (6 employees x 3 depts = 18 rows)
SELECT e.name, d.dept_name
FROM employees e
CROSS JOIN departments d;
```

**Tips & Tricks:**
- `RIGHT JOIN` is rarely used in practice — most people rewrite it as a `LEFT JOIN` by swapping table order for consistency.
- MySQL 8+ still has no native `FULL OUTER JOIN` — the `UNION` trick is the standard workaround (use `UNION`, not `UNION ALL`, to avoid duplicating matched rows... or use `UNION ALL` with a `WHERE ... IS NULL` filter on the second query to avoid duplicates precisely).
- `CROSS JOIN` grows extremely fast (`m x n` rows) — use intentionally, e.g., for generating combinations, not by accident (forgetting the `ON` clause creates an accidental cross join).

---

## 21. Self Join

**Definition:**
A self join joins a table to itself, typically to compare rows within the same table (e.g., employee-manager relationships).

**Syntax:**
```sql
SELECT a.column, b.column
FROM table_name a
JOIN table_name b ON a.some_col = b.other_col;
```

**Example:**
```sql
-- Show each employee with their manager's name
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- Find employees earning more than their manager
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;
```

**Tips & Tricks:**
- Always alias the two instances of the table differently (`e`, `m`) — you can't reference the same table name twice without aliases.
- Common use cases: org charts/hierarchies, finding duplicates, comparing consecutive rows (before window functions existed).
- For deep hierarchies (multi-level), a recursive CTE (Topic 30) is more powerful than a self join.

---

## 22. Subqueries

**Definition:**
A subquery (inner query) is a query nested inside another query. Can return a single value (scalar), a single row, a single column (multi-row), or a full table.

**Syntax:**
```sql
-- Scalar subquery
SELECT column FROM table WHERE column = (SELECT MAX(column) FROM table);

-- Multi-row subquery
SELECT column FROM table WHERE column IN (SELECT column FROM other_table);

-- Subquery in FROM (derived table)
SELECT * FROM (SELECT ... FROM table) AS derived;
```

**Example:**
```sql
-- Single-row: employees earning the max salary
SELECT name, salary FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Multi-row: employees in departments with more than 2 people
SELECT name FROM employees
WHERE dept_id IN (
    SELECT dept_id FROM employees GROUP BY dept_id HAVING COUNT(*) > 2
);

-- Subquery in FROM clause
SELECT dept_id, avg_sal
FROM (SELECT dept_id, AVG(salary) AS avg_sal FROM employees GROUP BY dept_id) AS dept_avg
WHERE avg_sal > 60000;

-- Subquery in SELECT (scalar)
SELECT name, salary,
  (SELECT AVG(salary) FROM employees) AS company_avg
FROM employees;
```

**Tips & Tricks:**
- A subquery used with `=`, `>`, `<` must return exactly **one value** — otherwise it errors out.
- Subqueries in `FROM` (derived tables) **must** have an alias in MySQL.
- Often a subquery can be rewritten as a `JOIN` or CTE for better readability/performance — compare execution plans.
- Use `EXISTS` instead of `IN` when checking existence for large subquery results (usually faster).

---

## 23. Correlated Subqueries

**Definition:**
A correlated subquery references a column from the **outer query**, so it is re-evaluated once per row of the outer query (unlike a regular subquery, which runs once).

**Syntax:**
```sql
SELECT column FROM outer_table o
WHERE column OPERATOR (SELECT ... FROM inner_table i WHERE i.col = o.col);
```

**Example:**
```sql
-- Employees earning more than the average salary of their OWN department
SELECT e.name, e.dept_id, e.salary
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.dept_id = e.dept_id     -- correlation: references outer 'e'
);

-- EXISTS example: departments that have at least one employee earning > 90000
SELECT dept_name FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e
    WHERE e.dept_id = d.dept_id AND e.salary > 90000
);
```

**Tips & Tricks:**
- Correlated subqueries can be slow on large tables since they run once per outer row — window functions (Topic 26-29) often replace them more efficiently (e.g., `AVG(salary) OVER (PARTITION BY dept_id)`).
- `EXISTS` with a correlated subquery is usually more efficient than `IN` for existence checks, and handles `NULL`s safely.
- Use `SELECT 1` inside `EXISTS` — the selected column doesn't matter, only row existence does.

---

## 24. Set Operations

**Definition:**
Set operations combine results of two or more `SELECT` queries (must have the same number of columns, compatible types).

| Operation | Behavior |
|---|---|
| `UNION` | Combines results, removes duplicates |
| `UNION ALL` | Combines results, keeps duplicates (faster) |
| `INTERSECT` | Rows common to both queries (MySQL 8.0.31+) |
| `EXCEPT` (MySQL) / `MINUS` (Oracle) | Rows in first query not in second (MySQL 8.0.31+) |

**Syntax:**
```sql
SELECT columns FROM table1
UNION [ALL]
SELECT columns FROM table2;

SELECT columns FROM table1
INTERSECT
SELECT columns FROM table2;

SELECT columns FROM table1
EXCEPT
SELECT columns FROM table2;
```

**Example:**
```sql
-- All names from engineering (dept 1) and HR (dept 3), deduped
SELECT name FROM employees WHERE dept_id = 1
UNION
SELECT name FROM employees WHERE dept_id = 3;

-- Keep duplicates (faster, no dedup step)
SELECT dept_id FROM employees
UNION ALL
SELECT dept_id FROM departments;

-- INTERSECT (MySQL 8.0.31+)
SELECT dept_id FROM employees
INTERSECT
SELECT dept_id FROM departments;
```

**Tips & Tricks:**
- Prefer `UNION ALL` over `UNION` when you know there are no duplicates (or don't care) — `UNION` does extra work to deduplicate.
- Column names in the result come from the **first** `SELECT`.
- If your MySQL version is older than 8.0.31, simulate `INTERSECT` using `INNER JOIN` or `IN`, and `EXCEPT` using `LEFT JOIN ... WHERE right.col IS NULL` or `NOT IN`.

---

## 25. CASE Statements

**Definition:**
`CASE` provides if/else-style conditional logic inside a SQL query.

**Syntax:**
```sql
-- Simple CASE
CASE column
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE default_result
END

-- Searched CASE (more flexible - conditions instead of exact values)
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result
END
```

**Example:**
```sql
SELECT name, salary,
  CASE
      WHEN salary >= 90000 THEN 'High'
      WHEN salary >= 60000 THEN 'Medium'
      ELSE 'Low'
  END AS salary_band
FROM employees;

-- CASE inside aggregate (conditional counting - very common pattern)
SELECT
  COUNT(CASE WHEN salary > 70000 THEN 1 END) AS high_earners,
  COUNT(CASE WHEN salary <= 70000 THEN 1 END) AS low_earners
FROM employees;

-- CASE in ORDER BY
SELECT name, dept_id FROM employees
ORDER BY CASE WHEN dept_id = 1 THEN 0 ELSE 1 END, name;
```

**Tips & Tricks:**
- `CASE` returns `NULL` by default if no `WHEN` matches and there's no `ELSE` — always include `ELSE` unless NULL is intentional.
- The "conditional `COUNT`" pattern (`COUNT(CASE WHEN ... THEN 1 END)`) is extremely useful for pivot-style reporting in one query.
- `CASE` can be used almost anywhere: `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`.

---

## 26. Window Functions Basics (OVER, PARTITION BY)

**Definition:**
Window functions perform calculations across a set of rows ("window") related to the current row, **without collapsing rows** like `GROUP BY` does. Defined with `OVER()`.

**Syntax:**
```sql
FUNCTION() OVER (
    [PARTITION BY column]
    [ORDER BY column]
    [ROWS/RANGE frame_clause]
)
```

**Example:**
```sql
-- Average salary per department, shown on every row (no row collapsing)
SELECT name, dept_id, salary,
  AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg_salary
FROM employees;

-- Compare each employee's salary to department average
SELECT name, dept_id, salary,
  salary - AVG(salary) OVER (PARTITION BY dept_id) AS diff_from_avg
FROM employees;

-- Running total ordered by hire date (no PARTITION - whole table is the window)
SELECT name, hire_date, salary,
  SUM(salary) OVER (ORDER BY hire_date) AS running_total
FROM employees;
```

**Tips & Tricks:**
- Unlike `GROUP BY`, window functions keep every row — great for "show detail + aggregate side by side".
- `PARTITION BY` = like `GROUP BY` but doesn't collapse rows; `ORDER BY` inside `OVER()` controls running calculations (e.g., running totals).
- Window functions run **after** `WHERE`/`GROUP BY`/`HAVING` but **before** the final `ORDER BY`/`LIMIT` — so you can't filter directly on a window function result in `WHERE`; wrap it in a subquery/CTE and filter outside.

### Understanding the Frame Clause (ROWS vs RANGE vs GROUPS)

The "frame" is the exact subset of rows within a partition that the function actually looks at for the *current row*. This is the part of window functions most people gloss over — and it's the source of the most confusing bugs.

```sql
FUNCTION() OVER (
    PARTITION BY col
    ORDER BY col
    {ROWS | RANGE | GROUPS} BETWEEN frame_start AND frame_end
)
```

Frame boundaries you can use: `UNBOUNDED PRECEDING`, `N PRECEDING`, `CURRENT ROW`, `N FOLLOWING`, `UNBOUNDED FOLLOWING`.

- **`ROWS`** — counts physical rows. `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` = "this row + the 2 rows immediately before it", regardless of tied values.
- **`RANGE`** — counts by *value*, not row position. `RANGE BETWEEN 1 PRECEDING AND CURRENT ROW` on a numeric `ORDER BY` includes every row whose value falls within that range — so **rows with a tied `ORDER BY` value are all included together**, not just N of them.
- **`GROUPS`** — counts by distinct peer groups (ties count as one "group") rather than by individual rows.

```sql
-- ROWS: exactly 3 physical rows (current + 2 before), even if salaries tie
SELECT name, hire_date, salary,
  AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS avg_last_3_rows
FROM employees;

-- RANGE: default frame when ORDER BY is present and no frame is specified
-- = RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW (classic running total)
SELECT name, hire_date, salary,
  SUM(salary) OVER (ORDER BY hire_date) AS running_total   -- implicit RANGE frame
FROM employees;

-- Full partition, ignoring row position entirely (common for "% of total" calcs)
SELECT name, dept_id, salary,
  SUM(salary) OVER (PARTITION BY dept_id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS dept_total
FROM employees;
```

**The classic gotcha:** if you write `ORDER BY` inside `OVER()` but forget the frame clause, MySQL silently defaults to `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` — turning what you expected to be a full-partition total into a running total. This is the single most common window-function bug. If you want the whole partition's value on every row, either drop `ORDER BY` from that `OVER()`, or explicitly write `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.

---

## 27. Ranking Functions (ROW_NUMBER, RANK, DENSE_RANK)

**Definition:**
Ranking window functions assign a rank/position to rows within a partition, based on an `ORDER BY`.

| Function | Behavior on ties |
|---|---|
| `ROW_NUMBER()` | Unique sequential number, no ties (arbitrary tie-break) |
| `RANK()` | Same rank for ties, **gaps** after ties (1,2,2,4) |
| `DENSE_RANK()` | Same rank for ties, **no gaps** (1,2,2,3) |

**Syntax:**
```sql
ROW_NUMBER() OVER (PARTITION BY col ORDER BY col)
RANK()       OVER (PARTITION BY col ORDER BY col)
DENSE_RANK() OVER (PARTITION BY col ORDER BY col)
```

**Example:**
```sql
SELECT name, dept_id, salary,
  ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num,
  RANK()       OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank_num,
  DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rank_num
FROM employees;

-- Top 2 earners per department (using a CTE, since you can't filter window functions in WHERE directly)
WITH ranked AS (
  SELECT name, dept_id, salary,
    ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
  FROM employees
)
SELECT * FROM ranked WHERE rn <= 2;
```

**Tips & Tricks:**
- `ROW_NUMBER()` is the go-to for deduplication (keep only rn = 1 per group) and pagination.
- Use `RANK()` for leaderboard-style ranking where ties should share a position (like Olympic medals).
- `DENSE_RANK()` is useful when you don't want gaps after ties (e.g., "top 3 distinct salary levels").

---

## 28. Aggregate Window Functions (SUM OVER, AVG OVER)

**Definition:**
Any aggregate function (`SUM`, `AVG`, `COUNT`, `MIN`, `MAX`) can be used as a window function with `OVER()`, enabling running totals, moving averages, and group-level stats without collapsing rows.

**Syntax:**
```sql
SUM(column) OVER (PARTITION BY col ORDER BY col ROWS BETWEEN ... AND ...)
```

**Example:**
```sql
-- Running total of salary, ordered by hire date, within each department
SELECT name, dept_id, hire_date, salary,
  SUM(salary) OVER (PARTITION BY dept_id ORDER BY hire_date) AS running_total
FROM employees;

-- Moving average of last 3 rows (current + 2 preceding)
SELECT name, hire_date, salary,
  AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_3
FROM employees;

-- % of department total
SELECT name, dept_id, salary,
  ROUND(salary / SUM(salary) OVER (PARTITION BY dept_id) * 100, 2) AS pct_of_dept
FROM employees;
```

**Tips & Tricks:**
- The frame clause (`ROWS BETWEEN ... AND ...`) controls exactly which rows are included — see the full breakdown of `ROWS` vs `RANGE` vs `GROUPS` under Topic 26.
- Default frame when `ORDER BY` is present: `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` (i.e., running total behavior) — this is why adding `ORDER BY` to a `SUM() OVER()` you intended as a partition-wide total silently turns it into a running total instead.
- Without `ORDER BY` in `OVER()`, the aggregate applies to the **entire partition** (or table), not a running calculation.
- This same default-frame behavior is exactly why `LAST_VALUE()` (Topic 29) needs an explicit `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` frame to actually return the last row of the partition, rather than just the current row.

---

## 29. Analytical Functions (LAG, LEAD, FIRST_VALUE, LAST_VALUE)

**Definition:**
Analytical functions let you access values from other rows relative to the current row within a window.

| Function | Purpose |
|---|---|
| `LAG(col, n)` | Value from `n` rows **before** current row |
| `LEAD(col, n)` | Value from `n` rows **after** current row |
| `FIRST_VALUE(col)` | First value in the window/frame |
| `LAST_VALUE(col)` | Last value in the window/frame |

**Syntax:**
```sql
LAG(column, offset, default) OVER (PARTITION BY col ORDER BY col)
LEAD(column, offset, default) OVER (PARTITION BY col ORDER BY col)
FIRST_VALUE(column) OVER (PARTITION BY col ORDER BY col)
LAST_VALUE(column) OVER (PARTITION BY col ORDER BY col ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
```

**Example:**
```sql
-- Compare each employee's salary to the previous hire in their department
SELECT name, dept_id, hire_date, salary,
  LAG(salary, 1) OVER (PARTITION BY dept_id ORDER BY hire_date) AS prev_salary,
  LEAD(salary, 1) OVER (PARTITION BY dept_id ORDER BY hire_date) AS next_salary
FROM employees;

-- Month-over-month style difference
SELECT name, hire_date, salary,
  salary - LAG(salary, 1, 0) OVER (ORDER BY hire_date) AS salary_change
FROM employees;

-- Highest earner's name shown on every row of that department
SELECT name, dept_id, salary,
  FIRST_VALUE(name) OVER (PARTITION BY dept_id ORDER BY salary DESC) AS top_earner
FROM employees;
```

**Tips & Tricks:**
- `LAG`/`LEAD` take an optional 3rd argument as a default value for when there's no previous/next row (avoids `NULL`).
- `LAST_VALUE` needs an explicit frame (`ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`) — otherwise, due to the default frame, it just returns the current row's value (a very common gotcha).
- These functions eliminate the need for slow self-joins when comparing a row to its neighbor.

---

## 30. CTE (Common Table Expressions)

**Definition:**
A CTE is a named, temporary result set defined with `WITH`, usable within the following query. Improves readability over nested subqueries. A **recursive CTE** references itself to handle hierarchical/iterative data.

**Syntax:**
```sql
WITH cte_name AS (
    SELECT ...
)
SELECT * FROM cte_name;

-- Recursive
WITH RECURSIVE cte_name AS (
    SELECT ... -- anchor member
    UNION ALL
    SELECT ... FROM cte_name JOIN ... -- recursive member
)
SELECT * FROM cte_name;
```

**Example:**
```sql
-- Basic CTE
WITH dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
)
SELECT e.name, e.salary, d.avg_salary
FROM employees e
JOIN dept_avg d ON e.dept_id = d.dept_id
WHERE e.salary > d.avg_salary;

-- Multiple CTEs
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 70000
),
dept_counts AS (
    SELECT dept_id, COUNT(*) AS cnt FROM high_earners GROUP BY dept_id
)
SELECT * FROM dept_counts;

-- Recursive CTE: organization chart (employee -> manager chain)
WITH RECURSIVE org_chart AS (
    SELECT emp_id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL          -- anchor: top-level employees
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.emp_id   -- recursive step
)
SELECT * FROM org_chart ORDER BY level;
```

**Tips & Tricks:**
- CTEs make deeply nested subqueries readable — treat them like named "temporary views" for one query.
- A CTE is **not materialized/indexed** like a real table in MySQL — it's re-evaluated, so don't expect performance gains, only readability gains (unlike temp tables).
- Recursive CTEs need `WITH RECURSIVE` in MySQL and must have an anchor member + recursive member joined via `UNION ALL`.
- Always add a level/depth guard in recursive CTEs to avoid infinite loops (`WHERE level < 10`) — MySQL has `cte_max_recursion_depth` as a safety net too.

---

## 31. Views

**Definition:**
A view is a saved, named `SELECT` query that acts like a virtual table. It doesn't store data itself (usually) — it runs the underlying query each time it's referenced.

**Syntax:**
```sql
CREATE VIEW view_name AS
SELECT ...;

-- Updating a view definition
CREATE OR REPLACE VIEW view_name AS SELECT ...;

DROP VIEW view_name;
```

**Example:**
```sql
CREATE VIEW dept_summary AS
SELECT d.dept_name, COUNT(e.emp_id) AS num_employees, AVG(e.salary) AS avg_salary
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- Use it like a table
SELECT * FROM dept_summary WHERE avg_salary > 60000;

-- Update the view
CREATE OR REPLACE VIEW dept_summary AS
SELECT d.dept_name, COUNT(e.emp_id) AS num_employees
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

DROP VIEW dept_summary;
```

**Tips & Tricks:**
- Views simplify repeated complex queries and can restrict access (expose only certain columns/rows to a user via `GRANT` on the view instead of the base table).
- A view is only **updatable** (supports `INSERT`/`UPDATE`/`DELETE` through it) if it's based on a single table without `GROUP BY`, aggregates, `DISTINCT`, or joins — most reporting views (with joins/aggregates) are read-only.
- Views don't store data (unlike "materialized views" in Postgres/Oracle) — MySQL has no native materialized views; simulate with a real table + scheduled refresh (event/cron).

---

## 32. Indexing

**Definition:**
An index is a data structure (commonly a B-Tree) that speeds up data retrieval by avoiding full table scans, at the cost of extra storage and slower writes.

**Syntax:**
```sql
CREATE INDEX index_name ON table_name (column);
CREATE INDEX index_name ON table_name (column1, column2);   -- composite index
CREATE UNIQUE INDEX index_name ON table_name (column);
DROP INDEX index_name ON table_name;
SHOW INDEX FROM table_name;
```

**Example:**
```sql
CREATE INDEX idx_dept_id ON employees (dept_id);

CREATE INDEX idx_dept_salary ON employees (dept_id, salary);  -- composite

CREATE UNIQUE INDEX idx_unique_name ON employees (name);

-- Check what indexes exist
SHOW INDEX FROM employees;

-- See if a query uses an index
EXPLAIN SELECT * FROM employees WHERE dept_id = 1;

DROP INDEX idx_dept_id ON employees;
```

**Tips & Tricks:**
- Index columns used often in `WHERE`, `JOIN ON`, and `ORDER BY` — but don't over-index; every index slows down `INSERT`/`UPDATE`/`DELETE`.
- Composite index column **order matters** — an index on `(dept_id, salary)` helps queries filtering on `dept_id` alone or `dept_id + salary`, but not `salary` alone.
- Primary keys and `UNIQUE` constraints automatically create an index.
- Use `EXPLAIN` before/after adding an index to confirm it's actually being used.

---

## 33. Index Types (Clustered, Non-Clustered)

**Definition:**
- **Clustered index** — determines the **physical order** of data on disk. A table can have only **one** (in MySQL/InnoDB, the `PRIMARY KEY` is always the clustered index).
- **Non-clustered (secondary) index** — a separate structure storing pointers back to the actual row (via the primary key in InnoDB). A table can have many.

**Syntax:**
```sql
-- Clustered index = the PRIMARY KEY itself (automatic in InnoDB)
CREATE TABLE t (id INT PRIMARY KEY, ...);

-- Non-clustered / secondary index
CREATE INDEX idx_name ON t (column);
```

**Example:**
```sql
CREATE TABLE employees_demo (
    emp_id INT PRIMARY KEY,     -- this IS the clustered index in InnoDB
    name VARCHAR(50),
    dept_id INT
);

CREATE INDEX idx_dept ON employees_demo (dept_id);  -- secondary/non-clustered
-- Lookup via idx_dept finds the emp_id, then does a lookup in the clustered index ("bookmark lookup")
```

**Covering Indexes (deeper look):**

A **covering index** is a secondary index that contains *every* column a query needs — so MySQL can answer the query entirely from the index, without a "bookmark lookup" back into the clustered index (table data).

```sql
-- Query needs only dept_id and salary
SELECT dept_id, salary FROM employees WHERE dept_id = 1;

-- A plain index on (dept_id) still requires a lookup into the table for 'salary'
CREATE INDEX idx_dept ON employees (dept_id);

-- A covering index on (dept_id, salary) answers the query from the index alone
CREATE INDEX idx_dept_salary_covering ON employees (dept_id, salary);

-- Confirm with EXPLAIN: look for "Using index" in the Extra column (means it's covering)
EXPLAIN SELECT dept_id, salary FROM employees WHERE dept_id = 1;
```

**Index Cardinality & Selectivity:**

- **Cardinality** = the number of distinct values in a column (`SHOW INDEX FROM employees;` shows a `Cardinality` estimate per index).
- **Selectivity** = cardinality ÷ total rows — closer to 1 means each value is more unique, and the index is more useful for filtering.
- A column like `is_active` (BOOLEAN, only 2 distinct values) has very **low** selectivity — an index on it rarely helps, since it doesn't narrow down rows much. A column like `email` (unique per user) has very **high** selectivity — an excellent index candidate.

**Tips & Tricks:**
- In InnoDB (MySQL's default engine), if you don't define a `PRIMARY KEY`, MySQL will use the first `UNIQUE NOT NULL` column, or create a hidden internal row ID as the clustered index.
- Secondary index lookups in InnoDB always do a second lookup ("bookmark lookup") into the clustered index to fetch full row data unless it's a **covering index**.
- Choose a small, sequential/auto-incrementing primary key when possible — a large or random clustered key (like a UUID) causes page fragmentation and slower inserts.
- Don't index low-selectivity columns (like a `status` flag with only 2-3 values) on their own — put them at the end of a composite index instead, after a high-selectivity column.

---

## 34. Performance Optimization

**Definition:**
The practice of writing queries and designing schemas so the database engine does the least possible work — using indexes effectively, minimizing scanned rows, and understanding the query execution plan.

**Syntax:**
```sql
EXPLAIN SELECT ...;
EXPLAIN ANALYZE SELECT ...;    -- MySQL 8.0.18+, shows actual execution stats
```

**Example:**
```sql
EXPLAIN SELECT * FROM employees WHERE dept_id = 1;

EXPLAIN ANALYZE
SELECT e.name, d.dept_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
WHERE e.salary > 60000;
```

**Reading `EXPLAIN` Output (column by column):**

| Column | Meaning |
|---|---|
| `select_type` | Query type: `SIMPLE`, `PRIMARY`, `SUBQUERY`, `DERIVED`, `UNION`, etc. |
| `table` | Which table this row of the plan refers to |
| `type` | **Access method** — how MySQL finds rows. From best to worst: `system`/`const` (single row) → `eq_ref` → `ref` → `range` → `index` (full index scan) → `ALL` (full table scan, usually bad) |
| `possible_keys` | Indexes MySQL *could* use for this query |
| `key` | The index MySQL *actually chose* (NULL = no index used) |
| `key_len` | How many bytes of the index were used — helps confirm if a composite index is fully or partially used |
| `rows` | Estimated number of rows MySQL expects to examine — lower is better |
| `filtered` | Estimated % of rows remaining after the `WHERE` filter is applied |
| `Extra` | Extra info: `Using index` (covering index, great), `Using where` (filtering after fetch), `Using filesort` (extra sort step, can be slow), `Using temporary` (temp table needed, can be slow) |

```sql
EXPLAIN SELECT name, salary FROM employees WHERE dept_id = 1 ORDER BY salary DESC;
-- Watch for: type = ALL (no index used on dept_id) and Extra = Using filesort (expensive sort)
-- Fix: CREATE INDEX idx_dept_salary ON employees (dept_id, salary);
-- Re-run EXPLAIN: type should improve to 'ref', and filesort may disappear since the index is already sorted
```

### Reading an EXPLAIN Output, Column by Column

| Column | Meaning | What to look for |
|---|---|---|
| `id` | Step number in the query plan | Higher `id` = executed first for subqueries; same `id` = tables joined together |
| `select_type` | Type of query block (`SIMPLE`, `SUBQUERY`, `DERIVED`, `UNION`) | `DERIVED` repeatedly = a subquery re-run each time; consider a temp table |
| `table` | Which table this row of output refers to | — |
| `type` | **The most important column** — join/access method | Best → worst: `system`/`const` > `eq_ref` > `ref` > `range` > `index` > `ALL`. `ALL` = full table scan, usually bad on large tables |
| `possible_keys` | Indexes MySQL *could* use | If `NULL`, no useful index exists for this query |
| `key` | Index MySQL *actually chose* | If `NULL` despite `possible_keys` having options, the optimizer decided the index wasn't worth it (often on small tables) |
| `key_len` | Bytes of the index actually used | Shorter than expected = only part of a composite index is being used |
| `rows` | Estimated rows MySQL will examine | Lower is better; compare against the table's real row count |
| `filtered` | % of `rows` estimated to survive `WHERE` | Low % + high `rows` = a lot of wasted scanning |
| `Extra` | Extra execution details | `Using filesort` (expensive sort not using an index) and `Using temporary` (needed a temp table) are the two biggest optimization targets |

**Tips & Tricks:**
- Read `EXPLAIN` output starting with `type` — `ALL` (full table scan) is bad, `ref`/`range`/`const`/`eq_ref` are good; then check `rows` (estimated rows scanned) — lower is better.
- Use `EXPLAIN ANALYZE` (MySQL 8.0.18+) instead of plain `EXPLAIN` when you want **actual** execution timings and row counts rather than the optimizer's estimate — it really runs the query and reports real numbers.
- `Extra = Using filesort` or `Using temporary` are red flags on large tables — often fixable by adding/adjusting an index to match the `ORDER BY`/`GROUP BY`.
- Avoid functions on indexed columns in `WHERE` (e.g., `WHERE YEAR(hire_date) = 2021` can't use an index on `hire_date`; rewrite as `WHERE hire_date >= '2021-01-01' AND hire_date < '2022-01-01'`).
- Avoid `SELECT *` — fetch only needed columns; this also enables "covering indexes" (index contains all needed columns, no table lookup needed).
- Filter as early as possible (`WHERE` before `JOIN` where logically valid) and reduce data volume before sorting/grouping.
- Batch large `INSERT`/`UPDATE`/`DELETE` operations instead of one giant statement, to avoid long locks.

---

## 35. Transactions (COMMIT, ROLLBACK, SAVEPOINT)

**Definition:**
A transaction is a group of SQL statements executed as a single unit — either **all** succeed (`COMMIT`) or **none** do (`ROLLBACK`). `SAVEPOINT` allows partial rollback within a transaction.

**Syntax:**
```sql
START TRANSACTION;
-- statements
SAVEPOINT sp1;
-- more statements
ROLLBACK TO sp1;   -- undo back to savepoint
COMMIT;             -- or ROLLBACK; to undo everything
```

**Example:**
```sql
START TRANSACTION;

UPDATE employees SET salary = salary - 5000 WHERE emp_id = 1;
UPDATE employees SET salary = salary + 5000 WHERE emp_id = 2;

SAVEPOINT before_bonus;

UPDATE employees SET salary = salary + 1000 WHERE emp_id = 2;

-- Oops, undo just the bonus, keep the transfer
ROLLBACK TO before_bonus;

COMMIT;   -- finalize the salary transfer
```

**Tips & Tricks:**
- Transactions require a transactional storage engine — InnoDB (MySQL's default) supports them; `MyISAM` does not.
- `AUTOCOMMIT` is `ON` by default in MySQL — every statement commits immediately unless you explicitly `START TRANSACTION`.
- Keep transactions short — long-running transactions hold locks and can block other users, hurting concurrency.
- Always handle errors in application code to `ROLLBACK` on failure, or you risk partial/inconsistent data.

---

## 36. ACID Properties

**Definition:**
ACID describes the guarantees a reliable transactional database provides:
- **Atomicity** — a transaction is all-or-nothing.
- **Consistency** — a transaction brings the database from one valid state to another (constraints/rules always hold).
- **Isolation** — concurrent transactions don't interfere with each other (as if run sequentially).
- **Durability** — once committed, changes survive crashes/power loss.

**Syntax / Example (Isolation levels in MySQL):**
```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;  -- MySQL InnoDB default
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

SHOW VARIABLES LIKE 'transaction_isolation';
```

**Example scenario:**
```sql
-- Atomicity example: bank transfer - both updates succeed or neither does
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;   -- if either UPDATE fails, ROLLBACK keeps both accounts consistent
```

**Isolation Levels & the Phenomena They Prevent:**

Each isolation level protects against certain "read phenomena" that occur when transactions run concurrently:

| Phenomenon | Definition |
|---|---|
| **Dirty Read** | Reading uncommitted changes from another transaction (which might later be rolled back) |
| **Non-Repeatable Read** | Re-reading the same row twice in one transaction gives different values, because another transaction updated + committed it in between |
| **Phantom Read** | Re-running the same range query twice in one transaction returns a different **set of rows**, because another transaction inserted/deleted rows matching that range |

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
|---|---|---|---|
| `READ UNCOMMITTED` | ❌ Possible | ❌ Possible | ❌ Possible |
| `READ COMMITTED` | ✅ Prevented | ❌ Possible | ❌ Possible |
| `REPEATABLE READ` (MySQL default) | ✅ Prevented | ✅ Prevented | ✅ Mostly prevented (via InnoDB gap locks) |
| `SERIALIZABLE` | ✅ Prevented | ✅ Prevented | ✅ Prevented |

```sql
-- Non-repeatable read scenario (run in two separate sessions)
-- Session A:
START TRANSACTION;
SELECT salary FROM employees WHERE emp_id = 1;   -- reads 95000

-- Session B (runs in between, then commits):
UPDATE employees SET salary = 100000 WHERE emp_id = 1;
COMMIT;

-- Session A (same transaction, reads again):
SELECT salary FROM employees WHERE emp_id = 1;
-- Under READ COMMITTED: now shows 100000 (non-repeatable read)
-- Under REPEATABLE READ: still shows 95000 (protected)
```

**Tips & Tricks:**
- InnoDB's default isolation level is **REPEATABLE READ**, which (combined with MySQL's implementation) also prevents most phantom reads via gap locking — stricter than the ANSI standard requires.
- Higher isolation = more safety but less concurrency (more locking, higher deadlock risk); choose based on your consistency needs.
- `READ UNCOMMITTED` is rarely used in practice — it trades away too much correctness for a small performance gain.
- ACID is what separates a "real" transactional RDBMS from a simple file/NoSQL store for use cases like financial transactions.

---

## 37. Constraints

**Definition:**
Constraints enforce rules on data in a table to maintain accuracy and integrity.

| Constraint | Purpose |
|---|---|
| `PRIMARY KEY` | Uniquely identifies each row (implies `NOT NULL` + `UNIQUE`) |
| `FOREIGN KEY` | Enforces a link to another table's primary key |
| `UNIQUE` | Ensures all values in a column are distinct |
| `NOT NULL` | Disallows NULL values |
| `CHECK` | Enforces a condition on values (MySQL 8.0.16+) |
| `DEFAULT` | Sets a default value if none provided |

**Syntax:**
```sql
CREATE TABLE table_name (
    col1 INT PRIMARY KEY,
    col2 VARCHAR(50) NOT NULL UNIQUE,
    col3 INT CHECK (col3 > 0),
    col4 INT DEFAULT 0,
    col5 INT,
    FOREIGN KEY (col5) REFERENCES other_table(id)
);
```

**Example:**
```sql
CREATE TABLE orders (
    order_id    INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    amount      DECIMAL(10,2) CHECK (amount > 0),
    status      VARCHAR(20) DEFAULT 'pending',
    emp_id      INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Adding a constraint to an existing table
ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary > 0);
ALTER TABLE employees ADD CONSTRAINT uq_name UNIQUE (name);
```

**Tips & Tricks:**
- `ON DELETE CASCADE` auto-deletes child rows when the parent is deleted; `ON DELETE SET NULL` nulls the foreign key instead — pick deliberately based on business rules.
- A table can have only **one** `PRIMARY KEY` but multiple `UNIQUE` constraints.
- `CHECK` constraints were silently ignored in MySQL before 8.0.16 — verify your version if constraints seem "not working".
- Name your constraints explicitly (`CONSTRAINT chk_salary CHECK(...)`) so error messages and later `ALTER`/`DROP` are easier.

---

## 38. Normalization

**Definition:**
Normalization is the process of organizing tables to reduce data redundancy and improve integrity, by progressively applying "normal forms."

- **1NF (First Normal Form):** Each column holds atomic (indivisible) values; no repeating groups/arrays in a single cell.
- **2NF (Second Normal Form):** Must be in 1NF + every non-key column depends on the **whole** primary key (relevant when using composite keys — removes partial dependency).
- **3NF (Third Normal Form):** Must be in 2NF + no non-key column depends on another non-key column (removes transitive dependency).

**Example (progression):**
```sql
-- ❌ Not 1NF: multiple phone numbers in one cell
-- customer_id | name  | phones
-- 1           | Alice | '9990001111, 8880002222'

-- ✅ 1NF: atomic values, separate rows
-- customer_id | name  | phone
-- 1           | Alice | 9990001111
-- 1           | Alice | 8880002222

-- ❌ Not 2NF (composite key: order_id + product_id; product_name depends only on product_id, not the whole key)
-- order_id | product_id | product_name | quantity

-- ✅ 2NF: split into two tables
CREATE TABLE products (product_id INT PRIMARY KEY, product_name VARCHAR(50));
CREATE TABLE order_items (order_id INT, product_id INT, quantity INT,
    PRIMARY KEY (order_id, product_id));

-- ❌ Not 3NF: dept_name depends on dept_id, not directly on emp_id (transitive dependency)
-- emp_id | name | dept_id | dept_name

-- ✅ 3NF: split dept_name into its own table
CREATE TABLE departments (dept_id INT PRIMARY KEY, dept_name VARCHAR(50));
CREATE TABLE employees_norm (emp_id INT PRIMARY KEY, name VARCHAR(50), dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id));
```

**Tips & Tricks:**
- Rule of thumb for 3NF: "Every non-key column depends on the key, the whole key, and nothing but the key."
- Normalization reduces redundancy/update anomalies but can require more joins to reconstruct data — balance with query performance needs.
- Most OLTP (transactional) systems target 3NF; reporting/analytics systems often deliberately denormalize (Topic 39).

---

## 39. Denormalization

**Definition:**
Denormalization deliberately introduces redundancy (e.g., duplicating or precomputing data) to improve read performance, at the cost of extra storage and more complex writes/updates.

**Syntax / Example:**
```sql
-- Normalized: dept_name requires a JOIN every time
SELECT e.name, d.dept_name
FROM employees e JOIN departments d ON e.dept_id = d.dept_id;

-- Denormalized: dept_name stored directly on employees (redundant, but avoids the JOIN)
ALTER TABLE employees ADD COLUMN dept_name VARCHAR(50);
UPDATE employees e
JOIN departments d ON e.dept_id = d.dept_id
SET e.dept_name = d.dept_name;

-- Precomputed aggregate table for fast dashboard reads
CREATE TABLE dept_stats (
    dept_id INT PRIMARY KEY,
    employee_count INT,
    total_salary DECIMAL(12,2),
    last_updated DATETIME
);
```

**The trade-off, made concrete:**
```sql
-- Normalized version: ALWAYS correct, but pays a JOIN cost on every read
SELECT e.name, d.dept_name FROM employees e JOIN departments d ON e.dept_id = d.dept_id;

-- Denormalized version: fast read, ZERO join cost...
SELECT name, dept_name FROM employees;

-- ...but now this is a trap: renaming a department requires updating EVERY employee row,
-- and if you forget this step, employees.dept_name silently goes stale/wrong:
UPDATE departments SET dept_name = 'Software Engineering' WHERE dept_id = 1;
UPDATE employees SET dept_name = 'Software Engineering' WHERE dept_id = 1;  -- easy to forget!
```
A trigger (Topic 47) is the usual safeguard to keep the denormalized copy in sync automatically instead of relying on developers to remember the second `UPDATE` every time.

**Tips & Tricks:**
- Common denormalization patterns: storing computed totals, duplicating a lookup value to avoid a join, or maintaining summary/reporting tables refreshed on a schedule.
- Trade-off: faster reads, but you now must keep duplicated data in sync (via triggers, application logic, or batch jobs) — risk of inconsistency if you forget, as shown above.
- Good fit for read-heavy analytics/reporting systems (data warehouses); risky for write-heavy transactional systems where consistency matters most.

---

## 40. String Functions

**Definition:**
Built-in functions to manipulate text data.

| Function | Purpose |
|---|---|
| `CONCAT(a, b, ...)` | Joins strings together |
| `SUBSTRING(str, start, len)` | Extracts part of a string |
| `LENGTH(str)` | Number of bytes (use `CHAR_LENGTH` for characters) |
| `TRIM(str)` | Removes leading/trailing spaces |
| `UPPER()` / `LOWER()` | Case conversion |
| `REPLACE(str, from, to)` | Replaces substring occurrences |

**Syntax & Example:**
```sql
SELECT CONCAT(name, ' - ', dept_id) AS label FROM employees;

SELECT SUBSTRING(name, 1, 3) AS short_name FROM employees;   -- first 3 chars

SELECT LENGTH(name) AS byte_len, CHAR_LENGTH(name) AS char_len FROM employees;

SELECT TRIM('  hello  ') AS trimmed;               -- 'hello'

SELECT UPPER(name) AS upper_name, LOWER(name) AS lower_name FROM employees;

SELECT REPLACE(name, 'a', '@') AS masked FROM employees;

-- Combine multiple with CONCAT_WS (with separator)
SELECT CONCAT_WS(', ', name, dept_id, salary) AS summary FROM employees;
```

**Tips & Tricks:**
- `CONCAT()` returns `NULL` if **any** argument is `NULL` — use `CONCAT_WS` (ignores NULLs) or wrap with `COALESCE` if that's a problem.
- `SUBSTRING` indexes start at **1**, not 0.
- Use `TRIM(BOTH/LEADING/TRAILING 'x' FROM str)` to trim specific characters, not just spaces.
- `LENGTH()` counts bytes (matters for multi-byte UTF-8 characters); `CHAR_LENGTH()` counts characters — use `CHAR_LENGTH` for accurate string length with emoji/non-ASCII text.

---

## 41. Date Functions

**Definition:**
Built-in functions to work with `DATE`/`DATETIME`/`TIMESTAMP` values.

| Function | Purpose |
|---|---|
| `NOW()` | Current date + time |
| `CURDATE()` | Current date |
| `DATE(expr)` | Extracts date part from a datetime |
| `EXTRACT(unit FROM date)` | Extracts a specific part (year, month, day...) |
| `DATEDIFF(d1, d2)` | Difference in days |
| `DATE_ADD` / `DATE_SUB` | Add/subtract intervals |

**Syntax & Example:**
```sql
SELECT NOW() AS current_datetime, CURDATE() AS today;

SELECT hire_date, YEAR(hire_date) AS yr, MONTH(hire_date) AS mo, DAY(hire_date) AS dy
FROM employees;

SELECT EXTRACT(YEAR FROM hire_date) AS hire_year FROM employees;

-- Days since hire
SELECT name, DATEDIFF(CURDATE(), hire_date) AS days_employed FROM employees;

-- Add/subtract intervals
SELECT DATE_ADD(hire_date, INTERVAL 1 YEAR) AS anniversary_date FROM employees;
SELECT DATE_SUB(CURDATE(), INTERVAL 30 DAY) AS thirty_days_ago;

-- Format for display
SELECT DATE_FORMAT(hire_date, '%d-%m-%Y') AS formatted_date FROM employees;

-- Employees hired in the last 2 years
SELECT * FROM employees WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 2 YEAR);
```

**Tips & Tricks:**
- Never apply a function to a date column in `WHERE` if you want to use an index (`YEAR(hire_date) = 2021` blocks index use) — use range comparisons instead (`hire_date >= '2021-01-01' AND hire_date < '2022-01-01'`).
- `DATEDIFF()` in MySQL returns whole **days** only, and takes `(later_date, earlier_date)` order.
- `DATE_FORMAT()` is MySQL-specific for display formatting — format codes differ from other databases (e.g., PostgreSQL's `TO_CHAR`).
- Store timestamps in `TIMESTAMP`/`DATETIME` in UTC when dealing with multiple time zones, and convert at the application layer.

---

## 42. Numeric Functions

**Definition:**
Built-in functions for numeric calculations and formatting.

| Function | Purpose |
|---|---|
| `ROUND(n, d)` | Rounds to `d` decimal places |
| `CEIL(n)` / `CEILING(n)` | Rounds up |
| `FLOOR(n)` | Rounds down |
| `ABS(n)` | Absolute value |
| `MOD(a, b)` / `a % b` | Remainder |
| `POWER(a, b)` | Exponentiation |

**Syntax & Example:**
```sql
SELECT ROUND(72345.6789, 2) AS rounded;     -- 72345.68
SELECT ROUND(72345.6789, -3) AS rounded_neg;-- 72000 (rounds to nearest thousand)

SELECT CEIL(4.1) AS ceil_val;    -- 5
SELECT FLOOR(4.9) AS floor_val;  -- 4

SELECT ABS(-25) AS abs_val;      -- 25

SELECT MOD(10, 3) AS remainder;  -- 1
SELECT 10 % 3 AS remainder2;     -- 1

SELECT POWER(2, 10) AS power_val; -- 1024

-- Applied to real data
SELECT name, salary, ROUND(salary * 0.10, 2) AS bonus FROM employees;
```

**Tips & Tricks:**
- `ROUND(n, -d)` (negative decimal places) rounds to the nearest 10/100/1000 — handy for "round to nearest thousand" reporting.
- `FLOOR()`/`CEIL()` behave differently from `ROUND()` on negative numbers — test edge cases if working with negative values.
- Use `DECIMAL` types for money to avoid floating-point rounding surprises in the first place, rather than relying on `ROUND()` to fix it after the fact.

---

## 43. Conditional Queries (CASE WHEN usage)

**Definition:**
Deeper, practical usage patterns of `CASE WHEN` beyond simple labeling — pivoting data, conditional aggregation, and dynamic sorting. (Builds on Topic 25.)

**Syntax & Example:**
```sql
-- Pivot-style report: employee counts per salary band per department
SELECT dept_id,
  COUNT(CASE WHEN salary < 60000 THEN 1 END) AS low_band,
  COUNT(CASE WHEN salary BETWEEN 60000 AND 90000 THEN 1 END) AS mid_band,
  COUNT(CASE WHEN salary > 90000 THEN 1 END) AS high_band
FROM employees
GROUP BY dept_id;

-- Conditional update
UPDATE employees
SET salary = CASE
    WHEN dept_id = 1 THEN salary * 1.10
    WHEN dept_id = 2 THEN salary * 1.05
    ELSE salary
END;

-- Nested CASE
SELECT name, salary,
  CASE
    WHEN salary > 80000 THEN
      CASE WHEN dept_id = 1 THEN 'Senior Engineer' ELSE 'Senior Staff' END
    ELSE 'Staff'
  END AS role_label
FROM employees;
```

**Tips & Tricks:**
- This "conditional `COUNT`/`SUM`" pattern is how you build pivot tables/cross-tab reports in plain SQL without a dedicated `PIVOT` operator (MySQL has no native `PIVOT`).
- `CASE` can be used inside `UPDATE ... SET` for conditional bulk updates in a single statement instead of multiple `UPDATE` statements.
- Keep nested `CASE` shallow (1-2 levels) — beyond that, consider a lookup table or application-side logic for readability.

---

## 44. Data Integrity (Referential Integrity)

**Definition:**
Referential integrity ensures relationships between tables stay valid — e.g., a foreign key value must always exist in the referenced table's primary key (or be `NULL`, if allowed).

**Syntax:**
```sql
FOREIGN KEY (col) REFERENCES parent_table(parent_col)
    ON DELETE [CASCADE | SET NULL | RESTRICT | NO ACTION]
    ON UPDATE [CASCADE | SET NULL | RESTRICT | NO ACTION];
```

**Example:**
```sql
CREATE TABLE employees_fk (
    emp_id INT PRIMARY KEY,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE RESTRICT   -- prevents deleting a department that still has employees
        ON UPDATE CASCADE    -- if dept_id changes in departments, update it here too
);

-- This will FAIL if department 1 still has employees (RESTRICT):
DELETE FROM departments WHERE dept_id = 1;

-- This succeeds and cascades:
-- (with ON DELETE CASCADE instead, deleting the department would delete its employees too)
```

**Tips & Tricks:**
- `RESTRICT` (default-like behavior) blocks the operation if related rows exist — safest default for critical relationships.
- `CASCADE` propagates the change automatically — powerful but dangerous; a single `DELETE` can ripple through many tables.
- Always check `FOREIGN KEY` constraints are actually enabled: MySQL lets you `SET FOREIGN_KEY_CHECKS = 0` temporarily (e.g., during bulk imports) — remember to turn it back `= 1`.
- Referential integrity is your safety net against orphaned rows (e.g., an employee pointing to a deleted department).

---

## 45. Temporary Tables

**Definition:**
Temporary tables exist only for the duration of a session/connection and are automatically dropped when it ends. A **derived table** is an inline subquery in `FROM` (temporary, exists only for that one query).

**Syntax:**
```sql
CREATE TEMPORARY TABLE temp_table_name AS
SELECT ...;

-- Derived table (inline, no CREATE needed)
SELECT * FROM (SELECT ... FROM table) AS derived_alias;
```

**Example:**
```sql
CREATE TEMPORARY TABLE high_earners AS
SELECT * FROM employees WHERE salary > 70000;

SELECT * FROM high_earners;   -- usable like a normal table, this session only

DROP TEMPORARY TABLE high_earners;   -- optional; auto-dropped when session ends

-- Derived table example
SELECT dept_id, avg_sal
FROM (
    SELECT dept_id, AVG(salary) AS avg_sal FROM employees GROUP BY dept_id
) AS dept_averages
WHERE avg_sal > 65000;
```

**Tips & Tricks:**
- Temporary tables are **session-scoped** — invisible to other connections, and dropped automatically on disconnect.
- Use them to break a complex multi-step query into stages, or to cache an expensive intermediate result reused multiple times in a script.
- Unlike CTEs, a `CREATE TEMPORARY TABLE` is materialized (actually stored), so it can be indexed for performance — useful when the same intermediate result is queried repeatedly.
- Name collisions: a temporary table can have the same name as a real table — it takes precedence for that session (can be confusing; name temp tables distinctly, e.g., `tmp_high_earners`).

---

## 46. Stored Procedures

**Definition:**
A stored procedure is a saved, precompiled block of SQL (with optional parameters/logic) that can be called by name — reusable, and reduces round trips between application and database.

**Syntax:**
```sql
DELIMITER //
CREATE PROCEDURE procedure_name (IN param1 datatype, OUT param2 datatype)
BEGIN
    -- SQL statements
END //
DELIMITER ;

CALL procedure_name(args);
```

**Example:**
```sql
DELIMITER //
CREATE PROCEDURE GetEmployeesByDept(IN p_dept_id INT)
BEGIN
    SELECT * FROM employees WHERE dept_id = p_dept_id;
END //
DELIMITER ;

CALL GetEmployeesByDept(1);

-- Procedure with logic + OUT parameter
DELIMITER //
CREATE PROCEDURE GiveRaise(IN p_emp_id INT, IN p_pct DECIMAL(5,2), OUT p_new_salary DECIMAL(10,2))
BEGIN
    UPDATE employees SET salary = salary * (1 + p_pct/100) WHERE emp_id = p_emp_id;
    SELECT salary INTO p_new_salary FROM employees WHERE emp_id = p_emp_id;
END //
DELIMITER ;

CALL GiveRaise(1, 10, @new_sal);
SELECT @new_sal;

DROP PROCEDURE GetEmployeesByDept;
```

**Tips & Tricks:**
- `DELIMITER //` is needed because the procedure body itself contains semicolons — temporarily change the statement delimiter so MySQL doesn't stop parsing early.
- Parameters: `IN` (input, default), `OUT` (returns a value to caller), `INOUT` (both).
- Stored procedures centralize business logic in the database — great for consistency across multiple apps, but can make logic harder to version-control/test compared to application code. Use judiciously.
- Use `SHOW PROCEDURE STATUS WHERE Db = 'company';` to list procedures, and `SHOW CREATE PROCEDURE proc_name;` to view its definition.

---

## 47. Triggers

**Definition:**
A trigger is a block of SQL that automatically runs (fires) in response to an `INSERT`, `UPDATE`, or `DELETE` event on a table — either `BEFORE` or `AFTER` the event.

**Syntax:**
```sql
DELIMITER //
CREATE TRIGGER trigger_name
{BEFORE | AFTER} {INSERT | UPDATE | DELETE} ON table_name
FOR EACH ROW
BEGIN
    -- statements, can use NEW.col / OLD.col
END //
DELIMITER ;
```

**Example:**
```sql
-- Audit log table
CREATE TABLE salary_audit (
    audit_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    changed_at DATETIME
);

DELIMITER //
CREATE TRIGGER trg_salary_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO salary_audit (emp_id, old_salary, new_salary, changed_at)
        VALUES (OLD.emp_id, OLD.salary, NEW.salary, NOW());
    END IF;
END //
DELIMITER ;

-- This UPDATE will automatically log the change
UPDATE employees SET salary = 100000 WHERE emp_id = 1;
SELECT * FROM salary_audit;

DROP TRIGGER trg_salary_update;
```

**Tips & Tricks:**
- `NEW.column` = the value **after** the change (available in `INSERT`/`UPDATE`); `OLD.column` = the value **before** the change (available in `UPDATE`/`DELETE`).
- `BEFORE` triggers can modify `NEW` values before they're saved (e.g., validation, auto-formatting); `AFTER` triggers are typically for logging/cascading actions.
- Triggers are invisible in application code — great for auditing/enforcing rules, but can surprise developers who don't know they exist. Document them well.
- A table can have multiple triggers for the same event, but avoid chains of triggers calling triggers — hard to debug and can cause infinite loops.

---

## 48. Security (GRANT, REVOKE)

**Definition:**
`GRANT` and `REVOKE` manage database user permissions (DCL) — controlling who can do what on which objects.

**Syntax:**
```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';

GRANT privilege [, privilege...] ON database.table TO 'username'@'host';
REVOKE privilege [, privilege...] ON database.table FROM 'username'@'host';

FLUSH PRIVILEGES;
SHOW GRANTS FOR 'username'@'host';
```

**Example:**
```sql
CREATE USER 'analyst'@'localhost' IDENTIFIED BY 'Str0ngP@ss';

-- Read-only access to the whole database
GRANT SELECT ON company.* TO 'analyst'@'localhost';

-- Specific privileges on one table
GRANT SELECT, INSERT, UPDATE ON company.employees TO 'app_user'@'localhost';

-- All privileges (use with caution)
GRANT ALL PRIVILEGES ON company.* TO 'admin_user'@'localhost';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'analyst'@'localhost';

REVOKE INSERT, UPDATE ON company.employees FROM 'app_user'@'localhost';

DROP USER 'analyst'@'localhost';
```

**Tips & Tricks:**
- Follow the **principle of least privilege** — grant only what a user/application truly needs (e.g., a reporting tool needs `SELECT` only, never `DELETE`/`DROP`).
- Always run `FLUSH PRIVILEGES;` after directly editing grant tables (not usually needed after `GRANT`/`REVOKE` statements themselves, but good habit when troubleshooting).
- Use separate accounts per application/purpose rather than sharing `root` credentials — makes auditing and revocation much easier.
- `'user'@'host'` — the host part matters: `'user'@'localhost'` differs from `'user'@'%'` (any host) — restrict host access when possible.

---

## 49. Backup & Recovery

**Definition:**
Strategies and tools to protect against data loss — creating copies of the database that can be restored after failure, corruption, or accidental deletion.

**Syntax (command-line tools, not pure SQL):**
```bash
# Full logical backup (schema + data) using mysqldump
mysqldump -u username -p company > company_backup.sql

# Backup a single table
mysqldump -u username -p company employees > employees_backup.sql

# Restore from a backup
mysql -u username -p company < company_backup.sql
```

```sql
-- SQL-level partial "backup" - snapshot a table
CREATE TABLE employees_backup_20260711 AS SELECT * FROM employees;
```

**Example workflow:**
```bash
# 1. Full backup before a risky migration
mysqldump -u root -p --databases company > company_full_backup_2026_07_11.sql

# 2. Restore into a fresh database if something goes wrong
mysql -u root -p -e "CREATE DATABASE company_restored;"
mysql -u root -p company_restored < company_full_backup_2026_07_11.sql
```

**Tips & Tricks:**
- Two main backup types: **logical** (`mysqldump` — portable SQL script, slower restore) and **physical** (raw data files / `Percona XtraBackup` — faster restore, larger, less portable across versions).
- Follow the **3-2-1 rule**: at least 3 copies of data, on 2 different media types, with 1 copy offsite.
- Enable **binary logging** (`log_bin`) for point-in-time recovery — lets you replay changes since the last full backup, not just restore to the last backup's moment.
- Always **test your restore process** periodically — a backup you've never restored is not a verified backup.
- For big production databases, schedule backups during low-traffic windows, and consider `--single-transaction` with `mysqldump` on InnoDB to get a consistent snapshot without locking tables.

---

## 50. Real-world Problem Solving

**Definition:**
Common interview/production query patterns that combine everything above: Top-N per group, duplicate detection, ranking, and running totals.

### a) Top-N per group
```sql
-- Top 2 highest-paid employees per department
WITH ranked AS (
    SELECT name, dept_id, salary,
      DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT * FROM ranked WHERE rnk <= 2;
```

### b) Finding duplicates
```sql
-- Find duplicate names
SELECT name, COUNT(*) AS occurrences
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;

-- Delete duplicates, keeping the lowest emp_id (using ROW_NUMBER)
WITH dupes AS (
    SELECT emp_id,
      ROW_NUMBER() OVER (PARTITION BY name ORDER BY emp_id) AS rn
    FROM employees
)
DELETE FROM employees
WHERE emp_id IN (SELECT emp_id FROM dupes WHERE rn > 1);
```

### c) Nth highest value
```sql
-- 2nd highest salary overall
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Same, using DENSE_RANK (handles ties correctly)
WITH ranked AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT DISTINCT salary FROM ranked WHERE rnk = 2;
```

### d) Running totals & moving averages
```sql
SELECT name, hire_date, salary,
  SUM(salary) OVER (ORDER BY hire_date) AS running_total,
  AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_avg_3
FROM employees;
```

### e) Percentage of total
```sql
SELECT dept_id, salary,
  ROUND(salary * 100.0 / SUM(salary) OVER (), 2) AS pct_of_company_payroll
FROM employees;
```

### f) Gaps and islands (consecutive hire streaks by year)
```sql
WITH yearly AS (
  SELECT DISTINCT YEAR(hire_date) AS yr FROM employees
),
grouped AS (
  SELECT yr, yr - ROW_NUMBER() OVER (ORDER BY yr) AS grp
  FROM yearly
)
SELECT MIN(yr) AS streak_start, MAX(yr) AS streak_end
FROM grouped
GROUP BY grp;
```

### g) Pivot-style report (rows to columns)
```sql
SELECT
  dept_id,
  SUM(CASE WHEN YEAR(hire_date) = 2020 THEN 1 ELSE 0 END) AS hired_2020,
  SUM(CASE WHEN YEAR(hire_date) = 2021 THEN 1 ELSE 0 END) AS hired_2021,
  SUM(CASE WHEN YEAR(hire_date) = 2022 THEN 1 ELSE 0 END) AS hired_2022
FROM employees
GROUP BY dept_id;
```

### h) Employees earning above their department average
```sql
SELECT name, dept_id, salary
FROM (
    SELECT name, dept_id, salary,
      AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg
    FROM employees
) t
WHERE salary > dept_avg;
```

**Tips & Tricks:**
- `ROW_NUMBER()` for exact-N results, `RANK()`/`DENSE_RANK()` when ties should be included/handled specially.
- The `value - ROW_NUMBER()` trick (in "gaps and islands") is a classic pattern: consecutive numbers minus their row number produce the same constant, letting you `GROUP BY` that constant to find streaks.
- For "delete duplicates," always `SELECT` first with the same logic to verify exactly which rows will be removed before running `DELETE`.
- Practice these patterns on sites like LeetCode (Database section), HackerRank (SQL track), and StrataScratch — they cover almost all interview SQL questions using these exact building blocks.

---

## 🎁 Bonus / Advanced Topics

These weren't in the original list but round out a "complete SQL" skillset.

### B1. GROUP_CONCAT()

**Definition:** Aggregates values from multiple rows into a single delimited string — MySQL's way of doing "string aggregation."

```sql
SELECT dept_id, GROUP_CONCAT(name) AS employee_names
FROM employees
GROUP BY dept_id;

-- With separator and ordering
SELECT dept_id, GROUP_CONCAT(name ORDER BY salary DESC SEPARATOR ' | ') AS names_by_salary
FROM employees
GROUP BY dept_id;

-- Deduplicated
SELECT GROUP_CONCAT(DISTINCT dept_id) AS all_depts FROM employees;
```
**Tips:** Default max length is 1024 chars — increase with `SET SESSION group_concat_max_len = 10000;` if truncation occurs.

---

### B2. JSON Functions

**Definition:** MySQL (5.7+) has a native `JSON` column type and functions to query/modify JSON data directly in SQL.

```sql
CREATE TABLE employee_meta (
    emp_id INT PRIMARY KEY,
    details JSON
);

INSERT INTO employee_meta VALUES
(1, '{"skills": ["SQL", "Python"], "remote": true}');

-- Extract a value
SELECT emp_id, JSON_EXTRACT(details, '$.remote') AS is_remote FROM employee_meta;

-- Shorthand operators
SELECT emp_id, details->>'$.remote' AS is_remote FROM employee_meta;  -- unquoted result

-- Filter on JSON content
SELECT * FROM employee_meta WHERE JSON_CONTAINS(details, '"Python"', '$.skills');

-- Update a JSON field
UPDATE employee_meta SET details = JSON_SET(details, '$.remote', false) WHERE emp_id = 1;
```
**Tips:** Great for flexible/semi-structured attributes, but don't use JSON columns to avoid designing a proper relational schema — index frequently-queried JSON keys with a generated column (`... GENERATED ALWAYS AS (details->>'$.remote') STORED, INDEX(...)`) if you filter on them often.

---

### B3. Bulk Import / Export (LOAD DATA INFILE)

**Definition:** The fastest way to bulk-load data from a file (e.g., CSV) into a table, or export a query result to a file.

```sql
LOAD DATA INFILE '/path/to/employees.csv'
INTO TABLE employees
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;   -- skip header row

SELECT * FROM employees
INTO OUTFILE '/path/to/export.csv'
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n';
```
**Tips:** Much faster than looping `INSERT` statements from an application. Requires `FILE` privilege and the file to be in a directory MySQL is allowed to access (`secure_file_priv` setting controls this).

---

### B4. User-Defined Functions (UDFs)

**Definition:** Unlike a stored procedure, a function returns a **single value** and can be used directly inside a `SELECT`/`WHERE` expression.

```sql
DELIMITER //
CREATE FUNCTION AnnualSalary(monthly DECIMAL(10,2))
RETURNS DECIMAL(12,2)
DETERMINISTIC
BEGIN
    RETURN monthly * 12;
END //
DELIMITER ;

SELECT name, salary, AnnualSalary(salary) AS annual FROM employees;
```
**Tips:** Mark functions `DETERMINISTIC` when the same input always gives the same output — required for replication/binary logging safety, and helps the optimizer.

---

### B5. Cursors & Error Handling in Stored Procedures

**Definition:** A cursor lets a stored procedure loop through a result set row-by-row (rare in SQL, but sometimes necessary). `DECLARE ... HANDLER` catches errors/conditions like "no more rows."

```sql
DELIMITER //
CREATE PROCEDURE ListEmployeeNames()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE emp_name VARCHAR(50);
    DECLARE emp_cursor CURSOR FOR SELECT name FROM employees;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN emp_cursor;
    read_loop: LOOP
        FETCH emp_cursor INTO emp_name;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SELECT emp_name;   -- or do something with each row
    END LOOP;
    CLOSE emp_cursor;
END //
DELIMITER ;
```
**Tips:** Cursors are row-by-row (slow) — prefer set-based SQL (`JOIN`, aggregate queries) whenever possible; reach for cursors only when logic genuinely can't be expressed as a single query.

---

### B6. Table Partitioning

**Definition:** Splits one large logical table into multiple physical pieces (partitions) based on a rule, so queries that hit only some partitions run faster ("partition pruning").

```sql
CREATE TABLE sales (
    sale_id INT,
    sale_date DATE,
    amount DECIMAL(10,2)
)
PARTITION BY RANGE (YEAR(sale_date)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026),
    PARTITION pmax  VALUES LESS THAN MAXVALUE
);

-- A query filtering by year only scans the relevant partition
EXPLAIN SELECT * FROM sales WHERE sale_date >= '2024-01-01' AND sale_date < '2025-01-01';
```
**Tips:** Useful for very large tables (100M+ rows) with a natural range key (dates are the most common). Doesn't replace indexing — it complements it. Adds complexity to schema changes and backups, so only adopt it when table size genuinely demands it.

---

### B7. Character Sets & Collations

**Definition:** The **character set** defines what characters can be stored (e.g., `utf8mb4` supports full Unicode including emoji); the **collation** defines how strings are compared/sorted (case sensitivity, accent sensitivity).

```sql
CREATE TABLE messages (
    id INT PRIMARY KEY,
    content VARCHAR(255)
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;   -- ci = case-insensitive

SHOW VARIABLES LIKE 'character_set_database';
SHOW COLLATION LIKE 'utf8mb4%';

-- Case-sensitive comparison override
SELECT * FROM employees WHERE name COLLATE utf8mb4_bin = 'alice';  -- won't match 'Alice'
```
**Tips:** Always use `utf8mb4` (not the older, incomplete `utf8` alias in MySQL) for new tables — it fully supports modern Unicode/emoji. A collation ending in `_ci` = case-insensitive comparisons (`'Alice' = 'alice'` → true); `_cs`/`_bin` = case-sensitive. Mismatched collations between joined columns can cause silent performance issues or comparison errors.

---

### B8. AUTO_INCREMENT / Sequences

**Definition:** `AUTO_INCREMENT` automatically generates a unique, incrementing number for a column (usually the primary key) every time a row is inserted without specifying that column.

```sql
CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY AUTO_INCREMENT,
    subject VARCHAR(100)
);

INSERT INTO tickets (subject) VALUES ('Login issue');    -- ticket_id auto-assigned as 1
INSERT INTO tickets (subject) VALUES ('Payment failed'); -- ticket_id auto-assigned as 2

-- Check/set the next auto-increment value
SHOW TABLE STATUS LIKE 'tickets';
ALTER TABLE tickets AUTO_INCREMENT = 1000;  -- next insert starts at 1000

-- Get the ID just generated by the current session
SELECT LAST_INSERT_ID();
```
**Tips:** `AUTO_INCREMENT` values are **not reused** after a `DELETE` (gaps are normal and expected — don't try to "fill" them). Values can also jump on `ROLLBACK`ed transactions or replication — never assume `AUTO_INCREMENT` IDs are perfectly sequential with no gaps. Unlike Oracle/PostgreSQL `SEQUENCE` objects (which exist independently of a table and can be shared across tables), MySQL's `AUTO_INCREMENT` is tied to a single column/table.

---

### B9. Locking & Deadlocks

**Definition:** Locks prevent concurrent transactions from corrupting each other's changes. A **deadlock** happens when two transactions each hold a lock the other needs, so neither can proceed — the database detects this and kills (rolls back) one transaction automatically.

```sql
-- Row-level exclusive lock: others can't modify or lock these rows until commit
START TRANSACTION;
SELECT * FROM employees WHERE emp_id = 1 FOR UPDATE;
UPDATE employees SET salary = salary + 1000 WHERE emp_id = 1;
COMMIT;

-- Shared lock: others can read, but not modify, until this transaction ends
START TRANSACTION;
SELECT * FROM employees WHERE emp_id = 1 LOCK IN SHARE MODE;  -- or FOR SHARE (MySQL 8+)
COMMIT;

-- Inspect current locks/transactions (MySQL 8+)
SELECT * FROM performance_schema.data_locks;
SHOW ENGINE INNODB STATUS;   -- shows the most recent deadlock's details
```

**How a deadlock happens (two transactions, opposite lock order):**
```sql
-- Transaction A                                 -- Transaction B
START TRANSACTION;                               START TRANSACTION;
UPDATE employees SET salary=1 WHERE emp_id=1;    UPDATE employees SET salary=1 WHERE emp_id=2;
UPDATE employees SET salary=1 WHERE emp_id=2;    UPDATE employees SET salary=1 WHERE emp_id=1;
-- A now waits for B's lock on emp_id=2          -- B now waits for A's lock on emp_id=1 -> DEADLOCK
```
**Tips:** Always access/update rows in a **consistent order** across all transactions to avoid the classic deadlock pattern above. Keep transactions short to hold locks for as little time as possible. Handle deadlock errors (MySQL error 1213) in application code by retrying the transaction — deadlocks are a normal, expected occurrence in concurrent systems, not a bug to "fix" once and for all.

---

### B10. Full-Text Search

**Definition:** A `FULLTEXT` index enables fast natural-language and boolean text search across large text columns — far more efficient than `LIKE '%word%'` for searching within long text.

```sql
CREATE TABLE articles (
    article_id INT PRIMARY KEY,
    title VARCHAR(200),
    body TEXT,
    FULLTEXT (title, body)
);

INSERT INTO articles VALUES
(1, 'SQL Joins Explained', 'Learn how INNER JOIN and LEFT JOIN work in relational databases.'),
(2, 'Indexing Basics', 'Indexes speed up SELECT queries significantly.');

-- Natural language search (ranked by relevance)
SELECT *, MATCH(title, body) AGAINST('joins relational') AS relevance
FROM articles
WHERE MATCH(title, body) AGAINST('joins relational');

-- Boolean mode: +required -excluded "exact phrase"
SELECT * FROM articles
WHERE MATCH(title, body) AGAINST('+joins -indexes' IN BOOLEAN MODE);
```
**Tips:** Much faster than `LIKE '%text%'` on large text columns because it uses an inverted index instead of a full table scan. By default, MySQL ignores words shorter than 4 characters and very common ("stopword") terms in natural language mode — adjust `innodb_ft_min_token_size` if short words matter to your search. Available on InnoDB (MySQL 5.6+) and MyISAM.

---

### B11. Roles

**Definition:** A role is a named collection of privileges that can be granted to multiple users at once — instead of repeating the same `GRANT` statements individually for every user (MySQL 8.0+).

```sql
CREATE ROLE 'read_only', 'app_write';

GRANT SELECT ON company.* TO 'read_only';
GRANT SELECT, INSERT, UPDATE ON company.* TO 'app_write';

-- Assign a role to a user
CREATE USER 'reporting_user'@'localhost' IDENTIFIED BY 'pass123';
GRANT 'read_only' TO 'reporting_user'@'localhost';
SET DEFAULT ROLE 'read_only' TO 'reporting_user'@'localhost';

SHOW GRANTS FOR 'reporting_user'@'localhost';
REVOKE 'read_only' FROM 'reporting_user'@'localhost';
DROP ROLE 'read_only';
```
**Tips:** Roles make permission management scalable — update the role's privileges once and every user holding that role is affected, instead of hunting down every individual `GRANT`. Don't forget `SET DEFAULT ROLE`, or a granted role stays inactive for a user's session until explicitly activated with `SET ROLE`.

---

## 📋 Quick Reference: Full Query Execution Order

Understanding this order explains *why* certain clauses can/can't reference others:

```
1. FROM        (+ JOINs)
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT       (+ window functions evaluated here)
6. DISTINCT
7. ORDER BY
8. LIMIT / OFFSET
```

## ✅ Learning Path Suggestion

1. Topics 1-10 — Foundations (structure, commands, SELECT, WHERE)
2. Topics 11-18 — Filtering, sorting, aggregation, grouping
3. Topics 19-25 — Joins, subqueries, set operations, CASE
4. Topics 26-30 — Window functions & CTEs (the "intermediate → advanced" leap)
5. Topics 31-39 — Views, indexing, performance, transactions, design theory
6. Topics 40-45 — Built-in functions & temporary data
7. Topics 46-49 — Procedures, triggers, security, backups (DBA-adjacent skills)
8. Topic 50 — Practice real-world problems to cement everything

---

*This guide covers all 50 requested topics. If you think of any topic that's missing, let me know and I'll add it in the same format.*
