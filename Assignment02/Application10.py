
# 10. Write a program which accept number from user and return addition of digits in that number.

# Input : 5187934 Output : 37

def sumOfDigits(number):
    if number < 0:
        number = -number

    sum = 0
    
    while(number != 0):
        sum += (number % 10)
        number = int(number / 10)
    
    return sum;
    

def main():
    print("Enter the number")
    value = int(input())

    result = sumOfDigits(value)

    print("Total digits in munber ", value, "is :", result)


if __name__ == "__main__":
    main()