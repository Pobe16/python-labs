# Write an object oriented program to handle four classes 
# (Apple, Orange, Basket and Barrel). Barrels are used to 
# store apples and baskets to store oranges. Each apple and 
# orange has an attribute which describes it weight and 
# baskets and barrels must have a means of keeping track of 
# how many apples or oranges they contain.

class Container:
    def __init__(self, name, usage, count):
        self.name = name
        self.usage = usage
        self.count = count


class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Apple(Fruit):
    def __init__(self, weight):
        Fruit.__init__(self, "Apple", weight)


class Orange(Fruit):
    def __init__(self, weight):
        Fruit.__init__(self, "Orange", weight)


class Basket(Container):
    def __init__(self, count):
        Container.__init__(self, "Basket", "Oranges", count)


class Barrel(Container):
    def __init__(self, count):
        Container.__init__(self, "Barrel", "Apples", count)