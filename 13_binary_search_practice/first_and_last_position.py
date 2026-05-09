# ============================================================
# FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY
# ============================================================

"""
Problem Statement:
------------------
Given a sorted array of integers nums and a target value,
return the starting and ending position of the target.

If the target is not found, return [-1, -1].

Example:
---------
Input:
nums = [5, 7, 7, 8, 8, 10]
target = 8

Output:
[3, 4]


Input:
nums = [5, 7, 7, 8, 8, 10]
target = 6

Output:
[-1, -1]



------------------------------------------------------------
APPROACH
------------------------------------------------------------

Observation:
-------------
Since the array is sorted, Binary Search can be used.

We need:
1. First occurrence of target
2. Last occurrence of target

So we perform Binary Search twice.


------------------------------------------------------------
FINDING FIRST OCCURRENCE
------------------------------------------------------------

1. If nums[mid] == target:
      - store mid as answer
      - continue searching on LEFT side
        because an earlier occurrence may exist

2. If nums[mid] < target:
      - move RIGHT

3. Otherwise:
      - move LEFT


------------------------------------------------------------
FINDING LAST OCCURRENCE
------------------------------------------------------------

1. If nums[mid] == target:
      - store mid as answer
      - continue searching on RIGHT side
        because a later occurrence may exist

2. If nums[mid] < target:
      - move RIGHT

3. Otherwise:
      - move LEFT


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


def searchRange(nums, target):
    def find_first():
        first = -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] ==  target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first
    
    def find_last():
        last = -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return last
    return [find_first(), find_last()]
        


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
print(f"The smallest element greater than {target} is: {searchRange(num, target)}")