# In strings3.py you wrote a program which reads a string and prints 
# out the first letter of each word in the string. Rewrite this program 
# using a function called printFirstLetters, and test the program.

def printFirstLetters(word):
    print(word[0])


print ("This program reads your first and last name, then write your last name and initial.")

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

print(last + ", ")
printFirstLetters(first)