class Calculator:
    def __init__(self, num1, num2):
        # Initialize the attributes num1 and num2
        self.num1 = num1
        self.num2 = num2

    def add(self):
        # Return the sum of num1 and num2
        return self.num1 + self.num2

    def subtract(self):
        # Return the result of subtracting num2 from num1
        return self.num1 - self.num2

    def multiply(self, factor):
        # Return the product of num1 and factor
        return self.num1 * factor

    def divide(self, divisor):
        # Return the result of dividing num1 by divisor
        # If divisor is zero, print an error message and return None
        if divisor == 0:
            print("Error: Cannot divide by zero")
            return None
        return self.num1 / divisor
        

## Creating an instance of the Calculator class
calculator = Calculator(10, 5)

print("Addition Result:", calculator.add()) 

print("Subtraction Result:", calculator.subtract())

print("Multiplication Result:", calculator.multiply(3))  

print("Division Result:", calculator.divide(2))

print("Division Result:", calculator.divide(0))  