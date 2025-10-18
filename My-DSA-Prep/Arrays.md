# Arrays: The Building Blocks of Data Structures

Hey there, fellow coder! If you're diving into data structures and algorithms, arrays are where it all starts. Think of arrays as the simplest way to store a collection of items in a contiguous block of memory. They're like a row of lockers, each holding a value, and you access them by their position (index). Arrays are fundamental because they're fast for random access, but they have limitations like fixed size in some languages. In competitive programming (CP), arrays are everywhere – from storing input data to implementing other structures. Let's break this down step by step, with examples, complexities, and my personal tips from banging my head against array problems.

## Introduction to Arrays

Arrays are ordered collections of elements of the same type. Why important? They allow efficient storage and retrieval. Use cases: storing scores in a game, pixels in an image, or coefficients in a polynomial. In Python, lists are dynamic arrays, but in C++, arrays are fixed-size. We'll cover both perspectives.

Key properties:
- Indexed from 0 (usually).
- Contiguous memory.
- O(1) access time.

Personal note: Arrays taught me indexing; I once forgot 0-based and wasted hours debugging.

## Basics: Declaration, Initialization, Indexing, Iteration

### Declaration
Declaring an array allocates memory for a collection of elements. In Python, lists are dynamic and can grow, while in C++ arrays are fixed-size unless using vectors.

Explanation: The following code shows how to declare arrays in Python and C++. In Python, we use square brackets to create lists, which can be empty or initialized with values. In C++, we specify the type and size in brackets.

In Python:
```python
arr = []  # Creates an empty list, which can be appended to later
arr = [1, 2, 3]  # Initializes a list with three integer elements
```
In C++:
```cpp
int arr[5];  // Declares a fixed-size array of 5 integers, uninitialized
```

Parameters: For static arrays like C++, you specify the size in brackets.
Return: Declaration doesn't return a value; it just sets up the array in memory.
Complexity: O(1) time for declaration, O(n) space where n is the size.

Example 1: Declare an array of integers and print it.
Explanation: This example creates a list of integers and prints it to the console, demonstrating basic declaration and output.

```python
numbers = [10, 20, 30, 40, 50]  # List with 5 elements
print(numbers)  # Output: [10, 20, 30, 40, 50]
```
Tip: In competitive programming, Python lists are flexible and resize automatically, making them ideal for dynamic problems.

### Initialization
Filling an array with initial values or creating arrays of a specific size and content.

```python
arr = [0] * 10  # Creates a list of 10 zeros: [0, 0, 0, ..., 0]
```
Complexity: O(n).

Example 2: Initialize with a sequence of numbers using range.
```python
arr = list(range(1, 11))  # Creates [1, 2, 3, ..., 10]
```

### Indexing
Accessing elements by their position (index) in the array.

```python
print(arr[0])  # Prints the first element of the array
```
Complexity: O(1).

Example: Get the middle element of the array.
```python
mid = len(arr) // 2
print(arr[mid])  # Prints the element at the middle index
```

### Iteration
Looping through each element in the array to perform operations.

```python
for i in range(len(arr)):
    print(arr[i])  # Prints each element using index-based loop
```
Complexity: O(n).

Example: Calculate the sum of all elements in the array.
```python
total = 0
for num in arr:
    total += num  # Adds each number to total
print(total)  # Prints the total sum
```

## Operations: Insert, Delete, Update, Search

### Insert
Explanation: Adding an element at a specific position in the array, which may require shifting other elements to the right.

In Python: arr.insert(index, value)
Complexity: O(n) worst case.

Example: Insert 99 at index 2.
Explanation: Inserts the value 99 at index 2, shifting the subsequent elements.

```python
arr = [1,2,3,4]
arr.insert(2, 99)  # [1,2,99,3,4]
```

### Delete
Explanation: Removing an element from the array, either by index or by value, which may require shifting elements.

arr.pop(index) or arr.remove(value)
Complexity: O(n).

