#Write a program which accept number from user and print that number of “*” on screen.

def display(number):
    for i in range(number):
        print("*", end=" ")
    

def main():
    print("How many times you  want to print * on console")
    value1 = int(input())

    display(value1)

if __name__ == "__main__":
    main()