from typing import Generic, List, TypeVar

T = TypeVar("T")  # any type
S = TypeVar("S", str, int)  # constraint to type str or int


class Calculator(Generic[T, S]):
    result: T

    def __init__(self, first: T, second: S) -> None:
        super().__init__()
        self.first = first
        self.second = second

    def print(self):
        print(f" T is {type(self.first)} with value {self.first}")
        print(f" S is {type(self.second)} with value {self.second}")


# Class first any kind of type
Calculator[str, int]("Hello World", 1).print()
Calculator[int, bool](100, True).print()
Calculator[List[int], int]([100, 200, 300], True).print()