Example: Remove first occurrence of 3.
Explanation: Removes the first occurrence of the value 3 from the array.

```python
arr.remove(3)
```

### Update
Explanation: Changing the value at a specific index in the array.

arr[index] = new_value
Complexity: O(1).

Example: Update index 1 to 100.
Explanation: Sets the element at index 1 to the new value 100.

```python
arr[1] = 100
```

### Search
Explanation: Finding the index of a specific value in the array.

arr.index(value)
Complexity: O(n).

Example: Find index of 4.
Explanation: Returns the index of the first occurrence of 4 in the array.

```python
idx = arr.index(4)
```

## Multi-dimensional Arrays

2D arrays are arrays of arrays.
Declaration: arr = [[0]*cols for _ in range(rows)]
Access: arr[row][col]

Example: 3x3 matrix.
```python
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][2])  # 6
```

Traversal: Nested loops.
Complexity: O(rows * cols)

## Methods: append, extend, pop, remove, insert, slicing, len, sum, min, max, sort, reverse

### append
Add to end.
arr.append(value)
Complexity: O(1) amortized.

Example: Append 5.
```python
arr.append(5)
```

### extend
Add iterable.
arr.extend([6,7])
Complexity: O(k) where k is length of iterable.

Example: Extend with list.
```python
arr.extend([6,7])
```

### pop
Remove and return last or at index.
arr.pop() or arr.pop(index)
Complexity: O(1) for end, O(n) for middle.

Example: Pop last.
```python
last = arr.pop()
```

### remove
Remove first occurrence.
arr.remove(value)
Complexity: O(n).

Example: Remove 2.
```python
arr.remove(2)
```

### insert
Insert at index.
arr.insert(index, value)
Complexity: O(n).

Example: Insert at 0.
```python
arr.insert(0, 0)
```

### slicing
Get subarray.
arr[start:end:step]
Complexity: O(k) where k is slice size.

Example: First 3 elements.
```python
sub = arr[:3]
```

### len
Get length.
len(arr)
Complexity: O(1).

Example: Print length.
```python
print(len(arr))
```

### sum
Sum elements.
sum(arr)
Complexity: O(n).

Example: Total sum.
```python
total = sum(arr)
```

### min/max
Min/max value.
min(arr), max(arr)
Complexity: O(n).

Example: Find min.
```python
smallest = min(arr)
```

### sort
Sort in place.
arr.sort()
Complexity: O(n log n).

Example: Sort ascending.
```python
arr.sort()
```

### reverse
Reverse in place.
arr.reverse()
Complexity: O(n).

Example: Reverse array.
```python
arr.reverse()
```

## Searching Algorithms

### Linear Search
Explanation: Linear search is a simple algorithm that checks each element in the array sequentially until the target is found or the end is reached. It's straightforward but inefficient for large arrays.

How it works:
1. Start from the first element (index 0).
2. Compare the current element with the target.
3. If it matches, return the index.
4. If not, move to the next element.
5. Repeat until the end of the array.
6. If not found, return -1.

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```
Complexity: O(n) time, O(1) space.

Example: Search for 5 in [1,2,3,4,5].
- Check 1: No
- Check 2: No
- Check 3: No
- Check 4: No
- Check 5: Yes, return 4.

Tip: Use when array is unsorted.

### Binary Search
Explanation: Binary search is an efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half. It requires the array to be sorted beforehand.

How it works:
1. Initialize left = 0, right = len(arr) - 1.
2. While left <= right:
   a. Calculate mid = (left + right) // 2.
   b. If arr[mid] == target, return mid.
   c. If arr[mid] < target, set left = mid + 1 (search right half).
   d. Else, set right = mid - 1 (search left half).
3. If not found, return -1.

```python
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
Complexity: O(log n) time, O(1) space.

