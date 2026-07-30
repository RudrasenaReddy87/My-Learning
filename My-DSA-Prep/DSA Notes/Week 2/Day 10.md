# Day 10 — Buy/Sell Stock + Rearranging

**Week 2: Arrays Part 1–2** | [Week overview](README.md)

**Language: Python**

---

## 1. Best Time to Buy and Sell Stock

**The problem:** given an array where `arr[i]` is a stock's price on day `i`,
find the **maximum profit** achievable by buying on one day and selling on a
**later** day (you must buy before you sell — only one transaction allowed).
If no profit is possible, return `0`.

**Example:** `[7, 1, 5, 3, 6, 4]` → buy at `1` (day 1), sell at `6` (day 4),
profit `= 5`.

### Brute force: check every buy/sell pair

```python
def max_profit_brute(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best
```
This checks all `O(n²)` pairs `(buy day, sell day)` with `buy < sell` — too
slow for large inputs.

### The optimal O(n) approach — track the minimum price seen so far

**Key insight:** for any given "sell day" `j`, the best possible profit
selling on that day is `prices[j] - (the minimum price at any day before j)`.
So instead of re-scanning backward for the minimum every time, just **track
the running minimum price** as you scan forward, once.

```python
def max_profit(prices):
    min_price_so_far = prices[0]
    best_profit = 0
    for price in prices[1:]:
        best_profit = max(best_profit, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)
    return best_profit
```

**Trace for `prices = [7, 1, 5, 3, 6, 4]`:**
| price | price - min_so_far | best_profit | min_price_so_far (after update) |
|---|---|---|---|
| start | — | 0 | 7 |
| 1 | 1-7=-6 | max(0,-6)=0 | min(7,1)=1 |
| 5 | 5-1=4 | max(0,4)=4 | min(1,5)=1 |
| 3 | 3-1=2 | max(4,2)=4 | min(1,3)=1 |
| 6 | 6-1=5 | max(4,5)=5 | min(1,6)=1 |
| 4 | 4-1=3 | max(5,3)=5 | min(1,4)=1 |

Result: `best_profit = 5`. Matches the expected answer (buy at `1`, sell at
`6`).

**Why compute `best_profit` before updating `min_price_so_far` on the same
iteration?** Because you can't sell and buy on the *same* day in this
problem — the profit at the current day must be based on a minimum price
from a **strictly earlier** day. Updating `min_price_so_far` after computing
that day's potential profit enforces "buy must happen before sell" correctly
without any extra bookkeeping.

