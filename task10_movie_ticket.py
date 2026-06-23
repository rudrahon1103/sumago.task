from abc import ABC, abstractmethod

class Ticket(ABC):
    def __init__(self, booking_id, customer_name, base_price):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.__base_price = base_price

    def get_price(self):
        return self.__base_price

    def show_booking_details(self):
        print("Booking ID:", self.booking_id)
        print("Customer:", self.customer_name)

    @abstractmethod
    def ticket_price(self):
        pass


class SilverTicket(Ticket):
    def ticket_price(self):
        print("Silver Ticket Price =", self.get_price() + 50)


class GoldTicket(Ticket):
    def ticket_price(self):
        print("Gold Ticket Price =", self.get_price() + 100)


class PlatinumTicket(Ticket):
    def ticket_price(self):
        print("Platinum Ticket Price =", self.get_price() + 200)


s = SilverTicket(1, "Rudra", 300)
s.ticket_price()

g = GoldTicket(2, "Rahul", 300)
g.ticket_price()

p = PlatinumTicket(3, "Amit", 300)
p.ticket_price()
