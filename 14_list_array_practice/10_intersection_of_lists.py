def intersection_brute(digit1, digit2):
    size1 = len(digit1)
    size2 = len(digit2)

    ans = list()
    for i in range(size1):
        for j in range(size2):
            if digit1[i] == digit2[j]:
                ans.append(digit1[i])
    ans = list(set(ans))
    return ans


def intersection_optimized(digit1, digit2):
    left, right = 0, 0
    size1 = len(digit1) - 1
    size2 = len(digit2) - 1
 
    digit1.sort()
    digit2.sort()

    ans = list()
    while left <= size1 and right <= size2:
        if digit1[left] == digit2[right]:
            if not ans or ans[-1] != digit1[left]:
                ans.append(digit1[left])
            left += 1
            right += 1
        elif digit1[left] < digit2[right]:
            left += 1
        else:
            right += 1

    return ans


def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    digit1 = create_list(n)
    print(f"List 1: {digit1}")

    m = int(input("Enter the size of the list: "))
    digit2 = create_list(m)
    print(f"List 2: {digit2}")
    print(f"The list with common elements: {intersection_optimized(digit1, digit2)}")