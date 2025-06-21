# Q5. Write a function that accepts a string and checks whether it is a palindrome.

# Expected Input:
# Enter a string: radar


# Expected Output:
# radar is a palindrome.

class StringX:
    def __init__(self, str):
        self.str = str.lower()

    def isPalindrome(self):
        left = 0
        right = len(self.str) - 1

        while(left < right):
            if(self.str[left] != self.str[right]):
                return False
            
            left = left + 1;
            right = right - 1

        return True

def main():
    print("Enter the string")
    value = input()

    sobj = StringX(value)

    result = sobj.isPalindrome()

    if(result == True):
        print(value,"is a Palindrome")
    else:
        print(value,"not a Palindrome")

if __name__ == "__main__":
    main()