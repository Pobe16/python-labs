# Write and test a program which has functions to calculate 
# the area of a circle and the area of a rectangle. There 
# should also be a menu which allows the user to select which 
# shape to get the area for, and enter the appropriate 
# parameters (radius or length and breadth)

# Area circle = PI x radius2
# Area rectangle = length x breadth


import math

def circleArea(radius):
    area = math.pi * radius * radius
    return area


def rectangleArea(width, length):
    area = width * length
    return area


def isNumber(value):
    try:
        var = float(value)
        return True
    except (TypeError, ValueError):
        return False


print("Welcome to the area calculating program")
print("---------------------------------------------")
print()
while True:
    # Print out the menu:
    print("Please select a geometrical figure:")
    print("1  Circle")
    print("2  Rectangle")
    print("3  Exit program")

    # Get the user's choice:
    choice = input("> ")

    if choice == '1':
        value = input("Please enter the radius length: ")
        if isNumber(value):
            value = float(value)
            result = circleArea(value)
            print("Circle with radius", value, "have an area equal to", result)
        else:
            print("Value is invalid - try again")
    elif choice == '2':
        width = input("Please enter width of the rectangle: ")
        length = input("Please enter length of the rectangle: ")

        if isNumber(width) and isNumber(length):
            width = float(width)
            length = float(length)
            result = rectangleArea(width, length)
            print("Rectangle", width, "x", length, "has an area of", result)
        else:
            print("Values are invalid - try again")
    elif choice == '3':
        print("Bye...")
        break
    else:
        print("Invalid choice - try again")
    print()
