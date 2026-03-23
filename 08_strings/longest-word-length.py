"""
You are given a string s. Your task is to find the length of the longest word in the string. A word is defined as a sequence of characters separated by spaces. Do not use any built-in functions for string manipulation.

Approach:
1. Initialize two variables:
   - cnt → current word length
   - max_cnt → maximum word length

2. Traverse the string character by character:
   - If character is space → reset cnt to 0
   - Else → increment cnt

3. After updating cnt:
   - Update max_cnt if cnt is greater

4. Return max_cnt

Time Complexity: O(n)
- Traverse string once

Space Complexity: O(1)
- No extra space used

"""

def longest_word_length(s):
    cnt = 0
    max_cnt = 0
    for i in range(len(s)):
        if s[i] == " ":
            cnt = 0
        
        else: 
            cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
    return max_cnt


def main():
    strs = input("Enter a string of your choice: ")
    print(f"Length of longest word in '{strs}': {longest_word_length(strs)}")

if __name__ ==  "__main__":
    main()