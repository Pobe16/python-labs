# Write a program to calculate compound interest.  The program 
# should ask the user for the initial sum invested, the term 
# (no of years) over which the interest should be paid and the 
# rate of interest. It should then calculate the compound 
# interest and print out the initial sum, interest and final 
# value of the savings. (Clue: the final value can be 
# calculated using the following formula 
# compound_interest = initial_sum(1+interest_rate/100)^term


import math
print("This program will calculate the compound interest.")
initial_sum = float(input("What is the invested sum? £"))
years = int(input("How many years it was invested for? "))
interest = float(input("What is the interest rate? "))
final_sum = initial_sum * (math.pow(1+interest/100, years))

print("The £%.2f deposited on %.2f%% interest rate will result in £%.2f after %d years." % (initial_sum, interest, final_sum, years))