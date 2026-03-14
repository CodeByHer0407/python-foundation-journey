def sum_of_even_numbers(n):
    total_sum = 0
    current_even_num = 2
    for i in range(n):
        total_sum += current_even_num
        current_even_num += 2
    return total_sum

num = int(input("Enter any number: "))
print(f"Sum of first {num} even numbers: {sum_of_even_numbers(num)}")