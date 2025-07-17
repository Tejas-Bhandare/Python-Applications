# 3.Write a program which contains filter(), map() and reduce() in it. Python application which  contains one list of numbers. List contains the numbers which are accepted from user. Filter  should filter out all such numbers which greater than or equal to 70 and less than or equal to  90. Map function will increase each number by 10. Reduce will return product of all that  numbers. 

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 

# List after filter = [76, 89, 86, 90, 70] 
# List after map = [86, 99, 96, 100, 80] 

# Output of reduce = 6538752000 


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
    result = 1

    for value in data :
        result = function_name(result, value)

    return result

dataFilter = lambda value : value >= 70
dataMapper = lambda value : value + 10
dataReducer = lambda value1, value2 : value1 * value2

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