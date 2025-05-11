#4.Write a program which display 5 times Marvellous on screen.

def display(number):
    for i in range(number):
        print("Marvellous")
    

def main():
    print("Enter number")
    print("How many times you  want to print 'Marvellous' on console")
    value1 = int(input())

    display(value1)

if __name__ == "__main__":
    main()