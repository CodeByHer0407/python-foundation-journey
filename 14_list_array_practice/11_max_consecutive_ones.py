"""
Max Consecutive Ones
====================
Given a binary list, find the length of the longest run of consecutive 1s.
 
Approach: Single Pass (Sliding Counter)
-----------------------------------------
- Maintain two counters: current_count (active run) and max_count (best seen).
- Traverse the list once:
    - num[i] == 1  →  extend the current run (current_count += 1)
    - num[i] == 0  →  reset current run (current_count = 0)
- After each step, update max_count = max(max_count, current_count).
- No need for nested loops or extra storage — one pass is sufficient.
 
Key insight: resetting current_count on 0 naturally ends any active run,
and max_count captures the peak before the reset.
 
Time Complexity  : O(n)  — single pass through the list
Space Complexity : O(1)  — only two integer counters used
"""

def find_max_consecutive_ones(num1):
    size = len(num1)
    max_count = 0
    current_count = 0
    for j in range(size):
        if num1[j] == 1 :
            current_count += 1
        else:
            current_count = 0
        max_count = max(max_count, current_count)
    return max_count

            

def create_list(n):
    return [int(input(f"Enter value {i}: ")) for i in range(n)]


if __name__ == "__main__":
    n = int(input("Enter the size of the list: "))
    digit1 = create_list(n)
    print(f"List 1: {digit1}")

    print(f"The maximum number of consecutive ones in '{digit1}': {find_max_consecutive_ones(digit1)}")