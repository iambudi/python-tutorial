"""
=========================================================================================
Python does not have class visibility modifier (private/protected)
all props and methods are exposable as public
Convention for prop visibility is just obfuscating using underscore prefix
single as protected, double as private. 
Example _color for private or __color for protected. It's just informal concencuss.
=========================================================================================
Method started and ended with __ is a magic method. They are also called dunder methods. 
Magic methods are not meant to be invoked externally, but the invocation happens 
internally from the class on a certain action.
"""

class Animal:
    type: str = "Omnivora" # the declaration here called class Attribute

    def __init__(self, name: str):
        self.name = name # declaration inside init is instance attribute

    def call(self) -> None:
        print(self.name)


# cat extend animal
class Cat(Animal):
    __color_pattern: str

    def __init__(self, name: str, color_pattern: str):
        super().__init__(name)
        self.__color_pattern = color_pattern

    def walk(self) -> None:
        print(f"🐈 {self.name} is walking nicely ")

    @property
    def color(self) -> str:
        return self.__color_pattern

    @color.setter
    def color(self, value: str) -> None:
        self.__color_pattern = value

    @color.deleter
    def color(self) -> None:
        del self.__color_pattern

    @classmethod
    def to_str(cls) -> None:
        """
        @classmethod decorator has a similiarity with @staticmethod
        both can be called by classname.method() or objectname.method()
        and can't call instance attribute.
        * but there are some differences:
        the former can access class attribute, even it's parent's class attribute
        it also can be used as object factory that return object of the class (see method factory)
        """
        print("Cat class attribute is {}. Note cls.name can't be called, it's instance attr.".format(cls.type)) 
        
    @classmethod
    def factory(cls) -> 'Cat': # return Cat object
        return cls("Kocheng Oren", "orange")

    @staticmethod
    def purr():  # No need self arg when using static
        print("Static: Purr..pur...")

    # a special method used to represent a class’s objects as a string
    # this will be called when __str__ not defined
    def __repr__(self) -> str:
        return f"Cat class {self.name}"

    # represents the class objects as a string
    # invoked on print() and str()
    def __str__(self) -> str:
        return f"Cat {self.name} with color patter {self.__color_pattern}"


cat = Cat("Cantik", "Calico")
print(f"Special class method:\n__str__ {cat},\n__repr__ {repr(cat)}")
cat.call()
cat.walk()

# cat.__color_pattern is accesible publicly
# but let's pretend it's private :)
print(f"{cat.name} color is {cat.color}")
cat.color = "Gray"
print(f"@property: {cat.name} color is {cat.color}")

# classmethod and static
Cat.to_str()
cat = Cat.factory()
cat.call()
print("@classmethod factory:", type(Cat.factory()))

# static method
Cat.purr()