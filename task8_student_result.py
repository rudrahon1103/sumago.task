from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, roll_no, student_name, marks):
        self.roll_no = roll_no
        self.student_name = student_name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def show_result(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.student_name)

    @abstractmethod
    def calculate_percentage(self):
        pass


class ScienceStudent(Student):
    def calculate_percentage(self):
        print("Percentage =", (self.get_marks()/500)*100)


class CommerceStudent(Student):
    def calculate_percentage(self):
        print("Percentage =", (self.get_marks()/600)*100)


class ArtsStudent(Student):
    def calculate_percentage(self):
        print("Percentage =", (self.get_marks()/400)*100)


s = ScienceStudent(1, "Rudra", 450)
s.calculate_percentage()

c = CommerceStudent(2, "Rahul", 500)
c.calculate_percentage()

a = ArtsStudent(3, "Amit", 350)
a.calculate_percentage()
