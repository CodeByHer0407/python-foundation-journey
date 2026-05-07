# BRUTE FORCE APPROACH
def countNegatives(grid):
    cnt = 0
    rows = len(grid)
    columns = len(grid[0])
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] < 0:
                cnt += 1
    return cnt


def countNegates(arr):
    low = 0
    high = len(arr) - 1
    first_negative_index = len(arr)     # assume no negatives
    while low <= high :
        mid = (low + high) // 2
        if arr[mid] < 0 :
            # Found a negative, but keep searching left
            first_negative_index = mid 
            high = mid - 1
        else:
            # Still non-negative, move right
            low = mid + 1
    return len(arr) - first_negative_index

# Binary Search applied to the whole grid
def countNegatives_optimized(grid):
    total = 0
    for row in grid:
        total += countNegates(row)
    return total


def create_matrix(n, m):
    lst = list()
    for i in range(n):
        row = []
        for j in range(m):
            ele = int(input(f"Enter element at [{i}][{j}]: "))
            row.append(ele)
        lst.append(row)
    return lst


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

grid = create_matrix(n, m)
print(f"My Grid: {grid}")

#print(f"There are {countNegatives(grid)} negative numbers in the matrix.")
print(f"Number of negatives in {grid}: {countNegatives_optimized(grid)}")         