# Modify the number guess program in writingfunctions2.py so that it checks for integer input.

import random

minValue = 1
maxValue = 49
target = random.randint(minValue, maxValue)


def check_integer(a):
    try:
        val = int(a)
        return True
    except (TypeError, ValueError):
        return False


def check_bigger_smaller(value):
    if value < minValue or value > maxValue:
        print("OUT OF RANGE!")
    elif value == target:
        print("GOT IT")
    elif value > target:
        print("HIGHER")
    elif value < target:
        print("LOWER")


print("This program get user to guess the number between 0 and 49.")

while True:
    userValue = input("Guess the number!\t\t")

    if check_integer(userValue):
        userValue = int(userValue)
        check_bigger_smaller(userValue)
    else:
        print("Naughty, naughty! Use an integer!")

    if userValue == target:
        break

