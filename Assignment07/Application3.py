# Q3. Accept a list of numbers and use filter() to keep only even numbers.

# Expected Input:
# Enter list: 1 2 3 4 5 6

# Expected Output:
# Even numbers: [2, 4, 6]

isEven = lambda value : value % 2 == 0

def filterX(function_name, data):
    result = []
    for value in data:
        if(function_name(value) == True):
            result.append(value)
    
    return result

def main():
    print("How many number you want to enter :")
    size = int(input())

    numList = []

    for i in range(size):
        numList.append(int(input()))

    result = filterX(isEven, numList)

    print("numList before Filter operation :",numList)

    print("numList after Filter operation :", result)

if __name__ == "__main__":
    main()