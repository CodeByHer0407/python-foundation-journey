"""
You are given an integer n. Your task is to check whether the number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself. Return True if the number is prime, and False otherwise.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def main():
    n = int(input("Enter any number: "))
    result = is_prime(n)
    if result:
        print(f"Yes, {n} is a prime number.")
    else:
        print(f"Sorry, {n} is not a prime number!!")


if __name__ == "__main__":
    main()