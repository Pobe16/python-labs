# Modify your student dictionary program from lists_tuples_dictionaries/dictionaries3.py 
# so that it is two separate programs. One should create the data and store it, while the 
# other should load the data and use it. Note that you can dump or load the entire 
# dictionary at once using pickle.

import pickle
print("This program saves student's data:")

try:
    f = open("students.pck", "rb")

    students = pickle.load(f)

    f.close()

except FileNotFoundError:
    g = open("students.pck", "wb")
    students = {}
    pickle.dump(students, g)
    g.close()

howmany = str(len(students))

print("The database currently holds " + howmany + " students. Adding a new one.")
bannerId = input("Banner ID: ")
name = input("Full name: ")
score1 = int(input("Score in course 1: "))
score2 = int(input("Score in course 2: "))
score3 = int(input("Score in course 3: "))

students[bannerId] = [bannerId, name, score1, score2, score3]

file = open("students.pck", "wb")

pickle.dump(students, file)

file.close()


print("Great success!")


