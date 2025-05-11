#6.Write a program which accept number from user and check whether that number is positive or negative or zero.

def checkNum(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
    
def main():
    print("Enter number")
    value1 = int(input())

    resutl = checkNum(value1)

    if resutl == 1:
        print("Positive Number")
    elif resutl == -1:
        print("Negative Number")
    else:
        print("Zero")

if __name__ == "__main__":
    main()