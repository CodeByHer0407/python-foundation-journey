"""
Problem: Check if a number is even.

Approach:
A number is even if it is divisible by 2.
"""

def is_even(n):
    return n%2 == 0
    
num = int(input("Enter any number: "))
result = is_even(num)
if result:
    print(f"Yes, {num} is an even number.")
else:
    print(f"Sorry, {num} is not an even number!")