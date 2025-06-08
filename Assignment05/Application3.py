
# Q3. Voting Eligibility Checker
# Accept age from the user and check whether the person is eligible to vote. (Age should be
# 18 or above.)

# Expected Input:
# Enter age: 19

# Expected Output:
# Eligible to vote.

class HumanRight:
    def __init__(self, age):
        self.age = age

    def isEligibleToVote(self):
        if self.age >= 18:
            return True
        else:
            return False

def main():
    print("Enter the age")
    value = int(input())

    hobj = HumanRight(value)

    result = hobj.isEligibleToVote()

    if(result == True):
        print("You are Eligible to Vote")
    else:
        print("You are not Eligible to Vote")

if __name__ == "__main__":
    main()