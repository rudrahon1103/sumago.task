from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_no, holder_name, balance):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def calculate_interest(self):
        print("Interest =", self.get_balance() * 0.04)


class CurrentAccount(Account):
    def calculate_interest(self):
        print("Interest =", self.get_balance() * 0.02)


class FixedDepositAccount(Account):
    def calculate_interest(self):
        print("Interest =", self.get_balance() * 0.08)


s = SavingsAccount(101, "Rudra", 10000)
s.calculate_interest()

c = CurrentAccount(102, "Rahul", 10000)
c.calculate_interest()

f = FixedDepositAccount(103, "Amit", 10000)
f.calculate_interest()
