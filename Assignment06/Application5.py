# Q5. Accept a number from the user and check whether it is prime or not.

# Expected Input:
# Enter a number: 11

# Expected Output:
# 11 is a prime number.

class Arithmetic:
    def __init__(self, num):
        self.number = num

    def checkPrime(self):
        if (self.number <= 1):
            return False
        
        if (self.number == 2):
            return True
        
        for i in range(2, int((self.number / 2) + 1)):
            if(self.number % i == 0):
                return False
        
        return True

def main():
    print("Enter the number")
    value = int(input())

    aobj = Arithmetic(value)

    result = aobj.checkPrime()

    if(result == True):
        print(value,"is a Prime number")
    else:
        print(value,"is not a Prime number")

if __name__ == "__main__":
    main()