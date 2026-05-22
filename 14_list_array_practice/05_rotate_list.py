"""
Array Rotation Utilities
------------------------
This module provides different approaches to rotate a list to the left:
1. rotate_left_by_1       -> Naive single-step rotation
2. rotate_left_by_K       -> Naive rotation by K positions using temp storage
3. rotate_left_by_K_opt   -> Optimized rotation using the reversal algorithm
"""

def rotate_left_by_1(arr):
    """
    Rotate the list to the left by 1 position.
    :param arr: List[int] -> The list of integers
    :return: List[int] -> The rotated list
    """
    val = arr[0]
    size = len(arr)
    for i in range(1, size):
        arr[i-1] = arr[i]
    arr[size-1] = val
    return arr


def rotate_left_by_K(arr, d):
    """
    Rotate the list to the left by d positions (naive approach).
    Uses temporary storage for the first d elements.
    :param arr: List[int]
    :param d: int -> Number of positions to rotate
    :return: List[int]
    """
    size = len(arr)
    if size == 0:
        return arr
    
    d %= size
    temp = arr[:d]
    for i in range(d, size):
        arr[i-d] = arr[i]
    for i in range(d):
        arr[size-d+i] = temp[i]
    return arr


def reverse_arr(arr, start, end):
    """
    Reverse a portion of the list in place between indices start and end (inclusive).
    :param arr: List[int]
    :param start: int -> Starting index
    :param end: int -> Ending index
    :return: List[int]
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def rotate_left_by_K_optimized(arr, d):
    """
    Rotate the list to the left by d positions using the reversal algorithm.
    Steps:
    1. Reverse the first d elements
    2. Reverse the remaining elements
    3. Reverse the entire list
    :param arr: List[int]
    :param d: int -> Number of positions to rotate
    :return: List[int]
    """
    size = len(arr)
    if size == 0:
        return arr
    
    d %= size
    reverse_arr(arr, 0, d-1)
    reverse_arr(arr, d, size-1)
    reverse_arr(arr, 0, size-1)
    return arr


def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    my_grid = create_list(n)
    print(f"My Grid: {my_grid}")

    d = int(input("Enter the number of rotations you want: "))
    print(f"The rotated list: {rotate_left_by_K_optimized(my_grid, d)}")
