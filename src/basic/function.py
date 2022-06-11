# function
def hello_world():
    print("Hello world! from function")


# define return type hint
def hello(name: str) -> None:
    print(f"Hello {name}")


# Union type using | exists in python 3.10
def multi_hint(a: int | str, b: int) -> int | str:
    return a * b


print("multi_hint('A', 5) = ", multi_hint("A", 5))

# Union type < 3.10
from typing import Callable, Union


def multi_hint_old(a: Union[int, str], b: int) -> Union[int, str]:
    return a * b


print("multi_hint_old('A', 5) = ", multi_hint_old("A", 5))

# one liner function can use lambda. see func_programming.py
# typehint should wrap inside callable with list of args and return types
multi_hint_lambda: Callable[[int | str, int], int | str] = lambda x, y: x * y
print("Lambda multi_hint('A', 5)", multi_hint_lambda("A", 5))
