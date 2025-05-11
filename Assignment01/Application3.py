#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def addition(number1, number2):
    sum = number1 + number2
    return sum
    

def main():
    print("Enter first number")
    value1 = int(input())

    print("Enter second number")
    value2 = int(input())

    result = addition(value1, value2)

    print("Adddition of",value1,"and",value2,"is :",result)

if __name__ == "__main__":
    main()