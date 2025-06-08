# Q1. Arithmetic Operations on Two Numbers
# Write a program to accept two integers from the user and display their:

# • Sum
# • Difference
# • Product
# • Division

# Expected Input:
# Enter first number: 10
# Enter second number: 2

# Expected Output:
# Sum: 12
# Difference: 8
# Product: 20
# Division: 5.0

class Arithmetic:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def addition(self):
        sum = 0
        sum = self.number1 + self.number2
        return sum

    def substraction(self):
        diff = 0
        diff = self.number1 - self.number2
        return diff
    
    def multiplication(self):
        product = 0
        product = self.number1 * self.number2
        return product
    
    def division(self):
        div = 0
        div = self.number1 / self.number2
        return div

def main():
    print("Enter the first number")
    value1 = int(input())

    print("Enter the second number")
    value2 = int(input())

    aobj = Arithmetic(value1, value2)

    result = aobj.addition()
    print("Addition of", value1, "and", value2, "is :", result)

    result = aobj.substraction()
    print("Difference of", value1, "and", value2, "is :", result)

    result = aobj.multiplication()
    print("Product of", value1, "and", value2, "is :", result)

    result = aobj.division()
    print("division of", value1, "and", value2, "is :", result)


if __name__ == "__main__":
    main()