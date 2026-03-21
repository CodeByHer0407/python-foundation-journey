"""
You are given two strings s and t. Your task is to determine if string t is a subsequence of string s. A subsequence of a string is a new string that is formed from the original string by deleting some (or no) characters without changing the order of the remaining characters.

Approach:
1. Use two pointers:
   - `left` for string `s`
   - `right` for string `t`

2. Traverse both strings:
   - If characters match → move both pointers
   - If not → move only `right` pointer

3. Continue until:
   - Either all characters of `s` are matched
   - Or `t` is fully traversed

4. Final check:
   - If `left == len(s)` → all characters matched → return True
   - Else → return False
   
Time Complexity: O(m)
- We traverse string t once

Space Complexity: O(1)
- No extra space used
"""

def is_subsequence(s, t):
    left = 0
    right = 0
    n = len(s)
    m = len(t)
    while left < n and right < m:
        if s[left] == t[right]:
            left += 1
            right += 1
        else: 
            right += 1
    if left == n:
        return True
    return False
        

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    result = is_subsequence(str1, str2)
    if result:
        print(f"Yes, '{str2} is a subsequence of '{str1}''")
    else:
        print(f"Sorry, '{str2} is not a subsequence of '{str1}''")