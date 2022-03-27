from random import randint

class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("заповнюєм об'єм наших ізвилин")
        self.progress += 0.12
        self.happiness -= 3

    def to_sleep(self):
        print("Дрихне")
        self.happiness += 3

    def to_chill(self):
        self.happiness += 5
        self.progress -= 0.1
        print("Time to chill")

    def is_alive(self):
        if self.progress < -0.5:
            print("Бан за лоу скілл в навчанні")
            self.alive = False
        elif self.happiness <= 0:
            print("Забулили")
            self.alive = False
        elif self.progress > 5:
            print("Вітаю, ви мегамозг")
            self.happiness = 10000000000
            self.alive = False

    def stats(self):
        print(f"Рівень щастя = {self.happiness}")
        print(f"Прогрес = {round(self.progress, 2)}")

    def live(self, day):
        print(f"День: {day} студента {self.name}")
        rand = randint(1, 3)
        if rand == 1:
            self.to_study()
        elif rand == 2:
            self.to_sleep()
        elif rand == 3:
            self.to_chill()
        self.stats()
        self.is_alive()

student = Student("Max")

for day in range(365):
    if student.alive == False:
        print("а все, треба було раніше думати")
        break
    student.live(day)

