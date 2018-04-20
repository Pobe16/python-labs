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

places = ["Factory", "Paisley", "Dubai"]

states = ["Manufactured"]

batchFileName = "../Data/BatchIndex.json"

batchesDirectory = "../Data/Batches/"

componentsDirectory = "../Data/Components/"


batchesList = []


# CLASSES
class Batch:
    def __init__(self, id, size, product, subtype):
        self.bid = id
        self.size = size
        self.manufactureDate = id[:6]
        self.product = int(product) - 1
        self.subtype = int(subtype) - 1
        self.productDesc = products[self.product]
        # adding subtypes descriptions based on global lists
        self.subtypeDesc = subtypes[self.product][self.subtype]
        self.place = 0
        self.placeDesc = places[self.place]
        self.state = 0
        self.stateDesc = states[self.state]
        self.components = []

    # properly present contents of the batch, defaults to also present all the components
    def present(self, full=True):
        # print(self.__dict__)
        print("Batch " + self.bid)
        print("Components number: " + str(self.size))
        print("Manufacture date: " + self.manufactureDate)

        # for listing all batches without going into details
        if not full:
            print("Type: " + self.productDesc + ", size: " + self.subtypeDesc)

        print("Current location: " + self.placeDesc)
        print("Current state: " + self.stateDesc)

        # for listing the batch with everything inside it
        if full:
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
        self.state = 0
        self.stateDesc = states[self.state]

    # properly present the component
    def present(self):
        print("")
        print("\tComponent " + self.cid)
        print("\tType: " + self.productDesc + ", size: " + self.subtypeDesc)
        print("\tState: "+ self.stateDesc)


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
    print("How many components there are in the batch? (1-9999)")
    while True:
        componentsNumber = input(">>>")
        if (checkInt(componentsNumber)):
            if (int(componentsNumber) > 0) and (int(componentsNumber) < 10000):
                componentsNumber = int(componentsNumber)
                break
            else:
                print("Please enter number between 1 and 9999")
        else:
            print("Please enter a number between 1 and 9999.")

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
                print("Creating a batch with " + str(componentsNumber) + " of " + products[int(componentChoice)-1] + ". " + subtypes[int(componentChoice)-1][int(typeChoice)-1] + " type.")
                print("Is that correct? (Y/N)")
                correct = input(">>")

                if correct == "Y" or correct == "y":
                    break

        elif componentChoice == "2":
            # to keep up with the lists of subtypes in global variables
            typeChoice = 1
            print("Creating a batch with " + str(componentsNumber) + " of " + products[int(componentChoice)-1] + ". " + subtypes[int(componentChoice)-1][int(typeChoice)-1] + " type.")
            print("Is that correct? (Y/N)")
            correct = input(">>")

            if correct == "Y" or correct == "y":
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
                print("Creating a batch with " + str(componentsNumber) + " of " + products[int(componentChoice)-1] + ". " + subtypes[int(componentChoice)-1][int(typeChoice)-1] + " type.")
                print("Is that correct? (Y/N)")
                correct = input(">>")
                if correct == "Y" or correct == "y":
                    break

    # Empty batch
    if componentChoice == "x" or typeChoice == "x":
        print("The batch will not be created.")
    else:
        # creating batch - the last number: 0 is to indicate where the batch is currently
        currentBatch = Batch(newID, componentsNumber, componentChoice, typeChoice)

        # this is used for storing batch info in json:
        # 0: id
        # 1: size
        # 2: manufacture date
        # 3: product
        # 4: subtype
        # 5: place
        # 6: state
        # 7: components
        batchArray = [newID, componentsNumber, newID[:6], int(componentChoice) - 1, int(typeChoice) - 1, 0, 0, []]

        # creating the components in batch
        for i in range(componentsNumber):
            componentID = newID + "-" + formatIntToFourDigits(i+1)
            currentComponent = Component(newID, componentID, componentChoice, typeChoice)
            # this is used for storing components info in json:
            # 0: id
            # 1: product
            # 2: subtype
            # 3: state
            componentArray = [componentID, int(componentChoice) - 1, int(typeChoice) - 1, 0]
            batchArray[7].append(componentArray)

            saveFile("component", currentComponent)
            currentBatch.components.append(currentComponent)

        batchesList.append(batchArray)

        show = input("Do you want to see batches details? (Y/N)")
        if show == "Y" or show =="y":
            currentBatch.present()

        saveBatchesList()
        saveFile("batch", currentBatch)


# saving json of batches
def saveBatchesList():
    f = open(batchFileName, "w")
    json.dump(batchesList, f)
    f.close()


# saving the .pck file for batch or components
def saveFile(filetype, data):

    if filetype == "component":
        filepath = componentsDirectory
        fileid = data.cid

    elif filetype == "batch":
        filepath = batchesDirectory
        fileid = data.bid

    fullfilepath = filepath + fileid + ".pck"
    f = open(fullfilepath, mode="wb")
    pickle.dump(data, f)
    f.close()


