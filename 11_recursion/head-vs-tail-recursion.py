"""
Head vs Tail Recursion in Python

- Head Recursion: Work happens after recursive call, Example: factorial (n*f(n-1))
- Tail Recursion: Work happens before recursive call, more optimized in some languages(not Python)

Note: Python does NOT optimize tail recursion
"""


# Head Recursion
def factHead(n):
    if n == 0:
        return 1
    return n * factHead(n - 1)


# Tail Recursion
def factTail(n, accumulator=1):
    if n == 0:
        return accumulator
    return factTail(n - 1, accumulator * n)


print("Head Recursion:", factHead(5))
print("Tail Recursion:", factTail(5))