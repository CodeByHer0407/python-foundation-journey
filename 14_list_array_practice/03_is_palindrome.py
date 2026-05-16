"""
Check if an Array is a Palindrome
------------------------------------
An array is a palindrome if it reads the same forwards and backwards.

Example: [1, 2, 3, 2, 1] -> True
         [1, 2, 3, 4, 5] -> False

Brute Force : O(n) | Space: O(n) -- reverse and compare
Optimized   : O(n) | Space: O(1) -- two pointer

------------------------------------------------------------
Brute Force Approach:
  - Reverse a copy of the array using slicing lst[::-1]
  - Compare original with reversed copy
  - Return True if equal, False otherwise
  - Extra O(n) space used for the reversed copy

Optimized Approach (Two Pointer):
  - Use two pointers left=0 and right=len(lst)-1
  - Compare lst[left] and lst[right] moving inward
  - If any pair mismatches, return False immediately (early exit)
  - Return True if all pairs match
  - O(1) space — no extra array needed
------------------------------------------------------------
"""



def is_palindrome(lst):
    return lst == lst[::-1]


def is_palindrome_optimized(lst):
    left, right = 0, len(lst) - 1 
    while left <= right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True


def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


n = int(input("Enter the size of the list: "))

 
my_grid = create_list(n)
print(f"My Grid: {my_grid}")

if is_palindrome_optimized(my_grid):
    print(f"{my_grid} is palindrome!")
else:
    print(f"Sorry, not a palindrome!")