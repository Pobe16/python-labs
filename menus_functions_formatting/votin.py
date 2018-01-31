# Write a program which asks the user to select to vote for Labour, 
# SNP, Liberal Democrat or Conservative parties. Each time a choice 
# is made one vote is added to a total for that party. When the user 
# chooses to exit the program, the total votes for each party should 
# be shown before the program ends.

key = "0"
parties = ["Labour", "SNP", "Liberal Democrat", "Conservative"]
parties_votes = [0, 0, 0, 0]

while key != "x":
    print("~~~~~~~~~~~~~~~~~~~~")
    print("1.", parties[0])
    print("2.", parties[1])
    print("3.", parties[2])
    print("4.", parties[3])
    print("~~~~~~~~~~~~~~~~~~~~")
    print("x to exit")
    key = input("Choose your destiny: ")
    if key == "1":
        parties_votes[0] += 1
    elif key == "2":
        parties_votes[1] += 1
    elif key == "3":
        parties_votes[2] += 1
    elif key == "4":
        parties_votes[3] += 1
    elif key != "x":
        print("ERROR")

print("Here are the results: ")
print("~~~~~~~~~~~~~~~~~~~~")
print(parties[0], "got", parties_votes[0], "votes", end=".\n\r")
print(parties[1], "got", parties_votes[1], "votes", end=".\n\r")
print(parties[2], "got", parties_votes[2], "votes", end=".\n\r")
print(parties[3], "got", parties_votes[3], "votes", end=".\n\r")
print("~~~~~~~~~~~~~~~~~~~~")





