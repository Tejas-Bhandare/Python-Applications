# 1.Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.

import threading

def displayEvenNumbers(number):
    for i in range(1, number + 1):
        if(i % 2 == 0):
            print(threading.current_thread().name,":",i)

def displayOddNumbers(number):
    for i in range(1, number + 1):
        if(i % 2 != 0):
            print(threading.current_thread().name,":",i)


def main():
    print("Enter the number")
    number = int(input())

    odd = threading.Thread(target = displayOddNumbers, args= (number,))
    odd.setName("odd_Thread")

    even = threading.Thread(target = displayEvenNumbers, args= (number,))
    even.setName("even_thread")

    even.start()
    odd.start()

if __name__ == "__main__":
    main()