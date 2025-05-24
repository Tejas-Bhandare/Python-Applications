# 2.Write a program which contains one lambda function which accepts two parameters and return its multiplication.

# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

muliplication = lambda no1, no2: no1 * no2

def main():
    print("Enter the first number")
    value1 = int(input())

    print("Enter the second number")
    value2 = int(input())

    result = muliplication(value1, value2)

    print("Multiplication of", value1, value2, "is :", result)

if __name__ == "__main__":
    main()