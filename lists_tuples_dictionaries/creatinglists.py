# Create three separate lists, each of which contains the names 
# of several cities in a different country. Create another list 
# which contains these three lists. Print the whole list of 
# nested lists. 
# Print the second member of the list of lists. 
# Use a while loop to print the names in the second member list.


cities1 = ["London", "Manchester", "Birmingham"]
cities2 = ["Krakow", "Warszawa", "Szczecin"]
cities3 = ["Glasgow", "Edinburgh", "Dundee"]

citiesall = [cities1, cities2, cities3]

print(citiesall[1])

i = 0
while (i < len(citiesall)):
    print(citiesall[i])
    i += 1