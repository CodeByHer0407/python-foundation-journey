# ============================================================
# FIND FIRST AND LAST OCCURRENCE OF AN ELEMENT
# ============================================================

"""
Problem Statement:
------------------
Given a sorted array of integers and a target value,
find the first and last occurrence of the target.

If the target does not exist, return -1.


Example:
---------
Input:
nums = [2, 4, 6, 8, 8, 8, 11, 13]
target = 8

Output:
First Occurrence = 3
Last Occurrence = 5



------------------------------------------------------------
BRUTE FORCE APPROACH
------------------------------------------------------------

Approach:
----------
1. Traverse the entire array.
2. When target is found:
      - store first occurrence only once
      - keep updating last occurrence

Time Complexity:
-----------------
O(n)

Space Complexity:
------------------
O(1)



------------------------------------------------------------
OPTIMIZED APPROACH (BINARY SEARCH)
------------------------------------------------------------

Observation:
-------------
The array is sorted.

This allows Binary Search to efficiently find:
1. First occurrence
2. Last occurrence


------------------------------------------------------------
FIND FIRST OCCURRENCE
------------------------------------------------------------

Logic:
-------
1. If nums[mid] == target:
      - store mid as answer
      - continue searching on LEFT side
        because an earlier occurrence may exist

2. If nums[mid] > target:
      - move LEFT

3. Otherwise:
      - move RIGHT



------------------------------------------------------------
FIND LAST OCCURRENCE
------------------------------------------------------------

Logic:
-------
1. If nums[mid] == target:
      - store mid as answer
      - continue searching on RIGHT side
        because a later occurrence may exist

2. If nums[mid] > target:
      - move LEFT

3. Otherwise:
      - move RIGHT



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

def count_occurrences(nums, target):
    first = find_first(nums, target)
    if first == -1:
        return (-1, -1)
    last = find_last(nums, target)
    return (first, last)



def count_occurrences_brute(nums, target):
    cnt = 0
    for i in range(len(nums)):
        if nums[i] == target:
            cnt += 1
    return cnt


def find_first(num, target):
    first = -1
    size = len(num) - 1
    low, high = 0, size
    while low <= high:
        mid = (low + high) // 2
        if num[mid] == target:
            first = mid
            high = mid - 1      # Search further on LEFT side
        elif num[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return first


def find_last(num, target):
    last = -1
    size = len(num) - 1
    low, high = 0, size
    while low <= high:
        mid = (low + high) // 2
        if num[mid] == target:
            last = mid
            low = mid + 1       # Search further on RIGHT side
        elif num[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return last

def find_first_and_last_brute(num, target):
    first = -1
    last = -1
    for i in range(len(num)):
        if num[i] == target:
            if first == -1:
                first = i
            last = i
    return first, last

def create_lst(n):
    lst = list()
    for i in range(n):
        ele = int(input("Enter any value: "))
        lst.append(ele)       
    return lst


n = int(input("Enter the size of the list: "))


num = create_lst(n)
print(f"My Grid: {num}")

target = int(input("Enter any element: "))
#print(f"The first and last position of {target} is: {find_first_and_last_brute(num, target)}")
print(f"The first occurrence of {target} is at index: {find_first(num, target)}")
print(f"The last occurrence of {target} is at index: {find_last(num, target)}")

first, last = count_occurrences(num, target)
if first == -1:
    print(f"{target} does not exist in the list.")
else:
    print(f"{target} occurs {last - first + 1} times.")
