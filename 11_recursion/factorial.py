import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(100)

def factorial(n):

    if n < 0 :
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter any number: "))
print(f"The factorial of {num} is: {factorial(num)}")