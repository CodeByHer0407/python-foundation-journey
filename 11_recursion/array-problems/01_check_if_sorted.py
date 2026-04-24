def is_sorted(arr1):
    if len(arr1) == 0 or len(arr1) == 1: 
        return True
    
    if arr1[0] > arr1[1]:
        return False
    return is_sorted(arr1[1:])


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
    if is_sorted(my_arr1):
        print(f"Yes, '{my_arr1}' is sorted!")
    else:
        print("Oops, not sorted!")

if __name__ == "__main__":
    main()