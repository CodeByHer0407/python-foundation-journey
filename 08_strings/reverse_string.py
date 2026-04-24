"""
Problem : Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.

Approach 1: Using slicing (Pythonic)
Approach 2: Two-pointer technique (Interview approach)

Time Complexity: O(n)
Space Complexity: O(n)
"""

def reverse_string(s):
    return s[::-1]

def main():
    strs = input("Enter any string of your choice: ")
    result = reverse_string(strs)
    print(f"The reversed string is: {result}")

if __name__ == "__main__":
    main()