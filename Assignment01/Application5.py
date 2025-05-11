#5.Write a program which display 10 to 1 on screen.

def display(number):
    for i in range(number, 0, -1):
        print(i, end=" ")
    
def main():
    print("Enter number")
    value1 = int(input())

    display(value1)

if __name__ == "__main__":
    main()