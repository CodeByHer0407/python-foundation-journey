"""
You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string.

Approach:
1. Use a set to track seen characters.
2. Traverse the string character by character.
3. If character is not in the set:
   - Add it to the set
   - Append it to result string
4. Return the result string.

Time Complexity: O(n)
- Single traversal with constant time lookup.

Space Complexity: O(n)
- Extra space for set and result string.

"""

def remove_duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char

    return result

def main():
    strs = input("Enter any string of your choice: ")
    result = remove_duplicates(strs)
    print(f"The updated string after removing duplicates: {result}")

if __name__ == "__main__":
    main()