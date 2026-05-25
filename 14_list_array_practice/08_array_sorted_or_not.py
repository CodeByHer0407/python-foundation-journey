# Given an array, return True if it is sorted in
# non-descending order, False otherwise.
#
# Example:
#   Input  : [1, 2, 3]
#   Output : True
#
#   Input  : [1, 3, 2]
#   Output : False
# ============================================================


# ------------------------------------------------------------
# Approach - Linear Scan
# Time: O(n) | Space: O(1)
#
# Compare each adjacent pair. If any element is greater than
# the next one, the array is not sorted.
# ------------------------------------------------------------

def is_sorted(nums):
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            return False
    return True 

def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    digits = create_list(n)
    print(f"My Grid: {digits}")
    
    if (is_sorted(digits)):
        print(f"Yes, {digits} is sorted!")
    else:
        print(f"Sorry, {digits} is not sorted!")