**Complexity:** **O(n) time** (single pass), **O(1) space** — versus the
brute force's O(n²) time. This is the exact same "running best" pattern
family as Day 3 (largest element) and Day 9 (Kadane's) — here, tracking a
running *minimum* instead of a running *maximum*, and combining it with a
running best *difference*.

**Connection to Kadane's Algorithm (worth noticing):** if you transform the
price array into an array of **day-to-day differences**
(`diffs[i] = prices[i] - prices[i-1]`), then the maximum profit from a
single buy/sell transaction is exactly the **maximum subarray sum** of
`diffs` — i.e., this problem can be solved with Kadane's Algorithm directly
on the differences array. Both approaches are O(n)/O(1) and give the same
answer; the min-tracking version above is simpler to reason about directly,
but recognizing the Kadane's connection is a good sign you're starting to
see how these patterns relate to each other rather than memorizing them as
unrelated tricks.

---

## 2. Rearrange Array Elements by Sign (Alternating +/-)

**The problem:** given an array with an **equal number** of positive and
negative integers, rearrange it so that positive and negative numbers
alternate, **starting with a positive number**, while preserving the
relative order of positives among themselves and negatives among themselves.

**Example:** `[3, 1, -2, -5, 2, -4]` (3 positives: `3,1,2`; 3 negatives:
`-2,-5,-4`) → `[3, -2, 1, -5, 2, -4]`.

**Idea:** since the counts are guaranteed equal, positives will land at all
the **even indices** (`0, 2, 4, ...`) and negatives at all the **odd
indices** (`1, 3, 5, ...`) of the output. Scan the original array once,
placing each positive into the next available even slot and each negative
into the next available odd slot, using a new result array.

```python
def rearrange_by_sign(arr):
    n = len(arr)
    result = [0] * n
    pos_index = 0     # next even index to fill with a positive
    neg_index = 1      # next odd index to fill with a negative
    for x in arr:
        if x > 0:
            result[pos_index] = x
            pos_index += 2
        else:
            result[neg_index] = x
            neg_index += 2
    return result
```

**Trace for `arr = [3, 1, -2, -5, 2, -4]`:**
| x | sign | slot filled | result after |
|---|---|---|---|
| 3 | + | index 0 | [3,_,_,_,_,_] |
| 1 | + | index 2 | [3,_,1,_,_,_] |
| -2 | - | index 1 | [3,-2,1,_,_,_] |
| -5 | - | index 3 | [3,-2,1,-5,_,_] |
| 2 | + | index 4 | [3,-2,1,-5,2,_] |
| -4 | - | index 5 | [3,-2,1,-5,2,-4] |

Result: `[3, -2, 1, -5, 2, -4]` — positives (`3,1,2`) and negatives
(`-2,-5,-4`) each keep their original relative order, and the signs
correctly alternate starting with positive.

**Complexity:** **O(n) time** (single pass), but **O(n) space** for the new
`result` array — this is *not* in-place, unlike most of this week's other
problems, because interleaving elements from two different original
positions while preserving order generally can't be done with a simple
in-place swap strategy (unlike, say, the Dutch National Flag partitioning,
where elements only need to be grouped, not precisely interleaved).

**What if the counts of positives/negatives are unequal?** The version above
assumes they're exactly equal (a common problem constraint). A more general
version would first place all the "fully alternated" pairs, then append the
leftover excess elements (all positive, or all negative) at the end — a
reasonable extension to think through on your own if you want to push this
further, but not required for today's practice question.

---

## Worked Examples — Trace These Yourself First

**Example A:** In `max_profit`, what does the function return if `prices`
is strictly decreasing, e.g. `[9, 7, 5, 3, 1]`? Why is that the correct
answer?
<details><summary>Answer</summary>
It returns `0`. At every step, `price - min_price_so_far` is `≤ 0` (since
each new price is lower than everything before it, meaning `min_price_so_far`
always equals the current price, giving a difference of exactly 0) — so
`best_profit`, initialized to `0`, never gets updated to anything positive.
This correctly reflects that there's no way to buy low and sell high later
in a strictly decreasing sequence — the best you can do is avoid a loss by
"not transacting," which the problem models as a profit of `0`.
</details>

**Example B:** Why can't `rearrange_by_sign` be done with a simple two-pointer
in-place swap, the way `move_negatives_to_left` was on Day 8?
<details><summary>Answer</summary>
`move_negatives_to_left` (Day 8) only needed to **group** negatives and
positives — it didn't need to preserve their exact relative order or
interleave them in a specific pattern, so a simple converging swap
sufficed. Today's problem needs a *precise interleaving* (positive,
negative, positive, negative, ...) while *also* preserving each group's
internal relative order — satisfying both constraints simultaneously with
in-place swaps would require much more intricate bookkeeping than a plain
two-pointer sweep can offer cleanly, so building a new result array (trading
O(1) space for a simpler O(n)-space single pass) is the practical choice.
</details>

**Example C:** How does the "maximum profit = maximum subarray sum of daily
differences" connection (mentioned at the end of section 1) work concretely
for `prices = [7, 1, 5, 3, 6, 4]`? Compute the diffs array and verify Kadane's
gives the same answer as the min-tracking approach.
<details><summary>Answer</summary>
`diffs = [1-7, 5-1, 3-5, 6-3, 4-6] = [-6, 4, -2, 3, -2]`. Running Kadane's
on `diffs`: `current_sum` starts at `-6`; at `4`, `max(4, -6+4=-2)=4`; at
`-2`, `max(-2, 4-2=2)=2`; at `3`, `max(3, 2+3=5)=5`; at `-2`,
`max(-2, 5-2=3)=3`. Best sum seen across all steps: `5` (reached right after
processing the `3` diff). This matches `max_profit([7,1,5,3,6,4]) = 5` from
section 1's trace — confirming the two approaches agree, since the subarray
`[4, -2, 3]` in `diffs` (corresponding to buying at price `1` and selling at
price `6`) sums to exactly `5`.
</details>

---

## Practice Questions

