from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def show_transaction(self):
        print("Transaction ID:", self.transaction_id)

    @abstractmethod
    def make_payment(self):
        pass


class UPIPayment(Payment):
    def make_payment(self):
        print("UPI Payment Successful:", self.get_amount())


class CreditCardPayment(Payment):
    def make_payment(self):
        print("Credit Card Payment Successful:", self.get_amount())


class NetBankingPayment(Payment):
    def make_payment(self):
        print("Net Banking Payment Successful:", self.get_amount())


u = UPIPayment("TXN101", 5000)
u.make_payment()

c = CreditCardPayment("TXN102", 5000)
c.make_payment()

n = NetBankingPayment("TXN103", 5000)
n.make_payment()
