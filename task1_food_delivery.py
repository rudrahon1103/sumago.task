from abc import ABC, abstractmethod

class FoodOrder(ABC):
    def __init__(self, order_id, customer_name, food_price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.__food_price = food_price

    def get_price(self):
        return self.__food_price

    def _restaurant_details(self):
        print("Restaurant: Sumago Foods")

    def __apply_discount(self):
        return self.__food_price * 0.95

    def show_discount(self):
        print("Discount Applied")

    @abstractmethod
    def generate_bill(self):
        pass


class VegOrder(FoodOrder):
    def __init__(self, order_id, customer_name, food_price):
        super().__init__(order_id, customer_name, food_price)

    def generate_bill(self):
        bill = self.get_price() + (self.get_price() * 0.05)
        print("Veg Order Bill =", bill)


class NonVegOrder(FoodOrder):
    def __init__(self, order_id, customer_name, food_price):
        super().__init__(order_id, customer_name, food_price)

    def generate_bill(self):
        bill = self.get_price() + (self.get_price() * 0.10)
        print("Non-Veg Order Bill =", bill)


v = VegOrder(101, "Rudra", 500)
v.generate_bill()

n = NonVegOrder(102, "Rahul", 500)
n.generate_bill()