Example: Search in [1,3,5,7,9] for 7.
- Initial: left=0, right=4, mid=(0+4)//2=2, arr[2]=5 < 7, so left = 2+1 = 3.
- Now: left=3, right=4, mid=(3+4)//2=3, arr[3]=7 == 7, return 3.

Tip: Requires sorted array. Use bisect in Python for efficiency.

### Ternary Search
Explanation: Ternary search is a divide and conquer algorithm that finds the maximum or minimum of a unimodal function by dividing the search space into three parts instead of two. It's useful for optimization problems on arrays.

How it works:
1. Divide the array into three parts by calculating two midpoints: mid1 = left + (right - left) // 3, mid2 = right - (right - left) // 3.
2. Compare arr[mid1] and arr[mid2]:
   - If arr[mid1] < arr[mid2], the peak is in the right part, so set left = mid1.
   - Else, the peak is in the left part, so set right = mid2.
3. Repeat until the search space is small (right - left <= 2).
4. Perform linear search in the remaining elements to find the target.

```python
def ternary_search(arr, left, right, target):
    while right - left > 2:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if arr[mid1] < arr[mid2]:
            left = mid1
        else:
            right = mid2
    # Linear search in the remaining elements
    for i in range(left, right + 1):
        if arr[i] == target:
            return i
    return -1
```
Complexity: O(log3 n) time.

Example: Search in a unimodal array [1,2,3,4,5,4,3,2,1] for 5.
- Initial: left=0, right=8, mid1=2 (arr[2]=3), mid2=5 (arr[5]=4), 3 < 4, so left=2.
- Next: left=2, right=8, mid1=4 (arr[4]=5), mid2=6 (arr[6]=3), 5 > 3, so right=6.
- Continue until small range, then linear search.

### Exponential Search
Explanation: Exponential search (also known as galloping search or doubling search) is a search algorithm that finds the range where the target may reside and then performs a binary search within that range. It's useful for unbounded or infinite arrays.

