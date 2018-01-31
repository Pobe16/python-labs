# Write a line-processing program which makes a copy of a file, 
# omitting any lines that begin with #. Test your program by 
# using it to remove all comment lines from a Python source file.

def commentOmmiter(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:

        text = f1.readline()

        if text == "":
            break
        elif text[0] != "#":
            f2.write(text)

    f1.close()
    f2.close()

# This is just an example comment.


print("This program copies text files omitting commented lines.")

commentOmmiter("linesoftext.py", "omitted.txt")
