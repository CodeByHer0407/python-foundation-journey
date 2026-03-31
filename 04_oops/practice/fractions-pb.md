# Fraction Class

## Problem Description

### Problem Title: Implement a Fraction Class

```
Design a Python class named Fraction to represent and manipulate mathematical fractions. The class should support basic arithmetic operations and comparisons.

Specifications:

Constructor Method (__init__):

Initialize the fraction with two attributes: numerator and denominator.

Ensure that the denominator is not zero. If zero is provided, raise a ValueError.

Methods:

- add(self, other): Add another Fraction object to the current fraction.

- subtract(self, other): Subtract another Fraction object from the current fraction.

- multiply(self, other): Multiply the current fraction by another Fraction object.

- divide(self, other): Divide the current fraction by another Fraction object. If the other fraction's numerator is zero, raise a ValueError for division by zero.

- __eq__(self, other): Check if two Fraction objects are equal.

- __str__(self): Return a string representation of the fraction in the form numerator/denominator.

- __repr__(self): Return a detailed string representation for debugging.

Simplify Fractions:

Ensure that fractions are always stored in their simplest form. Use a basic method to find the greatest common divisor (GCD) and simplify the fraction. Avoid recursion and imported functions.

Example:

Creating instances of the Fraction class
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
 
# Testing the add method
print(frac1.add(frac2))  # Output: 5/4
 
# Testing the subtract method
print(frac1.subtract(frac2))  # Output: -1/4
 
# Testing the multiply method
print(frac1.multiply(frac2))  # Output: 3/8
 
# Testing the divide method
print(frac1.divide(frac2))  # Output: 2/3
print(frac1.divide(Fraction(0, 1)))  # Output: Error: Cannot divide by zero
 
# Testing equality
print(frac1 == Fraction(2, 4))  # Output: True
 
# Testing string representation
print(frac1)  # Output: 1/2
```