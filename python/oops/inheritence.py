class Animal:
    def __init__(self,name):
        self.name = name
    def info(self):
        print(f"Animal name is {self.name}")
class Dog(Animal):
    def sound(self):
        print(self.name + " says Woof!")
d = Dog("Buddy")
d.info()  # Output: Animal name is Buddy    
d.sound()  # Output: Buddy says Woof!