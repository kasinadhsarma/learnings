from abc import ABC, abstractmethod
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass