class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()  # Simplify the fraction upon initialization
    

    def _find_gcd(self, a, b):
        # Your code to find GCD goes here
        a = abs(a)
        b = abs(b)

        while b != 0:
            a, b = b, a%b
        return a
    

    def _simplify(self):
        # Your code to simplify the fraction goes here
        gcd = self._find_gcd(self.numerator, self.denominator)

        self.numerator //= gcd
        self.denominator //= gcd

        # Ensure denominator is always positive
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    

    def add(self, other):
        # Your code to add fractions goes here
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)

    

    def subtract(self, other):
        # Your code to subtract fractions goes here
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)
        else:
            return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)

    

    def multiply(self, other):
        # Your code to multiply fractions goes here
        return Fraction(self.numerator * other.numerator , self.denominator * other.denominator)

    

    def divide(self, other):
        # Your code to divide fractions goes here
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero")
        return Fraction(self.numerator * other.denominator , self.denominator * other.numerator)

    

    def __eq__(self, other):
        # Your code to compare fractions goes here
        return (
            isinstance(other, Fraction) and
            self.numerator == other.numerator and
            self.denominator == other.denominator
        )

    def __str__(self):
        # Your code for string representation goes here
        return f"{self.numerator}/{self.denominator}"
    

    def __repr__(self):
        # Your code for detailed representation goes here
        return f"Fraction({self.numerator}, {self.denominator})"


## Creating instances of the Fraction class
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