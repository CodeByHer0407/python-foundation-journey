def first_index(arr1, val):
    if len(arr1) == 0:
        return -1
    if val == arr1[0]:
        return 0
    result = first_index(arr1[1:], val)
    if result == -1 :
        return -1
    return 1 + result


def last_index(arr1, val):
    if len(arr1) == 0 :
        return -1
    result = last_index(arr1[1:], val)
    if result != -1 :
        return 1 + result
    if val == arr1[0]:
        return 0
    return -1


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
    print(f"The first index of {element}: {first_index(my_arr1, element)}")

    print(f"The last index of {element}: {last_index(my_arr1, element)}")
if __name__ == "__main__":
    main()