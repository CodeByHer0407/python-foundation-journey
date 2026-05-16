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
