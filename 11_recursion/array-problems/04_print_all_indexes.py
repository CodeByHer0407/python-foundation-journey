def print_indexes(arr1):
    pass

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


if __name__ == "__main__":
    main()