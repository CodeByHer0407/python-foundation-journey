
"""
Problem Statement:
------------------
Given a sorted list of characters and a target character,
return the smallest character that is lexicographically
greater than the target.

If no such character exists, return the first character
of the list.

Example:
---------
Input:
letters = ['c', 'f', 'j']
target = 'c'

Output:
'f'


Approach:
----------
1. Use Binary Search because the list is sorted.

2. Store the first element as the default answer.
   This helps handle the circular condition.

3. If letters[mid] > target:
      - store it as a possible answer
      - move LEFT to find a smaller valid character

4. Otherwise:
      - move RIGHT

5. Return the stored result.


Time Complexity:
-----------------
O(log n)

Space Complexity:
------------------
O(1)
"""



def next_greatest_letter(letters, target):
    result = letters[0]
    low, high = 0, len(letters) - 1
    while low <= high :
        mid = (low + high) // 2
        if letters[mid] > target :
            result = letters[mid]
            high = mid - 1
        else:
            low = mid + 1
    return result


def create_lst(n):
    lst = list()
    for i in range(n):
        ele = input("Enter any value: ")
        lst.append(ele)       
    return lst


n = int(input("Enter the size of the list: "))


grid = create_lst(n)
print(f"My Grid: {grid}")

target = input("Enter any element: ")
print(f"Next greatest letter after {target} is: {next_greatest_letter(grid, target)}")

   