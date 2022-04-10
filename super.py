"""class Human:
    height = 170
    satiety = 50
class Student(Human):
    pass

class Worker(Human):
    satiety = 100

nick = Student()
ann = Worker()
print(nick.satiety)
print(ann.satiety)"""
"""class Grandparent:
    height = 170
    satiety = 100
    age = 60
    _balance = 231451
    def show_balace(self):
        print(self._balance)

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)
        print(self._balance)

nick = Child()
"""
"""class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_printer(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)

h1 = Hello_world()
h1.printer()
h2 = Hi()
h2.hi_printer()"""
