# Q2. Vowel or Consonant Check
# Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not,
# print it's a consonant.

# Expected Input:
# Enter a character: e

# Expected Output:
# 'e' is a vowel.

class Character:
    def __init__(self, char):
        self.character = char

    def isVowel(self):
        charList = ['A', 'a', 'E', 'e', 'I', 'i','O', 'o', 'U', 'u']

        for ch in charList:
            if(ch == self.char):
                return True
            
        return False
        
def main():
    print("Enter the charcter")
    value = input()

    cobj = Character(value)

    result = cobj.isVowel
    
    if(result == True):
        print(value,"is a Vowel")
    else:
        print(value,"is not a Vowel")


if __name__ == "__main__":
    main()