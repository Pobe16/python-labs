# Write a program which uses the function in the notes to make a copy of a file. 

def copyFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text = f1.read(20)
        if text == "":
            break
        f2.write(text)
    f1.close()
    f2.close()


print("This program copies file1.txt to file2.txt in current directory.")

copyFile("file1.txt", "file2.txt")
