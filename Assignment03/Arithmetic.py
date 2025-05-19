def listAddition(numbers):
    sum = 0
    for i in numbers:
       sum = sum + i
    
    return sum

def checkPrime(number):
    if(number <= 1):
        return False
    
    for divisor in range(2, int((number / 2) + 1)):
        if(number % divisor == 0):
            return False
    
    return True

