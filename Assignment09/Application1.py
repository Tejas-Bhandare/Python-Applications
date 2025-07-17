# 1.Create a Python program that starts 3 threads, each printing numbers
# from 1 to 5 with a delay of 1 second. Use threading.Thread.

import threading
import time

def printNumbers(number):
    for i in range(1, number + 1):
        print(threading.current_thread().name,":",i)
        time.sleep(1)

def main():
    value = 5

    Thread1 = threading.Thread(target= printNumbers, args= (value,))
    Thread1.name = "Thread1"

    Thread2 = threading.Thread(target= printNumbers, args= (value,))
    Thread2.name = "Thread2"

    Thread3 = threading.Thread(target= printNumbers, args= (value,))
    Thread3.name = "Thread3"

    Thread1.start()
    Thread2.start()
    Thread3.start()

    Thread1.join()
    Thread2.join()
    Thread3.join()

    print("End of main")

if __name__ == "__main__":
    main()