# Q1. Write two lambda functions:
# • One to calculate square of a number
# • Another to calculate cube of a number

# Expected Input:
# Enter a number: 3

# Expected Output:
# Square: 9
# Cube: 27

square = lambda number : number * number

cube = lambda number : number ** 3

def main():
    print("Enter the number")
    num = int(input())

    result = square(num)
    print("Square of", num, "is :", result)

    result = cube(num)
    print("Cube of", num, "is :", result)

if __name__ == "__main__":
    main()