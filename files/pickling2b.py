# Modify your student dictionary program from lists_tuples_dictionaries/dictionaries3.py 
# so that it is two separate programs. One should create the data and store it, while the 
# other should load the data and use it. Note that you can dump or load the entire 
# dictionary at once using pickle.

import pickle

print("This program shows the student average score.")

try:
    f = open("students.pck", "rb")

    dictionary = pickle.load(f)

    student = input("Please enter student number: ")

    if student in dictionary.keys():

        average = (dictionary[student][2] + dictionary[student][3] + dictionary[student][4]) / 3

        print(dictionary[student][1] + "'s marks average to " + str(average))
    else:
        print("Student does not exist. Session terminated.")



    f.close()

except FileNotFoundError:
    print("Add some students to the list first.")


