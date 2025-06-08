# Q4. Find Largest Among Three Numbers
# Accept three numbers from the user and print the largest using nested if-else statements.

# Expected Input:
# Enter three numbers: 5 9 3
# Expected Output:
# Largest number is 9.

class Arithmetic:
    def __init__(self, data):
        self.data = data
    
    def maximum(self):
        maxNum = self.data[0]
        for value in self.data:
            if value > maxNum:
                maxNum = value
        
        return maxNum

def main():
    print("How many numbers you want to enter ?")
    value = int(input())

    print("Enter the numbers :")

    numbers = []
    for i in range(value):
        numbers.append(int(input()))

    aobj = Arithmetic(numbers)

    result = aobj.maximum()
    print("Maximum number from :",numbers, "is :", result)


if __name__ == "__main__":
    main()