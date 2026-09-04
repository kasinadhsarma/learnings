from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
animal = Animal()  # This will raise an error because you cannot instantiate an abstract class