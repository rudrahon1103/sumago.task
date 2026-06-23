from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, emp_name, basic_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.__basic_salary = basic_salary

    def get_salary(self):
        return self.__basic_salary

    def show_details(self):
        print("ID:", self.emp_id)
        print("Name:", self.emp_name)

    @abstractmethod
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        total = self.get_salary() + self.get_salary() * 0.30
        print("Manager Salary =", total)


class Developer(Employee):
    def calculate_salary(self):
        total = self.get_salary() + self.get_salary() * 0.20
        print("Developer Salary =", total)


class Intern(Employee):
    def calculate_salary(self):
        total = self.get_salary() + self.get_salary() * 0.05
        print("Intern Salary =", total)


m = Manager(1, "Rudra", 50000)
m.calculate_salary()

d = Developer(2, "Rahul", 50000)
d.calculate_salary()

i = Intern(3, "Amit", 50000)
i.calculate_salary()
