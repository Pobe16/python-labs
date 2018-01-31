# Write a program which asks the user to guess an integer 
# between 1 and 49. The target number should be chosen at 
# random by the program. If the user enters a guess higher 
# than the target, the program should print HIGHER. If the 
# user enters a guess lower than the target the program 
# should print LOWER. If the guess is correct, then it 
# should print GOT IT. Use a function to do the comparison 
# of the guess and target.

# NOTE: to get a random integer you should include the line:

# import random

# at the top of your program, and the line

# target = random.randint(1,49)

# in your program.


import random

minValue = 1
maxValue = 49
target = random.randint(minValue, maxValue)


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
    userValue = int(input("Guess the number!\t\t"))
    check_bigger_smaller(userValue)
    if userValue == target:
        break

