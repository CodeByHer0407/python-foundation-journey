# Given an array, move all zeroes to the end
# while keeping the relative order of non-zero elements.
#
# Example:
#   Input  : [0, 1, 0, 3, 2]
#   Output : [1, 3, 2, 0, 0]
# ============================================================



# ------------------------------------------------------------
# Approach 1 - Brute Force
# Time: O(n) | Space: O(n)
#
# Just collect non-zeroes and zeroes into separate lists,
# then join them. Clean and readable but uses extra space.
# ------------------------------------------------------------

def move_zeroes_brute(nums):
    temp = list()
    ans = list()
    for i in range(len(nums)):
        if nums[i] == 0:
            temp.append(0)
        else:
            ans.append(nums[i])
    return ans + temp




# Approach 2 - Two Pointers (In-Place)
# Time: O(n) | Space: O(1)
# j tracks the first zero, i scans for non-zeroes and swaps into j
def move_zeroes_optimized(nums):
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break

    if j == -1:
        return nums
        
    for i in range(j+1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums
        



def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    digits = create_list(n)
    print(f"My Grid: {digits}")

    print(f"The updated list after moving all the zeroes to the end: {move_zeroes_optimized(digits)}")