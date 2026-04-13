def sum_of_natural_numbers(num):
    if num == 0:
        return 0
    return num + sum_of_natural_numbers(num-1)

def main():
    n = int(input("Enter any number: "))
    sum = sum_of_natural_numbers(n)
    print(f"The sum of first {n} numbers: {sum}")

if __name__ == "__main__":
    main()