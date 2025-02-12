# Basic Class and Object

class Car:
    total_car = 0
    def __init__(self, brand=None, model=None):
        # Encapsulation
        # Private attributes start with __
        self.__brand = brand
        self.model = model
        Car.total_car += 1 
    
    # getter methods
    def get_brand(self):
        return self.__brand
    def name(self):
        return (f"This car is {self.__brand} and {self.model}")
    
    # polymorphism
    def fuelType(self):
        return "Petrol Disel"
    
    # static properties
    @staticmethod
    def generalDescriptions():
        return "Cars are means of transportation"

# Inheritance

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # polymorphism
    def fuelType(self):
        return "Electric"
# Creating objects of the Car class

car1 = Car(model = "Q3", brand= "Audi")
print (car1.name())
print(car1.get_brand())

# Creating objects of the ElectricCar class

tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(tesla.name())