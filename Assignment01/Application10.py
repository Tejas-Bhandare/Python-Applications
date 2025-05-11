#Write a program which accept name from user and display length of its name.

def strLength(name):
    count = 0
    for ch in name:
        count = count + 1
    return count
    

def main():
    print("Enter your name")
    value1 = input()

    result = strLength(value1)

    print("Length of name is ", result)

if __name__ == "__main__":
    main()