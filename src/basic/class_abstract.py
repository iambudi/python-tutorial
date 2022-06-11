from abc import ABC, abstractmethod, abstractproperty
from random import choice

"""
 abc - abstract base class is a class contract
 Its like combination of interface & abstract
"""

class Animal(ABC):
    @abstractmethod
    def walk(self):
        print("Animal walk()")

    # decorate a method as prop. subclass must decorate using @property
    @abstractproperty
    def color(self):
        colors = ("white", "calico", "gray", "orange")
        return choice(colors)


class Cat(Animal):
    # this method should be implemented in child class or will thrown error
    def walk(self):
        super().walk()  # call its parent walk()
        print("Cat walk()")

    @property  # concrete decorator of @abstractproperty
    def color(self):
        return super().color


cat = Cat()
cat.walk()
print(f"🐈 has color {cat.color}")

# print("Cat is subclass of Animal?", issubclass(Cat, Animal))
# print("Cat instance of Animal?", isinstance(cat, Animal))
