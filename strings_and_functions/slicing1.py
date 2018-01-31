# Write a program which reads in a person's full name (first name and last name)
# and prints the name in the form last name, initial, for example:

# Input: Terry Jones
# Output: Jones, T


print("This program asks for firs and last name, then prints last name and initial.")

first = input("Please enter your first name: ")
last = input("Please enter your last name: ")

print(last + ", " + first[0])