#Write a program which accept one number from user and return its factorial.

def factorial(number):
    if number < 0:
        number = -number

    factorial = 1
    
    for i in range(1, number + 1):
        factorial = factorial * i
    
    return factorial;
    

def main():
    print("Enter the number")
    value = int(input())

    result = factorial(value)

    print("Factorial of", value, "is :", result)


if __name__ == "__main__":
    main()