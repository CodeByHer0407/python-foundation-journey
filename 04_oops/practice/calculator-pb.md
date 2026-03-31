# Calculator

## Create a Python class named Calculator with the following specifications:

```
Constructor Method (__init__): Initializes two attributes, num1 and num2.

Method add: Takes no arguments and returns the sum of num1 and num2.

Method subtract: Takes no arguments and returns the result of subtracting num2 from num1.

Method multiply: Takes a single argument factor and returns the product of num1 and factor.

Method divide: Takes a single argument divisor and returns the result of dividing num1 by divisor. If divisor is zero, print an error message and return None.

Example:

Creating an instance of the Calculator class
calculator = Calculator(10, 5)
 
# Testing the add method
print("Addition Result:", calculator.add())  # Output: 15
 
# Testing the subtract method
print("Subtraction Result:", calculator.subtract())  # Output: 5
 
# Testing the multiply method
print("Multiplication Result:", calculator.multiply(3))  # Output: 30
 
# Testing the divide method
print("Division Result:", calculator.divide(2))  # Output: 5.0
print("Division Result:", calculator.divide(0))  # Output: Error: Cannot divide by zero
```