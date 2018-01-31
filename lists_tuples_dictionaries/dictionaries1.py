# Put the cars' data in a dictionary

car1=["GH54CFG","Honda", "Jazz", "petrol", "hatchback", 1.4]
car2=["DC54SDA","Mazda", "6", "diesel", "estate", 2.0]
car3=["DG54AQW","Ford", "Focus", "petrol", "saloon", 1.6]
car4=["DF05VBN","Land Rover", "Discovery", "diesel", "SUV", 2.7]

cars = {car1[0]: car1, car2[0]:car2, car3[0]:car3, car4[0]:car4}

registration = input("Enter a registration number: ")
if registration in cars.keys():
    car = cars[registration]
    print(car[1], car[2]," - ",car[5],"litre",car[3], car[4])
else:
    print("Not found")
