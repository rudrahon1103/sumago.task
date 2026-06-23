from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, order_id, product_name, product_price):
        self.order_id = order_id
        self.product_name = product_name
        self.__product_price = product_price

    def get_price(self):
        return self.__product_price

    def show_order_details(self):
        print("Order ID:", self.order_id)
        print("Product:", self.product_name)

    @abstractmethod
    def calculate_total(self):
        pass


class LocalOrder(Order):
    def calculate_total(self):
        print("Total Amount =", self.get_price() + 50)


class StateOrder(Order):
    def calculate_total(self):
        print("Total Amount =", self.get_price() + 150)


class InternationalOrder(Order):
    def calculate_total(self):
        print("Total Amount =", self.get_price() + 500)


l = LocalOrder(101, "Mobile", 20000)
l.calculate_total()

s = StateOrder(102, "Laptop", 50000)
s.calculate_total()

i = InternationalOrder(103, "Camera", 30000)
i.calculate_total()
