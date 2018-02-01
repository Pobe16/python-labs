# Write a program which includes the Square and 
# Circle classes from the lecture, and also new 
# classes Rectangle and Triangle. Your program 
# should create a list of different shapes (i.e. 
# square, circle, rectangle and triangle), 
# similar to the example in the lecture and use 
# the for loop code from the lecture example to 
# find their areas.

# Area of a rectangle = length * breadth
# Area of a triangle = 0.5 * base * height


class Square:
    def __init__(self, side):
        self.side = side

    def calculateArea(self):
        return self.side * self.side

class Circle:
    # initialisation method
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        import math
        return math.pi*(self.radius**2)

class Triangle:
    # initialisation method
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculateArea(self):
        return 0.5 * self.base * self.height

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculateArea(self):
        return self.length * self.breadth


list = [Circle(5),Circle(7),Square(11),Square(12), Rectangle(5,8), Rectangle(6.5, 3.333), Triangle(3, 10), Triangle(12, 7.25)]

for shape in list:
     print("The area is: ", shape.calculateArea())