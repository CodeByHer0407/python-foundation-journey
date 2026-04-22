def power_num(base, exp):
    if exp == 0 :
        return 1
    return base * power_num(base, exp-1)

def main():
    base_val = int(input("Enter the base value: "))
    exp_val = int(input("Enter the exponential value: "))
    print(f"Result: {power_num(base_val, exp_val)}")

if __name__ == "__main__":
    main()