How it works:
1. Check if the target is at the first index (arr[0]). If yes, return 0.
2. Start with i = 1, and double i until arr[i] > target or i >= len(arr).
3. Once the range is found (from i//2 to min(i, len(arr)-1)), perform binary search in this subarray.

```python
import math

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i//2, min(i, len(arr)-1))
```
Complexity: O(log n) time.

Example: Search in [1,2,3,4,5,6,7,8,9,10] for 7.
- Check arr[0]=1 !=7, proceed.
- i=1, arr[1]=2 <=7, i=2
- i=2, arr[2]=3 <=7, i=4
- i=4, arr[4]=5 <=7, i=8
- i=8, arr[8]=9 >7, stop.
- Binary search in range 4 to 8: [5,6,7,8,9], find 7 at index 6.

### Jump Search
Explanation: Jump search (or block search) is a search algorithm for sorted arrays that jumps ahead by fixed steps or blocks and then performs a linear search within the block. It's a compromise between linear and binary search.

How it works:
1. Determine the block size, typically sqrt(n), where n is the array length.
2. Start from the beginning, jump ahead by block size until the element at the end of the current block is greater than or equal to the target.
3. Once the block is found, perform a linear search within that block to find the target.

```python
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1
```
Complexity: O(√n) time.

Example: Search in [1,2,3,4,5,6,7,8,9] for 6.
- n=9, step=int(sqrt(9))=3.
- Check arr[min(3,9)-1]=arr[2]=3 <6, so prev=3, step=3+3=6.
- Check arr[min(6,9)-1]=arr[5]=6 not <6, stop.
- Linear search from prev=3 to min(6,9)=6: indices 3,4,5: 4,5,6. Find 6 at index 5.

## Sorting Algorithms

### Bubble Sort
Explanation: Bubble sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. It's called bubble sort because smaller elements "bubble" to the top.

How it works:
1. Start from the beginning of the array.
2. Compare the first two elements; if the first is greater than the second, swap them.
3. Move to the next pair (second and third), and so on, until the end of the array. This completes one pass.
4. After each pass, the largest element "bubbles" to the end, so the next pass can ignore the last element.
5. Repeat the process for n-1 passes, where n is the array length, until no swaps are needed or the array is sorted.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```
Complexity: O(n^2) time, O(1) space.

Example: Sort [3,1,4,1,5].
- Pass 1: Compare 3>1, swap -> [1,3,4,1,5]; 3<4, no; 4>1, swap -> [1,3,1,4,5]; 4<5, no. Largest 5 at end.
- Pass 2: Compare 1<3, no; 3>1, swap -> [1,1,3,4,5]; 3<4, no; 4<5, no.
- Pass 3: Compare 1<1, no; 1<3, no; 3<4, no.
- Sorted: [1,1,3,4,5].

Tip: Simple but slow; avoid in CP.

### Selection Sort
Explanation: Selection sort divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.

How it works:
1. Start with the first element as the current minimum.
2. Scan the remaining unsorted part of the array to find the smallest element.
3. Swap the smallest element found with the first element of the unsorted part.
4. Move the boundary of the sorted part one step to the right.
5. Repeat the process for the remaining unsorted array until the entire array is sorted.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```
Complexity: O(n^2).

Example: Sort [3,1,4,1,5].
- Iteration 1: Unsorted [3,1,4,1,5], find min=1 at index 1, swap with index 0 -> [1,3,4,1,5]
- Iteration 2: Unsorted [3,4,1,5], find min=1 at index 3, swap with index 1 -> [1,1,4,3,5]
- Iteration 3: Unsorted [4,3,5], find min=3 at index 3, swap with index 2 -> [1,1,3,4,5]
- Iteration 4: Unsorted [4,5], find min=4 at index 3, already in place -> [1,1,3,4,5]
- Sorted: [1,1,3,4,5].

### Insertion Sort
Explanation: Insertion sort builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages: simple implementation, efficient for small data sets, and adaptive (efficient for data sets that are already substantially sorted).

How it works:
1. Start from the second element (index 1), consider it as the key.
2. Compare the key with elements before it, shifting larger elements to the right.
3. Insert the key into its correct position in the sorted subarray.
4. Repeat for each subsequent element.

Pros: Stable, adaptive (fast on nearly sorted arrays), in-place, simple.
Cons: O(n^2) worst-case, not suitable for large datasets.
When to use: Small arrays, nearly sorted data, or as part of more complex algorithms like Timsort.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
```
Complexity: O(n^2) worst, O(n) best.

Example: Sort [5,2,4,6,1,3].
- Start with [5], insert 2: [2,5], insert 4: [2,4,5], insert 6: [2,4,5,6], insert 1: [1,2,4,5,6], insert 3: [1,2,3,4,5,6].

### Merge Sort
Explanation: Merge sort is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

How it works:
1. Divide the array into two halves recursively until each subarray has one element.
2. Merge the sorted subarrays by comparing elements and placing them in order.
3. Repeat until the entire array is sorted.

Pros: Stable, guaranteed O(n log n), works well for large datasets, parallelizable.
Cons: Requires extra space O(n), not in-place.
When to use: When stability is needed, or for linked lists, or when extra space is acceptable.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```
Complexity: O(n log n).

Example: Sort [8,3,2,9,7,1,5,4].
- Divide: [8,3,2,9] and [7,1,5,4]
- Further divide until single elements, then merge back.
- Final: [1,2,3,4,5,7,8,9].

### Quick Sort
Explanation: QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways: Always pick first element as pivot, Always pick last element as pivot, Pick a random element as pivot, Pick median as pivot.

How it works:
1. Choose a pivot element.
2. Partition the array into elements less than pivot, equal to pivot, and greater than pivot.
3. Recursively sort the left and right partitions.
4. Combine the sorted partitions.

Pros: In-place (can be implemented in-place), fast in practice, cache-friendly.
Cons: O(n^2) worst-case (mitigated by good pivot selection), not stable.
When to use: General-purpose sorting, when in-place is needed, and average-case performance is acceptable.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```
Complexity: O(n log n) average, O(n^2) worst.

Example: Sort [3,6,8,10,1,2,1].
- Pivot=8, left=[3,6,1,2,1], middle=[8], right=[10]
- Recurse on left: pivot=1, etc.
- Final: [1,1,2,3,6,8,10].

### Heap Sort
Explanation: Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for the remaining elements.

How it works:
1. Build a max-heap from the array.
2. Swap the root (max element) with the last element, reduce heap size.
3. Heapify the root to maintain heap property.
4. Repeat until the array is sorted.

Pros: In-place, guaranteed O(n log n), no worst-case issues like quicksort.
Cons: Not stable, slower in practice than quicksort due to cache misses.
When to use: When worst-case guarantees are needed, or for priority queue-based sorting.

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```
Complexity: O(n log n).

Example: Sort [4,10,3,5,1].
- Build heap: [10,5,3,4,1]
- Swap 10 with 1: [1,5,3,4,10], heapify: [5,4,3,1,10]
- Swap 5 with 1: [1,4,3,5,10], heapify: [4,1,3,5,10]
- And so on, final: [1,3,4,5,10].

### Radix Sort
Explanation: Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.

How it works:
1. Find the maximum number to determine the number of digits.
2. For each digit place (units, tens, etc.), use counting sort to sort the array based on that digit.
3. Repeat for each digit until sorted.

Pros: Linear time for fixed digit lengths, stable, no comparisons.
Cons: Only for integers, requires extra space, not general-purpose.
When to use: Sorting large sets of integers with known digit ranges, like phone numbers or IDs.

```python
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
```
Complexity: O(n * d) where d is the number of digits.

Example: Sort [170, 45, 75, 90, 802, 24, 2, 66].
- Sort by units: [170,90,802,2,24,45,75,66]
- Tens: [802,2,24,45,66,170,75,90]
- Hundreds: [2,24,45,66,75,90,170,802].

## Advanced Array Techniques

### Dutch National Flag (3-way Partitioning)
Explanation: Used to sort an array of 0s, 1s, and 2s efficiently. It partitions the array into three sections: elements less than pivot, equal to pivot, and greater than pivot.

```python
def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
```
Complexity: O(n) time, O(1) space.

Example: Sort [0,1,2,0,1,2] -> [0,0,1,1,2,2]

### Mo's Algorithm
Explanation: An offline algorithm for answering range queries efficiently by sorting queries and processing them in blocks. Useful for static arrays with multiple queries.

```python
# Simplified example for sum queries
def mo_algorithm(arr, queries):
    block_size = int(len(arr) ** 0.5)
    queries.sort(key=lambda x: (x[0] // block_size, x[1]))
    current_sum = 0
    left, right = 0, -1
    answers = [0] * len(queries)
    for i, (l, r) in enumerate(queries):
        while right < r:
            right += 1
            current_sum += arr[right]
        while left > l:
            left -= 1
            current_sum += arr[left]
        while right > r:
            current_sum -= arr[right]
            right -= 1
        while left < l:
            current_sum -= arr[left]
            left += 1
        answers[i] = current_sum
    return answers
```
Complexity: O((n + q) * √n) for q queries.

Example: For range sum queries on static array.

### Array Rearrangements

#### Even-Odd Rearrangement
Rearrange array so that even numbers come before odd numbers.

```python
def even_odd_rearrange(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while arr[left] % 2 == 0 and left < right:
            left += 1
        while arr[right] % 2 == 1 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
```
Complexity: O(n).

Example: [1,2,3,4] -> [4,2,3,1] (one possible arrangement)

#### Positive-Negative Rearrangement
Rearrange so that positive and negative numbers alternate.

```python
def positive_negative_rearrange(arr):
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    result = []
    i, j = 0, 0
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
    result.extend(pos[i:])
    result.extend(neg[j:])
    return result
```
Complexity: O(n).

Example: [-1,2,-3,4] -> [2,-1,4,-3]

### Wave Array
Arrange array in wave form: arr[0] >= arr[1] <= arr[2] >= arr[3] <= ...

```python
def wave_array(arr):
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
```
Complexity: O(n log n) due to sort.

Example: [1,2,3,4] -> [2,1,4,3]

## Tips, Tricks, and Pitfalls for CP

- Use list comprehensions for initialization: [0 for _ in range(n)]
- For large arrays, consider numpy for efficiency.
- Pitfall: Off-by-one errors in indexing.
- Trick: Use negative indices: arr[-1] for last.
- In interviews, explain complexities.
- Cross-reference: Arrays are basis for stacks, queues.

This covers arrays thoroughly. Practice problems like two-sum, rotate array.

## Array Rotations

Rotating an array means shifting elements left or right.

### Left Rotation by k positions
```python
def rotate_left(arr, k):
    n = len(arr)
    k %= n
    return arr[k:] + arr[:k]
```
Complexity: O(n).

Example: rotate_left([1,2,3,4,5], 2) -> [3,4,5,1,2]

### Right Rotation
```python
def rotate_right(arr, k):
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]
```
Example: rotate_right([1,2,3,4,5], 2) -> [4,5,1,2,3]

### In-place Rotation using Reversal
```python
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_inplace(arr, k):
    n = len(arr)
    k %= n
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
```
Complexity: O(n), O(1) space.

## Prefix Sums

Precompute sums for range queries.

### Prefix Sum Array
```python
def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    return prefix

def range_sum(prefix, l, r):
    return prefix[r+1] - prefix[l]
```
Complexity: O(n) build, O(1) query.

Example: arr = [1,2,3,4], prefix = [0,1,3,6,10], range_sum(1,3) = 2+3+4=9

## Two-Pointer Technique

Use two pointers for efficient traversal.

### Remove Duplicates from Sorted Array
```python
def remove_duplicates(arr):
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1
```
Complexity: O(n).

Example: [1,1,2,2,3] -> [1,2,3], length 3

### Pair with Sum
```python
def two_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr)-1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []
```
Complexity: O(n log n) due to sort, O(n) if sorted.

## Kadane's Algorithm (Already mentioned, but expanding)

Handles negative numbers.

Variations: For all negative, return max element.

Circular max subarray: Consider wrapping.

```python
def max_circular_subarray(arr):
    def kadane(arr):
        max_current = max_global = arr[0]
        for num in arr[1:]:
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
        return max_global

    max_kadane = kadane(arr)
    max_wrap = sum(arr) - min(kadane([-x for x in arr]) for x in arr if x != 0)  # Simplified
    return max(max_kadane, max_wrap) if max_wrap else max_kadane
```
Complexity: O(n).

## Array Problems in Competitive Programming

### Two Sum
Find indices of two numbers summing to target.
Use hashmap for O(n).

```python
def two_sum_hash(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Majority Element (Boyer-Moore)
```python
def majority_element(arr):
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
```
Complexity: O(n), O(1) space.

### Find Missing Number
In 1 to n, one missing.
Use XOR or sum.

```python
def missing_number(arr, n):
    xor = 0
    for i in range(1, n+1):
        xor ^= i
    for num in arr:
        xor ^= num
    return xor
```

### Rotate Array k times
As above.

### Maximum Product Subarray
Similar to Kadane, but for product.

```python
def max_product_subarray(arr):
    if not arr:
        return 0
    max_so_far = min_so_far = result = arr[0]
    for num in arr[1:]:
        temp_max = max(num, max_so_far * num, min_so_far * num)
        min_so_far = min(num, max_so_far * num, min_so_far * num)
        max_so_far = temp_max
        result = max(result, max_so_far)
    return result
```

### Trapping Rain Water
```python
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```
Complexity: O(n).

### Subarray Sum Equals K
Count subarrays with sum equal to k.

```python
def subarray_sum(arr, k):
    count = 0
    prefix_sum = 0
    sum_map = {0: 1}
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in sum_map:
            count += sum_map[prefix_sum - k]
        sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1
    return count
```
Complexity: O(n).

Example: [1,1,1], k=2 -> 2

### Longest Consecutive Sequence
Find longest consecutive elements sequence.

```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current = 1
            while num + current in num_set:
                current += 1
            longest = max(longest, current)
    return longest
```
Complexity: O(n).

Example: [100,4,200,1,3,2] -> 4 (1,2,3,4)

### Find the Duplicate Number
In array of n+1 elements (1 to n), find duplicate.

```python
def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
```
Complexity: O(n).

Example: [1,3,4,2,2] -> 2

### Move Zeros to End
Move all zeros to end while maintaining order.

```python
def move_zeros(arr):
    last_non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[last_non_zero], arr[i] = arr[i], arr[last_non_zero]
            last_non_zero += 1
```
Complexity: O(n).

Example: [0,1,0,3,12] -> [1,3,12,0,0]

## Interview Questions

- Find the duplicate in array of n+1 elements (1 to n).
- Move zeros to end.
- Find intersection of two arrays.
- Container with most water (two pointers).
- 3Sum problem.

## Edge Cases

- Empty array: Handle with if not arr.
- Single element: Return it.
- All negative: For max subarray, return max.
- Duplicates: In searches, return any index.
- Large k in rotation: k %= n

## Time Complexities in Detail

- Access: O(1)
- Search unsorted: O(n)
- Search sorted: O(log n)
- Insert end: O(1) amortized
- Insert middle: O(n)
- Delete: O(n)
- Sort: O(n log n)

## Personal Stories

- In a contest, I used linear search on sorted array and TLE'd; switched to binary and passed.
- Forgot to handle empty array in two pointers, got index error.

## Code Variations

- Recursive binary search.
- Iterative vs recursive merge sort.
- In-place vs extra space sorts.

## Examples to Practice

1. Reverse array in place.
2. Find second largest.
3. Check if array is sorted.
4. Merge two sorted arrays.
5. Find pivot index (prefix sum).

## More Advanced Topics

### Sparse Arrays
Use dictionaries for large, sparse arrays.

### Dynamic Arrays in C++
std::vector.

### Numpy Arrays for Numerical Computing
```python
import numpy as np
arr = np.array([1,2,3])
print(arr * 2)  # [2,4,6]
```

### Bit Manipulation for Arrays
Count set bits, etc.

### Sliding Window Technique
For subarrays.

```python
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None
    max_sum = sum(arr[:k])
    current_sum = max_sum
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum
```

## Sorting Algorithm Comparison

| Algorithm     | Time Complexity | Space Complexity | Stable | In-Place | When to Use |
|---------------|-----------------|------------------|--------|----------|-------------|
| Bubble Sort  | O(n^2)         | O(1)            | Yes   | Yes     | Small datasets, educational purposes |
| Selection Sort | O(n^2)       | O(1)            | No    | Yes     | Small datasets, when swaps are expensive |
| Insertion Sort | O(n^2) worst, O(n) best | O(1) | Yes | Yes | Nearly sorted data, small datasets |
| Merge Sort   | O(n log n)     | O(n)            | Yes   | No      | Large datasets, stability needed, linked lists |
| Quick Sort   | O(n log n) avg, O(n^2) worst | O(log n) | No | Yes | General-purpose, in-place sorting |
| Heap Sort    | O(n log n)     | O(1)            | No    | Yes     | Worst-case guarantees, priority queues |
| Radix Sort   | O(n * d)       | O(n + k)        | Yes   | No      | Integers with fixed digit lengths |

## Array vs Linked List

Arrays and linked lists are both linear data structures, but they have different strengths:

### Arrays
- **Pros**: O(1) access by index, contiguous memory (cache-friendly), efficient for random access.
- **Cons**: Fixed size (in static arrays), O(n) insertions/deletions in middle, resizing costly.
- **Use when**: Need fast access, size known, or dynamic resizing acceptable (e.g., Python lists).

### Linked Lists
- **Pros**: Dynamic size, O(1) insertions/deletions at ends, no contiguous memory needed.
- **Cons**: O(n) access, extra space for pointers, not cache-friendly.
- **Use when**: Frequent insertions/deletions, unknown size, or as basis for stacks/queues.

In CP, arrays are preferred for their speed unless dynamic operations dominate.

## Memory Considerations and Cache Locality

Arrays store elements contiguously in memory, leading to good cache locality. This means accessing arr[i] loads nearby elements into cache, speeding up sequential access.

- **Cache Misses**: In linked lists, nodes are scattered, causing more misses.
- **Memory Overhead**: Arrays have no per-element overhead; linked lists have pointers (e.g., 8 bytes per node in 64-bit).
- **Fragmentation**: Arrays avoid heap fragmentation.
- **Large Arrays**: Use numpy for efficiency, or consider memory-mapped files for huge data.

Tip: In CP, prefer arrays for performance; use vectors in C++ for dynamic arrays.

## Recursive Code Variations

### Recursive Binary Search
```python
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```
Complexity: O(log n) time, O(log n) space due to recursion.

### Recursive Merge Sort
```python
def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```
Complexity: O(n log n) time, O(n) space.

### Recursive Quick Sort
```python
def quick_sort_recursive(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)
```
Complexity: O(n log n) avg, O(n^2) worst.

## More Competitive Programming Problems

### Median of Two Sorted Arrays
Find median of two sorted arrays.
```python
def find_median_sorted_arrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums2[j-1] > nums1[i]:
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            imax = i - 1
        else:
            if (m + n) % 2 == 1:
                return max(nums1[i-1] if i > 0 else float('-inf'), nums2[j-1] if j > 0 else float('-inf'))
            else:
                max_left = max(nums1[i-1] if i > 0 else float('-inf'), nums2[j-1] if j > 0 else float('-inf'))
                min_right = min(nums1[i] if i < m else float('inf'), nums2[j] if j < n else float('inf'))
                return (max_left + min_right) / 2
```
Complexity: O(log min(m,n)).

### Next Permutation
Generate next lexicographical permutation.
```python
def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i >= 0:
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
```
Complexity: O(n).

### Spiral Matrix
Traverse matrix in spiral order.
```python
def spiral_order(matrix):
    if not matrix:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
```
Complexity: O(n).

### Search in Rotated Sorted Array
Search in rotated sorted array.
```python
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```
Complexity: O(log n).

### Kth Largest Element
Find kth largest in unsorted array.
```python
import heapq
def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]
```
Complexity: O(n log k).

## Common Mistakes and Pitfalls

- **Off-by-one in loops**: For i in range(len(arr)), but accessing arr[i+1].
- **Modifying array during iteration**: Use copy or iterate backwards.
- **Forgetting base cases**: In recursion, handle empty/single element.
- **Ignoring stability**: If order matters, use stable sorts.
- **Large inputs**: Use fast input in CP (sys.stdin.read()).
- **Negative indices**: arr[-1] works in Python, but not in C++.
- **Floating point precision**: Avoid in comparisons.
- **Memory limits**: For large arrays, consider generators or streaming.
- **Edge cases**: Empty, single, all same, all negative, etc.
- **Time limits**: O(n^2) may TLE; optimize to O(n) or O(n log n).

Personal tip: Always test with edge cases before submitting.

## Final Tips

- Master indexing and slicing.
- Know when to use each search/sort.
- Practice LeetCode array problems.
- In CP, read input fast: sys.stdin.read().split()

This now covers arrays extensively. Keep coding!

