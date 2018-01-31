# Write a program which reads in six numbers and prints them out in reverse 
# order - that is, the number entered last should be printed first, and so on. 

print("This program reads 6 numbers and then prints them out in reverse order.")

numbers = [0,0,0,0,0,0]
for i in range(6):
    numbers[i] = input("Please enter " + str(i+1) + " number: ")

for j in range(-1, -7, -1):
    print(numbers[j])