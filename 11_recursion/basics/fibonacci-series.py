def fibonacci_series(num):
    if num == 1 :
        return 1
    elif num == 0 :
        return 0
    return fibonacci_series(num - 1) + fibonacci_series(num - 2)


def main():
    n = int(input("Enter the number upto which u want to print the fibonacci series: "))
    print("Fibonacci series: ")
    for i in range(n+1):
        print(fibonacci_series(i), end=" ")

if __name__ == "__main__":
    main()