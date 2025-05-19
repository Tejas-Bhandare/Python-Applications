# 5.Write a program which accept N numbers from user and store it into List. Return addition of all

# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 32 (13 + 5 + 7 +2 + 5)

import Arithmetic

def sumPrimeNumber(numbers):
    sum = 0
    primeNumbers = []
    for num in numbers:
        if(Arithmetic.checkPrime(num)):
            primeNumbers.append(num)

    sum = Arithmetic.listAddition(primeNumbers)
    
    return sum
    

def main():
    print("How many numbers you want to enter :")
    value = int(input())

    if value <= 0:
        print("Invalid input : Enter any positive number greater than 0")
        return

    numbers = []

    for i in range(value):
        numbers.append(int(input()))
    
    result = sumPrimeNumber(numbers)
    print("Addition of prime numbers is :",result)

if __name__ == "__main__":
    main()