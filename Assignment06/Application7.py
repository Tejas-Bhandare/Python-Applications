# Q7. Accept 5 numbers from the user. Find and print the largest number.

# Expected Input:
# Enter 5 numbers: 23 89 12 56 45

# Expected Output:
# Maximum number is: 89

class Mathematics:
    def __init__(self, array):
        self.numbers = array

    def findMaxNum(self):
        maxNum = self.numbers[0]
        for value in self.numbers:
            if(value > maxNum):
                maxNum = value

        return maxNum
    
def main():
    print("How many numbers you want to enter ?:")
    value = int(input())

    numList = []

    for i in range(value):
        numList.append(int(input()))

    mobj = Mathematics(numList)

    result = mobj.findMaxNum()
    print("Maximum number from :", numList,"is :",result)

if __name__ == "__main__":
    main()