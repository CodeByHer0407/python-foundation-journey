"""
Find Maximum Element in an Array
----------------------------------
Given an unsorted array, find the largest element.

Example: [3, 1, 4, 1, 5, 9, 2, 6] -> 9

Brute Force : O(n log n) | Space: O(n) -- sort and return last element
Optimized   : O(n)       | Space: O(1) -- linear scan

------------------------------------------------------------
Brute Force Approach:
  - Sort a copy of the array in ascending order
  - Return the last element (largest)
  - Uses sorted() instead of .sort() to avoid mutating the original array

Optimized Approach:
  - Initialise max_ele as nums[0]
  - Linear scan from index 1 (index 0 already stored)
  - Update max_ele whenever a larger value is found
  - Return max_ele
------------------------------------------------------------
"""


def find_max_element_optimized(grid):
    max_ele = grid[0]
    for i in range(1, len(grid)):
        if grid[i] > max_ele:
            max_ele = grid[i]
    return max_ele


def find_max_element_brute(grid):
    nums = grid.sort()
    return nums[-1]


def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


n = int(input("Enter the size of the list: "))


my_grid = create_list(n)
print(f"My Grid: {my_grid}")

print(f"The largest element is: {find_max_element_optimized(my_grid)}")