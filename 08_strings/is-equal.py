"""
You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.

Approach:
1. Compare lengths of both strings.
2. If lengths differ, return False.
3. Iterate through each character.
4. Return False on first mismatch.
5. If all characters match, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def are_equal_strings(s, t):
    if len(s) == len(t):
        return False
    for i in range(len(s)):
        if s[i] != t[i]:
            return False
        
    return True

def main():
    str1 = input("Enter the first string your choice: ")
    str2 = input("Enter the second string: ")
    result = are_equal_strings(str1, str2)
    if result:
        print(f"Yes, both the strings are equal.")
    else:
        print(f"Sorry, the given strings are not equal.")

if __name__ == "__main__":
    main()