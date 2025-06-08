# Q7. Area and Perimeter of Rectangle
# Accept the length and width of a rectangle. Calculate and display the area and perimeter.

# Expected Input:
# Enter length: 5
# Enter width: 3

# Expected Output:
# Area: 15
# Perimeter: 16

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length;
        self.breadth = breadth;

    def area(self):
        result = 0
        result = self.length * self.breadth
        return result
    
    def perimeter(self):
        result = 0
        result = (self.length + self.breadth) * 2
        return result
    
def main():
    print("Enter length :")
    value1 = int(input())

    print("Enter breadth :")
    value2 = int(input())

    robj = Rectangle(value1, value2)

    result = robj.area()
    print("Area of rectangle is :",result)

    result = robj.perimeter()
    print("Perimeter of rectangle is :",result)

if __name__ == "__main__":
    main()