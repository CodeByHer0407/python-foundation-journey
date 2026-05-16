def sum_of_elements(lst):
    total = 0
    for ele in lst:
        total += ele
    return total


def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


n = int(input("Enter the size of the list: "))

 
my_grid = create_list(n)
print(f"My Grid: {my_grid}")

print(f"The Sum is: {sum_of_elements(my_grid)}")