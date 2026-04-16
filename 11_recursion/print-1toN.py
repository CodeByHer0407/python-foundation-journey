## HEAD RECURSION

def count_to_n(n):
    if n <= 0 :
        return []
    if n == 1 :
        return [1]
    new = count_to_n(n-1)
    new.append(n)
    return new

num = int(input("Enter any number: "))
print(count_to_n(num))