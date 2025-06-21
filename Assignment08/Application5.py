# 5.Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2.

import threading

def printNumbers(number, flag):
    if(flag == 1):
        for i in range(1, number + 1, 1):
            print(i, end=" ")
        print()

    if(flag == -1):
        for i in range(number + 1, 0, -1):
            print(i, end=" ")
        print()

def main():
    value = 50

    Thread1 = threading.Thread(target= printNumbers, args= (value, 1))
    Thread1.name = "Thread1"

    Thread2 = threading.Thread(target= printNumbers, args= (value, 1))
    Thread1.name = "Thread1"

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("End of main")

if __name__ == "__main__":
    main()