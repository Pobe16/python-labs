# This exercise extends the username check program from usinglists3.py. 
# Write a program which maintains a list of usernames. It should 
# repeatedly show a menu with the following options:

#    Add a new username to the list
#    Read in a name and check whether it is in the list
#    Read in a name and append it to the list
#    Read in a name and delete it from the list if it exists
#    Read in a name and change it to a new value if it exists
#    Exit the program

# The program should make appropriate use of functions.


option = 999
userlist = []
a = ""


def read_user():
    global a
    a = input("Enter username: ")


def add_user(user):
    global userlist
    userlist += [user]
    print("User " + user + " added.")


def check_user(user):
    if (user in userlist):
        print("User " + user + " exist in the list.")
        return True
    else:
        print("User " + user + " does not exist in the list.")
        return False


def change_user(user, newUser):
    global a, userlist
    a = userlist.index(user)
    userlist[a] = newUser
    print("From now on, user " + user + " will be known as " + newUser + ".")


def delete_user(index):
    global userlist
    del userlist[index]
    print("User " + a + " deleted.")


while (option != "0"):
    print("Choose an option:")
    print("######")
    print("1. Add new user.")
    print("2. Check for user.")
    print("3. Change username.")
    print("4. Delete user.")
    print("0. Exit.")
    print("######")

    option = input(": ")

    if (option == "1"):
        read_user()
        add_user(a)
    elif (option == "2"):
        read_user()
        check_user(a)
    elif (option == "3"):
        read_user()
        if (check_user(a)):
            newu = input("Please input new username: ")
            change_user(a, newu)
    elif (option == "4"):
        read_user()
        if (check_user(a)):
            delete_user(userlist.index(a))
    elif (option == 0):
        print("Goodbye.")
    else:
        print("Error. Choose again.")

