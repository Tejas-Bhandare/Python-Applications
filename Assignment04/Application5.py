# 5.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).

# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# # Output of reduce = 62

# custom filter function
def filterX(function_name, data):
    result = []
    for value in data:
        ret = function_name(value)
        if(ret == True):
            result.append(value)
        
    return result

# custom map function
def mapX(function_name, data):
    result = []
    for value in data:
        result.append(function_name(value))
    
    return result

# custom reduce functions
def reduceX(function_name, data):
    result = 0
    for value in data:
        result = function_name(result, value)
    
    return result



def checkPrime(value):
    if value < 2:
        return False
    
    if value == 2:
        return True
    
    for i in range(2, int((value / 2) + 1)):
        if(value % i == 0):
            return False
    
    return True
    
increment = lambda value : (value * 2)

def maxNum(value1, value2):
    if(value1 > value2):
        return value1
    else:
        return value2


def main():

    numbersList = []
    
    print("How many numbers you want to enter :")
    value = int(input())

    for i in range(value):
        numbersList.append(int(input()))

    print(numbersList)

    filterResult = list(filterX(checkPrime, numbersList))
    print("List after filter :", filterResult)

    mapResult = list(mapX(increment, filterResult))
    print("List after map :", mapResult)

    reduceResult = reduceX(maxNum, mapResult)
    print("Output of reduce :", reduceResult)

if __name__ == "__main__":
    main()