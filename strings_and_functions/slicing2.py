# Write a program which reads a string which contains a number of 
# pieces of information separated by colons, and prints each piece 
# of information separately. For example

# Input:  Life of Brian:Terry Jones:1979:Comedy:15
# Output:
# Life of Brian
# Terry Jones
# 1979
# Comedy
# 15


print("This program is slicing strings on colon, then writes the results in new lines")
something = input("Please enter something: ")
somethingElse = something.split(":")
for sentence in somethingElse:
    print(sentence)