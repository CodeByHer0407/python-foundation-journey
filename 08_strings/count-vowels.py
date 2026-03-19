"""
You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count.

Approach:
1. Iterate through each character.
2. Convert character to lowercase.
3. Check if it exists in vowel set.
4. Increment counter accordingly.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def count_vowels(s):
    cnt = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in s:
        if char.lower() in vowels:
            cnt += 1
    return cnt

def main():
    strs = input("Enter any string of your choice: ")
    result = count_vowels(strs)
    print(f"The count of vowels in '{strs}' is: {result}")


if __name__ == "__main__":
    main()