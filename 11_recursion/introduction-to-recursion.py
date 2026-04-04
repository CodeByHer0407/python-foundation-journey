def printNumFive(num):
    print(num)
    printNumFour(num-1)

def printNumFour(num):
    print(num)
    printNumThree(num-1)

def printNumThree(num):
    print(num)
    printNumTwo(num-1)

def printNumTwo(num):
    print(num)
    printNumOne(num-1)

def printNumOne(num):
    print(num)
    
printNumFive(5)
""" printNumFive(4)
printNumFive(3)
printNumFive(2)
printNumFive(1) """

# To just use above function and a single print statement to print out numbers from 5 to 1


"""
KEY POINTS LEARNT SO FAR:

1. We can call a function from inside of another function.

2. A function stays in the memory until it gets fully executed.

3. We are doing almost similar work in each of the above fucntions.
"""