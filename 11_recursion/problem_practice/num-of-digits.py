def number_of_digits(num):
    if num >= 1 and num <= 9 :
        return 1
    elif num == 0:
        return 1
    
    smallNumber = int(num/10)
    smallAnswer = number_of_digits(smallNumber)

    return 1 + smallAnswer
    

def main():
    n = int(input("Enter any number: "))
    print(f"The number of digits in {n}: {number_of_digits(n)}")


if __name__ == "__main__":
    main()