"""
You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined as a sequence of characters separated by spaces.

Approach:
1. Initialize a counter to 0.
2. Traverse the string character by character.
3. A word starts when:
   - The current character is NOT a space, AND
   - Either it is the first character OR the previous character is a space.
4. Increment the counter whenever a new word start is found.
5. Return the final count.

Time Complexity: O(n)
- We traverse the string once.

Space Complexity: O(1)
- No extra space is used (only a counter variable).

"""
def count_words(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] != " " and(i == 0 or s[i-1] == ' '):
            cnt += 1
    return cnt


def main():
    strs = input("Enter any string of your choice: ")
    print(f"Word Count in '{strs}': {count_words(strs)}")

if __name__ == "__main__":
    main()