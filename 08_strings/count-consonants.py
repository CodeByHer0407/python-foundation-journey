"""
You are given a string s. Your task is to count the number of consonants in the string and return the total count. A consonant is any alphabetic character that is not a vowel (a, e, i, o, u).

Approach:
1. Define a set of vowels.
2. Traverse each character in the string.
3. Check:
   - Character is alphabetic
   - Character is not a vowel
4. Increment count for each consonant.

Time Complexity: O(n)
- Traverse string once.

Space Complexity: O(1)
- Fixed-size vowel set.
"""

def count_consonants(s):
    cnt = 0
    vowels = {"a", "e", "i", "o", "u"}
    for char in s:
        if char.isalpha() and char.lower() not in vowels:
            cnt += 1
    return cnt

def main():
    strs = input("Enter any string of your choice: ")
    print(f"The number of consonants in '{strs}: {count_consonants(strs)}'")


if __name__ == "__main__":
    main()