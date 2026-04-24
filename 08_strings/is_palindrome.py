"""
You are given a string s. Your task is to check if the string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.

Approach:
1. Preprocess the string:
   - Convert all characters to lowercase
   - Remove non-alphanumeric characters (ignore spaces & punctuation)
2. Use two-pointer technique:
   - Initialize two pointers: start (0) and end (len(s)-1)
   - Compare characters at both ends
   - If mismatch → return False
   - Move pointers inward
3. If all characters match → return True

Time Complexity: O(n)
- One pass for cleaning + one pass for comparison

Space Complexity: O(n)
- Extra space used for cleaned string
"""

def is_palindrome(s): 
    start = 0
    end = len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


def clean_string(s):
    cleaned = ""
    for char in s:
        if char.isalnum():      # Keeps only letters and numbers
            cleaned += char.lower()
    return cleaned

def main():
    strs = input("Enter any string of your choice: ")
    updated_s = clean_string(strs)

    print(updated_s)


    result = is_palindrome(updated_s)
    if result:
        print(f"Yes, '{strs}' is palindrome.")
    else:
        print(f"Sorry, '{strs}' is not palindrome.")


if __name__ == "__main__":
    main()


# Note:
# This can be further optimized to O(1) space by avoiding creation of a new string
# and skipping invalid characters during pointer traversal.