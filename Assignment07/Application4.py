# Q4. Accept a list of numbers and use reduce() (from functools) to find the product of all numbers.

# Expected Input:
# Enter list: 2 3 4

# Expected Output:
# Product: 24

from functools import reduce

product = lambda value1, value2 : value1 * value2

def main():
    print("How many number you want to enter :")
    size = int(input())

    numList = []

    for i in range(size):
        numList.append(int(input()))

    result = reduce(product, numList)

    print("Final result after Reduce operation :", result)

if __name__ == "__main__":
    main()