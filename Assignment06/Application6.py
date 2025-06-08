# Q6. Print Triangle Pattern using Nested Loops

# Expected Output:

# *
# * *
# * * *
# * * * *

class Patterns:
    def __init__(self, num):
        self.number = num

    def displayTrianglePattern(self):
        
        for i in range(1, self.number + 1):
            for j in range(1, i + 1):
                print("*", end="")

            print()

def main():
    print("Enter the number")
    value = int(input())

    pobj = Patterns(value)

    pobj.displayTrianglePattern()

if __name__ == "__main__":
    main()