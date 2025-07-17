# 4.Write a program which contains filter(), map() and reduce() in it. Python application which  contains one list of numbers. List contains the numbers which are accepted from user. Filter  should filter out all such numbers which are even. Map function will calculate its square.  Reduce will return addition of all that numbers. 

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 

# List after filter = [2, 4, 4, 2, 8, 10] 
# List after map = [4, 16, 16, 4, 64, 100] 
# Output of reduce = 204 


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

dataFilter = lambda value : (value % 2 == 0)
dataMapper = lambda value : value ** 2
dataReducer = lambda value1, value2 : value1 + value2

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