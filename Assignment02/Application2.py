#Write a program which accept one number and display below pattern.
# Input : 5
# Output :    * * * * *
#             * * * * *
#             * * * * *
#             * * * * *
#             * * * * *


def printPattern(number):
    if number < 0:
        number = -number
    for i in range(number):
        for j in range (number):
            print("*", end=" ")
        print("\n")

    

def main():
    print("Enter the number")
    value = int(input())

    printPattern(value)

if __name__ == "__main__":
    main()