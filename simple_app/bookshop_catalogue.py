# Group work.
# Create a program for book sales. You should be able to:
#     load the books database from a file
#     update the sales figure for a book
#     add a new book
#     delete a specified book



import pickle
# this is a function to check for  a numeric value
def isNumber(value):
   try:
      var = float(value)
      return True
   except (TypeError, ValueError):
      return False


# initialise catalogue using hard coded data - update this to load from the supplied json
def initialise():
    file = open("data.pck", "rb")

    cat = pickle.load(file)
    return cat


# list all book codes and titles
def showAllBooks(cat):
    for book in cat.values():
        print("%-4s => %-50s" % (book[0], book[1]))


# list all details for one book
def bookDetail(cat):
    code = input("Enter book code: ")
    if code in cat.keys():
        book = cat[code]
        print("Code:", book[0])
        print("Title:", book[1])
        print("Author(s):", book[2])
        print("Publisher:", book[3])
        print("Year:", book[4])
        print("Price:", end=" ")
        print("$%5.2f" % book[5])
        print("Sales:", book[6])
    else:
        print("Book not found")


# update price for a book
def updatePrice(cat):
   code = input("Enter book code: ")
   if code in cat.keys():
      book = cat[code]
      price = input("New price:")
      if isNumber(price):
         priceValue = float(price)
      else:
         priceValue = 0.0
         print("Warning: invalid price, set to 0")
      book[5] = priceValue
      print("Price of book", code, "is now $", book[5])
   else:
      print("Book not found")

def updateSalesFigure(cat):
    code = input("Enter book code: ")
    if code in cat.keys():
        book = cat[code]
        sold = input("How many did you sell: ")
        if isNumber(sold):
            soldValue = int(sold)
        else:
            soldValue = 0
            print("If you have not sold enough book get back to work!")
        book[6] = book[6]+ soldValue
        print ("Total amount of book",code,"sold is now ", book[6])
    else:
        print("Book not found")

def AddNewBook(cat):
    book = []
    code = input("Please enter the Book Code for Check")
    if code in cat.keys():
        print("This Book already exists in the code")
        return cat
    else:
        book.append(code)
        book.append(input("What is the new Books Title"))
        book.append(input("Who is the Books Author"))
        book.append(input("Who is the Books publisher"))
        book.append(input("When was the book Published"))
        book.append(float(input("What is the books Price")))
        book.append(0)
        cat[code] = book
        print("This Book has been added")
        return cat

def deletebook(cat):
    code=input("Please enter the book you want to delete")
    if code in cat.keys():
        del cat[code]
        print("Book",code,"deleted")
    else:
        print("This book does not exist")
    return cat


# start main program
catalogue = initialise()

# print greeting
print("Welcome to the book sales program")
print("..........................")
print()
while True:
    # Print out the menu:
    print("Please select an option :")
    print("1  List all books")
    print("2  View details of a book")
    print("3  Update price")
    print("4  update sales figure")
    print("5  Add a new book")
    print("6  Delete a specified book")
    print("X  Exit")

    # Get the user's choice:
    choice = input("> ")

    # Carry out task:
    if choice == '1':
        showAllBooks(catalogue)
    elif choice == '2':
        bookDetail(catalogue)
    elif choice == '3':
        updatePrice(catalogue)
    elif choice == '4':
        updateSalesFigure(catalogue)
    elif choice == '5':
        catalogue = AddNewBook(catalogue)
    elif choice == '6':
        catalogue = deletebook(catalogue)
    elif choice == 'X':
        print("Bye")
        file = open("data.pck", "wb")
        pickle.dump(catalogue, file)
        file.close()
        break
    else:
        print("Invalid choice")
    print()

