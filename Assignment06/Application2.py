# Q2. Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum

# sum of all even numbers from 1 to 100.

# Expected Output:
# Sum of even numbers between 1 to 100 is: 2550

def main():
    sum = 0
    for i in range(1,101):
        if(i % 2 == 0):
            sum = sum + i
    
    print("Sum of even numbers between 1 to 100 is: ",sum)

if __name__ == "__main__":
    main()