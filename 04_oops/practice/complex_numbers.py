class ComplexNumber:
    def __init__(self, real, imaginary):
        # Initialize real and imaginary parts
        self.real = real
        self.imaginary = imaginary
    
    def add(self, other):
        # Add another ComplexNumber object
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def subtract(self, other):
        # Subtract another ComplexNumber object
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def multiply(self, other):
        # Multiply by another ComplexNumber object
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        image_part = (self.real * other.imaginary) + (self.imaginary * other.real)
        return ComplexNumber(real_part, image_part)
    
    
    def __eq__(self, other):
        # Compare two ComplexNumber objects
        return self.real == other.real and self.imaginary == other.imaginary
    
    def __str__(self):
        # Return string representation of the complex number
        if self.imaginary >= 0:
            sign = "+"
        else:
            sign = "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"
    
    
## Creating instances of ComplexNumber class
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
 
# Testing the add method
print("Addition Result:", c1.add(c2))  # Output: "3 + 7i"
 
# Testing the subtract method
print("Subtraction Result:", c1.subtract(c2))  # Output: "1 - 1i"
 
# Testing the multiply method
print("Multiplication Result:", c1.multiply(c2))  # Output: "-10 + 11i"
 
# Testing the equality method
print("Equality Test:", c1 == ComplexNumber(2, 3))  # Output: True
 
# Comparison with Python's built-in complex class
py_c1 = complex(2, 3)
py_c2 = complex(1, 4)
 
print("Python Addition Result:", py_c1 + py_c2)  # Output: (3+7j)
print("Python Subtraction Result:", py_c1 - py_c2)  # Output: (1-1j)
print("Python Multiplication Result:", py_c1 * py_c2)  # Output: (-10+11j)