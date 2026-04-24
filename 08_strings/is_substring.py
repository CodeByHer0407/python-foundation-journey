"""
You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s. A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for string operations and do not use recursion.


Approach:
1. Handle edge cases:
   - If length of `t` is greater than `s` → return False
   - If `t` is empty → return True

2. Iterate through all possible starting indices in `s`:
   - Loop from i = 0 to (len(s) - len(t))

3. For each starting index `i`, try to match string `t`:
   - Compare characters one by one:
     s[i + j] with t[j]
   - If mismatch occurs → break and move to next index

4. If all characters match for any index:
   - Return True

5. If no match is found after checking all positions:
   - Return False


Time Complexity: O(n * m)
- n = length of s
- m = length of t
- For each position in s, we compare up to m characters

Space Complexity: O(1)
- No extra space used
"""
def is_substring(s, t):
    if len(t) > len(s):
        return False

    if len(t) == 0:
        return True
    
    for i in range(len(s)-len(t)+1):
        for j in range(len(t)):
            if s[i+j] != t[j]:
                break
        else:
            return True
    return False
    
      

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    result = is_substring(str1, str2)
    if result:
        print(f"Yes, '{str2}' is a substring of '{str1}'")
    else:
        print(f"Sorry, '{str2}' is not a substring of '{str1}'")

if __name__ ==  "__main__":
    main()