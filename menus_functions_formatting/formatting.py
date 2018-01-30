# Write a program to print the invoice for a car service. 
# It should accept the customer name, address and postcode, 
# car make model and registration number as input. It should 
# also ask for the number of hours spent (labour) doing the 
# job and the amount of oil used during the service. The 
# total cost of the service should be calculated and a 
# properly formatted invoice produced on screen. Assume that 
# labour costs £45.50 per hour and that engine oil costs 
# £5.85 per litre. Every car service requires a replacement 
# oil filter at a fixed cost of £9.99. You should use the 
# new (.format method).

print("This program will print invoice for car service.")

servicePriceLabour = 45.5
servicePriceOil = 5.85
servicePriceOilFilter = 9.99

print("~~~~~~~~~~~~~~~~~~~~")
customerName = input("Customer name: ")
customerAddressFirstLine = input("Address 1: ")
customerAddressSecondLine = input("Address 2: ")
customerAddressPostcode = input("Postcode: ")
customerAddressCity = input("City: ")
print("~~~~~~~~~~~~~~~~~~~~")
customerCarMake = input("Car model / make: ")
customerCarRegistrationNumber = input("Car registration number: ")
print("~~~~~~~~~~~~~~~~~~~~")
serviceHours = int(input("How many labour hours for this car? "))
serviceOilUsed = float(input("How many litres of oil used? "))
print("~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~")

totalCostLabour = serviceHours * servicePriceLabour

totalCostOil = serviceOilUsed * servicePriceOil

totalCostTotal = totalCostLabour + totalCostOil + servicePriceOilFilter

print("The Servicing Carpany")
print("End of Scotland")
print("G1 1AA")
print("Gowglas")
print("")

print(customerName)
print(customerAddressFirstLine)
if customerAddressSecondLine != "":
    print(customerAddressSecondLine)
print(customerAddressPostcode)
print(customerAddressCity)
print("")

print("Service charges for work done on {0:s} registered as {1:s}.".format(customerCarMake, customerCarRegistrationNumber))
print("")
print("Labour:\t\t\t\t{1:d} hours at\t\t£{0:.2f}:\t\t£{2:.2f}".format(servicePriceLabour, serviceHours, totalCostLabour))
print("Oil change:\t\t\t{0:.1f} litres at\t£{1:.2f}:\t\t £{2:.2f}".format(servicePriceOil, serviceOilUsed, totalCostOil))
print("New oil filter:\t\t\t\t\t\t\t\t\t£{0:.2f}".format(servicePriceOilFilter))
print("")
print("Total:\t\t\t\t\t\t\t\t\t\t\t£{0:.2f}".format(totalCostTotal))