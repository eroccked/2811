import random
brands_of_car = {
 "BMW":{"fuel":100, "strength":100, "consumption": 6},
 "Lada":{"fuel":50, "strength":40, "consumption": 10},
 "Volvo":{"fuel":70, "strength":150, "consumption": 8},
 "Ferrari":{"fuel":80, "strength":120, "consumption": 14},
"Бандеромобіль":{"fuel":10000, "strength":100000, "consumption": 1},
 }
job_list = {
 "Java developer": {"salary":50, "gladness_less": 10 },
 "Python developer": {"salary":40, "gladness_less": 3 },
 "C++ developer": {"salary":45, "gladness_less": 25 },
 "Rust developer": {"salary":70, "gladness_less": 1 },
 }

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.happy = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive:
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 99
                return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.happy -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("Я заправиив машину")
            self.car.fuel += 100
            self.money -= 100
        elif manage == "food":
            print("Я купив їжу")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Купили вкусняшки, ура")
            self.happy += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.happy += 10
        self.home.mess += 5

    def clean_home(self):
        self.happy -= 5
        self.home.mess = 1
        self.money -= 15

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        print(f"Персонаж {self.name} день {day}")
        print(f"Баланс =  {self.money} Щастя = {self.happy} Ситість = {self.satiety}")
        print(f"Машина: Модель = {self.car.brand} Паливо = {self.car.fuel} Стан машини = {self.car.strength}")
        print(f"В будинку {self.home.food} їжі, рівень свинарника = {self.home.mess}")

    def is_alive(self):
        if self.happy < 0:
            print("Депресія.....")
            return False
        if self.satiety < 0:
            print("PRESS F TO PAY RESPECT")
            return False
        if self.money < -500:
            print("Банкрот")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Лутаєм будинок")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Вітаю з покупкою {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Вітаю вас прийняли на роботу {self.job.job}. Ваш оклад = {self.job.salary}")
        self.days_indexes(day)
        rand = random.randint(1, 4)
        if self.satiety < 20:
            print("я пішов їсти")
            self.eat()
        elif self.happy < 20:
            if self.home.mess > 15:
                print("я не можу чілити, тому що вдома свинарник")
                self.clean_home()
            else:
                print("Відпочинок")
                self.chill()
        elif self.money < 0:
            print("Йди працюй")
            self.work()
        elif self.car.strength < 15:
            print("я в гараж")
            self.to_repair()
        elif rand == 1:
            print("го чілити")
            self.chill()
        elif rand == 2:
            print("Йдем працювати")
            self.work()
        elif rand == 3:
            print("Прибирання")
            self.clean_home()
        elif rand == 4:
            print("Час їсти вкусняшки")
            self.shopping(manage="delicacies")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Машина не може їатии")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human("Nick")
for day in range(1, 8):
    if nick.live(day) == False:
        break