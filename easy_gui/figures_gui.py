# Rewrite your solution to object_classes/figures.py such that dimensions 
# given in the list of shapes are replaced by a series of dialogue boxes 
# (one for each shape) which accept the appropriate dimension (length of 
# side, diameter…). For example dialogue box one may ask for the diameter 
# of circle number one. 
# Now extend your solution such that the user dialogue inputs both the 
# type of shape (circle, square etc.) and the relevant dimension.


import easygui as eg


def main():
    msg = "Choose a figure and enter dimensions to calculate area."
    title = "Area calculation."
    choices = ['Square', 'Circle', 'Triangle', 'Rectangle']

    figure = eg.buttonbox(msg, title, choices)

    if figure == "Square":
        square()
    elif figure == "Circle":
        circle()
    elif figure == "Triangle":
        triangle()
    elif figure == "Rectangle":
        rectangle()
    else:
        print("Goodbye!")


def square():
    msg = "Please enter the length of your square's side."
    title = "Area calculation for a square"
    fields = ["Side"]
    dimensions = eg.multenterbox(msg, title, fields)
    if dimensions != None:
        calculateArea("Square", dimensions)
    else:
        print("Goodbye!")


def circle():
    msg = "Please enter the length of your circle's radius."
    title = "Area calculation for a circle"
    fields = ["Radius"]
    dimensions = eg.multenterbox(msg, title, fields)
    if dimensions != None:
        calculateArea("Circle", dimensions)
    else:
        print("Goodbye!")


def triangle():
    msg = "Please enter the lengths of your triangle's side and corresponding heigt."
    title = "Area calculation for a triangle"
    fields = ["Side", "Height"]
    dimensions = eg.multenterbox(msg, title, fields)
    if dimensions != None:
        calculateArea("Triangle", dimensions)
    else:
        print("Goodbye!")


def rectangle():
    msg = "Please enter the lengths of your rectangle's sides."
    title = "Area calculation for a rectangle"
    fields = ["Side1", "Side2"]
    dimensions = eg.multenterbox(msg, title, fields,)
    if dimensions != None:
        calculateArea("Rectangle", dimensions)
    else:
        print("Goodbye!")

def calculateArea(figure, dimensions):
    print(dimensions)
    try:
        for i in dimensions:
            float(i)

        global area
        if figure == "Square":
            area = float(dimensions[0]) ** 2
        elif figure == "Circle":
            import math
            area = math.pi * float(dimensions[0]) ** 2
        elif figure == "Triangle":
            area = float(dimensions[0]) * float(dimensions[1]) / 2
        elif figure == "Rectangle":
            area = float(dimensions[0]) * float(dimensions[1])
        else:
            print("Goodbye!")

        msg = "Your " + figure + "'s area is equal to " + str(area) + ". Do you want to calculate some more?"
        title = "Area calculated. Great Success!"
        cont = eg.ynbox(msg, title, ['Yes', 'No'])
        if cont:
            main()
        else:
            print("Goodbye!")


    except ValueError:
        print("Just write numbers, please.")
        if figure == "Square":
            square()
        elif figure == "Circle":
            circle()
        elif figure == "Triangle":
            triangle()
        elif figure == "Rectangle":
            rectangle()

main()
