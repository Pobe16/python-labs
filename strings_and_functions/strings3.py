# Write a program which reads a string and prints out the first letter of each word in the string.

print("This program prints the first letter of every word in a sentence you provide.")

sentence = input("Please enter sentence: ")

result = ""

if sentence[0] != " ":
    result += sentence[0]
space_position = 0
while space_position >-1:
    space_position = sentence.find(" ", space_position+1)
    if (space_position > 0) and (space_position+1 < len(sentence)):
        result += " " + sentence[space_position+1]

print(result)