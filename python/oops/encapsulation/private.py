class private:
    def __init__(self,name):
        self.__name=name # private attribute
    def display_name(self):
        print(f"Private name is {self.__name}")
emp=private("John")
emp.display_name() # Output: Private name is John
