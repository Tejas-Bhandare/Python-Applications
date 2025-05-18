#7. Write a program which accept one number and display below pattern.
# Input : 5
# Output :    1 2 3 4 5
#             1 2 3 4 5
#             1 2 3 4 5
#             1 2 3 4 5
#             1 2 3 4 5

def printPattern(number):
    if number < 0:
        number = -number
    for i in range(number):
        for j in range (1, number + 1):
            print(j, end=" ")
        print("\n")

    

def main():
    print("Enter the number")
    value = int(input())

    printPattern(value)

if __name__ == "__main__":
    main()