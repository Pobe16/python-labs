# IMPORTS
import os
import pickle
import json
from datetime import date
from pprint import *

# GLOBAL VARIABLES
products = ["Winglet Attachment Strut", "Door Seal Clamp Handle", "Rudder Pivot Pin"]

# variables named after the index of the product in products list:
subtypes = [["Airbus A320", "Airbus A380"], ["Universal"], ["10mm diameter x 75mm length", "12mm diameter x 100mm length", "16mm diameter x 150mm length"]]

locations = ["Paisley", "Dubai"]

batchFileName = "../Data/BatchIndex.json"

batchesList = []


# CLASSES
class Batch:
    def __init__(self, id, size):
        self.bid = id
        self.size = size
        self.manufactureDate = date.today()
        self.place = "Factory"
        self.components = []

    # properly present contents of the batch
    def present(self):
        print("Batch " + self.bid)
        print("Components number: " + str(self.size))
        print("Manufacture date: " + self.manufactureDate.strftime("%d%m%y"))
        print("Current location: " + self.place)
        for i in self.components:
            i.present()
        print("")


class Component:
    def __init__(self, batch, id, product, subtype):
        self.batch = batch
        self.cid = id
        self.product = int(product) - 1
        self.subtype = int(subtype) - 1
        self.productDesc = products[self.product]
        # adding subtypes descriptions based on global lists
        self.subtypeDesc = subtypes[self.product][self.subtype]
        self.state = "Manufactured"

    # properly present the component
    def present(self):
        print("")
        print("\tComponent " + self.cid)
        print("\tType: " + self.productDesc + ", size: " + self.subtypeDesc)
        print("\tState: "+ self.state)



# FUNCTIONS
# get current date as a string of DDMMYY
def getFormattedToday():
    return date.today().strftime("%d%m%y")


# checks if the argument is an integer
def checkInt(arg):
    try:
        int(arg)
        return True
    except (TypeError, ValueError):
        return False


# checks if the argument is a floating point number
def checkFloat(arg):
    try:
        float(arg)
        return True
    except (TypeError, ValueError):
        return False


def createBatch():
    global batchesList
    newID = createBatchID()
    print("Creating new batch with ID " + newID + ".")
    print("How many components there are in the batch? (0-9999)")
    while True:
        componentsNumber = input(">>>")
        if (checkInt(componentsNumber)):
            if (int(componentsNumber) > 0) and (int(componentsNumber) < 10000):
                break
            else:
                print("Please enter number between 0 and 9999")
        else:
            print("Please enter a number between 0 and 9999.")

    currentBatch = Batch(newID, componentsNumber)


    # Choosing component details.
    while True:
        print("Choose the manufactured component:")
        print("1. " + products[0])
        print("2. " + products[1])
        print("3. " + products[2])
        print("")
        print("x to cancel")
        componentChoice = input(">>> ")
        if componentChoice =="x":
            break
        elif componentChoice == "1":
            print("Creating " + products[0] + ". Choose type:")
            print("1. " + subtypes[0][0])
            print("2. " + subtypes[0][1])
            print("")
            print("x to cancel")
            typeChoice = input(">>> ")
            if typeChoice == "x":
                break
            elif typeChoice != "1" and typeChoice != "2":
                print("Wrong choice!")
            else:
                break
        elif componentChoice == "2":
            # to keep up with the lists of subtypes in global variables
            typeChoice = 1
            break
        elif componentChoice == "3":
            print("Creating " + products[2] + ". Choose type:")
            print("1. " + subtypes[2][0])
            print("2. " + subtypes[2][1])
            print("3. " + subtypes[2][2])
            print("")
            print("x to cancel")
            typeChoice = input(">>> ")
            if typeChoice == "x":
                break
            elif (typeChoice != "1" and typeChoice != "2" and typeChoice != "3"):
                print("Wrong choice!")
            else:
                print("Creating a batch with " + componentsNumber + " of " + products[int(componentChoice)-1] + ". " + subtypes[int(componentChoice)-1][int(typeChoice)-1] + " type.")
                print("Is that correct? (Y/N)")
                correct = input(">>")
                if correct == "Y" or correct == "y":
                    break

    # Empty batch
    if componentChoice == "x" or typeChoice == "x":
        print("The batch will not be created.")
    else:
        # creating the components in batch
        for i in range(int(componentsNumber)):
            componentID = newID + "-" + formatIntToFourDigits(i+1)
            currentComponent = Component(newID, componentID, componentChoice, typeChoice)
            saveFile("component", currentComponent)
            currentBatch.components.append(currentComponent)

        batchesList.append(newID)

        show = input("Do you want to see batches details? (Y/N)")
        if show == "Y" or show =="y":
            currentBatch.present()

        saveBatchesList()
        saveFile("batch", currentBatch)

#saving json of batches
def saveBatchesList():
    f = open(batchFileName, "w")
    json.dump(batchesList, f)
    f.close()

# saving the .pck file for batch or components
def saveFile(type, data):
    if type == "component":
        filepath = "../Data/Components/"
        fileid = data.cid
        fullfilepath = filepath + fileid + ".pck"
        # if the directory does not exist, this line creates it
        os.makedirs(os.path.dirname(fullfilepath), exist_ok=True)
        f = open(fullfilepath, mode="wb")
        pickle.dump(data, f)
        f.close()
    elif type == "batch":
        filepath = "../Data/Batches/"
        fileid = data.bid
        fullfilepath = filepath + fileid + ".pck"
        # if the directory does not exist, this line creates it
        os.makedirs(os.path.dirname(fullfilepath), exist_ok=True)
        f = open(fullfilepath, mode="wb")
        pickle.dump(data, f)
        f.close()



def createBatchID():
    today = getFormattedToday()
    if (batchesList == []):
        return today + '0001'
    else:
        lastID = batchesList[len(batchesList)-1]
        if lastID[:6] == today:
            # gets the last four digits of batch id, changes it to int, adds 1, then returns as 4 digits
            number = formatIntToFourDigits(int(lastID[6:]) + 1)
            return today + number
        else:
            return today + "0001"


# the parts of ID have to be formatted as XXXX. That's why I add 0s if they are less than certain number
def formatIntToFourDigits(number):
    if number < 10:
        formattedNumber = "000" + str(number)
    elif number < 100:
        formattedNumber = "00" + str(number)
    elif number < 1000:
        formattedNumber = "0" + str(number)
    else:
        formattedNumber = str(number)
    return formattedNumber



# Checks if the json files used by program were created. If not, create them.
def initFile():
    global batchesList
    if (os.path.exists(batchFileName)):
        f = open(batchFileName, "r")
        batchesList = json.load(f)
        f.close()
    else:
        batchesList = []
        f = open(batchFileName, "w")
        json.dump(batchesList, f)
        f.close()


# MAIN FUNCTION
def main():
    while True:
        print("Welcome to the PPEC inventory system.")
        print("")
        print("Choose an option:")
        print("\t1. Create a new batch.")
        print("\t2. Quit")
        print(">>>")
        choice = input()

        if choice == "1":
            createBatch()

        elif choice == "2":
            print("Good bye!")
            break
        else:
            print("Wrong option chosen. Can you into keyboard?")


# INITIALIZATION
initFile()

main()