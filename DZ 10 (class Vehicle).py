class Vehicle:
    def __init__(self,brand, year):
        self.brand = brand
        self.year = year
class Motorcycle(Vehicle):
     def __init__(self, brand, year, speed):
           super().__init__(self, brand, year)
           self.speed = speed
           motorcycle = Motorcycle("Suzuki", 2023, "220 km/h")
class Car(Vehicle):
       def __init__(self, brand, year, color):
        super().__init__(self, brand, year)
        self.color = color
        car = Car("BMW", 2023, "Black")
        car.display.info()
        motorcycle.display.info()
