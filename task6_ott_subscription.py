from abc import ABC, abstractmethod

class Subscription(ABC):
    def __init__(self, user_name, monthly_fee):
        self.user_name = user_name
        self.__monthly_fee = monthly_fee

    def get_fee(self):
        return self.__monthly_fee

    def show_plan_details(self):
        print("User:", self.user_name)

    @abstractmethod
    def show_features(self):
        pass


class BasicPlan(Subscription):
    def show_features(self):
        print("Basic Plan: Mobile Only")


class StandardPlan(Subscription):
    def show_features(self):
        print("Standard Plan: HD Streaming")


class PremiumPlan(Subscription):
    def show_features(self):
        print("Premium Plan: 4K + Multiple Devices")


b = BasicPlan("Rudra", 199)
b.show_features()

s = StandardPlan("Rahul", 499)
s.show_features()

p = PremiumPlan("Amit", 799)
p.show_features()
