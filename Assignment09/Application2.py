# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display
# addition of even factors of given number and oddfactor will display addition of odd
# factors of given number. After execution of both the thread gets completed main
# thread should display message as “exit from main”.

import threading

def sumEvenFactors(number):
    factorsSum = 0
    for i in range(1, number + 1):
        if(i % 2 == 0 and number % i == 0):
            factorsSum = factorsSum + i

    print("Addition of even factors is:", factorsSum)

def sumOddNumbers(number):
    factorsSum = 0
    for i in range(1, number + 1):
        if(i % 2 != 0 and number % i == 0):
            factorsSum = factorsSum + i

    print("Addition of odd factors is:", factorsSum)

def main():
    print("Enter the number")
    number = int(input())

    oddfactor = threading.Thread(target = sumOddNumbers, args= (number,))
    oddfactor.setName("odd_Thread")

    evenFactor = threading.Thread(target = sumEvenFactors, args= (number,))
    evenFactor.setName("even_thread")

    evenFactor.start()
    oddfactor.start()

    evenFactor.join()
    oddfactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()