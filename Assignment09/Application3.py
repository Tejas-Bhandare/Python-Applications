# 3.Design python application which creates two threads as evenlist and oddlist. Both the
# threads accept list of integers as parameter. Evenlist thread add all even elements
# from input list and display the addition. Oddlist thread add all odd elements from input
# list and display the addition.

import threading

def sumEvenNumbers(numbers):
    evenNumSum = 0
    for num in numbers:
        if(num % 2 == 0):
            evenNumSum = evenNumSum + num

    print("Addition of even numbers is:", evenNumSum)

def sumOddNumbers(numbers):
    oddNumSum = 0
    for num in numbers:
        if(num % 2 != 0):
            oddNumSum = oddNumSum + num

    print("Addition of odd numbers is:", oddNumSum)

def main():
    print("How many number you want to enter :")
    size = int(input())
    numList = []
    for i in range(size):
        numList.append(int(input()))

    oddList = threading.Thread(target = sumOddNumbers, args= (numList,))
    oddList.setName("odd_Thread")

    evenList = threading.Thread(target = sumEvenNumbers, args= (numList,))
    evenList.setName("even_thread")

    evenList.start()
    oddList.start()

    evenList.join()
    oddList.join()

    print("End of main")

if __name__ == "__main__":
    main()