"""
You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s. A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for string operations and do not use recursion.
"""
def is_substring(s, t):
    pass


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
result = is_substring(str1, str2)
if result:
    print(f"Yes, '{str2}' is a substring of '{str1}'")
else:
    print(f"Sorry, '{str2}' is not a substring of '{str1}'")