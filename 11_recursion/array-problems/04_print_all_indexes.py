def print_indexes(arr1, val):
    if len(arr1) == 0:
        return []
    result = print_indexes(arr1[1:], val)
    shifted = [i+1 for i in result]
    if arr1[0] == val:
        return [0] + shifted
    else:
        return shifted


def print_indexes_modified(arr2, val, index):
    if len(arr2) == index:
        return []
    
    rest = print_indexes_modified(arr2, val, index+1)
    if arr2[index] == val:
        return [index] + rest
    else:
        return rest
    

def printAllIndicesOfAnElementHelper(l1,x, index):
    if len(l1) == index:
        return 
    if l1[index] == x:
        print(index)
    
    printAllIndicesOfAnElementHelper(l1, x, index+1)


def printAllIndicesOfAnElement(l1, x):
    #Helper function
    printAllIndicesOfAnElementHelper(l1,x, 0)
 
    
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
    element = int(input("Enter the element to search: "))

    print(f"\nUsing print_indexes:          {print_indexes(my_arr1, element)}")
    print(f"Using print_indexes_modified: {print_indexes_modified(my_arr1, element, 0)}")
    print(f"Using printAllIndices (print): ", end="")
    printAllIndicesOfAnElement(my_arr1, element)

if __name__ == "__main__":
    main()