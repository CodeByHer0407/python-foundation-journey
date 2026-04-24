
def sum_digits(num):
    if num == 0 :
        return 0
    
    lastDigit = num % 10
    
    return lastDigit + sum_digits(num//10)
    

def main():
    n = int(input("Enter any number: "))
    print(f"The sum of digits of '{n}': {sum_digits(n)}")

if __name__ == "__main__":
    main()