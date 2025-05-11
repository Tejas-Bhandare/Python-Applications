#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def isDivisibleBy5(number):
    if number % 5 == 0:
        return True
    else:
        return False
    
def main():
    print("Enter number")
    value1 = int(input())

    resutl = isDivisibleBy5(value1)

    if resutl == True:
        print(value1, "is divisible by 5")
    else:
        print(value1, "is not divisible by 5")

if __name__ == "__main__":
    main()