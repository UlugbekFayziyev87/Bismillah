class Animal:
    def make_sound(selfself,s):
        print(s)
class Horse (Animal):
    pass
pony = Horse()
pony.make_sound("Igogo")

class Roditel:
    def make_mark(selfself,s):
        print(s)
class Rebenok (Roditel):
    pass
starshiy = Rebenok()
starshiy.make_mark("Otlichno")

class Car:
    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year
class SuperCar(Car):
    def __init__(self, model, color, yera, sponsor):
        super().__init__(self, model, color, year)
        self.sponsor=sponsor

class Myclass:
    @classmethod
    def say_hello(cls, word):
        print(word)
Myclass.say_hello("Hello!")

class Player:
    def __int__(self, stamina, power, accuracy, speed):
        self.stamina = stamina
        self.power = power
        self.accuracy = accuracy
        self.speed = speed
class Attacker (Player):
    def __int__(self, stamina, power, accuracy, speed):
        super().__init__(self, stamina, power, accuracy, speed)
    def goal(self):
        print("Zabil gol")
class Halfback (Player):
    def __int__(self, stamina, power, accuracy, speed):
        super().__init__(self, stamina, power, accuracy, speed)
    def podacha(self):
         print("pasuy")
class Goolkeeper (Player):
    def __int__(self, stamina, power, accuracy, speed):
         super().__init__(self, stamina, power, accuracy, speed)
    def zaxvat(self):
         print("vzyal")
class Defender(Player):
    def __int__(self, stamina, power, accuracy, speed):
        super().__init__(self, stamina, power, accuracy, speed)
    def zashita(self):
        print("Moy")
