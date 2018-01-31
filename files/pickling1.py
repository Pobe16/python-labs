# Write a program which uses pickle to dump three integers, 
# and then load the three integers and calculate their average.

import pickle

f = open("test.pck", "wb")

numbers = [3, 5, 8]

pickle.dump(numbers, f)

f.close()

g = open("test.pck", "rb")


newnumbers = pickle.load(g)

average = (newnumbers[0] + newnumbers[1] + newnumbers[2])/3

print(average)