# Given an array of n distinct numbers in the range [0, n],
# return the one number missing from the range.
#
# Example:
#   Input  : [3, 0, 1]
#   Output : 2
#
#   Input  : [0, 1]
#   Output : 2
# ============================================================
 
 
# ------------------------------------------------------------
# Approach 1 - Brute Force (Linear Search with `in`)
# Time: O(n²) | Space: O(1)
#
# For every number in range 0 to max, check if it exists.
# `in` on a list is O(n), making the overall complexity O(n²).
# ------------------------------------------------------------


def find_missing_number_brute1(nums):
    max_ele = max(nums)
    for i in range(0, max_ele+1):
        if i not in nums:
            return i
    return max_ele+1    


# ------------------------------------------------------------
# Approach 2 - Brute Force (Nested Loop)
# Time: O(n²) | Space: O(1)
#
# For every number in range 0 to n, manually scan the array
# to check if it exists. Same complexity as brute1 but
# without using the `in` operator.
# ------------------------------------------------------------

def find_missing_number_brute2(nums):
    size = len(nums)
    for i in range(size+1):
        found = False
        for j in range(size):
            if nums[j] == i:
                found = True
                break
        
        if not found:
            return i 
    return -1



# ------------------------------------------------------------
# Approach 3 - Sum Formula (Optimized)
# Time: O(n) | Space: O(1)
#
# If no number was missing, sum of 0..n = n*(n+1)/2.
# The difference between expected and actual sum is the answer.
# ------------------------------------------------------------
def find_missing_number_optimized(nums):
    n = len(nums)
    expected_sum = n *(n+1) // 2 
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    digits = create_list(n)
    print(f"My Grid: {digits}")

    print(f"The missing number from the '{digits}' is:  {find_missing_number_optimized(digits)}")