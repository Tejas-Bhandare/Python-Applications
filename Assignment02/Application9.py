# 9. Write a program which accept number from user and return number of digits in that number.

# Input : 5187934 Output : 7

def countDigits(number):
    if number < 0:
        number = -number

    count = 0
    
    while(number != 0):
        count = count + 1
        number = int(number / 10)
    
    return count;
    

def main():
    print("Enter the number")
    value = int(input())

    result = countDigits(value)

    print("Total digits in number ", value, "is :", result)


if __name__ == "__main__":
    main()