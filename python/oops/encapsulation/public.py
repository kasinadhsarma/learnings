class Employee:
    def __init__(self,name):
        self.name = name # public attribute
    def display_name(self):
        print(f"Employee name is {self.name}")
emp = Employee("John")
emp.display_name()  # Output: Employee name is John