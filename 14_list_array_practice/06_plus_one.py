# Given a large integer represented as a digit array,
# increment it by one and return the resulting array.
#
# Example:
#   Input  : [1, 2, 3]
#   Output : [1, 2, 4]
#
#   Input  : [9, 9, 9]
#   Output : [1, 0, 0, 0]
# ============================================================
 
 
# ------------------------------------------------------------
# Approach 1 - Brute Force (Convert to Number)
# Time: O(n) | Space: O(n)
#
# Reconstruct the integer from the digit array, add 1,
# then split back into digits using str().
# Simple but involves type conversions.
# ------------------------------------------------------------

def plus_one_brute(digit):

    #TODO:  combine all the elements of the array
    current_num = 0
    size = len(digit)
    for i in range(size):
        num = 10**(size - 1 - i)
        current_num += num * digit[i]

    #TODO:  ADD 1
    current_num += 1

    #TODO:  separate them into elements 
    res = [int(d) for d in str(current_num)]
    return res



# ------------------------------------------------------------
# Approach 2 - Carry-Based (In-Place)
# Time: O(n) | Space: O(1)
#
# Scan from the rightmost digit. If it's not 9, just increment
# and return. If it is 9, set it to 0 and carry over to the
# next digit. If all digits were 9, prepend a 1.
# ------------------------------------------------------------
def plus_one_optimized(digit):
    size = len(digit) - 1
    for i in range(size, -1, -1):
        if digit[i] != 9:
            digit[i] += 1
            return digit
        else:
            digit[i] = 0
    return [1] + digit
        

def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    digits = create_list(n)
    print(f"My Grid: {digits}")

    print(f"The updated list: {plus_one_optimized(digits)}")