def loadFile(filetype, id):
    if filetype == "component":
        filepath = componentsDirectory
    elif filetype == "batch":
        filepath = batchesDirectory
    fullfilepath = filepath + id + ".pck"
    f = open(fullfilepath, mode="rb")
    data = pickle.load(f)
    f.close()
    return data


def createBatchID():
    today = getFormattedToday()
    if (batchesList == []):
        return today + '0001'
    else:
        lastID = batchesList[len(batchesList)-1][0]
        if lastID[:6] == today:
            # gets the last four digits of batch id, changes it to int, adds 1, then returns as 4 digits
            number = formatIntToFourDigits(int(lastID[6:]) + 1)
            return today + number
        else:
            return today + "0001"


def checkIfThereAreBatches():
    if not len(batchesList) == 0:
        return True
    else:
        print("")
        print("There are no batches yet.")
        print("")
        return False


def listAllBatches():
    if checkIfThereAreBatches():
        for i in batchesList:
            currentBatchPath = batchesDirectory + i[0] + ".pck"
            f = open(currentBatchPath, "rb")
            currentBatch = pickle.load(f)
            currentBatch.present(False)
            f.close()


def showBatchDetails():
    if checkIfThereAreBatches():
        print("Please enter batch id (x to cancel):")
        batchid = input(">>")
        if not(batchid == "x" or batchid == "X"):
            currentBatchPath = batchesDirectory + batchid + ".pck"
            if os.path.exists(currentBatchPath):
                f = open(currentBatchPath, "rb")
                currentBatch = pickle.load(f)
                currentBatch.present()
                f.close()
            else:
                print("Batch " + batchid + " does not exist.")
                print("")
                showBatchDetails()


def showComponentDetails():
    if checkIfThereAreBatches():
        print("Please enter component id (x to cancel):")
        componentid = input(">>")
        if not (componentid == "x" or componentid == "X"):
            currentComponentPath = componentsDirectory + componentid + ".pck"
            if os.path.exists(currentComponentPath):
                f = open(currentComponentPath, "rb")
                currentComponent = pickle.load(f)
                currentComponent.present()
                f.close()
            else:
                print("Component " + componentid + " does not exist.")
                print("")
                showComponentDetails()


def allocateBatch(id, location):

    # change the info in pickled files
    currentBatch = loadFile("batch", id)
    currentBatch.place = location
    currentBatch.placeDesc = places[location]
    saveFile("batch", currentBatch)

    # change the info in json:
    for i in batchesList:
        if i[0] == id:
            i[5] = location
            break

    saveBatchesList()

    print("Batch " + id + " has been moved to " + places[location] + ".")

def allocateBatchMenu():
    if checkIfThereAreBatches():
        batchesThatRequireAllocation = 0
        listOfbatchesThatRequireAllocation = []
        for i in batchesList:
            if i[5] == 0:
                batchesThatRequireAllocation = batchesThatRequireAllocation + 1
                listOfbatchesThatRequireAllocation.append(i[0])
        print("")
        print("There are currently " + str(batchesThatRequireAllocation) + " batches that require allocation.")
        if batchesThatRequireAllocation > 0:
            print("Here is the list:")
            for j in listOfbatchesThatRequireAllocation:
                print(j)

            while True:
                print("")
                print("Please enter ID of a batch you want to allocate (x to cancel):")
                print(">>")
                batchToAllocate = input()
                if batchToAllocate in listOfbatchesThatRequireAllocation:
                    while True:
                        print("Where do you want to allocate the batch?")
                        print("0. " + places[0] + " (don't move)")
                        print("1. " + places[1])
                        print("2. " + places[2])
                        print(">>")
                        whereToAllocate = input()

                        if checkInt(whereToAllocate):
                            if int(whereToAllocate) in range(1, len(places)):
                                allocateBatch(batchToAllocate, int(whereToAllocate))
                                break
                            elif int(whereToAllocate) == 0:
                                print("Batch will not be allocated.")
                                break
                            else:
                                print("Wrong location.")
                        else:
                            print("Wrong location")
                    break
                elif batchToAllocate == "x" or batchToAllocate == "X":
                    break
                else:
                    print("Wrong batch ID.")
        print("")

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
        # Creates the directories first, then the file.
        os.mkdir("../Data")
        os.mkdir(batchesDirectory)
        os.mkdir(componentsDirectory)
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
        print("\t2. List all batches")
        print("\t3. View details of a batch")
        print("\t4. View details of a component")
        print("\t5. Allocate manufactured stock")
        print("\tX. Quit")
        print(">>>")
        choice = input()

        if choice == "1":
            createBatch()

        elif choice == "2":
            listAllBatches()

        elif choice == "3":
            showBatchDetails()

        elif choice == "4":
            showComponentDetails()

        elif choice == "5":
            allocateBatchMenu()

        elif choice == "X" or choice == "x":
            print("Good bye!")
            break
        else:
            print("Wrong option chosen. Can you into keyboard?")


# INITIALIZATION
initFile()

main()