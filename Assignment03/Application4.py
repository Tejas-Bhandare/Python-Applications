# 4.Write a program which accept N numbers from user and store it into List. Accept one another

# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def getNumberFrequency(numbers, target):
    count = 0
    for i in numbers:
        if( i == target):
            count = count + 1
    
    return count
    

def main():
    print("How many numbers you want to enter :")
    value1 = int(input())

    if value1 <= 0:
        print("Invalid input : Enter any positive number greater than 0")
        return

    numbers = []

    for i in range(value1):
        numbers.append(int(input()))

    print("Enter number to find frequency :")
    value2 = int(input())
    
    result = getNumberFrequency(numbers, value2)
    print("Frequency of", value2,"is :",result)

if __name__ == "__main__":
    main()