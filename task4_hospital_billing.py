from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, patient_id, patient_name, treatment_cost):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.__treatment_cost = treatment_cost

    def get_cost(self):
        return self.__treatment_cost

    def patient_details(self):
        print("Patient ID:", self.patient_id)
        print("Patient Name:", self.patient_name)

    @abstractmethod
    def generate_bill(self):
        pass


class GeneralPatient(Patient):
    def generate_bill(self):
        bill = self.get_cost() + 500
        print("General Patient Bill =", bill)


class ICUPatient(Patient):
    def generate_bill(self):
        bill = self.get_cost() + 5000
        print("ICU Patient Bill =", bill)


class EmergencyPatient(Patient):
    def generate_bill(self):
        bill = self.get_cost() + 3000
        print("Emergency Patient Bill =", bill)


g = GeneralPatient(1, "Rudra", 10000)
g.generate_bill()

i = ICUPatient(2, "Rahul", 10000)
i.generate_bill()

e = EmergencyPatient(3, "Amit", 10000)
e.generate_bill()
