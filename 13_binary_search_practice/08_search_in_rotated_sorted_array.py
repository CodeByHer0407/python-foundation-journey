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
    



def create_lst(n):
    lst = list()
    for i in range(n):
        ele = int(input("Enter any value: "))
        lst.append(ele)       
    return lst


n = int(input("Enter the size of the list: "))


num = create_lst(n)
print(f"My Grid: {num}")

target = int(input("Enter the target value: "))
print(f"The {target} lies at index: {search_index(num, target)}")