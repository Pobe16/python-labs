# Write a program which checks if a username which is entered exists 
# in a list of users. Your program should create a list, for example: 
# theusers = ["John","Eric", "Graham", "Terry", "Michael"]
# It should then read in a name, and use a function to output a 
# message which says whether the name entered is in the list.


print("This program checks if entered username exists.")
theusers = ["John", "Eric", "Graham", "Terry", "Michael", "Miko"]
checking = input ("Please enter username: ")

if checking in theusers:
    print("User found.")
else:
    print("User not found.")