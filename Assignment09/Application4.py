# 4.Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.

import threading

def countSmallLetters(str):
    count = 0
    for ch in str:
        if(ch >= 'a' and ch <='z'):
            count+= 1
    print("Thread id:",threading.get_ident(),"Thread name :",threading.current_thread().name)
    print("Count of small letters in :",str, "is :",count)

def countCapitalLetters(str):
    count = 0
    for ch in str:
        if(ch >= 'A' and ch <='Z'):
            count+= 1
    print("Thread id:",threading.get_ident(),"Thread name :",threading.current_thread().name)
    print("Count of capital letters in :",str, "is :",count)

def countDigits(str):
    count = 0
    for ch in str:
        if(ch >= '0' and ch <='9'):
            count+= 1
    print("Thread id:",threading.get_ident(),"Thread name :",threading.current_thread().name)
    print("Count of digits in :",str, "is :",count)

def main():
    print("Enter the string composed of captal, small letters and digits :")

    inputString = input()

    small = threading.Thread(target=countSmallLetters, args= (inputString,))
    small.name = "Small_Letter_Counter"

    capital = threading.Thread(target=countCapitalLetters, args= (inputString,))
    capital.name = "Capital_Letter_Counter"

    digit = threading.Thread(target= countDigits, args= (inputString,))
    digit.name = "Digit_Counter"

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

    print("End of main")

if __name__ == "__main__":
    main()