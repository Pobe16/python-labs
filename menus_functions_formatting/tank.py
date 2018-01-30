# Write a program which accepts the radius and height (in metres) 
# of a cylindrical fuel storage tank, calculates the maximum volume 
# of fuel it will be able to hold and prints the result. Ensure that 
# you use appropriate units of measure in your output (e.g. would 
# it be better to describe fuel in m3 or in litres?). The formula 
# for volume of a cylinder: V = πr2h, where is r the radius and h 
# is the height.

import math
print("This program will calculate the maximum fuel volume for a cylindrical tank")
# multiply the given values by 10 to get them in decimetres, to easily convert dm^3 to litres
height = 10*float(input("What is the height (m): "))
radius = 10*float(input("What is the radius (m): "))

volume = math.pi * radius * radius * height

print("This cylindrical tank will be able to hold", volume, "litres.")