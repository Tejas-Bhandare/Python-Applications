# 1.Write a program which contains one lambda function which accepts one parameter and return  power of two. 

# Input : 4 Output : 16 
# Input : 6 Output : 64 

square = lambda number : number ** 2

def main():
    print("Enter the number :")
    value = int(input())

    result = square(value)
    print("Square of", value, "is :", result)

if __name__ == "__main__":
    main()