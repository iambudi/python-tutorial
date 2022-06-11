"""
=========================================================================================
more_itertools is Additional building blocks, recipes, and routines for working with 
Python iterables. This enhances builtin itertools. For complete list of functions see
Ref: https://more-itertools.readthedocs.io/en/latest/
=========================================================================================
"""

from typing import Dict
from more_itertools import flatten, take, filter_except, first, tail, first_true

# flatten accept any iterable, can combine tuple or list
# for dict, the keys that will be flattened not its value
numbers = [(1, 2), (3, 4), [5, 6], {7, 8}, {"a": 9, "b": 10}]
print("Flatten Numbers:", list(flatten(numbers)))

print("Take first", list(first(numbers)))
print("Take first Dict", list(first_true(numbers, default="Missing", pred=lambda x: isinstance(x, Dict))))
print("Take 2", list(take(2, numbers)))
print("Tail 2", list(tail(3, numbers)))

# Get item that does not raise exception based on validator
# Here the validator is type dict. Exception will catch by *third args - n
# ACHTUNG: THE VALIDATOR IS WRONG. validator dict returns correct, tuple is wrong
print("Filter Except", list(filter_except(tuple, numbers, TypeError)))
