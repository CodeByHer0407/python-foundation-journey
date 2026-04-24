"""
You are given two strings s and t. Your task is to determine if string t is an anagram of string s. An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, using all the original characters exactly once.


Approach:
1. Check if lengths of both strings are equal.
   - If not, they cannot be anagrams → return False.

2. Create a dictionary (hash map) to store character frequencies of string `s`.
   - Traverse `s` and count occurrences of each character.

3. Traverse string `t` and update the dictionary:
   - If a character is not found → return False.
   - Decrease its count in the dictionary.
   - If count becomes negative → return False.

4. Final validation:
   - Check if all values in the dictionary are 0.
   - If yes → return True (valid anagram)
   - Else → return False

Time Complexity: O(n)
- One pass for building frequency
- One pass for reducing
- One pass for validation

Space Complexity: O(n)
- Dictionary stores character frequencies
"""


def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    mydict = dict()
    for char in s:
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1

    for char in t:
        if char not in mydict:
            return False
        else:
            mydict[char] -= 1
            if mydict[char] < 0:
                return False
            
    
    for value in mydict.values():
        if value != 0:
            return False
    return True






def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    result = is_anagram(str1, str2)
    if result:
        print(f"yes, '{str2}' is an anagram of '{str1}'")
    else:
        print(f"Sorry, '{str2}' is not an anagram of '{str1}'")

if __name__ == "__main__":
    main()