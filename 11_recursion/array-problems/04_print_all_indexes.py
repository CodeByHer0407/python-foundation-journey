def print_indexes(arr1, val):
    if len(arr1) == 0:
        return []
    result = print_indexes(arr1[1:], val)
    shifted = [i+1 for i in result]
    if arr1[0] == val:
        return [0] + shifted
    else:
        return shifted


def create_array(n):
    arr = []

    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        arr.append(val)
    return arr


def main():
    n = int(input("Enter the size of the array: "))
    my_arr1 = create_array(n)

    print(f"The array is: {my_arr1}")
    element = int(input("Enter the element whose first index you want to search: "))
    print(f"The first index of {element}: {print_indexes(my_arr1, element)}")

if __name__ == "__main__":
    main()