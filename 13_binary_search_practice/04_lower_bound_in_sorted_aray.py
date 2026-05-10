def lower_bound(num, target):
    lb = len(num)
    low, high = 0, len(num) - 1
    while low <= high :
        mid = (low + high)//2
        if num[mid] >= target:
            lb = mid
            high = mid - 1
        else: 
            low = mid + 1
    return lb

def create_lst(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


n = int(input("Enter the size of the list: "))


num = create_lst(n)
print(f"My Grid: {num}")

target = int(input("Enter any element: "))
idx = lower_bound(num, target)
if idx == len(num):
    print(f"No element >= {target}, lower bound is beyond array.")
else:
    print(f"Lower bound of {target} is at index {idx}, value {num[idx]}")
