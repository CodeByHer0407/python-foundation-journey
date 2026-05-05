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

print(f"There are {countNegatives(grid)} negative numbers in the matrix.")
