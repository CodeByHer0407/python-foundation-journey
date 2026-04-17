## HEAD RECURSION

def count_to_n(n):
    if n == 1 :
        return [1]
    if n <= 0 :
        return
    result = [n]
    return result + count_to_n(n-1)
    

def main():
    num = int(input("Enter any number: "))
    print(count_to_n(num))

if __name__ == "__main__":
    main()