### Question 1 — Best Time to Buy and Sell Stock
**Question:** Given daily stock prices, find the maximum profit from a
single buy followed by a later sell. Return `0` if no profit is possible.
**Input:** `prices = [7, 1, 5, 3, 6, 4]`
**Output:** `5`
**Input 2:** `prices = [9, 7, 5, 3, 1]`
**Output 2:** `0`
**Solution:**
```python
def max_profit(prices):
    min_price_so_far = prices[0]
    best_profit = 0
    for price in prices[1:]:
        best_profit = max(best_profit, price - min_price_so_far)
        min_price_so_far = min(min_price_so_far, price)
    return best_profit

print(max_profit([7, 1, 5, 3, 6, 4]))   # 5
print(max_profit([9, 7, 5, 3, 1]))       # 0
```
Track the minimum price seen so far while scanning forward once; at each
day, check the profit from selling today against the cheapest earlier buy
price. Complexity: `O(n)` time, `O(1)` space (section 1).

### Question 2 — Rearrange Array Elements by Sign
**Question:** Given an array with an equal number of positive and negative
integers, rearrange it so signs alternate starting with positive, preserving
each group's relative order.
**Input:** `arr = [3, 1, -2, -5, 2, -4]`
**Output:** `[3, -2, 1, -5, 2, -4]`
**Solution:**
```python
def rearrange_by_sign(arr):
    n = len(arr)
    result = [0] * n
    pos_index = 0
    neg_index = 1
    for x in arr:
        if x > 0:
            result[pos_index] = x
            pos_index += 2
        else:
            result[neg_index] = x
            neg_index += 2
    return result

print(rearrange_by_sign([3, 1, -2, -5, 2, -4]))   # [3, -2, 1, -5, 2, -4]
```
Positives fill even indices, negatives fill odd indices, each advancing
independently through the original array in order. Complexity: `O(n)` time,
`O(n)` space (section 2 — not in-place, unlike most of this week's other
problems).

## Revision

- Quick recall (5 min): re-derive Kadane's Algorithm from Day 9 from
  scratch — write the recurrence (`current_sum = max(x, current_sum + x)`),
  then the code, without looking back.

## Key Takeaways

- **Best Time to Buy and Sell Stock** is solved by tracking a running
  **minimum price** while scanning forward once, comparing each day's price
  against that minimum — `O(n)` time, `O(1)` space, and it's secretly
  equivalent to running **Kadane's Algorithm on the array of daily price
  differences**.
- Compute the current day's potential profit **before** updating the running
  minimum, so a day never incorrectly "buys and sells" using its own price
  as both bounds.
- **Rearranging by sign** requires precise interleaving *and* order
  preservation within each group simultaneously — a constraint combination
  that's naturally solved with a new result array (`O(n)` space) rather than
  in-place swaps, unlike simpler grouping problems (Day 8's move-negatives).
- Recognizing when two seemingly different problems (buy/sell stock, max
  subarray sum) reduce to the **same underlying pattern** is a skill that
  compounds — it's worth actively looking for these connections rather than
  treating every new problem as unrelated.

---

## Additional Topics — Filling Gaps in Day 10's Scope

Day 10 covered the **single-transaction** Buy/Sell Stock problem. Its two
natural follow-ups — allowing **multiple** transactions, and allowing **at
most two** transactions — are both extremely common interview variants and
belong here.

### 3. Best Time to Buy and Sell Stock II (Unlimited Transactions)

**The problem:** same setup as section 1, but now you're allowed to
complete **as many transactions as you like** (buy then sell, buy then
sell, ...) — as long as you don't hold more than one share at a time (you
must sell before buying again). Maximize total profit.

**Key insight:** since there's no limit on the number of transactions,
you can capture **every single upward price movement** independently —
buy right before each rise and sell right after it. This means the answer
is simply the **sum of every positive day-to-day price difference**.

```python
def max_profit_ii(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

print(max_profit_ii([7, 1, 5, 3, 6, 4]))   # 7
```

**Trace for `prices = [7, 1, 5, 3, 6, 4]`:** day-to-day diffs are
`1-7=-6, 5-1=4, 3-5=-2, 6-3=3, 4-6=-2`. Sum only the positive ones:
`4 + 3 = 7`. This corresponds to buying at `1` and selling at `5` (profit
`4`), then buying at `3` and selling at `6` (profit `3`) — two separate
transactions, total `7`.

