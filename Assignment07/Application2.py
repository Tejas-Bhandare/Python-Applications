# Q2. Accept a list of integers from the user and use the map() function to double each value.

# Expected Input:
# Enter list: 1 2 3 4 5

# Expected Output:
# Doubled list: [2, 4, 6, 8, 10]

increment = lambda value : value * 2

def mapX(function_name, data):
    result = []
    for value in data:
        result.append(function_name(value))

    return result

def main():
    print("How many number you want to enter :")
    size = int(input())

    numList = []

    for i in range(size):
        numList.append(int(input()))

    result = mapX(increment, numList)

    print("numList before Map operation :", numList)

    print("numList after Map operation :", result)
    
if __name__ == "__main__":
    main()