def first_index(arr1, val, index):
    if index >= len(arr1):
        return -1
    if val == arr1[index]:
        return index
    result = first_index(arr1, val, index + 1)
    return result


def last_index(arr1, val, index):
    if index < 0 :
        return -1
    if arr1[index] == val:
        return index
    result = last_index(arr1, val, index-1)
    return result


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
    print(f"The first index of {element}: {first_index(my_arr1, element, 0)}")

    print(f"The last index of {element}: {last_index(my_arr1, element, len(my_arr1)-1)}")
if __name__ == "__main__":
    main()