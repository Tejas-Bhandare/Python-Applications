# 3.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 653875200

from FMR import filterX
from FMR import mapX
from FMR import reduceX

select = lambda value : (value >= 70 and value <= 90)
increment = lambda value : (value + 10)
product = lambda value1, value2 : (value1 * value2)

def main():

    numbersList = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

    print(numbersList)

    filterResult = list(filterX(select, numbersList))
    print("List after filter :", filterResult)

    mapResult = list(mapX(increment, filterResult))
    print("List after map :", mapResult)

    reduceResult = reduceX(product, mapResult)
    print("Output of reduce :", reduceResult)

if __name__ == "__main__":
    main()