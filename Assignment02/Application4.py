#4.Write a program which accept one number form user and return addition of its factors.

def factorsAddition(number):
    if number < 0:
        number = -number

    factorsSum = 0

    if (number % 2 == 0):
        factorsSum = 0
        for i in range(1,int((number / 2)) + 1, 1):
            if(number % i == 0.0):
                factorsSum = factorsSum + i
                print(i)
    else:
        factorsSum = 0
        for i in range(1,int((number / 2) + 1), 2):
            if(number % i == 0):
                factorsSum = factorsSum + i

    return factorsSum
    
def main():
    print("Enter number")

    value = int(input())

    result = factorsAddition(value)
    print("Addition of all factors of", value,"is :", result)

if __name__ == "__main__":
    main()