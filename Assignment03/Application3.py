# 3.Write a program which accept N numbers from user and store it into List. Return Minimum

# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def minimum(numbers):
    minNum = numbers[0]

    for num in numbers:
       if(num < minNum):
           minNum = num
    
    return minNum

def main():
    print("How many numbers you want to enter")
    value = int(input())

    if value <= 0:
        print("Invalid input : Enter any positive number greater than 0")
        return
        
    numbers = []

    for i in range(1, value + 1):
        numbers.append(int(input()))
    
    result = minimum(numbers)
    print("Minimum of all numbers is :", result)
    

if __name__ == "__main__":
    main()