from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_number, rent_per_day):
        self.vehicle_number = vehicle_number
        self.__rent_per_day = rent_per_day

    def get_rent(self):
        return self.__rent_per_day

    def show_vehicle_details(self):
        print("Vehicle Number:", self.vehicle_number)

    @abstractmethod
    def calculate_rent(self, days):
        pass


class Bike(Vehicle):
    def calculate_rent(self, days):
        print("Bike Rent =", self.get_rent() * days)


class Car(Vehicle):
    def calculate_rent(self, days):
        print("Car Rent =", (self.get_rent() + 500) * days)


class Bus(Vehicle):
    def calculate_rent(self, days):
        print("Bus Rent =", (self.get_rent() + 1000) * days)


b = Bike("MH01B1234", 300)
b.calculate_rent(5)

c = Car("MH01C5678", 1000)
c.calculate_rent(5)

bs = Bus("MH01D9999", 2000)
bs.calculate_rent(5)
