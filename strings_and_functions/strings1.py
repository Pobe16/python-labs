# Write a program which reads a string and counts the number 
# of vowels it contains. (Hint - this can be done efficiently 
# using nested for loops)

print("This program counts vowels in whatever you enter.")
whatever = input("Please enter something: ")
count = 0
for char in whatever:
    for a in ["a", "e", "i", "o", "u", "y"]:
        if char == a:
            count += 1
print("There are", count, "vowels in your something.")
