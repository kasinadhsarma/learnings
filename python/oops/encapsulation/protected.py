class Employee:
    def __init__(self,name,age):
        self._name = name # protected attribute
class Manager(Employee):
    def display_name(self):
        print(f"Manager name is {self._name}")
emp = Manager("John", 30)
emp.display_name()  # Output: Manager name is John