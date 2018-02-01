# Group work.
# Program starting the bookshop catalogue.

import pickle

file = open("data.pck", "wb")

book1 = ["BX", "Learning Python", "D. Lutz & M. Asher", "O'Reilly", "2004", 17.50, 250]
book2 = ["BT", "Python in a Nutshell", "A, Martelli", "O'Reilly", "2003", 17.50, 150]
book3 = ["BY", "Python Programming for the Absolute Beginner", "M. Dawson", "Premier Press", "2003", 13.50, 340]
book4 = ["BZ", "Dive into Python", "M. Pilgrim", "APress", "2004", 21.50, 185]
books = {"BX": book1, "BT": book2, "BY": book3, "BZ": book4}

pickle.dump(books, file)

file.close()