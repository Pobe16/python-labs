# Write a program to calculate how many rolls of wallpaper are needed for a room. The program should 
# ask the user for the height, length and width of the room then ask for the height and width of any 
# doors or windows in the room (hint you will need to have some form of iteration here). The program 
# will calculate the total wall area to be wallpapered (total area of walls minus total area of 
# openings) and then calculate (and print) the number of rolls required (assume that one roll will 
# cover 5m2). You should use either math.floor() or math.ceil()  to round up the numbers of rolls 
# required. Research online what each of these two functions does and choose the correct one to use 
# in this situation.

import math
print("This program will tell you how many rolls of wallpaper you need for your rectangular room.")
roomHeight = float(input("What is the height of walls? (m) "))
roomLenght = float(input("What is the length of room? (m) "))
roomWidth = float(input("What is the width of room? (m) "))

windowsArea = 0.0
windowsCount = 0
windows = int(input("How many windows are there? "))
while windows>0 and windowsCount < windows:
    windowLenght = float(input("What is the window #" + str(windowsCount + 1) +"'s length? (m) "))
    windowWidth = float(input("What is the window #" + str(windowsCount + 1) + "'s width? (m) "))
    windowsArea += windowLenght*windowWidth
    windowsCount += 1

doorsArea = 0.0
doorsCount = 0
doors = int(input("How many doors are there? "))
while doors>0 and doorsCount < doors:
    doorLenght = float(input("What is the door #" + str(doorsCount + 1) +"'s length? (m) "))
    doorWidth = float(input("What is the door #" + str(doorsCount + 1) + "'s width? (m) "))
    doorsArea += doorLenght*doorWidth
    doorsCount += 1

roomArea = (2 * roomLenght + 2 * roomWidth) * roomHeight - (windowsArea + doorsArea)

rollsRequired = math.ceil(roomArea/5)

print("For your room you will need %d wallpaper rolls." % rollsRequired)