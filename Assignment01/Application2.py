#Write a program which conntains one function named as CheckNum(). Which accept one parameter as number. if number is even it should display "Even number" otherwise display "Odd number" on console.

def checkOddEven(number):
    if number % 2 == 0 :
        return True
    else:
        return False
    

def main():
    print("Enter the number")
    value1 = int(input())

    result = checkOddEven(value1)

    if result == True:
        print(value1,"is Even Number")
    else:
        print(value1,"is Odd number")

if __name__ == "__main__":
    main()