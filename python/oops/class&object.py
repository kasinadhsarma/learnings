# here class is class and dog is object
class Dog:
    species = "Canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age
dog1 = Dog("Buddy", 3)
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3