# ============================================================
# FIND FLOOR AND CEIL IN A SORTED ARRAY
# ============================================================

"""
Problem Statement:
------------------
Given a sorted array and a target value:

1. Floor:
   Largest element smaller than or equal to target.

2. Ceil:
   Smallest element greater than or equal to target.

Return both floor and ceil values.

If floor or ceil does not exist, return -1.


Example:
---------
Input:
nums = [1, 2, 4, 6, 10]
target = 5

Output:
Floor = 4
Ceil = 6



------------------------------------------------------------
APPROACH
------------------------------------------------------------

Since the array is sorted, Binary Search can be used.


------------------------------------------------------------
FIND FLOOR
------------------------------------------------------------

Goal:
------
Find the largest element <= target.


Logic:
-------
1. If nums[mid] <= target:
      - nums[mid] can be a possible floor
      - store it
      - move RIGHT to find a larger valid floor

2. Otherwise:
      - move LEFT


Example:
---------
nums = [1, 2, 4, 6]
target = 5

Possible floors:
1 -> 2 -> 4

Answer:
4



------------------------------------------------------------
FIND CEIL
------------------------------------------------------------

Goal:
------
Find the smallest element >= target.


Logic:
-------
1. If nums[mid] >= target:
      - nums[mid] can be a possible ceil
      - store it
      - move LEFT to find a smaller valid ceil

2. Otherwise:
      - move RIGHT


Example:
---------
nums = [1, 2, 4, 6]
target = 5

Possible ceils:
6

Answer:
6



------------------------------------------------------------
TIME COMPLEXITY
------------------------------------------------------------

Binary Search runs twice:

O(log n) + O(log n)
= O(log n)



------------------------------------------------------------
SPACE COMPLEXITY
------------------------------------------------------------

O(1)
"""


def find_floor(num, target):
    floor = -1
    size = len(num) - 1
    low, high = 0, size
    while low <= high:
        mid = (low + high) // 2
        if num[mid] <= target:
            floor = num[mid]
            low = mid + 1
        else:
            high = mid - 1
    return floor


def find_ceil(num, target):
    size = len(num) - 1
    ceil = -1
    low, high = 0, size
    while low <= high:
        mid = (low + high) // 2
        if num[mid] >= target:
            ceil = num[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ceil 


def create_lst(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]

n = int(input("Enter the size of the list: "))

num = create_lst(n)
print(f"My Grid: {num}")

target = int(input("Enter any element: "))  
floor = find_floor(num, target)
ceil = find_ceil(num, target)
print(f"The floor of {target} is: {floor}, ceil is {ceil}")