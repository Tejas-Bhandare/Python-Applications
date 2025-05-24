# 4.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from FMR import filterX
from FMR import mapX
from FMR import reduceX

checkEven = lambda value : (value % 2 == 0)
square = lambda value : (value ** 2)
addiiton = lambda value1, value2 : (value1 + value2)

def main():

    numbersList = []
    
    print("How many numbers you want to enter :")
    value = int(input())

    for i in range(value):
        numbersList.append(int(input()))

    print(numbersList)

    filterResult = list(filterX(checkEven, numbersList))
    print("List after filter :", filterResult)

    mapResult = list(mapX(square, filterResult))
    print("List after map :", mapResult)

    reduceResult = reduceX(addiiton, mapResult)
    print("Output of reduce :", reduceResult)

if __name__ == "__main__":
    main()