# Write a function which checks for an integer value. Write a program to test this function.

def check_integer(a):
    try:
        val = int(a)
        return True
    except (TypeError, ValueError):
        return False


print("This program checks if you have entered a proper integer.")
i = input("Please enter integer: ")

if check_integer(i):
    print("Good!")
else:
    print("Naughty, naughty!")