# Write a program which reads in a string and counts the number of occurrences 
# of each letter in the string. The results should be stored in a dictionary 
# and displayed. For example:

# Enter text to count: mississippi
# {'i': 4, 'p': 2, 's': 4, 'm': 1}


print("This program counts the different characters in given strings.")

a = input("Please enter some text: ")

counting = {}

for i in a:
    if i in counting:
        counting[i] += 1
    else:
        counting[i] = 1

print(counting)