# Write a program to create a body mass index (BMI) calculator. The program 
# should have appropriate dialogue boxes and buttons to allow input of the 
# users height and weight and to both calculate the BMI and display the result 
# of the calculation. BMI is calculated as follows:

# BMI = Weight (in Kilogrammes) / (Height(in metres) * Height (in metres))

import easygui as eg


def main():
    msg = "Please enter your measurements"
    title = "BMI calculator"
    fields = ["Weight (kg)", "Height (cm)"]
    measurements = eg.multenterbox(msg, title, fields)
    try:
        for i in measurements:
            float(i)
        calculateBMI(measurements)

    except ValueError:
        print("Please enter only numbers")
        main()
    except TypeError:
        print("Good bye!")


def calculateBMI(measurements):
    bmi = float(measurements[0]) / ((float(measurements[1])/100) ** 2)
    msg = "Your BMI is " + str(bmi) + ". Wanna do it again?"
    title = "BMI calculated. Great success!"

    decision = eg.ynbox(msg, title, ["Yes", "No"])

    if decision:
        main()


main()