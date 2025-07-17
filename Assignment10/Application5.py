# 5.Write a program which contains filter(), map() and reduce() in it. Python application which  contains one list of numbers. List contains the numbers which are accepted from user. Filter  should filter out all prime numbers. Map function will multiply each number by 2. Reduce will  return Maximum number from that numbers. (You can also use normal functions instead of  lambda functions). 

# Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 

# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62] 
# Output of reduce = 62 


def filterX(function_name, data):
    result = []

    for value in data:
        if(function_name(value)):
            result.append(value)
    
    return result

def mapX(function_name, data):
    result = []

    for value in data:
        result.append(function_name(value))

    return result

def reduceX(function_name, data):
    result = 0

    for value in data :
        result = function_name(result, value)

    return result

def dataFilter(value):
    for divisor in range(2, int(value / 2) + 1):
        if(value % divisor == 0):
            return False
    
    return True

dataMapper = lambda value : value * 2

dataReducer = lambda value1, value2 : value1 if value1 >= value2 else value2

def main():
    print("How many number you want to enter :")
    size = int(input())
    numList = []
    
    for i in range(size):
        numList.append(int(input()))

    filterResult = filterX(dataFilter, numList)
    print("List after performing filter :", filterResult)

    mapResult = mapX(dataMapper, filterResult)
    print("List after performing map :", mapResult)

    reduceResult = reduceX(dataReducer, mapResult)
    print("Output of reduce :", reduceResult)

    

if __name__ == "__main__":
    main()