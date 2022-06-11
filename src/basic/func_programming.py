""" 
=========================================================================================
Lambda, Closure, Map, Filter, Reduce
=========================================================================================
Functional programming is a programming paradigm in which the primary method of 
computation is evaluation of pure functions. 
Although Python is not primarily a functional language, it’s good to be familiar with 
lambda, map(), filter(), and reduce() because they can help write concise, high-level, 
parallelizable code. Look at src itertool_more.py for more functional variation
=========================================================================================
"""
from functools import reduce
import operator
from typing import List

# closure: function inside function (nested)
# used as callback functions, they provide some sort of data hiding.
# This helps us to reduce the use of global variables or creating class
def sort_numbers(x: List[int]):
    # this nested is closure
    def sort():
        return sorted(x) # x parent scope allowed

    return sort

print("Closure", sort_numbers([4,3,1,0,2])())

animals = ["Cat", "Tiger", "Lion", "Zebra", "Deer", "Chicken"]
# map will produce a new map object
map_animal_with_i = map(lambda a: a if "i" in a else None, animals)
filter_animal_with_i = filter(lambda a: a if "i" in a else None, animals)
# convert back to list so it won't print the memory address of map object value
print("Map Animal with i", list(map_animal_with_i))
print("Filter Animal with i", list(filter_animal_with_i))

# reduce is different with map and filter. it only returns single value
numbers = [1, 2, 3, 4, 5]
print("SUM addition of numbers is", reduce(lambda x, y: x + y, numbers))
print("SUM multiply of numbers is", reduce(operator.mul, numbers))
