#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.

import Arithmetic

def main():
    print("Enter the first number")
    value1 = int(input())

    print("Enter the second number")
    value2 = int(input())

    ret = Arithmetic.addition(value1, value2)
    print("Addition of", value1,"and",value2,"is :",ret)

    ret = Arithmetic.substraction(value1, value2)
    print("Substratction of", value1,"and",value2,"is :",ret)

    ret = Arithmetic.multiplication(value1, value2)
    print("Multiplication of", value1,"and",value2,"is :",ret)

    ret = Arithmetic.division(value1, value2)
    print("Division of", value1,"and",value2,"is :",ret)


if __name__ == "__main__":
    main()