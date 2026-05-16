# ============================================================
# SEARCH INSERT POSITION
# ============================================================

"""
Problem Statement:
------------------
Given a sorted array of distinct integers and a target value,
return the index if the target is found.

If not found, return the index where it would be inserted
to maintain sorted order.

Example:
---------
Input:
nums = [1, 3, 5, 6]
target = 5

Output:
2


Input:
nums = [1, 3, 5, 6]
target = 2

Output:
1


Input:
nums = [1, 3, 5, 6]
target = 7

Output:
4



------------------------------------------------------------
APPROACH
------------------------------------------------------------

Observation:
-------------
The array is already sorted.

We can use Binary Search to efficiently find:
1. The target element
2. OR the correct insertion position


Logic:
-------
1. If nums[mid] >= target:
      - mid can be a valid insert position
      - store it
      - move LEFT to find a smaller valid index

2. Otherwise:
      - move RIGHT


Why initialize:
----------------
insert_index = len(nums)

This handles the case where:
target is greater than all elements.

Example:
---------
nums = [1, 3, 5]
target = 7

Correct insert index:
3


------------------------------------------------------------
TIME COMPLEXITY
------------------------------------------------------------

O(log n)


------------------------------------------------------------
SPACE COMPLEXITY
------------------------------------------------------------

O(1)
"""


# ============================================================
# SEARCH INSERT FUNCTION
# ============================================================

def search_insert(nums, target):
    """
    Returns the index where target exists
    or should be inserted.
    """

    low, high = 0, len(nums) - 1

    # Default insertion position = end of array
    insert_index = len(nums)

    while low <= high:

        mid = (low + high) // 2
        # Possible insert position found
        if nums[mid] >= target:
            insert_index = mid
            high = mid - 1          # Search further on LEFT side
        else:
            # Move RIGHT
            low = mid + 1

    return insert_index




def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]



n = int(input("Enter the size of the list: "))

nums = create_list(n)

print(f"\nSorted Array: {nums}")

target = int(input("\nEnter target element: "))

answer = search_insert(nums, target)

print(f"\nTarget {target} should be placed "
    f"at index: {answer}"
)