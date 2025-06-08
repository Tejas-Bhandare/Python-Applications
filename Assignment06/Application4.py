# Q4. Accept a number and print its factorial using a for loop.
# Expected Input:
# Enter a number: 5

# Expected Output:
# Factorial of 5 is: 120

def factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i
    
    return factorial

def main():
    print("Enter the number")
    value = int(input())

    result = factorial(value)
    print("Factorial of",value,"is :",result)

if __name__ == "__main__":
    main()