"""
Decorator (part of meta programming) is a function that takes another function 
as its argument, and returns yet another function
Decorators can be extremely useful as they allow the extension of an existing function,
without any modification to the original function source code.
Decorator can be used both in def or in class methods like @staticmethod @property
"""

import datetime
import time
import os
from types import FunctionType
from typing import Any


def time_it(func: Any) -> FunctionType:
    # *args is not necessary when wrapped func does not have args
    # but in this case class method require to pass self so wrapper should accept *args
    # NOTE: vscode typechecking will tell it's error when **kwargs not defined
    def wrapper(*args: Any, **kwargs: Any) -> None:
        start = time.time()
        func(*args)
        print("Elapsed {} secs".format(time.time() - start))

    # return wrapper object, not result of wrapper() call
    return wrapper  # type: ignore


class Benchmark:
    @time_it
    def hello(self):
        time.sleep(1)
        print("Benchmark done")


b = Benchmark()
b.hello()


def log(func: Any) -> FunctionType:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        log_file = os.path.abspath(os.curdir) + os.sep + "src/storage/log.txt"
        with open(log_file, "a") as f:
            # combine both args and keyword args
            all_args = ", ".join(
                [str(arg) for arg in list(args) + list(kwargs.values())]
            )
            f.write(
                "[{}] called func calculate({})\n".format(
                    datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"), all_args
                )
            )
        val = func(*args, **kwargs)  # call wrapped func and return its value
        return val

    return wrapper  # type: ignore


@log
def calculate(a: int, b: int, multiplier: int = 1) -> None:
    # multiplier is kwargs = arg which has default value and can be assigned with its name
    print(a + b * multiplier)


calculate(1, 2, multiplier=100)
calculate(1, 2)
calculate(1, 2, 50)
