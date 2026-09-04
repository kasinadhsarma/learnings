from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def species(self):
        pass
class Dog(Animal):
    @property
    def species(self):
        return "Canine"
dog = Dog()
print(dog.species)  # Output: Canine
    