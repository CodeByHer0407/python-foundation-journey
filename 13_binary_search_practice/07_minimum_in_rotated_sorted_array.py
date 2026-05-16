"""
Minimum in Rotated Sorted Array
---------------------------------
A sorted array rotated at an unknown pivot. Find the minimum element.

Example: [4, 5, 6, 7, 0, 1, 2] -> 0

Brute Force : O(n)     | Space: O(1) -- linear scan
Optimized   : O(log n) | Space: O(1) -- binary search

------------------------------------------------------------
Brute Force Approach:
  - Initialise min_element as nums[0]
  - Linear scan through the array
  - Update min_element whenever a smaller value is found
  - Return min_element

Optimized Approach (Binary Search):
  - Compare nums[mid] with nums[high] each iteration
  - If nums[mid] > nums[high]: right half is unsorted, rotation point lies there -> move low to mid + 1
  - If nums[mid] <= nums[high]: right half is sorted, min is in left half -> shrink high to mid (mid could be the answer)
  - Loop exits when low == high, both pointing at the minimum
------------------------------------------------------------
"""


def findMin_brute(nums):
    # Implement your solution here
    min_element = nums[0]
    for i in range(len(nums)):
        if nums[i] < min_element:
            min_element = nums[i]
    return min_element


def findMin_optimized(nums):
    size = len(nums) - 1
    low, high = 0, size
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] > nums[high]:
             low = mid + 1
        else:
             high = mid 
    return nums[low]

def create_list(n):
        return [int(input(f"Enter value {i}: ")) for i in range(n)]


n = int(input("Enter the size of the list: "))


num = create_list(n)
print(f"My Grid: {num}")

print(f"The smallest element greater than is: {findMin_optimized(num)}")
