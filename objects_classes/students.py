# Rewrite the student marks program from lists_tuples_dictionaries/dictionaries3.py to use a class instead of lists. 

class Student:
    # initialization
    def __init__(self, banner, name, grade1, grade2, grade3):
        self.banner = banner
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3


student1 = Student("B00329768", "Mikolaj Lukasik", 80, 90, 99)
student2 = Student("B00123456", "Someone Else", 50, 33, 99)
student3 = Student("B00987654", "Proper Student", 100, 100, 100)
dictionary = {student1.banner: student1, student2.banner: student2, student3.banner: student3}

numero = input("Please enter student number: ")

average = (dictionary[numero].grade1 + dictionary[numero].grade2 + dictionary[numero].grade3) / 3

print (dictionary[numero].name + "'s marks average to " + str(average))