**Why is "sum every positive diff" equivalent to "buy at every local
minimum, sell at every local maximum"?** Any profitable run of consecutive
price increases can be captured as one transaction (buy at the run's start,
sell at its end) — and the profit from that one transaction equals the
**sum of the individual day-to-day increases** within that run (they
telescope: `(p2-p1)+(p3-p2)+...+(pn-pn-1) = pn-p1`). So summing every
positive daily diff directly, without explicitly identifying runs, gives
the identical total profit.

**Complexity:** **O(n) time**, **O(1) space** — even simpler than the
single-transaction version (section 1), since there's no "track the
minimum so far" bookkeeping needed once unlimited transactions are allowed.

### 4. Best Time to Buy and Sell Stock III (At Most Two Transactions)

**The problem:** like section 1 (single transaction), but now up to **two**
transactions are allowed (you must still sell before buying again).
Maximize total profit.

**Idea — track four running states** as you scan once: `buy1` (max profit
after one buy — i.e., the negative of the cheapest first-buy price seen so
far), `sell1` (max profit after completing one full transaction), `buy2`
(max profit after buying a second time, funded by `sell1`'s profit), and
`sell2` (max profit after completing a second full transaction). Update all
four at each price, in this dependency order.

```python
def max_profit_iii(prices):
    if not prices:
        return 0
    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0
    for p in prices:
        buy1 = max(buy1, -p)                 # best (most negative) cost so far for buy #1
        sell1 = max(sell1, buy1 + p)          # best profit after selling #1
        buy2 = max(buy2, sell1 - p)           # best "net cost" for buy #2, funded by sell1's profit
        sell2 = max(sell2, buy2 + p)          # best profit after selling #2
    return sell2

print(max_profit_iii([3, 3, 5, 0, 0, 3, 1, 4]))   # 6
```

**Trace for `prices = [3, 3, 5, 0, 0, 3, 1, 4]`** (abbreviated — key
milestones): starting `buy1=buy2=-inf, sell1=sell2=0`. At `p=3`:
`buy1=max(-inf,-3)=-3`, `sell1=max(0,-3+3=0)=0`, `buy2=max(-inf,0-3=-3)=-3`,
`sell2=max(0,-3+3=0)=0`. ... at `p=0` (index 3): `buy1=max(-3,0)=0`
(cheapest buy price now recorded as `0`, since `-0=0 > -3`). ... at `p=3`
(index 5): `sell1=max(...,0+3=3)=3` (first transaction: buy at `0`, sell at
`3`, profit `3`); `buy2=max(...,3-3=0)`. ... at `p=4` (index 7):
`sell2=max(...,buy2+4)` — working out to `6` total (buy at `0` sell at `3`
= profit `3`; buy at `1` sell at `4` = profit `3`; total `6`).

**Why does `buy2 = max(buy2, sell1 - p)` correctly "fund" the second buy
using the first transaction's profit?** `sell1` represents the best profit
achievable from exactly one completed transaction up through the current
day. `sell1 - p` represents "spend `p` today to buy a second share, using
whatever profit the first transaction already banked" — so `buy2` tracks
the best possible **net position** (profit-so-far minus new purchase cost)
across all ways of having completed one transaction and then bought a
second time.

**Complexity:** **O(n) time** (single pass, constant work per step),
**O(1) space** — this is a compact **dynamic programming** formulation (a
preview of the DP-on-arrays style you'll see more of in later weeks),
distinct in spirit from the simpler greedy pattern of section 1 and
Question II above.

## Additional Key Takeaways (Day 10 Supplement)

- **Unlimited transactions (Stock II)** reduces to summing every positive
  day-to-day price difference — no running-minimum tracking needed, since
  every profitable up-move can be captured independently.
- **At most two transactions (Stock III)** requires tracking four running
  states (`buy1, sell1, buy2, sell2`) in dependency order within a single
  pass — an early example of the dynamic-programming-on-arrays style,
  distinct from this week's greedy/two-pointer/hashing patterns.
- The general **Stock I → II → III → (k transactions)** progression is a
  good example of a problem family that gets progressively harder not by
  changing the core insight, but by adding more simultaneously-tracked
  states — worth remembering the pattern rather than each variant in
  isolation.
