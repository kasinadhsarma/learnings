class Animal:
    def sound(self):
        return "some generic sound"
class Dog(Animal):
    def sound(self):
        return "Woof!"
class Cat(Animal):
    def sound(self):
        return "Meow!"
#polymorphism behaviour

animals = [Dog(), Cat(),Animal()]
for animal in animals:
    print(animal.sound())  # Output: Woof! Meow! some generic sound