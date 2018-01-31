# Write a program which reads in ten numbers and stores these in a list. 
# It should then calculate the average and print out each number together 
# with the difference between the number and the average.

print("This program reads 10 numbers and then prints out the average and difference.")
numbers = []
total = 0
for i in range(10):
    numbers += [float(input("Please enter " + str(i+1) + " number: "))]
    total += numbers[i]


average = total / len(numbers)

for j in range(10):
    difference = average - numbers[j]
    print(numbers[j], difference)
