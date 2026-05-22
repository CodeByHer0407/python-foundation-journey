def plus_one_brute(digit):

    #TODO:  combine all the elements of the array
    current_num = 0
    size = len(digit)
    for i in range(size):
        num = 10**(size - 1 - i)
        current_num += num * digit[i]

    #TODO:  ADD 1
    current_num += 1

    #TODO:  separate them into elements 
    res = [int(d) for d in str(current_num)]
    return res


def plus_one_optimized(digit):
    size = len(digit) - 1
    for i in range(size, -1, -1):
        if digit[i] != 9:
            digit[i] += 1
            return digit
        else:
            digit[i] = 0
    return [1] + digit
        

def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    digits = create_list(n)
    print(f"My Grid: {digits}")

    print(f"The updated list: {plus_one_optimized(digits)}")