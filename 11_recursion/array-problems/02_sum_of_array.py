def summHead(arr1):
    if len(arr1) == 0:
        return 0
    if len(arr1) == 1:
        return arr1[0]
    return arr1[0] + summHead(arr1[1:])


def summTail(arr1, accumulator=0):
    if len(arr1) == 0:
        return accumulator
    
    accumulator += arr1[0]
    return summTail(arr1[1:], accumulator)


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
    print(f"The sum of the array is: {summHead(my_arr1)}")
    print(f"The sum of the array is: {summTail(my_arr1)}")

if __name__ == "__main__":
    main()