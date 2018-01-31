# Write a program which reads a string and checks whether
# it is a palindrome, in other words that it is the same 
# read forwards or backwards. Test this by entering a string 
# which is not a palindrome, and then by entering a palindrome,
# and noting the results. Here are a couple of palindromes to 
# try (enter the letters only in your program, with no spaces 
# or punctuation)

# No mists or frost, Simon (enter as nomistsorfrostsimon)
# A dog! A panic in a pagoda!


print("This program checks if provided string is a palindrome.")
something = input("Please provide string: ")
length = len(something)

palindrome = True
count = 0
while palindrome and count < length:
    if something[count] != something[(count+1)*(-1)]:
        palindrome = False
    count += 1

if palindrome:
    print("The string you entered is a palindrome.")
else:
    print("You have failed to enter a palindrome")
