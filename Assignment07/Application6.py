# Q6. Write a function that accepts a list of integers and returns a list of prime numbers using filter().

# Expected Input:
# Enter list: 10 11 12 13 14 15 16 17

# Expected Output:
# Prime numbers: [11, 13, 17]

import math

def isPrime(number):
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True

def main():
    print("How many number you want to enter :")
    size = int(input())

    numList = []

    for i in range(size):
        numList.append(int(input()))

    result = list(filter(isPrime, numList))

    print("numList before Filter operation :",numList)
    print("Final result after Filter operation :", result)

if __name__ == "__main__":
    main()