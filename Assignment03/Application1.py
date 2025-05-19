# 1.Write a program which accept N numbers from user and store it into List. Return addition of all

# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def addition(numbers):
    sum = 0
    for i in numbers:
       sum = sum + i
    
    return sum

def main():
    print("How many numbers you want to enter")
    value = int(input())

    if value <= 0:
        print("Invalid input : Enter any positive number greater than 0")
        return

    numbers = []

    for i in range(1, value + 1):
        numbers.append(int(input()))
    
    result = addition(numbers)
    print("Addition of all numbers is :", result)
    

if __name__ == "__main__":
    main()