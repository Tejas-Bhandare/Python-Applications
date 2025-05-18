#5.Write a program which accept one number for user and check whether number is prime or not.


def isPrime(number):
    for i in range(2,int((number / 2)) + 1, 1):
            if(number % i == 0):
                return False
    return True

def main():
    print("Enter number")
    value = int(input())

    result = isPrime(value)

    if result == True:
        print(value, "is a prime number")
    else:
        print(value, "not a prime number")     
         

if __name__ == "__main__":
    main()