"""
Reverse an Array
------------------
Given an array, return it in reverse order.

Example: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

Brute Force : O(n) | Space: O(n) -- slicing creates a new reversed copy
Optimized   : O(n) | Space: O(1) -- two pointer in-place swap

------------------------------------------------------------
Brute Force Approach:
  - Use slicing lst[::-1] to create a new reversed copy
  - Return the reversed copy
  - Extra O(n) space used for the new array

Optimized Approach (Two Pointer):
  - Use two pointers left=0 and right=len(lst)-1
  - Swap lst[left] and lst[right] moving inward
  - Stop when left >= right
  - Modifies the original array in place — O(1) space
------------------------------------------------------------
"""

def reverse_list_brute(lst):
    return lst[::-1]


def reverse_list_optimized(lst):
    left, right = 0, len(lst) - 1 
    while left <= right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst 


def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


n = int(input("Enter the size of the list: "))

 
my_grid = create_list(n)
print(f"My Grid: {my_grid}")
print(f"The reversed list: {reverse_list_optimized(my_grid)}")