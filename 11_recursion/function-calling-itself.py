def printNum(num):
    print(num)
    if num == 1:
        return 
    printNum(num-1)


printNum(5)

"""
With this excercie 2 things are clear:

1. Functions wait in the memory till they are resolved.

2. When a function finishes execution, then only it comes out of program and gets deleted from our stack.



Recursion is a function calling itself.
Recursion is when the solution of a problem depends on same smaller problem.
eg: 5 -> 4 -> 3 -> 2 -> 1
"""