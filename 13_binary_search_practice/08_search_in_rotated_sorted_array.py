"""
Search in Rotated Sorted Array
---------------------------------
A sorted array rotated at an unknown pivot. Search for a target element.

Example: [4, 5, 6, 7, 0, 1, 2], target = 0 -> index 4
         [4, 5, 6, 7, 0, 1, 2], target = 3 -> -1

Brute Force  : O(n)     | Space: O(1) -- linear scan
Optimized    : O(log n) | Space: O(1) -- binary search (no duplicates)
With Duplicates: O(n) worst case | Space: O(1) -- binary search (with duplicates)

------------------------------------------------------------
Brute Force Approach:
  - Linear scan through the array
  - Return index if target found, else return -1

Optimized Approach (No Duplicates):
  - One half is always sorted in a rotated sorted array
  - Check which half is sorted using nums[low] <= nums[mid]
  - If left half is sorted: check if target lies in [nums[low], nums[mid])
      -> yes: shrink to left half | no: move to right half
  - If right half is sorted: check if target lies in (nums[mid], nums[high]]
      -> yes: shrink to right half | no: move to left half
  - Return -1 if not found

With Duplicates:
  - Duplicates break the "one half is always sorted" guarantee
  - Edge case: nums[low] == nums[mid] == nums[high] -> can't determine sorted half
      -> shrink both pointers (low++, high--) and continue
  - Otherwise same logic as optimized approach
  - Worst case O(n) when all elements are duplicates e.g. [1,1,1,1,1]
------------------------------------------------------------
"""

def search_index_brute(num, target):
    # linear search
    for i in range(len(num)):
        if num[i] == target:
            return i
    return -1


def search_index(num, target):
    size = len(num) - 1
    low, high = 0, size
    while low <= high:
        mid = (low + high) // 2

        # If target found at mid, return index
        if num[mid] == target:
            return mid
        
        # Check if left half is sorted
        if num[low] <= num[mid]:
            # If target lies in left half
            if num[low] <= target < num[mid]:
                high = mid - 1 
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if num[mid] < target <= num[high]:
                low = mid + 1
            else:
                high = mid - 1
    # Target not found
    return -1



def search_index_duplicates(num, target):
    size = len(num) - 1
    low, high = 0, size
    while low <= high:
        mid = (low + high) // 2
    
        # If target found at mid, return index
        if num[mid] ==  target:
            return True
    
        if num[low] == num[mid] == num[high]:
            low = low + 1
            high = high - 1
            continue

        # Check if left half is sorted
        if num[low] <= num[mid]:
            if num[low] <= target <= num[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Check if right half is sorted
        elif num[mid] <= num[high]:
            if num[mid] <= target <= num[high]:
                low = mid + 1 
            else:
                high = mid - 1
    return False
    



def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


n = int(input("Enter the size of the list: "))


num = create_list(n)
print(f"My Grid: {num}")

target = int(input("Enter the target value: "))
print(f"The {target} lies at index: {search_index(num, target)}")