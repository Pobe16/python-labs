# Modify the program so it check that the temperature value is numeric

# Temperature conversion program
def centigradeToFahrenheit(cent):
    fahr = (9.0 / 5.0) * cent + 32
    return fahr


def fahrenheitToCentigrade(fahr):
    cent = (5.0 / 9.0) * (fahr - 32)
    return cent


def isNumber(value):
    try:
        var = float(value)
        return True
    except (TypeError, ValueError):
        return False


print("Welcome to the temperature conversion program")
print("---------------------------------------------")
print()
while True:
    # Print out the menu:
    print("Please select a conversion:")
    print("1  Centigrade to Fahrenheit")
    print("2  Fahrenheit to Centigrade")
    print("3  Exit program")

    # Get the user's choice:
    convert = input("> ")

    if convert == '1':
        value = input("Please enter value in degrees Centigrade: ")
        if isNumber(value):
            value = float(value)
            result = centigradeToFahrenheit(value)
            print(result, "degrees Fahrenheit")
        else:
            print("Value is invalid - try again")
    elif convert == '2':
        value = input("Please enter value in degrees Fahrenheit: ")
        if isNumber(value):
            value = float(value)
            result = fahrenheitToCentigrade(value)
            print(result, "degrees Centigrade")
        else:
            print("Value is invalid - try again")
    elif convert == '3':
        print("Bye...")
        break
    else:
        print("Invalid choice - try again")
    print()
