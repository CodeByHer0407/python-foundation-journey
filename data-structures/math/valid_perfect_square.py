def is_perfect_square(num):
    if num < 1:
        return False
    
    i = 1
    while i*i <= num:
        if i*i == num:
            return True
        i += 1
    return False


n = int(input("Enter any number: "))

result = is_perfect_square(n)
if result:
    print(f"Yes, {n} is a perfect square!")
else:
    print(f"Sorry, {n} is not a perfect square!")