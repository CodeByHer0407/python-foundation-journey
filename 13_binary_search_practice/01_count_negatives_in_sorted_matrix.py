# ============================================================
# COUNT NEGATIVE NUMBERS IN A SORTED MATRIX
# ============================================================

"""
Problem Statement:
------------------
Given a matrix where each row is sorted in non-decreasing
order, count the total number of negative numbers.

Example:
---------
Input:
grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]

Output:
8


------------------------------------------------------------
BRUTE FORCE APPROACH
------------------------------------------------------------

Approach:
----------
1. Traverse every element of the matrix.
2. If the element is negative, increase the count.

Time Complexity:
-----------------
O(n * m)

Space Complexity:
------------------
O(1)



------------------------------------------------------------
OPTIMIZED APPROACH (BINARY SEARCH)
------------------------------------------------------------

Observation:
-------------
Each row is already sorted.

This means:
- All negative numbers will appear together at the end.
- We can use Binary Search to find the FIRST negative number.

Approach:
----------
1. For every row:
      - Find the first negative element using Binary Search.
      - Count all elements after that index.

2. Add counts from all rows.

Example:
---------
Row = [4, 2, 1, -1, -3]

First negative index = 3

Negative count:
len(row) - 3 = 2


Time Complexity:
-----------------
For each row:
    O(log m)

For entire matrix:
    O(n log m)

Space Complexity:
------------------
O(1)
"""

# BRUTE FORCE APPROACH
def countNegatives(grid):
    cnt = 0
    rows = len(grid)
    columns = len(grid[0])
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] < 0:
                cnt += 1
    return cnt


def countNegates(arr):
    low = 0
    high = len(arr) - 1
    first_negative_index = len(arr)     # assume no negatives
    while low <= high :
        mid = (low + high) // 2
        if arr[mid] < 0 :
            # Found a negative, but keep searching left
            first_negative_index = mid 
            high = mid - 1
        else:
            # Still non-negative, move right
            low = mid + 1
    return len(arr) - first_negative_index

# Binary Search applied to the whole grid
def countNegatives_optimized(grid):
    total = 0
    for row in grid:
        total += countNegates(row)
    return total


def create_matrix(n, m):
    lst = list()
    for i in range(n):
        row = []
        for j in range(m):
            ele = int(input(f"Enter element at [{i}][{j}]: "))
            row.append(ele)
        lst.append(row)
    return lst


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

grid = create_matrix(n, m)
print(f"My Grid: {grid}")

#print(f"There are {countNegatives(grid)} negative numbers in the matrix.")
print(f"Total number of negative numbers: {countNegatives_optimized(grid)}")
        