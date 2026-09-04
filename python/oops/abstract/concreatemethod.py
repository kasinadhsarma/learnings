from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        return "Animal is moving"
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
dog = Dog()
print(dog.make_sound())  # Output: Woof!
print(dog.move())        # Output: Animal is moving