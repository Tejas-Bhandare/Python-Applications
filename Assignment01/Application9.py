#Write a program which display first 10 even numbers on screen.

def Display():
    for i in range(1,11):
        print(i * 2)
    
def main():
    print("Displaying first 10 even numbers :")
    Display()
    

if __name__ == "__main__":
    main()