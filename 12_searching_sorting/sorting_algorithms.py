def create_list(n):
    my_lst = []
    for i in range(n):
        ele = int(input(f"Enter element {i+1}: "))
        my_lst.append(ele)
    return my_lst
    

def swap(lst, val1, val2):
    lst[val1], lst[val2] = lst[val2], lst[val1]
    return lst


def bubble_sort(lst1):
    size = len(lst1)
    for passes in range(size-1):
        for j in range(size-1-passes):
            if lst1[j] > lst1[j+1]:
                swap(lst1, j, j+1)
    return lst1


def selection_sort(lst1):
    size = len(lst1)
    for i in range(size-1):
        current_min = i
        for j in range(i+1, size):
            if lst1[j] < lst1[current_min]:
                current_min = j
        swap(lst1, i, current_min)
    return lst1


def insertion_sort(lst1):
    size = len(lst1)
    for current in range(1, size):
        currentCard = lst1[current]
        correctPosition = current - 1
        while correctPosition >= 0:
            if lst1[correctPosition] < currentCard:
                break
            else:
                lst1[correctPosition + 1] = lst1[correctPosition]
                correctPosition -= 1
                lst1[correctPosition + 1] = currentCard
    return lst1


n = int(input("Enter the size of the list: "))
lst1 = create_list(n)
print(f"List: {lst1}")
print(f"Before Sorting: {lst1}")    #11, 25, 12, 34, 50, 22

#result = bubble_sort(lst1)
#result1 = selection_sort(lst1)
result2 = insertion_sort(lst1)
print(f"After Sorting: {result2}")   



