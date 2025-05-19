# 2.Write a program which accept N numbers from user and store it into List. Return Maximum

# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def maximum(numbers):
    maxNum = numbers[0]

    for num in numbers:
       if(num > maxNum):
           maxNum = num
    
    return maxNum

def main():
    print("How many numbers you want to enter")
    value = int(input())

    if value <= 0:
        print("Invalid input : Enter any positive number greater than 0")
        return
        
    numbers = []

    for i in range(1, value + 1):
        numbers.append(int(input()))
    
    result = maximum(numbers)
    print("Maximum of all numbers is :", result)
    

if __name__ == "__main__":
    main()