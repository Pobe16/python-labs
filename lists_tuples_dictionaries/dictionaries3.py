# Write a program which creates a number of lists, each of which 
# contains the following information about a student: student number, 
# name, and marks out of 100 for three subjects. These should then 
# be added to a list, using the student number as the key.

# The program should then prompt for a student number, and print 
# out the specified student's name and the average of the student's marks.


students = [["B00329768", "Mikolaj Lukasik", 80, 90, 99], ["B00123456", "Someone Else", 50, 33, 99], ["B00987654", "Proper Student", 100, 100, 100]]

dictionary = {students[0][0]: students[0], students[1][0]: students[1], students[2][0]: students[2]}

student = input("Please enter student number: ")

average = (dictionary[student][2] + dictionary[student][3] + dictionary[student][4]) / 3

print (dictionary[student][1] + "'s marks average to " + str(average))