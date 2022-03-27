class Human:
    def __init__(self, name="Human"):
        self.name = name

class Bibimobile:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add(self, *human):
        for i in human:
            self.passengers.append(i)

    def info(self):
        if self.passengers != []:
            print(f"В машині {self.brand} пасажири:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"Машина {self.brand} немає пасажирів")


h1 = Human("Taras")
h2 = Human("Max")
h3 = Human("Ruslan")
h4 = Human("Volodymir")
audi = Bibimobile("audi")
audi.add(h1, h3, h2, h4)
audi.info()