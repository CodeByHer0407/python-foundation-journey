def findMin(nums):
    # Implement your solution here
    pass

def create_lst(n):
    lst = list()
    for i in range(n):
        ele = int(input("Enter any value: "))
        lst.append(ele)       
    return lst


n = int(input("Enter the size of the list: "))


num = create_lst(n)
print(f"My Grid: {num}")

print(f"The smallest element greater than is: {findMin(num)}")