# Q5. Even or Odd Number Check
# Write a program to check whether the entered number is even or odd.

# Expected Input:
# Enter a number: 17

# Expected Output:
# 17 is an odd number.

class Arithmetic:
    def __init__(self, num):
        self.number = num

    def checkEvenOdd(self):
        if self.number % 2 == 0:
            return True
        else:
            return False

def main():
    print("Enter the number")
    value = int(input())

    aobj = Arithmetic(value)

    result = aobj.checkEvenOdd()

    if(result == True):
        print(value,"is an Even number")
    else:
        print(value,"is an odd number")

if __name__ == "__main__":
    main()