# Q3. Accept a number from the user and print its multiplication table up to 10.

# Expected Input:
# Enter a number: 7

# Expected Output
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

def main():
    print("Enter the number :")
    number = int(input())

    print("Printing table of :", number)
    for i in range(1,11):
        print(number,"*",i,"=", (number * i))

if __name__ == "__main__":
    main()