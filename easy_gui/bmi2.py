# Extend question bmi1.py to allow additional options of using imperial measurements 
# (feet and inches, pounds). You should use a search engine to find the 
# appropriate conversion factors.

import easygui as eg

def main():
    msg = "Choose your unit system:"
    title = "BMI calculator"
    choices = ["Metric", "Imperial"]
    unit = eg.buttonbox(msg, title, choices)
    if unit == "Metric":
        metric()
    elif unit == "Imperial":
        imperial()
    else:
        print("Good bye!")

def imperial():
    msg = "Please enter your measurements"
    title = "BMI calculator (Imperial)"
    fields = ["Pounds (lbs)", "Feet (')", "Inches (\")"]
    measurements = eg.multenterbox(msg, title, fields)
    try:
        for i in measurements:
            float(i)
        kg = float(measurements[0]) * 0.453592
        cm = float(measurements[1]) * 2.54 * 12 + float(measurements[2]) * 2.54
        new_measurements = [str(kg), str(cm)]
        calculateBMI(new_measurements)

    except ValueError:
        print("Please enter numbers")
        imperial()
    except TypeError:
        print("Good bye!")

def metric():
    msg = "Please enter your measurements"
    title = "BMI calculator (Metric)"
    fields = ["Weight (kg)", "Height (cm)"]
    measurements = eg.multenterbox(msg, title, fields)
    try:
        for i in measurements:
            float(i)
        calculateBMI(measurements)

    except ValueError:
        print("Please enter numbers")
        metric()
    except TypeError:
        print("Good bye!")


def calculateBMI(measurements):
    bmi = float(measurements[0]) / ((float(measurements[1])/100) ** 2)
    msg = "Your BMI is " + str(bmi) + ". Wanna do it again?"
    title = "BMI calculated. Great success!"

    decision = eg.ynbox(msg, title, ["Yes", "No"])

    if decision:
        main()
    else:
        print("Good bye.")


main()