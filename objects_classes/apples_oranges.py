juice_squeezed = 0.0


class Apple():
    def __init__(self, weight, colour):
        self.name = "Apple"
        self.colour = colour
        self.barrel = ""
        self.weight = weight

    def pick(self, barrel):
        if self.barrel == "":
            barrel.apples.append(self)
            barrel.count = barrel.count + 1
            self.barrel = barrel
        else:
            print("Apple already picked.")


class Orange():
    def __init__(self, weight, orchard, date_picked):
        self.name = "Orange"
        self.weight = weight
        self.orchard = orchard
        self.date_picked = date_picked
        self.basket = ""

    def pick(self, basket):
        if self.basket == "":
            basket.oranges.append(self)
            basket.count = basket.count + 1
            self.basket = basket
        else:
            print("Orange already picked.")

    def squeeze(self):
        global juice_squeezed
        juice_squeezed = juice_squeezed + self.weight * 0.25
        self.basket.oranges.remove(self)
        self.basket = ""




class Basket():
    def __init__(self, location):
        self.name = "Basket"
        self.usage = "Oranges"
        self.location = location
        self.count = 0
        self.oranges = []

    def discard(self):
        self.count = 0
        list = self.oranges
        self.oranges = []
        for a in list:
            a.basket = ""


class Barrel():
    def __init__(self):
        self.name = "Barrel"
        self.usage = "Apples"
        self.count = 0
        self.apples = []

    def discard(self):
        self.count = 0
        list = self.apples
        self.apples = []
        for a in list:
            a.barrel = ""




barrel1 = Barrel()

apple1 = Apple(1.3, "red")
apple2 = Apple(1.1, "green")

apple1.pick(barrel1)
apple2.pick(barrel1)

print(barrel1.apples[0].colour)
print(barrel1.apples[0].barrel.apples[0].barrel.apples[0].barrel.apples[0].barrel.apples[0].barrel.apples[0].colour)
print(barrel1.apples[0].__dict__)
print(barrel1.__dict__)

orange1 = Orange(2.3, "Pleasure Yard", "18/01/18")
orange2 = Orange(2.5, "Pleasure Yard", "18/01/18")
orange3 = Orange(2.8, "Pleasure Yard", "18/01/18")

basket1 = Basket("UWS")

orange1.pick(basket1)
orange2.pick(basket1)
orange3.pick(basket1)

print(basket1.__dict__)

orange2.squeeze()

print(basket1.__dict__)
print(juice_squeezed)

basket1.discard()

print(orange1.__dict__)
